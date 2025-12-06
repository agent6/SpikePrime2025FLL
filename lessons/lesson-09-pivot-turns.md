# Lesson 9 – Pivot Turns

> Environment: Spike App IDE with our FLL robot and `master.py`  
> API reference: https://tuftsceeo.github.io/SPIKEPythonDocs/SPIKE3.html

## Lesson Goals

By the end of this lesson, students will be able to:
- Use the four pivot helpers in `master.py`:
  - `pivot_left_outside(speed, target_angle_degrees)`
  - `pivot_left_inside(speed, target_angle_degrees)`
  - `pivot_right_outside(speed, target_angle_degrees)`
  - `pivot_right_inside(speed, target_angle_degrees)`
- Understand inside vs outside wheel behavior.
- Use pivots to make a square path and fine‑tune alignments on the field.

---

## 1. Pivot Helpers Overview

Open `master.py` and find:

```python
def pivot_left_outside(speed, target_angle_degrees):
    ...

def pivot_left_inside(speed, target_angle_degrees):
    ...

def pivot_right_outside(speed, target_angle_degrees):
    ...

def pivot_right_inside(speed, target_angle_degrees):
    ...
```

Recap our drive ports:
- `port.A` – left drive motor
- `port.E` – right drive motor

Concepts:
- **Outside wheel** – the wheel farther from the turn center.
- **Inside wheel** – the wheel closer to the turn center.

---

## 2. What Each Pivot Does

All pivots:
- Reset yaw: `motion_sensor.reset_yaw(0)`.
- Run **one motor** while the other stays stopped.
- Check `motion_sensor.tilt_angles()[0]` (yaw) until the angle is reached.

Summarize behavior:

- `pivot_left_outside(speed, angle)`  
  - Turn **left** using the **right (outside)** wheel forward.  
  - Left wheel stopped.

- `pivot_left_inside(speed, angle)`  
  - Turn **left** using the **inside** wheel backward (right wheel backward).  
  - Left wheel stopped.

- `pivot_right_outside(speed, angle)`  
  - Turn **right** using the **left (outside)** wheel forward.  
  - Right wheel stopped.

- `pivot_right_inside(speed, angle)`  
  - Turn **right** using the **inside** wheel backward (left wheel backward).  
  - Right wheel stopped.

Ask students:
- “Which wheel moves in each case?”
- “Which side of the robot is the center of the turn?”

---

## 3. Simple Test Missions for Pivots

Use the existing pivot test missions or create one like:

```python
async def mission_pivots_demo():
    # 90-degree left outside pivot
    pivot_left_outside(200, 90)

    # 90-degree right outside pivot
    pivot_right_outside(200, 90)
```

Run on the field and observe:
- Does the robot pivot around the **stopped** wheel?
- Does the yaw reading seem close to the requested angle?

Adjust `speed` if the turn is too jerky or if the robot overshoots.

---

## 4. Practice – Square Path

Goal: Use outside pivots to drive in a **square** on the field.

Simple pattern:
1. Drive straight a fixed distance.
2. Pivot 90°.
3. Repeat 4 times.

Example (pseudocode using our helpers):

```python
async def mission_square():
    for _ in range(4):
        drive_forward(20, 250, 720)          # tune distance
        pivot_right_outside(200, 90)         # 90-degree right turn
```

Field activity:
- Use tape or mat lines as visual guides.
- Run the square mission and see if the robot comes back close to its starting point.
- Tune:
  - `target_degrees` in `drive_forward` for side length.
  - pivot angle (e.g., 88°, 90°, 92°) until the square closes more accurately.

---

## 5. Practice – Precise Alignments

Set up small targets (field lines, models, or tiles).

Exercises:
1. Start against base wall, pivot left/right until the robot lines up with a field line.
2. Mark the angle that works reliably (e.g., 35°, 42°) for a specific model.
3. Record these “favorite angles” in a notebook or comments in `master.py`.

Discussion:
- When might you prefer a pivot vs a spin turn?
  - Pivots: turning around a fixed wheel, often more controlled near walls.
  - Spins: turning in place when space is tight.

These pivot skills will be used throughout missions to line up for attachments and models.  

---

[Back to Lessons Index](index.html)
