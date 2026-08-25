AE01M — The Transcending Form

«สถาปัตยกรรมการรู้คิดภายในเครื่อง สำหรับสร้างจิตประดิษฐ์เริ่มต้นแบบ Newborn Brain»

AE01M / The Transcending Form (TTF) เป็นโครงการทดลองสร้างสถาปัตยกรรมการรู้คิดภายในเครื่อง (Local Cognitive Architecture) ที่มีขนาดเล็ก มีสถานะต่อเนื่อง (stateful) และสามารถเริ่มต้นในสภาพ Newborn Brain จากนั้นเรียนรู้จากประสบการณ์ สะสมความทรงจำ พัฒนาความสามารถ และในระยะยาวทำงานเป็นผู้ช่วยส่วนตัวด้านการรู้คิดที่มีสถานะต่อเนื่องได้

โครงการนี้ไม่ได้มุ่งสร้าง Chatbot ที่ต้องเรียก LLM เพื่อคิดในทุก cycle

เป้าหมายระยะยาวคือการสร้าง กลไกการรู้คิดที่อยู่รอบโมเดล AI เพื่อให้โมเดล AI เป็นเพียงองค์ประกอบหนึ่งของระบบ ไม่ใช่ตัวระบบทั้งหมด

---

วิสัยทัศน์

แนวคิดหลักคือ:

สมองแรกเกิด (Newborn Brain)
        ↓
ประสบการณ์
        ↓
การรับรู้
        ↓
ความทรงจำ
        ↓
การรู้คิด
        ↓
เป้าหมาย / เจตจำนง
        ↓
การตัดสินใจ
        ↓
การกระทำ
        ↓
ผลตอบกลับ
        ↓
การสะท้อนผล
        ↓
การเรียนรู้
        ↓
การพัฒนา
        ↺

ระบบควรค่อย ๆ สะสมความรู้ ทักษะ กลยุทธ์ และความสามารถทางพฤติกรรมจากประสบการณ์ แทนที่จะเขียนความสามารถทั้งหมดไว้ล่วงหน้าแบบ hard-code

เป้าหมายระยะยาวคือผู้ช่วยส่วนตัวที่มีพฤติกรรมในลักษณะ JARVIS ในระดับสถาปัตยกรรมและพฤติกรรม:

ผู้ใช้
  ↓
AE01M
  ↓
เข้าใจ
  ↓
จดจำ
  ↓
ให้เหตุผล
  ↓
วางแผน
  ↓
ลงมือทำ
  ↓
ตรวจสอบผล
  ↓
เรียนรู้
  ↓
ปรับปรุง
  ↺

นี่เป็นโครงการวิจัยและทดลอง โครงการไม่ได้อ้างว่าระบบจะมีจิตสำนึก มีความคิดเหมือนมนุษย์ หรือมีสติปัญญาทั่วไป (AGI)

---

หลักการแกนกลาง

กฎสำคัญที่สุดของสถาปัตยกรรมคือ:

AI Model ≠ Identity
AI Model ≠ Memory
AI Model ≠ Cognitive Runtime

โมเดล AI เช่น Qwen ถูกมองเป็นองค์ประกอบด้านการรู้คิด/ภาษา ซึ่งสามารถเปลี่ยนหรือถอดออกได้

Identity, Memory, Development State, Goal, Experience และ Runtime State ต้องอยู่นอกโมเดล

ทำให้สามารถเปลี่ยนโมเดล AI ได้โดยไม่ทำลาย Identity และสถานะที่ระบบสะสมมา

---

สิ่งที่เรากำลังสร้าง

เราไม่ได้พยายามโปรแกรมหุ่นยนต์ให้ฉลาดสำเร็จรูป

เรากำลังสร้าง กลไกสำหรับการพัฒนาความสามารถทางการรู้คิด

ว่างเปล่า / NEWBORN
        ↓
การสอน
        ↓
ประสบการณ์
        ↓
ความทรงจำ
        ↓
การเรียนรู้
        ↓
