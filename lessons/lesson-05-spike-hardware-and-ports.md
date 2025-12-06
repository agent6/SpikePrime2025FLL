# Lesson 5 – Spike Hardware & Ports

> Environment: Spike App IDE (with a Spike Prime hub connected)  
> Reference docs: https://tuftsceeo.github.io/SPIKEPythonDocs/SPIKE3.html

## Lesson Goals

By the end of this lesson, students will be able to:
- Identify the **hub**, **ports**, **motors**, and **sensors** on our Spike Prime robot.
- Map our physical wiring to code: `port.A`, `port.B`, `port.C`, `port.E`.
- Open and read the Tufts SPIKE 3 Python docs to find functions and examples.

---

## 1. Hardware Tour – Hub, Ports, Motors, Sensors

Gather around a real robot and a **bare hub**.

Discuss:
- **Hub** – the “brain” running Python.
- **Ports** – labeled letters around the hub (A–F for motors, 1–6 for sensors).
- **Motors** – large/small motors plugged into motor ports.
- **Sensors** – color, distance, force, plus the hub’s built‑in **motion sensor**.

Hands‑on:
- Have students point to each port label.
- Ask: “Which cables go to drive motors? Which go to attachments?”

---

## 2. Our Robot’s Port Mapping

Open `master.py` and show the imports:

```python
from hub import port
```

Explain our wiring **contract**:
- `port.A` – **left drive motor**
- `port.E` – **right drive motor**
- `port.C` – **left attachment** motor
- `port.B` – **right attachment** motor

Show a few examples from `master.py`:

```python
motor.run(port.A, -left_command)   # left wheel
motor.run(port.E, right_command)   # right wheel

motor.run_for_degrees(port.C, degrees, speed)  # left attachment
motor.run_for_degrees(port.B, degrees, speed)  # right attachment
```

Activity:
- Have students trace a wire from each motor on the robot to the hub port.
- Then, have them write one comment in `master.py` (or on paper):  
  `"port.A = left drive, port.E = right drive, port.C = left attachment, port.B = right attachment"`.

---

## 3. Reading the Tufts SPIKE 3 Python Docs

Open the docs in a browser:  
https://tuftsceeo.github.io/SPIKEPythonDocs/SPIKE3.html

Walk through:
- The **Table of Contents** (Hub, Motor, MotorPair, Sensors, `runloop`, etc.).
- The **Motor** section: look for `run`, `run_for_degrees`, `stop`.
- The **Motion Sensor** section: look for `tilt_angles`.

Connect to our code:
- Show how `motor.run_for_degrees` in the docs matches our usage in `left_attachment_up` and `right_attachment_up`.
- Show how `motion_sensor.tilt_angles()` in the docs matches our pivots and spins.

Mini‑task:
- Ask each student (or pair) to find one function in the docs (e.g., `motor.stop` or `button.pressed`) and:
  - Read the description.
  - Point to where something similar is used in `master.py`.

Emphasize: *“When we forget how a Spike function works, the Tufts docs are our first stop.”*  

---

[Back to Lessons Index](index.html)
