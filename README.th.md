# AE01M — The Transcending Form

**AE01M** คือโครงการทดลองสร้าง **Cognitive Architecture หรือ “สมองซอฟต์แวร์” ขนาดเล็ก** ที่เริ่มต้นจากสถานะคล้าย Newborn Brain แล้วค่อย ๆ เรียนรู้จากประสบการณ์ จดจำสิ่งที่เรียนรู้ ประเมินผล และพัฒนาความสามารถของตัวเอง

เป้าหมายไม่ใช่การสร้าง Chatbot ที่มีคำตอบสำเร็จรูปจำนวนมาก แต่คือการสร้าง **กลไกพื้นฐานที่ทำให้ AI สามารถเรียนรู้และพัฒนาความสามารถจากประสบการณ์ได้**

โครงการยังอยู่ในขั้นวิจัยและพัฒนา จึงไม่อ้างว่า AE01M มีจิตสำนึกหรือคิดเหมือนมนุษย์

## แนวคิดหลัก

AE01M แยก “สมอง” ออกจาก “โมเดล AI”

```text
AI Model ≠ Identity
AI Model ≠ Memory
AI Model ≠ Cognitive Runtime
```

โมเดลอย่าง Qwen เป็นเครื่องมือสำหรับงานด้านภาษาและการให้เหตุผลที่ซับซ้อน ส่วน Cognitive Runtime, Memory, Learning และ State เป็นองค์ประกอบของ AE01M เอง

แนวคิดคือให้ระบบมีความสามารถพื้นฐานก่อน แล้วให้ความรู้และทักษะเพิ่มขึ้นจากการเรียนรู้ แทนการ hard-code ความสามารถทั้งหมดตั้งแต่ต้น

## AE01M ทำงานอย่างไร

วงจรหลักที่ต้องการสร้างคือ

```text
รับรู้
  ↓
เรียกความจำ
  ↓
คิด
  ↓
กำหนดเป้าหมาย / ความตั้งใจ
  ↓
ตัดสินใจ
  ↓
ลงมือทำ
  ↓
รับผลลัพธ์
  ↓
ประเมิน
  ↓
สะท้อนผล
  ↓
เรียนรู้
  ↓
อัปเดตความจำ
  ↓
นำสิ่งที่เรียนรู้ไปใช้ในรอบถัดไป
  ↺
```

เป้าหมายระยะยาวคือให้วงจรนี้สามารถทำงานต่อเนื่องได้โดยไม่ต้องให้ผู้พัฒนาเรียกแต่ละขั้นตอนเอง

## การเรียนรู้

หลักสำคัญคือแยก **เป้าหมาย** ออกจาก **วิธีการ**

ผู้ใช้กำหนดเป้าหมาย เช่น

```text
“สร้างโปรแกรมที่ทำงานได้ตามข้อกำหนด”
```

AE01M สามารถเรียนรู้และเปลี่ยนวิธีการเพื่อไปถึงเป้าหมายนั้นได้ เช่น

```text
ค้นข้อมูล
  ↓
เรียนรู้
  ↓
ทดลอง
  ↓
ตรวจผล
  ↓
พบข้อผิดพลาด
  ↓
วิเคราะห์
  ↓
ปรับวิธี
  ↓
ทดลองใหม่
```

แต่การเรียนรู้ไม่ควรมีสิทธิ์เปลี่ยนเป้าหมายหลักของผู้ใช้หรือแก้ Core และ Safety Boundary โดยพลการ

ดังนั้น:

```text
เรียนรู้วิธีทำงาน       ✓
สร้าง Learning Task     ✓
เพิ่ม Knowledge         ✓
ปรับ Strategy           ✓

เปลี่ยน User Goal       ✗
แก้ Safety Core         ✗
ทำลาย Identity/Core    ✗
เขียนทับ Runtime เอง   ✗
```

แนวคิดนี้ทำให้ AE01M สามารถพัฒนาความสามารถได้ โดยยังคงมีขอบเขตที่ควบคุมได้

## Memory — ความจำของ AE01M

Memory เป็นหนึ่งในส่วนสำคัญที่สุดของโครงการ

ปัจจุบันมีพื้นฐานของ:

```text
Working Memory
Episodic Memory
Semantic Memory
Experience
Recall Index
Semantic Index
Memory Consolidation
Associative Recall
```

แนวทางที่กำลังพัฒนาคือทำให้ Memory มีลักษณะเป็นระบบที่สามารถเลือก เชื่อมโยง รวม และเรียกคืนข้อมูลได้มากกว่าเพียงการเก็บข้อความเป็นรายการ

เป้าหมายของ Brain-like Memory คือ

```text
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
```

ในอนาคตสามารถพัฒนาไปสู่แนวคิด **Computational Memory Cell** ซึ่งเป็นหน่วยความจำเชิงซอฟต์แวร์ที่มีข้อมูล เช่น ความสำคัญ ความมั่นใจ จำนวนครั้งที่ถูกเรียกใช้ และความสัมพันธ์กับความทรงจำอื่น

