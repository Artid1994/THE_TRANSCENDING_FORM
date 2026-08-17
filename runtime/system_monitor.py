from __future__ import annotations

import os
import platform
import time
from dataclasses import dataclass


@dataclass(frozen=True)
class SystemInfo:
    os_name: str
    kernel: str
    architecture: str
    cpu_model: str
    cpu_cores: int
    ram_total: int
    ram_available: int
    swap_total: int
    swap_used: int
    disk_total: int
    disk_used: int
    disk_available: int
    disk_usage_percent: float
    cpu_usage_percent: float
    uptime_seconds: float
    cpu_temperature: float | None


class SystemMonitor:
    def __init__(self, cpu_interval: float = 0.25):
        self.cpu_interval = cpu_interval
        self._previous_cpu = self._read_cpu_stat()

    @staticmethod
    def _read_cpu_stat() -> tuple[int, int]:
        with open("/proc/stat", encoding="utf-8") as f:
            values = list(map(int, f.readline().split()[1:]))

        total = sum(values)
        idle = values[3] + values[4]
        return total, idle

    def _read_cpu_usage(self) -> float:
        time.sleep(self.cpu_interval)

        total_a, idle_a = self._previous_cpu
        total_b, idle_b = self._read_cpu_stat()

        total_delta = total_b - total_a
        idle_delta = idle_b - idle_a

        self._previous_cpu = (total_b, idle_b)

        if total_delta <= 0:
            return 0.0

        return (1.0 - idle_delta / total_delta) * 100.0

    @staticmethod
    def _read_meminfo() -> dict[str, int]:
        data = {}

        with open("/proc/meminfo", encoding="utf-8") as f:
            for line in f:
                key, value = line.split(":", 1)
                data[key] = int(value.strip().split()[0]) * 1024

        return data

    @staticmethod
    def _read_swap() -> tuple[int, int]:
        total = 0
        used = 0

        with open("/proc/swaps", encoding="utf-8") as f:
            next(f, None)

            for line in f:
                fields = line.split()
                if len(fields) >= 4:
                    total += int(fields[2]) * 1024
                    used += int(fields[3]) * 1024

        return total, used

    @staticmethod
    def _read_disk() -> tuple[int, int, int]:
        stat = os.statvfs("/")

        total = stat.f_blocks * stat.f_frsize
        available = stat.f_bavail * stat.f_frsize
        used = total - available

        return total, used, available

    @staticmethod
    def _read_cpu_info() -> tuple[str, int]:
        model = "Unknown"
        cores = os.cpu_count() or 1

        with open("/proc/cpuinfo", encoding="utf-8") as f:
            for line in f:
                if line.startswith("model name"):
                    model = line.split(":", 1)[1].strip()
                    break

        return model, cores

    @staticmethod
    def _read_temperature() -> float | None:
        thermal_path = "/sys/class/thermal"

        if not os.path.isdir(thermal_path):
            return None

        for zone in os.listdir(thermal_path):
            temp_file = os.path.join(thermal_path, zone, "temp")

            try:
                with open(temp_file, encoding="utf-8") as f:
                    value = int(f.read().strip())

                return value / 1000.0

            except (FileNotFoundError, PermissionError, ValueError):
                continue

        return None

    def snapshot(self) -> SystemInfo:
        mem = self._read_meminfo()

        ram_total = mem.get("MemTotal", 0)
        ram_available = mem.get("MemAvailable", 0)

        swap_total, swap_used = self._read_swap()
        disk_total, disk_used, disk_available = self._read_disk()
        cpu_model, cpu_cores = self._read_cpu_info()

        disk_usage = (
            (disk_used / disk_total) * 100.0
            if disk_total
            else 0.0
        )

        return SystemInfo(
            os_name=platform.platform(),
            kernel=platform.release(),
            architecture=platform.machine(),
            cpu_model=cpu_model,
            cpu_cores=cpu_cores,
            ram_total=ram_total,
            ram_available=ram_available,
            swap_total=swap_total,
            swap_used=swap_used,
            disk_total=disk_total,
            disk_used=disk_used,
            disk_available=disk_available,
            disk_usage_percent=disk_usage,
            cpu_usage_percent=self._read_cpu_usage(),
            uptime_seconds=self._read_uptime(),
            cpu_temperature=self._read_temperature(),
        )

    @staticmethod
    def _read_uptime() -> float:
        with open("/proc/uptime", encoding="utf-8") as f:
            return float(f.readline().split()[0])