ความสามารถ
        ↓
การปรับตัว
        ↓
การพัฒนา
        ↓
ประสบการณ์ใหม่
        ↺

ผู้ใช้เป็นผู้กำหนดเป้าหมาย การสอน ขอบเขต และทรัพยากร

AE01M ควรค่อย ๆ เรียนรู้วิธีบรรลุเป้าหมายเหล่านั้น

สิ่งที่ Learning สามารถเปลี่ยนได้:

- ความรู้
- กลยุทธ์
- ทักษะ
- การคาดการณ์
- วิธีการทำงาน
- การแตกงาน
- ความสัมพันธ์ที่เรียนรู้

สิ่งที่ Learning ไม่ควรเปลี่ยนโดยพลการ:

- เป้าหมายของ Owner/User
- Hard Safety Boundary
- Identity/Core State ที่ได้รับการป้องกัน
- กลไกป้องกัน Runtime ที่สำคัญ

---

สถาปัตยกรรม

สถาปัตยกรรมเชิงแนวคิดในปัจจุบัน:

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
     Identity             Perception            Internal State
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

Cognitive Core ถูกออกแบบเป็นโมดูลขนาดเล็กหลายตัว ไม่ใช่ framework ขนาดใหญ่เพียงตัวเดียว

---

Cognitive Cycle

วงจรการรู้คิดพื้นฐานคือ:

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

ในอนาคต "autonomous_step()" จะเป็นตัวแทนของ cognitive cycle หนึ่งรอบ

สถาปัตยกรรมตั้งใจแยก cognitive cycle ออกจาก scheduler หรือ background process อย่างชัดเจน โดยจะเพิ่มการทำงานอัตโนมัติแบบต่อเนื่องหลังจากพิสูจน์ state transition และ lifecycle แล้ว

---

Newborn Micro-Brain

สมองเริ่มต้นควรมีขนาดเล็กที่สุดเท่าที่จำเป็น

เป้าหมายไม่ใช่ preload ความรู้จำนวนมาก

แต่ละ instance ใหม่ควรเริ่มต้นในลักษณะ:

Knowledge       = น้อยที่สุด
Experience      = ว่าง
Episodic Memory = ว่าง
Semantic Memory = ว่าง
Skills          = ขั้นต่ำ
Goals           = ได้รับจากภายนอก
Identity        = โครงสร้างสถานะที่ได้รับการป้องกัน

กลไกสำหรับเรียนรู้จะมีอยู่ก่อนที่ความรู้จะมี

จึงสามารถแยก:

Knowledge

ออกจาก:

ความสามารถในการเรียนรู้ Knowledge

สิ่งที่สองคือสิ่งที่โครงการพยายามสร้างเป็นหลัก

---

Memory Architecture

Memory เป็นหนึ่งในองค์ประกอบหลักของ AE01M

Foundation ปัจจุบันประกอบด้วย:

Working Memory
Episodic Memory
Semantic Memory
Experience Objects
Recall Index
Semantic Index
Memory Consolidation

เป้าหมายของ Brain-like Memory คือ:

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

กลไก Memory ในระยะต่อไปประกอบด้วย:

- Associative Recall
- Contextual Recall
- Salience
- Novelty
- Relevance
- Confidence
- Repetition
- Consolidation
- Decay
- Forgetting
- Reconsolidation
- Self Memory
- Memory Association

เป้าหมายไม่ใช่สร้างฐานข้อมูลข้อความแบบไม่จำกัด

เป้าหมายคือสร้างกลไก Memory ที่สามารถพิจารณาว่าอะไรมีประโยชน์ อะไรเกี่ยวข้อง อะไรควร consolidate และอะไรควรถูกพัฒนาเป็นความรู้

---

Cell-Based Memory

สถาปัตยกรรม Memory ในอนาคตจะใช้แนวคิด Computational Memory Cell

Cell เหล่านี้เป็น abstraction ทางซอฟต์แวร์ ไม่ได้หมายความว่าเป็น neuron ทางชีววิทยาโดยตรง

