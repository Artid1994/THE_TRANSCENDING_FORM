from __future__ import annotations

from dataclasses import dataclass


@dataclass
class InternalState:
    active: bool = True
    attention: float = 0.0
    arousal: float = 0.0
    valence: float = 0.0
    processing: bool = False


class InternalStateManager:
    def __init__(self) -> None:
        self.state = InternalState()

    def snapshot(self) -> InternalState:
        return InternalState(
            active=self.state.active,
            attention=self.state.attention,
            arousal=self.state.arousal,
            valence=self.state.valence,
            processing=self.state.processing,
        )

