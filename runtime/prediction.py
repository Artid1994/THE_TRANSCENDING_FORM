from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PredictionState:
    prediction_count: int = 0
    last_prediction: str | None = None


class Prediction:
    def __init__(self) -> None:
        self.state = PredictionState()

    def record(self, prediction: str) -> None:
        prediction = prediction.strip()

        if not prediction:
            return

        self.state = PredictionState(
            prediction_count=self.state.prediction_count + 1,
            last_prediction=prediction,
        )

    def snapshot(self) -> PredictionState:
        return PredictionState(
            prediction_count=self.state.prediction_count,
            last_prediction=self.state.last_prediction,
        )