AE01M Memory
│
├── Working Cells
├── Episodic Cells
├── Association Cells
├── Semantic Cells
├── Self Cells
└── Safety Cells

ข้อมูลของ Cell อาจประกอบด้วย:

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

Memory ต้องมีขนาดจำกัด

เมื่อเกิด Memory Pressure:

New Experience
      ↓
ตรวจสอบความจุ Memory
      ↓
Consolidation
      ↓
Merge / Promote / Forget
      ↓
คืนพื้นที่
      ↓
บันทึกประสบการณ์ใหม่

สถาปัตยกรรม Cell ไม่ได้มีเป้าหมายลบ Memory architecture เดิม แต่เป็นชั้นสำหรับจัดระเบียบและจัดเก็บข้อมูล โดยต้องรักษา interface และ regression behavior เดิมไว้

---

Associative Memory

ปัจจุบันมีต้นแบบ Associative Recall แล้ว แต่ Contextual / Semantic Recall ยังอยู่ระหว่างการพัฒนา

เป้าหมายคือ:

Memory A
   ↕
Association
   ↕
Memory B
   ↕
Association
   ↕
Memory C

เพื่อให้สามารถเรียกคืน Memory จาก:

- บริบท
- ความสัมพันธ์ทางความหมาย
- ประสบการณ์ที่ผ่านมา
- Salience
- Relevance
- Association

แทนการพึ่งพา Exact String Matching เพียงอย่างเดียว

---

Learning

Learning Pipeline มีรูปแบบ:

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

หลักสำคัญคือ:

Learning เปลี่ยน "วิธีการ" เพื่อบรรลุเป้าหมาย

ไม่ใช่:

Learning เปลี่ยน "เป้าหมาย" ของ Owner โดยพลการ

ตัวอย่าง:

เป้าหมายของผู้ใช้:
เรียนรู้ BLE บน ESP32

AE01M:
ค้นคว้า
 ↓
ทดลอง
 ↓
ล้มเหลว
 ↓
Reflection
 ↓
พบ Knowledge Gap
 ↓
สร้าง LearningTask ถัดไป
 ↓
เรียนรู้ใหม่

ผู้ใช้ไม่จำเป็นต้องกำหนดทุกบทเรียนย่อยด้วยตนเอง

---

Reflection

Reflection ทำหน้าที่เปลี่ยนประสบการณ์ให้กลายเป็น Learning

Reflection สามารถระบุ:

SUCCESS
FAILURE
MISSING_KNOWLEDGE

และสร้าง:

Lesson
Next Learning Task

เป้าหมาย Autonomous Learning Loop:

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
มี Knowledge Gap หรือไม่?
 ├── NO → ดำเนินการ / เสร็จสิ้น
 │
 └── YES
       ↓
   New LearningTask
       ↓
      Learn
       ↺

---

Autonomous Growth

AE01M จะถือว่าเริ่มมี Growth Loop จริงเมื่อสามารถ:

1. จดจำประสบการณ์ของตัวเองได้
2. ประเมินได้ว่าตัวเองยังขาดอะไร
3. สร้างและทำ LearningTask ถัดไปได้เอง

วงจรเป้าหมาย:

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

นี่คือคำจำกัดความของ Autonomous Growth ในโครงการ

ไม่ได้หมายความว่าระบบมีจิตสำนึก

---

Goal / Intention / Teaching

ผู้ใช้คือ Owner และเป็นแหล่งกำหนดเป้าหมายระดับสูง

ลำดับการควบคุม:

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

AE01M สามารถเรียนรู้วิธีที่ดีขึ้นเพื่อบรรลุเป้าหมาย

แต่ไม่ควรเปลี่ยนเป้าหมายของ Owner โดยเงียบ ๆ

ระบบ Teaching ในระยะยาว:

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

คู่มือควรกำหนดสิ่งที่ต้องเรียนและวิธีประเมินผล โดยไม่จำเป็นต้องบรรจุคำตอบทั้งหมดไว้ล่วงหน้า

