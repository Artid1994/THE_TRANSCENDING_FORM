from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class MemoryState:
    working: list = field(default_factory=list)
    episodic: list = field(default_factory=list)
    semantic: list = field(default_factory=list)


class Memory:
    def __init__(self) -> None:
        self.state = MemoryState()

    def snapshot(self) -> MemoryState:
        return MemoryState(
            working=list(self.state.working),
            episodic=list(self.state.episodic),
            semantic=list(self.state.semantic),
        )

    def is_empty(self) -> bool:
        return not (
            self.state.working
            or self.state.episodic
            or self.state.semantic
        )