ไม่ได้หมายความว่า Cell เหล่านี้คือ neuron จริง แต่เป็น abstraction สำหรับทดลองกลไกความจำ

## Reflection

หลังจาก AE01M ทำงาน จะต้องสามารถประเมินผลที่เกิดขึ้นได้

```text
ผลลัพธ์
  ↓
Reflection
  ├── สำเร็จ
  ├── ล้มเหลว
  └── ขาดความรู้
```

หากพบว่าความรู้ยังไม่เพียงพอ เป้าหมายระยะยาวคือให้ระบบสามารถสร้าง Learning Task ถัดไปเองได้

```text
Goal
  ↓
Task
  ↓
ทำงาน
  ↓
Reflection
  ↓
Missing Knowledge
  ↓
New Learning Task
  ↓
Learn
  ↓
Memory
  ↺
```

## Autonomous Growth

คำว่า “เติบโตเอง” ในโครงการมีความหมายทางวิศวกรรม ไม่ได้หมายถึงการมีจิตสำนึก

AE01M จะถือว่าเริ่มมี Growth Loop เมื่อสามารถทำได้ครบ:

1. จำประสบการณ์ของตัวเอง
2. ประเมินได้ว่าความรู้ยังไม่เพียงพอ
3. สร้างและทำ Learning Task ถัดไป
4. นำสิ่งที่เรียนรู้กลับมาใช้
5. ประเมินผลใหม่

วงจรเป้าหมายคือ

```text
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
Learn
  ↓
Consolidate
  ↓
Reuse
  ↺
```

จุดนี้ยังเป็นเป้าหมายที่กำลังพัฒนา ไม่ใช่ความสามารถที่ควรอ้างว่าสมบูรณ์แล้ว

## Internet และการเรียนรู้

ในระยะต่อไป Internet สามารถเป็นหนึ่งในแหล่งข้อมูลสำหรับการเรียนรู้ของ AE01M

ตัวอย่าง:

```text
Knowledge Gap
  ↓
Learning Task
  ↓
ค้นข้อมูล
  ↓
อ่านหลายแหล่ง
  ↓
เปรียบเทียบ
  ↓
ทดลอง / ตรวจสอบ
  ↓
ประเมิน
  ↓
Memory
```

ข้อมูลจาก Internet ไม่ควรถูกถือว่าเป็นความจริงทันที แต่ควรผ่านการประเมินก่อนนำเข้าสู่ความรู้ที่ระบบเชื่อถือ

## การใช้ Local AI

AE01M ถูกออกแบบให้ Local AI เป็น **ส่วนประกอบ** ไม่ใช่สมองทั้งหมด

```text
              AE01M
                │
        ┌───────┴────────┐
        │ Cognitive Core │
        └───────┬────────┘
                │
       ┌────────┴────────┐
       ↓                 ↓
 Native Runtime       Local AI
                         │
                        Qwen
```

งานที่เป็น deterministic ควรให้ Python หรือระบบภายในจัดการโดยตรง

งานด้านภาษา การตีความ หรือ reasoning ที่ซับซ้อนจึงค่อยเรียก Local AI

เป้าหมายคือไม่ต้องเรียก LLM ในทุก cognitive cycle และลดภาระด้านทรัพยากร

## Research Engine

อีกแนวคิดหนึ่งของโครงการคือให้ Python เป็น “ห้องทดลอง” ของ AE01M

```text
AE01M
  ↓
Hypothesis
  ↓
Python Experiment
  ↓
Simulation / Calculation
  ↓
Metrics
  ↓
Evaluation
  ↓
Memory
  ↓
Hypothesis ใหม่
  ↺
```

Python จึงสามารถรับผิดชอบงานคำนวณ ทดลอง เปรียบเทียบผล และวัดประสิทธิภาพ ขณะที่ AI ช่วยเสนอสมมติฐาน วิเคราะห์ผล และตีความข้อมูล

แนวทางนี้ช่วยลดการใช้ LLM ในงานที่ Python สามารถทำได้แม่นยำกว่า

## Simulator

โครงการมีแนวคิดสร้าง Simulator เป็นสนามทดลองสำหรับ Cognitive Loop

ระยะแรกเน้น **Text/State Simulator** ที่มีองค์ประกอบพื้นฐาน เช่น

```text
World State
Time
Events
Actions
Consequences
Experience
```

วงจรคือ

```text
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
```

เป้าหมายคือใช้ Simulator ทดสอบการเรียนรู้และการทำงานอัตโนมัติก่อนเชื่อมต่อกับระบบจริง

## Brain Subsystem Simulator

โครงการยังมีแนวคิดสำหรับการจำลองระบบประสาทในระดับใหญ่เพื่อการทดลอง

```text
Hippocampus      40,000,000 logical cells
Motor Cortex     60,000,000 logical cells
--------------------------------------------
รวม             100,000,000 logical cells
```

