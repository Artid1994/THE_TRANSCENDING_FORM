from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Action:
    decision: str
    executed: bool


class ActionModule:
    def execute(self, decision: str) -> Action:
        executed = decision not in ("", "NO_ACTION")

        return Action(
            decision=decision,
            executed=executed,
        )

    def snapshot(self, action: Action | None) -> Action | None:
        if action is None:
            return None

        return Action(
            decision=action.decision,
            executed=action.executed,
        )
