from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Perception:
    raw_input: str
    normalized_input: str
    has_input: bool


class PerceptionModule:
    def process(self, user_input: str) -> Perception:
        normalized = user_input.strip()

        return Perception(
            raw_input=user_input,
            normalized_input=normalized,
            has_input=bool(normalized),
        )

    def snapshot(self, perception: Perception | None) -> Perception | None:
        if perception is None:
            return None

        return Perception(
            raw_input=perception.raw_input,
            normalized_input=perception.normalized_input,
            has_input=perception.has_input,
        )
