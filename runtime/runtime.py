from __future__ import annotations

from runtime.system_monitor import SystemMonitor
from runtime.identity import Identity
from runtime.memory import Memory
from runtime.internal_state import InternalStateManager
from runtime.personality import Personality
from runtime.self_model import SelfModel
from runtime.cognitive_engine import CognitiveEngine
from runtime.learning import Learning


class TranscendingRuntime:
    def __init__(self) -> None:
        self.system = SystemMonitor()
        self.identity = Identity()
        self.memory = Memory()
        self.internal_state = InternalStateManager()
        self.personality = Personality()
        self.self_model = SelfModel()
        self.cognitive = CognitiveEngine(self.memory)
        self.learning = Learning(self.memory)

    def snapshot(self) -> dict:
        return {
            "system": self.system.snapshot(),
            "identity": self.identity.snapshot(),
            "memory": self.memory.snapshot(),
            "internal_state": self.internal_state.snapshot(),
            "personality": self.personality.snapshot(),
            "self_model": self.self_model.snapshot(),
            "cognitive": self.cognitive.snapshot(),
            "learning": self.learning.snapshot(),
        }
