from __future__ import annotations

from dataclasses import dataclass


@dataclass
class PersonalityState:
    openness: float = 0.0
    conscientiousness: float = 0.0
    extraversion: float = 0.0
    agreeableness: float = 0.0
    stability: float = 0.0


class Personality:
    def __init__(self) -> None:
        self.state = PersonalityState()

    def snapshot(self) -> PersonalityState:
        return PersonalityState(
            openness=self.state.openness,
            conscientiousness=self.state.conscientiousness,
            extraversion=self.state.extraversion,
            agreeableness=self.state.agreeableness,
            stability=self.state.stability,
        )
