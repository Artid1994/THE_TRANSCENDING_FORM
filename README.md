<div align="right">
  <a href="README.th.md">ไทย</a> | <a href="README.md">English</a>
</div>


# AE01M — The Transcending Form

> **A Local Cognitive Architecture for a Newborn Artificial Mind**

AE01M / **The Transcending Form (TTF)** is an experimental project to build a small, stateful, local cognitive architecture that can begin as a **Newborn Brain**, learn from experience, accumulate memory, develop capabilities, and eventually operate as a persistent personal cognitive assistant.

The project does **not** aim to create a chatbot that depends on an LLM for every thought.

The long-term goal is to create the **cognitive machinery around the AI model** so that the model becomes one component of the system rather than the system itself.

---

## Vision

The central idea is:

```text
Newborn Brain
      ↓
Experience
      ↓
Perception
      ↓
Memory
      ↓
Cognition
      ↓
Goal / Intention
      ↓
Decision
      ↓
Action
      ↓
Feedback
      ↓
Reflection
      ↓
Learning
      ↓
Development
      ↺

The system should gradually acquire knowledge, skills, strategies, and behavioral capability through experience instead of having every capability hard-coded in advance.

The ultimate goal is an AI personal assistant with JARVIS-like behavior at the architectural and behavioral level:

User
  ↓
AE01M
  ↓
Understand
  ↓
Remember
  ↓
Reason
  ↓
Plan
  ↓
Act
  ↓
Verify
  ↓
Learn
  ↓
Improve
  ↺

This is a research project. The project does not claim that the resulting system will become conscious, human-like, or generally intelligent.


---

Core Principle

The most important architectural rule is:

AI Model ≠ Identity
AI Model ≠ Memory
AI Model ≠ Cognitive Runtime

An AI model such as Qwen is treated as a replaceable cognitive/language component.

Identity, memory, development state, goals, experience, and runtime state exist outside the model.

This allows the underlying model to be replaced without destroying the identity and accumulated state of AE01M.


---

What We Are Actually Building

We are not trying to pre-program an intelligent robot.

We are building a mechanism for cognitive development.

EMPTY / NEWBORN
      ↓
TEACH
      ↓
EXPERIENCE
      ↓
MEMORY
      ↓
LEARNING
      ↓
CAPABILITY
      ↓
ADAPTATION
      ↓
DEVELOPMENT
      ↓
MORE EXPERIENCE
      ↺

The user provides goals, teaching, boundaries, and resources.

AE01M should progressively learn how to accomplish those goals.

Learning may change:

knowledge

strategies

skills

predictions

methods

task decomposition

learned associations


Learning must not arbitrarily change:

Owner/User goals

hard safety boundaries

protected identity/core state

critical runtime protections



---

Architecture

The current conceptual architecture is:

USER / OWNER
                              │
                        Goal / Teaching
                              │
                              ▼
                           AE01M
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
   Identity              Perception            Internal State
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              ▼
                          Attention
                              │
                              ▼
                            Memory
                              │
                              ▼
                          Cognition
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
                  Goal              Intention
                    └─────────┬─────────┘
                              ▼
                        Safety Boundary
                              │
                              ▼
                           Decision
                              │
                              ▼
                            Action
                              │
                              ▼
                    Environment / Tools
                              │
                              ▼
                          Feedback
                              │
                              ▼
                         Reflection
                              │
                              ▼
                          Learning
                              │
                              ▼
                        Development
                              │
                              └───────────────↺

The cognitive core is designed as a set of small modules rather than one large framework.


---

Cognitive Cycle

The fundamental cognitive cycle is:

OBSERVE
   ↓
PERCEIVE
   ↓
RECALL
   ↓
THINK
   ↓
GOAL
   ↓
INTENTION
   ↓
SAFETY
   ↓
DECIDE
   ↓
ACT
   ↓
OBSERVE RESULT
   ↓
EVALUATE
   ↓
REFLECT
   ↓
LEARN
   ↓
UPDATE MEMORY
   ↺

A future autonomous_step() is intended to represent one complete cognitive cycle.

The architecture intentionally separates a cognitive cycle from a scheduler or background process. Continuous autonomous execution is added only after the lifecycle and state transitions are proven.


---

Newborn Micro-Brain

The initial brain should be as small as possible.

The objective is not to preload knowledge.

A new instance should conceptually begin with:

Knowledge       = minimal
Experience      = empty
Episodic Memory = empty
Semantic Memory = empty
Skills          = minimal
Goals           = externally provided
Identity        = protected structural state

The mechanisms for learning exist before the knowledge does.

This makes it possible to distinguish:

Knowledge

from:

Capability to acquire knowledge

The second is what the project is primarily trying to build.


---

Memory Architecture

Memory is one of the central components of AE01M.

The current foundation contains:

Working Memory
Episodic Memory
Semantic Memory
Experience Objects
Recall Index
Semantic Index
Memory Consolidation

The intended brain-like memory flow is:

Experience
   ↓
Salience
   ↓
Working Memory
   ↓
Episodic Memory
   ↓
Association
   ↓
Consolidation
   ↓
Semantic Memory
   ↓
Recall
   ↓
Cognition

Future memory mechanisms include:

associative recall

contextual recall

salience

novelty

relevance

confidence

repetition

consolidation

decay

forgetting

reconsolidation

self-memory

memory association


The goal is not to build an unlimited text database.

The goal is to create a memory mechanism capable of deciding what is useful, what is related, what should be consolidated, and what should become knowledge.


---

Cell-Based Memory

A future memory architecture uses computational memory cells.

These are software abstractions and are not intended to represent biological neurons one-to-one.

Conceptually:

AE01M Memory
│
├── Working Cells
├── Episodic Cells
├── Association Cells
├── Semantic Cells
├── Self Cells
└── Safety Cells

A cell can contain metadata such as:

id
type
content
associations
salience
confidence
access_count
created_at
last_access
source_refs

Memory capacity should be bounded.

When memory pressure occurs:

New Experience
      ↓
Memory Capacity Check
      ↓
Consolidation
      ↓
Merge / Promote / Forget
      ↓
Free Capacity
      ↓
Store New Experience

The existing memory architecture is not intended to be discarded. Cell-based memory is intended as a lower-level organization and storage mechanism that can preserve existing interfaces and regression behavior.


---

Associative Memory

The current project has an associative recall prototype, but contextual/semantic recall is still under development.

The target is:

Memory A
   ↕
Association
   ↕
Memory B
   ↕
Association
   ↕
Memory C

This should eventually allow the system to retrieve memories based on:

context

semantic relationship

previous experience

salience

relevance

association


rather than relying only on exact string matching.


---

Learning

Learning is designed as:

Experience
   ↓
Candidate
   ↓
Evaluation
   ↓
Memory
   ↓
Reflection
   ↓
Development

The important distinction is:

Learning changes HOW to achieve a goal

rather than:

Learning arbitrarily changes WHAT the owner wants

For example:

User Goal:
Learn BLE on ESP32

AE01M:
Research
 ↓
Experiment
 ↓
Failure
 ↓
Reflection
 ↓
Missing knowledge identified
 ↓
Create next LearningTask
 ↓
Learn again

The user does not need to provide every intermediate lesson.


---

Reflection

Reflection is the mechanism that allows experience to become useful learning.

A reflection can identify:

SUCCESS
FAILURE
MISSING_KNOWLEDGE

and produce:

Lesson
Next Learning Task

The intended autonomous learning loop is:

Goal
 ↓
Task
 ↓
Research / Experiment
 ↓
Result
 ↓
Reflection
 ↓
Missing Knowledge?
 ├── NO → Continue / Complete
 │
 └── YES
       ↓
   New LearningTask
       ↓
      Learn
       ↺


---

Autonomous Growth

AE01M is considered to have a real Growth Loop only when it can:

1. remember its experience;


2. evaluate what it knows and does not know;


3. create and execute the next appropriate LearningTask.



The target loop is:

Observe
   ↓
Think
   ↓
Act
   ↓
Evaluate
   ↓
Reflect
   ↓
Identify Knowledge Gap
   ↓
Create LearningTask
   ↓
Learn
   ↓
Consolidate
   ↓
Update Memory
   ↓
Reuse Knowledge
   ↺

This is the project's definition of Autonomous Growth.

It does not imply consciousness.


---

Goal, Intention and Teaching

The user is the owner and primary source of high-level goals.

The intended control flow is:

USER COMMAND
     ↓
UNDERSTAND
     ↓
GOAL
     ↓
INTENTION
     ↓
SAFETY
     ↓
DECISION
     ↓
ACTION

AE01M may learn better ways to accomplish the goal.

It should not silently replace the owner's goal with a self-generated goal.

The long-term teaching mechanism is intended to look like:

Teaching Guide
      ↓
Learning Goal
      ↓
Learning Task
      ↓
Research
      ↓
Experiment
      ↓
Evaluation
      ↓
Memory
      ↓
Skill

The guide should define what to learn and how success is evaluated, without necessarily containing all of the answers.


---

Safety Architecture

Safety is a protected architectural boundary.

The conceptual flow is:

Cognition
   ↓
Thought / Intention
   ↓
Cognitive Safety Gate
   ↓
Decision
   ↓
Action

Hard safety boundaries are protected from ordinary learning.

Learning may accumulate experience about safety, but learned information should not automatically become a permanent hard behavioral rule.

The system should distinguish:

HARD SAFETY

from:

LEARNED EXPERIENCE ABOUT SAFETY

The hard boundary remains protected.


---

Local AI / Qwen

Qwen and other local models are treated as optional cognitive resources.

The intended architecture is:

AE01M
               │
       ┌───────┴────────┐
       │ Native Core    │
       │ small/stateful │
       └───────┬────────┘
               │
        Local AI when needed
               │
             Qwen

The system should not require an LLM call for every cognitive cycle.

Examples:

Simple state operation
    → Native Cognitive Core

Language processing
    → Local AI

Complex reasoning
    → Local AI + Cognitive Core

Direct deterministic operation
    → Tool directly

This separation is particularly important because the target development machine has approximately 4 GB RAM.


---

Resource Constraints

The project is intentionally designed around constrained hardware.

Primary constraints:

RAM        ≈ 4 GB
CPU        Limited
Storage    Limited
Dependency Low
Architecture Micro-Module
Runtime    Stateful

Design priorities:

small modules

low dependency count

bounded memory

deterministic state transitions where possible

trigger-based AI usage

disk-backed persistence where appropriate

regression testing

checkpoint/recovery

no unnecessary frameworks


Large models are not considered the solution to the core architectural problem.


---

Brain Subsystem Simulator

A separate research direction exists for a larger-scale neural subsystem simulator.

The current experimental target is:

Hippocampus       40,000,000 logical cells
Motor Cortex      60,000,000 logical cells
--------------------------------------------
Total             100,000,000 logical cells

The proposed neuron model is:

Leaky Integrate-and-Fire (LIF)

The implementation target is:

NumPy
Vectorization
Block / Chunk Processing

The system must not create 100 million Python neuron objects.

The 100M-cell design is a research/simulation scale and is not a requirement that the entire simulator run simultaneously on the 4 GB production machine.

The practical AE01M cognitive runtime remains a small micro-architecture.


---

Environment Simulator

Before physical hardware, the project uses a lightweight Text/State Simulator.

The simulator should contain:

World State
Time
Events
Needs
Actions
Consequences
Experience

The loop is:

World
  ↓
Perception
  ↓
AE01M
  ↓
Decision
  ↓
Action
  ↓
World Changes
  ↓
Experience
  ↓
Learning
  ↺

This provides a safe environment for testing autonomous cognition without requiring a physical robot.

A heavy 3D simulator is not currently required.


---

Tools, Web and Environment

External capabilities are considered services around the cognitive core.

Examples:

Web
Tools
Computer
MCP
Local AI
Sensors
Robot

They should not become the owner of the cognitive state.

The intended relationship is:

Cognitive Core
      ↓
Action Request
      ↓
Safety / Permission
      ↓
Tool / Environment
      ↓
Result
      ↓
Experience

Internet access, when introduced, should initially be treated as a research capability:

Search
 ↓
Read
 ↓
Extract
 ↓
Validate
 ↓
Learn
 ↓
Memory

External information should not be written directly into trusted memory without evaluation.


---

Claude Code and External Projects

Claude Code and other agent frameworks are treated as reference architecture / infrastructure, not as the brain itself.

Useful concepts include:

agent lifecycle

capability boundaries

tool execution

permissions

memory ownership

task orchestration

concurrency patterns

persistent state


The project should not replace its Cognitive Core with an external agent loop.

Likewise, BrainCog is used as a source of ideas and research reference rather than being installed wholesale as the primary AE01M dependency.

The same principle applies to other external repositories:

External Project
      ↓
Study
      ↓
Identify useful mechanism
      ↓
Extract concept / minimal implementation
      ↓
Adapt to AE01M
      ↓
Focused Test
      ↓
Regression

External architecture does not automatically become AE01M architecture.


---

Current Development Status

The project currently has the following major components:

Cognitive Architecture / AI Brain       ✅
Perception                              ✅
Current State                           ✅
Working Memory                          ✅
Episodic Memory                         ✅
Semantic Memory                         ✅
Identity / Self Model                   ✅
Cognitive Loop                          ✅
Learning Pipeline                       ✅
Prediction / Reflection                 ✅
Brain Integration                       ✅
Action Module                           ✅
Safety / Action Gate                    ✅
Autonomous Step                         ✅
Autonomous Runtime Loop                 ✅
Goal / Intention / Teaching             ✅
Memory Consolidation                    ✅
Associative Recall Prototype             ✅
Associative Recall → CognitiveLoop       ⚠️
Semantic / Contextual Recall             ⏳
Self-directed Learning Loop              ⏳
Autonomous Perception → Think → Act      ⏳
Persistent Memory / Continuity            ⏳
Environment Interaction                  ⏳
Autonomous Life Loop                     ⏳
Long-term Cognitive Development          ⏳
AE01M autonomous life                    ⏳

The current project milestone is the Associative Recall / Memory stage.

The latest regression baseline recorded in the project is:

363 tests — OK

This baseline is treated as a protected checkpoint for subsequent development.


---

Current Roadmap

The project roadmap is intentionally sequential.

PHASE 0
Foundation / Safety
        ↓
PHASE 1
Newborn Micro-Brain
        ↓
PHASE 2
Brain-like Memory
        ↓
PHASE 3
Learning + Reflection
        ↓
PHASE 4
Autonomous Cognitive Loop
        ↓
PHASE 5
Self-directed Growth
        ↓
PHASE 6
Local AI / Qwen
        ↓
PHASE 7
Tools / Web / Computer
        ↓
PHASE 8
Personal Assistant
        ↓
PHASE 9
Embodiment / Robot

The practical near-term sequence is:

CURRENT
Brain-like Memory
      ↓
Semantic / Contextual Recall
      ↓
Self-directed Learning Loop
      ↓
Autonomous Perception → Think → Decide → Act
      ↓
Persistent Memory / Continuity
      ↓
Environment Interaction
      ↓
Autonomous Life Loop
      ↓
Long-term Cognitive Development
      ↓
AE01M Personal Cognitive Assistant


---

Development Rules

The project is intentionally protected against uncontrolled scope expansion.

Every implementation task must answer:

1. Which Phase does this belong to?
2. What problem does it solve?
3. Which existing module does it extend?
4. Which files/contracts are affected?
5. How will success be tested?

If these cannot be answered, the task should not be implemented yet.


---

No Scope Creep

Ideas such as:

Voice
Vision
Web
Robot
GUI
New LLM
Large Neural Network
Advanced Self-awareness

are placed into a future backlog unless they are required by the current Phase.

A new idea must not automatically change the active roadmap.


---

Test First / Regression Protection

The development cycle is:

Current Contract
      ↓
Implement
      ↓
Focused Tests
      ↓
Regression
      ↓
Architecture Check
      ↓
Git Checkpoint
      ↓
Next Task

Existing tests must not be removed or weakened simply to make a new implementation pass.

A failed test is treated as information about the implementation, not as permission to delete the test.


---

Checkpoints and Recovery

Before risky changes:

KNOWN GOOD CHECKPOINT
        ↓
EXPERIMENT
        ↓
PASS → Keep
FAIL → Repair / Rollback

Source code, persistent cognitive state, and experimental data should remain separated.

Experimental data must not overwrite the real identity or memory state.


---

Definition of Success

The project is not considered successful merely because it can answer questions.

The long-term success criteria are behavioral and architectural.

AE01M should eventually be able to:

Receive a goal
      ↓
Understand the goal
      ↓
Recall relevant experience
      ↓
Reason
      ↓
Create an intention
      ↓
Check safety
      ↓
Plan
      ↓
Act
      ↓
Observe the result
      ↓
Verify
      ↓
Reflect
      ↓
Identify knowledge gaps
      ↓
Create the next LearningTask
      ↓
Learn
      ↓
Store knowledge / skill
      ↓
Reuse it
      ↓
Continue

The critical milestone is therefore not:

> “AE01M became smarter.”



It is:

> “AE01M can identify what it needs to learn, learn it, remember it, evaluate the result, and use the acquired capability in a future cycle without requiring the developer to hard-code the answer.”




---

Long-Term Vision

The intended evolution is:

NEWBORN
                    │
                    ▼
                EXPERIENCE
                    │
                    ▼
                  MEMORY
                    │
                    ▼
                LEARNING
                    │
                    ▼
               CAPABILITY
                    │
                    ▼
                ADAPTATION
                    │
                    ▼
              DEVELOPMENT
                    │
                    ▼
          PERSONAL COGNITIVE ASSISTANT
                    │
                    ▼
               EMBODIMENT
                    │
                    ▼
                  ROBOT

The robot is therefore not the starting point.

The robot is the eventual body of a cognitive system that has already been developed in software.


---

The Core Philosophy

The Transcending Form follows a simple principle:

> Do not hard-code intelligence when it is possible to build a mechanism that can learn the capability.



The project therefore focuses on:

Mechanism
   >
Preloaded Knowledge

and:

Learning Capability
   >
Hard-coded Behavior

while maintaining:

Safety
Identity
User Goals
State Integrity
Resource Limits

as protected boundaries.


---

Final Project Objective

The long-term objective of AE01M is to create a small local cognitive architecture that begins as a Newborn Brain, receives goals and teaching from its owner, accumulates experience and memory, learns from outcomes, develops capabilities, maintains continuity across sessions, and eventually operates as a persistent personal cognitive assistant and, later, an embodied system.

The project is intentionally incremental.

The immediate objective is not to build the final AI.

The immediate objective is to build the smallest cognitive mechanism that can learn and grow, prove it experimentally, and then allow the system's capabilities to emerge progressively from that foundation.


---

Project Status

Current focus:

Brain-like Memory
        ↓
Semantic / Contextual Recall
        ↓
Autonomous Learning Growth

Regression baseline:

363 tests — OK

Long-term target:

Newborn
  ↓
Learn
  ↓
Remember
  ↓
Think
  ↓
Act
  ↓
Reflect
  ↓
Develop
  ↺

The Transcending Form — AE01M

A research project exploring how a small local cognitive architecture can develop capability through memory, experience, learning, and autonomous cognitive cycles. :::
