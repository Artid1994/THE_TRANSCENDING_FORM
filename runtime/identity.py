from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class IdentityState:
    stage: str = "NEWBORN"
    experience: int = 0
    identity_level: str = "MINIMAL"
    created_at: str = ""


class Identity:
    def __init__(self) -> None:
        self.state = IdentityState(
            created_at=datetime.now(timezone.utc).isoformat()
        )

    def snapshot(self) -> IdentityState:
        return IdentityState(
            stage=self.state.stage,
            experience=self.state.experience,
            identity_level=self.state.identity_level,
            created_at=self.state.created_at,
        )