แนวทางที่กำหนดไว้คือใช้โมเดล **Leaky Integrate-and-Fire (LIF)** ร่วมกับ NumPy, vectorization และ block/chunk processing

100 ล้านเซลล์นี้เป็น **ขนาดเชิงตรรกะของการจำลอง** ไม่ใช่ข้อกำหนดว่าจะต้องสร้าง Python object จำนวน 100 ล้านตัว หรือรันทั้งหมดพร้อมกันบนเครื่อง RAM 4 GB

ส่วน Cognitive Core ที่ใช้งานจริงยังคงเน้น Micro-Architecture ขนาดเล็ก

## ข้อจำกัดด้านทรัพยากร

AE01M ถูกออกแบบโดยคำนึงถึงเครื่องที่มีทรัพยากรจำกัด ประมาณ:

```text
RAM       ~ 4 GB
CPU       จำกัด
Dependency ต่ำ
Architecture แบบ Micro-Module
Stateful Runtime
```

ดังนั้นโครงการให้ความสำคัญกับ:

```text
โมดูลขนาดเล็ก
ใช้ทรัพยากรเท่าที่จำเป็น
ไม่พึ่ง Framework ขนาดใหญ่โดยไม่จำเป็น
ใช้ Local AI เฉพาะเมื่อจำเป็น
จัดการ State อย่างชัดเจน
มี Test และ Regression
มี Checkpoint / Recovery
```

## BrainCog และโครงการภายนอก

BrainCog และโครงการวิจัยอื่น ๆ ใช้เป็นแหล่งศึกษาและอ้างอิงกลไก ไม่ได้หมายความว่าจะนำ Framework ทั้งหมดมาเป็น dependency ของ AE01M

หลักการคือ

```text
ศึกษาของที่มีอยู่
  ↓
หาแนวคิดที่พิสูจน์แล้ว
  ↓
คัดเฉพาะกลไกที่จำเป็น
  ↓
ปรับให้เข้ากับ AE01M
  ↓
ทดสอบ
  ↓
รักษา Regression
```

แนวทางเดียวกันใช้กับ Agent Architecture และงานวิจัยอื่น ๆ

## สถานะปัจจุบัน

จากสถานะโครงการล่าสุดที่บันทึกไว้:

```text
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

Semantic / Contextual Recall             ⏳
Self-directed Learning Loop              ⏳
Autonomous Perception → Think → Act      ⏳
Persistent Memory / Continuity            ⏳
Environment Interaction                  ⏳
Autonomous Life Loop                     ⏳
Long-term Cognitive Development          ⏳
AE01M ใช้ชีวิตเองได้                     ⏳
```

สถานะที่บันทึกไว้ระบุว่า Associative Recall เชื่อมเข้ากับ CognitiveLoop แล้ว แต่ Recall ยังไม่ถึงระดับ Semantic/Contextual Recall เต็มรูปแบบ

## Roadmap

ทิศทางหลักของโครงการคือ

```text
PHASE 0
Foundation / Safety
        ↓
PHASE 1
Newborn Brain Mechanism
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
```

ลำดับนี้อาจปรับวิธีดำเนินงานได้ตามผลการทดลอง แต่เป้าหมายหลักของโครงการไม่ควรถูกเปลี่ยนเพียงเพราะ implementation ของขั้นใดขั้นหนึ่งยาก

## เป้าหมายระยะยาว

เป้าหมายของ AE01M คือสร้างผู้ช่วยส่วนตัวที่มี Cognitive Runtime ต่อเนื่อง และสามารถ:

```text
รับเป้าหมาย
  ↓
เข้าใจเป้าหมาย
  ↓
ตรวจความรู้ที่มี
  ↓
ถ้ารู้ → ลงมือทำ
  ↓
ถ้าไม่รู้ → เรียนรู้
  ↓
ทดลอง
  ↓
ตรวจสอบ
  ↓
เรียนรู้จากผล
  ↓
จดจำ
  ↓
พัฒนาวิธีการ
  ↓
นำทักษะกลับมาใช้
  ↺
```

ปลายทางคือระบบที่สามารถรับ Goal จากผู้ใช้ ทำงานผ่าน Cognitive Loop เรียนรู้จากประสบการณ์ และเพิ่มความสามารถของตัวเองอย่างต่อเนื่องภายใต้ขอบเขตที่กำหนดไว้

แนวคิดสุดท้ายของโครงการจึงไม่ใช่

> “สร้าง AI ที่รู้ทุกอย่างตั้งแต่เริ่มต้น”

แต่คือ

> **“สร้างสมองซอฟต์แวร์ที่เริ่มต้นจากความสามารถพื้นฐาน แล้วสามารถเรียนรู้ จดจำ ทดลอง ประเมิน และพัฒนาความสามารถจากประสบการณ์ได้”**

นี่คือเป้าหมายหลักของ **AE01M — The Transcending Form**.
