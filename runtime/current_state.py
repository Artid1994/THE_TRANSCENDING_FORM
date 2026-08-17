from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CurrentState:
    has_input: bool
    input_length: int


class CurrentStateModule:
    def capture(self, input_text: str) -> CurrentState:
        return CurrentState(
            has_input=bool(input_text),
            input_length=len(input_text),
        )

    def snapshot(self, state: CurrentState | None) -> CurrentState | None:
        if state is None:
            return None

        return CurrentState(
            has_input=state.has_input,
            input_length=state.input_length,
        )
