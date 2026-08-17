from __future__ import annotations

from dataclasses import dataclass

from runtime.memory import Memory


@dataclass
class CognitiveState:
    recall_active: bool = False
    reasoning_active: bool = False
    decision_active: bool = False
    last_input: str = ""
    last_decision: str = ""


class CognitiveEngine:
    def __init__(self, memory: Memory) -> None:
        self.state = CognitiveState()
        self.memory = memory

    def snapshot(self) -> CognitiveState:
        return CognitiveState(
            recall_active=self.state.recall_active,
            reasoning_active=self.state.reasoning_active,
            decision_active=self.state.decision_active,
            last_input=self.state.last_input,
            last_decision=self.state.last_decision,
        )

    def process(self, user_input: str) -> str:
        self.state.last_input = user_input

        self.state.recall_active = True
        recalled = self._recall(user_input)

        self.state.reasoning_active = True
        reasoning = self._reason(recalled)

        self.state.decision_active = True
        decision = self._decide(reasoning)

        self.state.last_decision = decision

        if decision == "RESPOND":
            self.memory.add_experience(user_input)

        self.state.recall_active = False
        self.state.reasoning_active = False
        self.state.decision_active = False

        return decision

    @staticmethod
    def _recall(user_input: str) -> str:
        return user_input.strip()

    @staticmethod
    def _reason(recalled: str) -> str:
        return recalled

    @staticmethod
    def _decide(reasoning: str) -> str:
        if not reasoning:
            return "NO_ACTION"

        return "RESPOND"
