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

    @staticmethod
    def _clamp(value: float) -> float:
        return max(0.0, min(1.0, value))

    def update(
        self,
        self_awareness_delta: float = 0.0,
        self_knowledge_delta: float = 0.0,
        history_entry: str | None = None,
    ) -> None:
        self.state.self_awareness = self._clamp(
            self.state.self_awareness + self_awareness_delta
        )
        self.state.self_knowledge = self._clamp(
            self.state.self_knowledge + self_knowledge_delta
        )

        if history_entry is not None:
            history_entry = history_entry.strip()

            if history_entry:
                self.state.self_history.append(history_entry)

    def snapshot(self) -> SelfModelState:
        return SelfModelState(
            self_awareness=self.state.self_awareness,
            self_knowledge=self.state.self_knowledge,
            goals=list(self.state.goals),
            beliefs=list(self.state.beliefs),
            self_history=list(self.state.self_history),
        )