---

Safety Architecture

Safety เป็นขอบเขตทางสถาปัตยกรรมที่ได้รับการป้องกัน

Cognition
   ↓
Thought / Intention
   ↓
Cognitive Safety Gate
   ↓
Decision
   ↓
Action

Hard Safety Boundary ต้องได้รับการป้องกันจาก Learning ปกติ

ระบบสามารถเรียนรู้ประสบการณ์เกี่ยวกับความปลอดภัยได้ แต่ข้อมูลที่เรียนรู้ไม่ควรถูกเปลี่ยนเป็น Hard Rule ถาวรโดยอัตโนมัติ

ต้องแยก:

HARD SAFETY

ออกจาก:

LEARNED EXPERIENCE ABOUT SAFETY

Hard Boundary ยังคงได้รับการป้องกัน

---

Local AI / Qwen

Qwen และ Local AI Model อื่น ๆ เป็นทรัพยากรด้านการรู้คิดที่เรียกใช้เมื่อจำเป็น

             AE01M
               │
       ┌───────┴────────┐
       │ Native Core    │
       │ ขนาดเล็ก       │
       └───────┬────────┘
               │
        Local AI เมื่อจำเป็น
               │
             Qwen

ไม่ควรเรียก LLM ในทุก cognitive cycle

ตัวอย่าง:

งาน State ที่ง่าย
    → Native Cognitive Core

งานภาษา
    → Local AI

งาน Reasoning ที่ซับซ้อน
    → Local AI + Cognitive Core

งาน Deterministic
    → Tool โดยตรง

การแยกส่วนนี้สำคัญมาก เนื่องจากเครื่องเป้าหมายมี RAM ประมาณ 4 GB

---

ข้อจำกัดทรัพยากร

โครงการออกแบบโดยคำนึงถึง Hardware ที่จำกัด:

RAM        ≈ 4 GB
CPU        จำกัด
Storage    จำกัด
Dependency ต่ำ
Architecture Micro-Module
Runtime    Stateful

ลำดับความสำคัญ:

- โมดูลขนาดเล็ก
- Dependency ต่ำ
- Memory มีขอบเขต
- State Transition ชัดเจน
- เรียก AI แบบ Trigger-based
- ใช้ Disk สำหรับ Persistence เมื่อเหมาะสม
- Regression Testing
- Checkpoint / Recovery
- ไม่ใช้ Framework ใหญ่โดยไม่จำเป็น

โมเดลที่ใหญ่ขึ้นไม่ใช่คำตอบหลักของปัญหา Architecture

---

Brain Subsystem Simulator

มีทิศทางการทดลองแยกสำหรับ Neural Subsystem Simulator ขนาดใหญ่:

Hippocampus       40,000,000 logical cells
Motor Cortex      60,000,000 logical cells
--------------------------------------------
รวม               100,000,000 logical cells

โมเดล neuron ที่กำหนดไว้:

Leaky Integrate-and-Fire (LIF)

แนวทาง implementation:

NumPy
Vectorization
Block / Chunk Processing

ต้องไม่สร้าง Python Object จำนวน 100 ล้านตัว

100M cells เป็นขนาดเชิงวิจัย/การจำลอง และ ไม่ใช่ข้อกำหนดว่าต้องรันทั้งระบบพร้อมกันบนเครื่อง RAM 4 GB

AE01M Cognitive Runtime ที่ใช้งานจริงยังคงเป็น Micro-Architecture ขนาดเล็ก

---

Environment Simulator

ก่อนต่อ Hardware จริง จะมี Text/State Simulator แบบเบา:

World State
Time
Events
Needs
Actions
Consequences
Experience

วงจร:

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

Simulator ทำหน้าที่เป็นสนามทดสอบ Autonomous Cognition โดยไม่ต้องเสี่ยงกับระบบจริง

ยังไม่จำเป็นต้องใช้ 3D Simulator ขนาดใหญ่

---

Tools / Web / Environment

