from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class IdentityContinuityState:
    snapshot_count: int = 0
    last_stage: str | None = None
    last_experience: int | None = None


class IdentityContinuity:
    def __init__(self) -> None:
        self.state = IdentityContinuityState()

    def record(self, identity) -> None:
        snapshot = identity.snapshot()

        self.state = IdentityContinuityState(
            snapshot_count=self.state.snapshot_count + 1,
            last_stage=snapshot.stage,
            last_experience=snapshot.experience,
        )

    def snapshot(self) -> IdentityContinuityState:
        return IdentityContinuityState(
            snapshot_count=self.state.snapshot_count,
            last_stage=self.state.last_stage,
            last_experience=self.state.last_experience,
        )
