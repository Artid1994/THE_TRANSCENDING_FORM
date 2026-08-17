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

    @staticmethod
    def _clamp(value: float) -> float:
        return max(0.0, min(1.0, value))

    def adapt(
        self,
        openness_delta: float = 0.0,
        conscientiousness_delta: float = 0.0,
        extraversion_delta: float = 0.0,
        agreeableness_delta: float = 0.0,
        stability_delta: float = 0.0,
    ) -> None:
        self.state.openness = self._clamp(
            self.state.openness + openness_delta
        )
        self.state.conscientiousness = self._clamp(
            self.state.conscientiousness + conscientiousness_delta
        )
        self.state.extraversion = self._clamp(
            self.state.extraversion + extraversion_delta
        )
        self.state.agreeableness = self._clamp(
            self.state.agreeableness + agreeableness_delta
        )
        self.state.stability = self._clamp(
            self.state.stability + stability_delta
        )

    def snapshot(self) -> PersonalityState:
        return PersonalityState(
            openness=self.state.openness,
            conscientiousness=self.state.conscientiousness,
            extraversion=self.state.extraversion,
            agreeableness=self.state.agreeableness,
            stability=self.state.stability,
        )