ความสามารถภายนอกถือเป็นบริการรอบ Cognitive Core:

Web
Tools
Computer
MCP
Local AI
Sensors
Robot

สิ่งเหล่านี้ไม่ควรเป็นเจ้าของ Cognitive State

ความสัมพันธ์ที่ต้องการ:

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

เมื่อเพิ่ม Internet ในอนาคต จะใช้เป็นแหล่ง Research:

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

ข้อมูลจากภายนอกไม่ควรถูกเขียนเข้า Trusted Memory โดยตรงโดยไม่มี Evaluation

---

Claude Code และโครงการภายนอก

Claude Code และ Agent Framework อื่น ๆ ถูกใช้เป็น Reference Architecture / Infrastructure ไม่ใช่สมองของ AE01M

แนวคิดที่สามารถศึกษาได้:

- Agent Lifecycle
- Capability Boundary
- Tool Execution
- Permission
- Memory Ownership
- Task Orchestration
- Concurrency
- Persistent State

แต่ Cognitive Core ของ AE01M จะไม่ถูกแทนที่ด้วย Agent Loop จาก Framework ภายนอก

เช่นเดียวกับ BrainCog ซึ่งใช้เป็นแหล่งศึกษาและอ้างอิงกลไก ไม่ได้ติดตั้งทั้ง Framework เป็น Dependency หลักของ AE01M

หลักการเดียวกันใช้กับ Repository ภายนอกอื่น ๆ:

External Project
      ↓
ศึกษา
      ↓
หา Mechanism ที่มีประโยชน์
      ↓
Extract Concept / Minimal Implementation
      ↓
Adapt เข้ากับ AE01M
      ↓
Focused Test
      ↓
Regression

Architecture ของโครงการภายนอกจะไม่ถูกนำมาใช้เป็น Architecture ของ AE01M โดยอัตโนมัติ

---

สถานะการพัฒนาปัจจุบัน

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
Goal / Intention / Teaching              ✅
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

สถานะปัจจุบันของโครงการอยู่ที่ Associative Recall / Memory Stage

Regression baseline ล่าสุดที่บันทึกไว้:

363 tests — OK

Baseline นี้ถือเป็น Checkpoint ที่ต้องรักษาไว้ในการพัฒนาต่อ

---

Roadmap ปัจจุบัน

Roadmap ถูกออกแบบให้ทำตามลำดับ:

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

ลำดับงานระยะใกล้:

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

กฎการพัฒนาโครงการ

โครงการมีระบบป้องกัน Scope Creep อย่างชัดเจน

ทุกงานต้องตอบ:

1. งานนี้อยู่ Phase ไหน?
2. แก้ปัญหาอะไร?
3. ต่อกับ Module เดิมตัวไหน?
4. กระทบไฟล์ / Contract ใด?
5. จะพิสูจน์ความสำเร็จอย่างไร?

ถ้าตอบไม่ได้ → ยังไม่ควร Implement

---

No Scope Creep

ไอเดีย เช่น:

Voice
Vision
Web
Robot
GUI
New LLM
Large Neural Network
Advanced Self-awareness

จะถูกส่งเข้า Future Backlog หากยังไม่จำเป็นกับ Phase ปัจจุบัน

ไอเดียใหม่ไม่สามารถเปลี่ยน Roadmap ปัจจุบันโดยอัตโนมัติ

---

Test และ Regression Protection

Workflow:

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

ห้ามลบหรือทำให้ Test อ่อนลงเพียงเพื่อให้ Implementation ผ่าน

Test ที่ล้มเหลวถือเป็นข้อมูลเกี่ยวกับปัญหาของ Implementation ไม่ใช่เหตุผลในการลบ Test

---

Checkpoint และ Recovery

ก่อนการแก้ไขที่มีความเสี่ยง:

KNOWN GOOD CHECKPOINT
        ↓
EXPERIMENT
        ↓
PASS → Keep
FAIL → Repair / Rollback

Source Code, Persistent Cognitive State และ Experimental Data ต้องแยกจากกัน

