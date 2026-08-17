from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DevelopmentAssessment:
    stage: str
    experience: int
    episodic_memory_count: int
    semantic_memory_count: int
    learning_candidate: object | None
    learning_evaluation: object | None
    personality: object
    self_model: object


class Development:
    def __init__(self, identity, memory, learning, personality, self_model) -> None:
        self.identity = identity
        self.memory = memory
        self.learning = learning
        self.personality = personality
        self.self_model = self_model

    def assess(self) -> DevelopmentAssessment:
        identity = self.identity.snapshot()
        memory = self.memory.snapshot()

        return DevelopmentAssessment(
            stage=identity.stage,
            experience=identity.experience,
            episodic_memory_count=len(memory.episodic),
            semantic_memory_count=len(memory.semantic),
            learning_candidate=self.learning.last_candidate,
            learning_evaluation=self.learning.last_evaluation,
            personality=self.personality.snapshot(),
            self_model=self.self_model.snapshot(),
        )
