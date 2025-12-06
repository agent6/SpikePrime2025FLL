# Spike Prime Python v3 – FLL Team Learning Plan

This plan is for teaching our FLL team Spike Prime Python v3, starting with core Python concepts, then moving into robot programming using `master.py`, and finishing with a lesson for each helper method.

---

## Phase 1 – Python Basics (Off‑Robot)

Goal: Everyone can read and write simple Python and understand the core ideas used later in robot code.

**Lesson 1 – Python Foundations**
- Variables and types (`int`, `float`, `bool`, `str`)
- Expressions and operators
- Simple `print()` and string formatting

**Lesson 2 – Control Flow**
- `if/elif/else` conditions
- Comparison and logical operators
- Small exercises: “grading”, “even/odd”, simple decision trees

**Lesson 3 – Loops and Functions**
- `while` loops
- `for` loops with `range`
- Defining functions, parameters, and return values
- Mini‑project: text‑only “robot” that follows simple rules

**Lesson 4 – Lists and Dictionaries (Optional / Stretch)**
- Lists for sequences of values
- Simple indexing and loops over lists
- Dictionaries for named settings (e.g., speeds, distances)

---

## Phase 2 – Spike Prime Runtime Concepts

Goal: Connect Python basics to Spike Prime’s APIs and async model.

**Lesson 5 – Spike Hardware & Ports**
- What is the hub, ports, motors, sensors
- Mapping our robot: drive motors on `port.A` / `port.E`, attachments on `port.B` / `port.C`
- Reading docs: using the Tufts SPIKE 3 Python reference

**Lesson 6 – Motors, Encoders, and Motion Sensor**
- `motor.run`, `motor.run_for_degrees`, `motor.stop`
- `motor.relative_position` and why we reset encoders
- `motion_sensor.tilt_angles()` and yaw for turning

**Lesson 7 – Async and `runloop`**
- What `async` and `await` mean on the hub
- `runloop.run(main)`, `await runloop.until(...)`
- Simple demo: wait for a tilt or button press, then react

---

## Phase 3 – Core Robot Helpers in `master.py`

Goal: Understand and practice with the main drive and turn helpers.

**Lesson 8 – Straight Driving**
- `drive_forward(min_speed, max_speed, target_degrees, kP)`
- `drive_backward(min_speed, max_speed, target_degrees, kP)`
- How proportional correction uses yaw
- Field practice: tuning speeds and distances

**Lesson 9 – Pivot Turns**
- `pivot_left_outside(speed, target_angle_degrees)`
- `pivot_left_inside(speed, target_angle_degrees)`
- `pivot_right_outside(speed, target_angle_degrees)`
- `pivot_right_inside(speed, target_angle_degrees)`
- Practice: square path, precise alignments

**Lesson 10 – Spin Turns**
- `spin_left(speed, target_angle_degrees)`
- `spin_right(speed, target_angle_degrees)`
- When to use spins vs pivots on the FLL field

**Lesson 11 – Attachments**
- Left attachment: `left_attachment_up/down`
- Right attachment: `right_attachment_up/down`
- Using encoder degrees to get repeatable attachment positions
- Practice: hit a model, then safely return home

---

## Phase 4 – Async Helpers and Motor Feedback

Goal: Introduce more advanced patterns for parallel actions and reliable stopping.

**Lesson 12 – Async Motion Helpers**
- `async_drive_forward`, `async_drive_backward`
- `async_left_attachment_up/down`, `async_right_attachment_up/down`
- Concept of parallel tasks with `runloop.create_task`
- Example: drive while raising an arm

**Lesson 13 – Detecting Motor Stop**
- `MotorIsStopped(motor_port, samples=100)`
- How encoder readings show motion vs stop
- Using `await runloop.until(lambda: MotorIsStopped(port.C))`
- Practice: wait for a mechanism to settle before the next action

---

## Phase 5 – Mission Selector and Full Runs

Goal: Use all helpers inside a structured mission system.

**Lesson 14 – Mission Selector UX**
- `mission_selector()` loop
- Using LEFT to run and RIGHT to change mission
- Displaying mission numbers and the selector indicator LED

**Lesson 15 – Mission Functions**
- `mission_0`–`mission_9` structure
- How each mission currently tests one helper:
  - `mission_0` – `drive_forward`
  - `mission_1` – `drive_backward`
  - `mission_2` – `pivot_left_outside`
  - `mission_3` – `pivot_left_inside`
  - `mission_4` – `pivot_right_outside`
  - `mission_5` – `pivot_right_inside`
  - `mission_6` – `spin_left`
  - `mission_7` – `spin_right`
  - `mission_8` – left attachment up/down
  - `mission_9` – right attachment up/down
- Activity: replace one test mission with a real FLL run

---

## Phase 6 – One Lesson per Helper Method

Below are focused lesson topics for each method in `master.py`. Each lesson should include:
- Quick recap of what the method does.
- One small “desk‑check” example (pseudo‑field).
- One field exercise.

**Drive and Turns**
- Lesson DF – `drive_forward`
- Lesson DB – `drive_backward`
- Lesson PLO – `pivot_left_outside`
- Lesson PLI – `pivot_left_inside`
- Lesson PRO – `pivot_right_outside`
- Lesson PRI – `pivot_right_inside`
- Lesson SL – `spin_left`
- Lesson SR – `spin_right`

**Attachments**
- Lesson LAU – `left_attachment_up`
- Lesson LAD – `left_attachment_down`
- Lesson RAU – `right_attachment_up`
- Lesson RAD – `right_attachment_down`

**Async Helpers**
- Lesson ADF – `async_drive_forward`
- Lesson ADB – `async_drive_backward`
- Lesson ALAU – `async_left_attachment_up`
- Lesson ALAD – `async_left_attachment_down`
- Lesson ARAU – `async_right_attachment_up`
- Lesson ARAD – `async_right_attachment_down`

**Feedback and Control**
- Lesson MIS – `MotorIsStopped`
- Lesson SEL – `mission_selector`
- Lesson Mx – `mission_0`–`mission_9` (how to build and test full missions)

Each of these can become a dedicated lesson file under `lessons/` (for example, `lessons/lesson_drive_forward.md`) as the team builds experience and wants more detailed step‑by‑step guides.

