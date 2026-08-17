from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class SelfModelState:
    self_awareness: float = 0.0
    self_knowledge: float = 0.0
    goals: list[str] = field(default_factory=list)
    beliefs: list[str] = field(default_factory=list)
    self_history: list[str] = field(default_factory=list)


class SelfModel:
    def __init__(self) -> None:
        self.state = SelfModelState()

    def snapshot(self) -> SelfModelState:
        return SelfModelState(
            self_awareness=self.state.self_awareness,
            self_knowledge=self.state.self_knowledge,
            goals=list(self.state.goals),
            beliefs=list(self.state.beliefs),
            self_history=list(self.state.self_history),
        )
