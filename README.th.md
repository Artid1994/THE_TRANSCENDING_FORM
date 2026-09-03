AE01M — Project Context / Current Plan

AE01M (THE TRANSCENDING FORM) เป็นโครงการพัฒนา AI Agent ที่มี Cognitive Runtime ของตัวเอง เป้าหมายหลักไม่ใช่การสร้าง chatbot แต่คือการสร้างระบบที่สามารถเรียนรู้จากประสบการณ์ พัฒนาความสามารถ และนำความรู้ไปใช้กับงานวิจัยคณิตศาสตร์/วิทยาศาสตร์ได้

เป้าหมายหลัก

เป้าหมายระยะยาวคือให้ AE01M สามารถ:

รับโจทย์ → วิเคราะห์ → ตรวจว่าขาดความรู้อะไร → เรียนรู้ → ฝึก → ตรวจสอบ → สร้างสมมติฐาน → ทดลองด้วย Python → ประเมินผล → สะท้อนผล → ปรับปรุง → จดจำ → นำประสบการณ์ไปใช้ครั้งต่อไป

โจทย์วิจัยหลักที่วางไว้คือ Quantum Measurement Problem โดยเฉพาะการศึกษาความสัมพันธ์ระหว่าง quantum behavior, decoherence, environment/system size และ classical behavior

ยังไม่มีการอ้างว่า AE01M ค้นพบสูตรหรือคำตอบใหม่ทางฟิสิกส์แล้ว ปัจจุบันมีเพียง infrastructure สำหรับ numerical research และ research loop

Architecture หลัก

                         AE01M
                           │
              ┌────────────┴────────────┐
              │                         │
        Cognitive Runtime          Research Runtime
              │                         │
       ┌──────┼──────┐           ┌──────┼──────┐
       │      │      │           │      │      │
    Identity Memory Action    Hypothesis Model Experiment
       │      │      │                  │
       └──────┼──────┘                  ↓
              │                     Python
              ↓                       ↓
       Cognitive Loop             Evaluation
              │                       │
              └──────────┬────────────┘
                         ↓
                    Experience
                         ↓
                  Memory / Learning

Cognitive Strategy

แนวทางที่วางไว้คือการใช้ต้นทุนการคิดหลายระดับ:

System 0
Rule / Reflex / Safety
        ↓
System 1
Memory Graph / Association / Heuristic
        ↓
System 2
Local SLM / LLM

LLM ไม่ใช่ทั้งสมองของ AE01M แต่เป็นหนึ่ง component ใน Cognitive Runtime

Memory

Memory Graph เป็นศูนย์กลางสำคัญของการพัฒนา

Memory ไม่ควรเป็นเพียงฐานข้อมูล และไม่ควร hard-code ความสัมพันธ์ทั้งหมดล่วงหน้า

แนวคิด:

Experience
   ↓
Memory Cell
   ↕
Association
   ↕
Knowledge / Skill
   ↓
Recall
   ↓
Cognition
   ↓
Action
   ↓
Experience ใหม่

Memory Cell ควรมีกลไกสำหรับ activation, strengthening, decay, pruning และ association แต่ความสัมพันธ์ควรเกิดจากประสบการณ์ของระบบ ไม่ใช่กำหนดล่วงหน้าทั้งหมด

Learning Loop

Knowledge Gap
      ↓
Learning Task
      ↓
Research / Internet
      ↓
Learn
      ↓
Practice
      ↓
Python Verification
      ↓
Knowledge / Skill
      ↓
Memory
      ↓
นำไปใช้กับงานจริง

หลักสำคัญ:

"ไม่รู้ → เรียน → ตรวจสอบ → จำ → นำไปใช้"

AE01M ไม่ควรเพียงอ่านข้อมูลแล้วถือว่าเป็นความรู้ที่ถูกต้อง ต้องมี source, verification และประสบการณ์การใช้งานประกอบเมื่อเหมาะสม

Skill Matrix

Skill ไม่ควรเป็นเพียงตัวเลขที่กำหนดโดยมนุษย์

ควรมีหลักฐานจากประสบการณ์ เช่น:

Skill
├── level
├── confidence
├── attempts
├── success_count
├── failure_count
├── performance
├── resource_cost
├── latency
└── supporting_experiences

เป้าหมายคือให้ AE01M เรียนรู้ว่าวิธีใดทำงานได้ดีจากผลลัพธ์จริง และสามารถเลือก preferred strategy ในอนาคต

Research Loop

Research Agent ใช้ AI สำหรับ reasoning/hypothesis และใช้ Python สำหรับ deterministic computation และ validation

Research Problem
      ↓
Analyze
      ↓
Hypothesis
      ↓
Mathematical Model
      ↓
Python Simulation
      ↓
Parameter Search
      ↓
Evaluation
      ↓
Error Analysis
      ↓
Reflection
      ↓
ปรับ Hypothesis / Model
      ↺

ไม่ควรส่งข้อมูล numerical ดิบจำนวนมากให้ LLM หาก Python สามารถคำนวณ/สรุป metric ได้ก่อน

ตัวอย่าง:

Python:
parameter sweep
simulation
error
best result
comparison

        ↓

LLM:
วิเคราะห์ผล
เสนอ hypothesis ใหม่
เสนอการทดลองถัดไป

สถานะปัจจุบัน

ส่วนพื้นฐานจำนวนมากถูกสร้างแล้ว:

Foundation / Safety                 DONE
Cognitive Architecture              DONE
Perception / State                  DONE
Working Memory                      DONE
Episodic Memory                     DONE
Semantic Memory                     DONE
Identity / Self Model               DONE
Cognitive Loop                      DONE
Learning Pipeline                   DONE
Prediction / Reflection             DONE
Action + Safety Gate                DONE
Autonomous Step                     DONE
Autonomous Runtime Loop             DONE
Memory Consolidation                DONE
Associative Recall                  PROTOTYPE
Semantic / Contextual Recall        NEXT
Self-directed Learning              NEXT
Persistent Continuity               NEXT
Environment Interaction             NEXT
Autonomous Life Loop                NEXT
Long-term Cognitive Development     NEXT

มี regression baseline ที่ยืนยันแล้วคือ:

534 tests passed

Current Development Direction

ตอนนี้ไม่ควรขยายไปยัง feature ภายนอกจำนวนมาก

ลำดับปัจจุบัน:

1. ตรวจ Identity / Self Model ที่มีอยู่จริง
2. Identity Core
3. Role / Purpose
4. Skill Matrix + Evidence
5. Cognitive Strategy
6. Memory Graph Integration
7. Learning Loop
8. Research Loop
9. Integration Tests
10. UI แสดงข้อมูลจริง

ทำทีละ micro-step และต้องรักษา regression baseline

UI

UI มีเป้าหมายเป็น interface สำหรับระบบจริง ไม่ใช่ Cognitive Core

Tabs:

Chat
Memory
Research
System

UI ต้องอ่านข้อมูลจาก Runtime / Memory / Research จริง ไม่ใช้ mock data เพื่อทำให้หน้าตาดูสมบูรณ์

Simulator

Simulator ถ้ามีการสร้าง จะเป็น Text/State Simulator สำหรับทดสอบ autonomous cognitive loop ก่อน ไม่ใช่ 3D life simulator

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
World changes
 ↓
Experience
 ↓
Learning
 ↺

Research Infrastructure

มี Numerical Research infrastructure แล้ว แต่ต้องระวังว่า reference dynamics หรือ toy model ไม่ใช่ physical evidence

ผลจาก parameter landscape หรือ numerical experiment ปัจจุบันต้องตีความเป็นผลของ model ที่กำหนดไว้เท่านั้น

ห้ามสรุปว่าเป็น discovery ทางฟิสิกส์จนกว่าจะมีแบบจำลองและ validation ที่เหมาะสม

Constraints

เครื่องเป้าหมายมี RAM จำกัดประมาณ 4 GB

ดังนั้น:

- หลีกเลี่ยง framework agent ขนาดใหญ่
- ใช้ Python micro-agent/controller เป็นหลัก
- ใช้ LLM เฉพาะงาน reasoning/language ที่จำเป็น
- ใช้ NumPy/Python สำหรับ numerical computation
- หลีกเลี่ยงการสร้าง Python object จำนวนมหาศาล
- ไม่สร้างระบบซับซ้อนเกิน requirement
- ไม่เพิ่ม feature ที่อยู่นอก current phase

Development Rules

ทุกการแก้ไขต้อง:

Current State
   ↓
Contract
   ↓
Implement
   ↓
Focused Test
   ↓
Regression Test
   ↓
Checkpoint
   ↓
Next Step

กฎสำคัญ:

1. ห้ามเดาความสามารถที่ยังไม่มี
2. ห้ามบอกว่าระบบทำได้ถ้ายังไม่ได้ทดสอบ
3. ห้ามใช้ mock data แทนระบบจริงโดยไม่ระบุ
4. ห้าม hard-code ความสัมพันธ์ของ Memory ที่ควรเกิดจากประสบการณ์
5. ห้ามเพิ่ม scope เอง
6. ต้องตรวจ code ปัจจุบันก่อนแก้
7. ต้องรักษา regression baseline
8. ทำทีละ micro-step
9. ถ้าเป็นข้อมูลจาก GitHub/source ภายนอก ให้ตรวจ source จริงก่อนสรุป
10. แยกให้ชัดระหว่าง implemented, prototype, planned และ research hypothesis

สิ่งที่ยังไม่ควรทำตอนนี้

ยังไม่ต้องเพิ่ม:

- Voice
- Vision
- Robot
- 3D simulator
- 100M logical neurons ใน runtime จริง
- Self-modifying source code
- Agent framework ขนาดใหญ่
- เปลี่ยน LLM โดยไม่มีเหตุผลจาก requirement
- Feature ที่ไม่เกี่ยวกับ current phase

เป้าหมายของ AI Agent ที่เข้ามาช่วย

เมื่อทำงานกับ repository นี้ ให้ทำหน้าที่เป็น engineering/research agent:

1. ตรวจสิ่งที่มีอยู่จริงก่อน
2. เข้าใจ architecture ก่อนเสนอการแก้
3. ไม่สร้างระบบซ้ำกับของเดิม
4. เสนอการเปลี่ยนแปลงที่เล็กที่สุด
5. ทดสอบทุกการเปลี่ยนแปลง
6. รายงานผลตามจริง
7. ไม่อ้างเกินหลักฐาน
8. รักษาเป้าหมายหลักของ AE01M
9. ถ้าข้อมูลไม่พอ ให้ถามหรือขอตรวจไฟล์ที่เกี่ยวข้อง
10. อย่าขยาย scope โดยไม่ได้รับอนุญาต

เป้าหมายสูงสุดของระบบ

AE01M
  ↓
เรียนรู้สิ่งที่ยังไม่รู้
  ↓
ฝึกและตรวจสอบ
  ↓
สะสมประสบการณ์
  ↓
พัฒนาความรู้และทักษะ
  ↓
ตั้งสมมติฐาน
  ↓
ทดลอง
  ↓
ประเมิน
  ↓
ปรับปรุง
  ↓
สร้างความสามารถที่ดีขึ้นจากประสบการณ์

แกนกลางของโครงการคือ:

Cognitive Runtime + Memory + Learning + Research

ไม่ใช่เพียง LLM chatbot
