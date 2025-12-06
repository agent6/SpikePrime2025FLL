# Lesson 10 – Spin Turns

> Environment: Spike App IDE with our FLL robot and `master.py`  
> API reference: <https://tuftsceeo.github.io/SPIKEPythonDocs/SPIKE3.html>

## Lesson Goals

By the end of this lesson, students will be able to:
- Use `spin_left(speed, target_angle_degrees)` and `spin_right(speed, target_angle_degrees)`.
- Describe the difference between **spins** and **pivots**.
- Decide when to use spins vs pivots on the FLL field.

---

## 1. Spin Helpers in `master.py`

Open `master.py` and find:

```python
def spin_right(speed, target_angle_degrees):
    ...

def spin_left(speed, target_angle_degrees):
    ...
```

Recap ports:
- `port.A` – left drive motor
- `port.E` – right drive motor

Spins use **both wheels**, in opposite directions (relative to forward), to turn **in place**.

Summary:
- `spin_right(speed, angle)` – robot nose turns right.
- `spin_left(speed, angle)` – robot nose turns left.

---

## 2. How Spins Work (Concept)

Inside each spin function:
- Reset yaw: `motion_sensor.reset_yaw(0)`.
- Run **both motors** so the robot rotates around its center.
- Use `motion_sensor.tilt_angles()[0]` to decide when to stop.

Conceptual behavior:
- **Spin right**:
  - Left wheel forward, right wheel backward (relative to forward).
  - Yaw decreases toward `-target_angle_degrees`, then stop.

- **Spin left**:
  - Left wheel backward, right wheel forward (relative to forward).
  - Yaw increases toward `target_angle_degrees`, then stop.

Ask students:
- “What is different from a pivot turn?”
  - Pivot: one wheel stays still, one moves.
  - Spin: both wheels move in opposite directions → tighter turn.

---

## 3. Simple Spin Test Missions

Create or reuse missions like:

```python
async def mission_spin_left_test():
    spin_left(200, 90)   # ~90-degree left spin

async def mission_spin_right_test():
    spin_right(200, 90)  # ~90-degree right spin
```

Run on an open area of the field:
- Confirm the robot rotates roughly in place.
- Check direction: does “left” actually feel like a left spin?
- Adjust `speed` if the robot overshoots or struggles.

---

## 4. Spins vs Pivots – When to Use Which?

Discussion with the robot on the mat:

**Use pivots when:**
- You want to turn around one wheel (inside/outside control).
- You are near a wall and want the robot to “swing” around a wheel.
- Aligning alongside a line, model, or wall.

**Use spins when:**
- Space is tight and you must turn in place.
- You need a quick reorientation without changing your position much.
- You’re in the middle of the field and want fast directional changes.

Activity:
1. Place the robot in a tight space between models or lines.
2. Try using a **pivot** to turn — does it bump something?
3. Try using a **spin** — does it stay more centered?
4. Decide which is better for that situation.

Encourage students to:
- Note down good spin angles (e.g., 85°, 90°, 95°) and speeds that work well on your specific robot and mat.
- Use spins for “turn on a spot” maneuvers in missions, and pivots for “turn around a wheel” maneuvers.  

---

[Back to Lessons Index](index.html)
