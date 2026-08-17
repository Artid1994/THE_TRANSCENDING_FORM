from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CognitiveState:
    recall_active: bool = False
    reasoning_active: bool = False
    decision_active: bool = False
    last_input: str = ""
    last_decision: str = ""


class CognitiveEngine:
    def __init__(self) -> None:
        self.state = CognitiveState()

    def snapshot(self) -> CognitiveState:
        return CognitiveState(
            recall_active=self.state.recall_active,
            reasoning_active=self.state.reasoning_active,
            decision_active=self.state.decision_active,
            last_input=self.state.last_input,
            last_decision=self.state.last_decision,
        )