Experimental Data ต้องไม่เขียนทับ Identity หรือ Memory จริง

---

Definition of Success

โครงการจะไม่ถือว่าสำเร็จเพียงเพราะ AE01M ตอบคำถามได้

เกณฑ์ความสำเร็จระยะยาวคือ:

รับ Goal
      ↓
เข้าใจ Goal
      ↓
เรียก Memory ที่เกี่ยวข้อง
      ↓
Reasoning
      ↓
สร้าง Intention
      ↓
ตรวจ Safety
      ↓
วางแผน
      ↓
ลงมือทำ
      ↓
สังเกตผล
      ↓
ตรวจสอบผล
      ↓
Reflection
      ↓
ระบุ Knowledge Gap
      ↓
สร้าง LearningTask ถัดไป
      ↓
เรียนรู้
      ↓
เก็บ Knowledge / Skill
      ↓
นำกลับมาใช้
      ↓
ดำเนินต่อ

Milestone ที่สำคัญจึงไม่ใช่:

«“AE01M ฉลาดขึ้น”»

แต่คือ:

«“AE01M สามารถระบุสิ่งที่ต้องเรียนรู้ เรียนรู้ จดจำ ประเมินผล และนำความสามารถที่ได้ไปใช้ในรอบถัดไป โดยไม่จำเป็นต้องให้ผู้พัฒนาฮาร์ดโค้ดคำตอบใหม่ทุกครั้ง”»

---

วิสัยทัศน์ระยะยาว

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

Robot จึงไม่ใช่จุดเริ่มต้น

Robot คือ ร่างกายของ Cognitive System ที่ได้รับการพัฒนาในซอฟต์แวร์ก่อน

---

ปรัชญาหลักของโครงการ

The Transcending Form ยึดหลัก:

«อย่า Hard-code Intelligence หากสามารถสร้างกลไกที่เรียนรู้ความสามารถนั้นได้»

ดังนั้นโครงการให้ความสำคัญกับ:

Mechanism
   >
Preloaded Knowledge

และ:

Learning Capability
   >
Hard-coded Behavior

โดยมีสิ่งเหล่านี้เป็น Boundary ที่ได้รับการป้องกัน:

Safety
Identity
User Goals
State Integrity
Resource Limits

---

เป้าหมายสุดท้ายของโครงการ

เป้าหมายระยะยาวของ AE01M คือการสร้าง Local Cognitive Architecture ขนาดเล็ก ที่เริ่มต้นเป็น Newborn Brain รับ Goal และการสอนจาก Owner สะสมประสบการณ์และความทรงจำ เรียนรู้จากผลลัพธ์ พัฒนาความสามารถ รักษาความต่อเนื่องข้าม Session และในระยะยาวทำงานเป็น Personal Cognitive Assistant ที่มีสถานะต่อเนื่อง รวมถึงสามารถพัฒนาไปสู่ระบบที่มีร่างกายและ Robot ได้

โครงการจะพัฒนาแบบค่อยเป็นค่อยไป

เราไม่ได้พยายามสร้าง AI สุดท้ายตั้งแต่วันแรก

เป้าหมายแรกคือการสร้าง กลไกการรู้คิดที่เล็กที่สุดที่สามารถเรียนรู้และเติบโตได้ พิสูจน์ด้วยการทดลอง แล้วจึงปล่อยให้ความสามารถของระบบเพิ่มขึ้นจากพื้นฐานนั้น

---

สถานะโครงการ

งานที่กำลังมุ่งเน้น:

Brain-like Memory
        ↓
Semantic / Contextual Recall
        ↓
Autonomous Learning Growth

Regression Baseline:

363 tests — OK

เป้าหมายระยะยาว:

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

«โครงการวิจัยเพื่อสำรวจว่า Local Cognitive Architecture ขนาดเล็กสามารถพัฒนาความสามารถผ่าน Memory, Experience, Learning และ Autonomous Cognitive Cycle ได้อย่างไร»
