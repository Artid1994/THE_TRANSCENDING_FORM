from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CognitiveCycle:
    input_text: str
    recalled: str
    reasoning: str
    decision: str
    experience_recorded: bool


class CognitiveLoop:
    def __init__(self, cognitive, learning) -> None:
        self.cognitive = cognitive
        self.learning = learning
        self.last_cycle: CognitiveCycle | None = None

    def process(self, user_input: str) -> CognitiveCycle:
        user_input = user_input.strip()

        decision = self.cognitive.process(
            user_input,
            record_experience=False,
        )

        experience_recorded = False

        if decision == "RESPOND":
            candidate = self.learning.create_candidate(
                user_input,
                "GENERAL",
                1.0,
            )
            evaluation = self.learning.evaluate(candidate)
            experience_recorded = evaluation.accepted

        cycle = CognitiveCycle(
            input_text=user_input,
            recalled=user_input,
            reasoning=user_input,
            decision=decision,
            experience_recorded=experience_recorded,
        )

        self.last_cycle = cycle
        return cycle

    def snapshot(self) -> CognitiveCycle | None:
        if self.last_cycle is None:
            return None

        return CognitiveCycle(
            input_text=self.last_cycle.input_text,
            recalled=self.last_cycle.recalled,
            reasoning=self.last_cycle.reasoning,
            decision=self.last_cycle.decision,
            experience_recorded=self.last_cycle.experience_recorded,
        )
