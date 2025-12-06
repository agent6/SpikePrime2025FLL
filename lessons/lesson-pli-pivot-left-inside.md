# Lesson PLI – `pivot_left_inside`

> Environment: Spike App IDE with our FLL robot and `master.py`

## Lesson Goals

By the end of this lesson, students will be able to:
- Explain what `pivot_left_inside(speed, target_angle_degrees)` does.
- Predict which wheel moves and which stays still.
- Tune a left **inside** pivot angle for accurate field turns.

---

## 1. What `pivot_left_inside` Does

Open `master.py` and find:

```python
def pivot_left_inside(speed, target_angle_degrees):
    """
    Pivot turn to the LEFT using the inside wheel.

    Left turn, inside wheel moves BACKWARD:
    - Right motor (port.E) is treated as the inside wheel and moves backward.
    - Left motor (port.A) stays stopped.
    The motion sensor yaw is used as the angle reference.
    """
    motion_sensor.reset_yaw(0)

    while motion_sensor.tilt_angles()[0] < target_angle_degrees:
        motor.run(port.E, -speed)

    motor.stop(port.E, stop=motor.BRAKE)
```

Summarize behavior:
- Resets yaw to 0.
- Runs the **right wheel (port.E)** **backward**.
- Keeps the **left wheel (port.A)** stopped.
- Reads yaw (`tilt_angles()[0]`) until it reaches `target_angle_degrees`.
- Stops the right wheel with brake.

Concept:
- The robot turns **left**, but now the moving wheel is on the **inside** of the turn (backing up around the left side).

---

## 2. Quick Mental Model

Ask students:
- “If the right wheel moves backward and the left wheel is stopped, which way does the robot turn?”  
  → Left.
- “Is the turning center closer to the left wheel or the right wheel?”  
  → Closer to the left side; the right wheel is the inside wheel backing around.

Compare to `pivot_left_outside`:
- Outside pivot: right wheel moves **forward**.
- Inside pivot: right wheel moves **backward**.
- Both produce a left turn, but the path and feel are different.

---

## 3. Simple Field Test Mission

Create or reuse a mission that calls `pivot_left_inside`:

```python
async def mission_pivot_left_inside_test():
    # Adjust speed and angle on the field
    pivot_left_inside(200, 45)
    return
```

On the field:
1. Place the robot square against base or a line.
2. Run the mission from the selector.
3. Observe:
   - Does the robot pivot with the right wheel backing up?
   - How big is the turn compared to `pivot_left_outside`?

---

## 4. Tuning the Inside Pivot Angle

Goal: Achieve a reliable left inside pivot for a chosen speed (e.g., ~45° or 90°).

Steps:
1. Start with `speed = 200`, `target_angle_degrees = 45`.
2. Run several times and check where the robot ends up.
3. If it **under-turns**:
   - Increase `target_angle_degrees` (e.g., 50–60).
4. If it **over-turns**:
   - Decrease `target_angle_degrees` (e.g., 35–40).

Suggested tuning table:

| Test | speed | target_angle | Result / Notes                    |
|------|-------|--------------|-----------------------------------|
| 1    | 200   | 45           | Turn smaller than expected        |
| 2    | 200   | 55           | Closer to desired angle           |
| 3    | 200   | 55           | Repeatable within small error     |

Encourage:
- Compare the same target angle for `pivot_left_outside` vs `pivot_left_inside`.
- Decide when an inside pivot feels more natural for a given mission.

---

## 5. Connecting to Real Missions

Ask:
- “Where might backing the inside wheel be useful?”
  - Example: backing around a model or avoiding an obstacle on the outside.

Activity:
- Identify one mission where the robot needs a **small, controlled left turn** that doesn’t swing the outside of the robot too far.
- Use your tuned `pivot_left_inside` values in that mission.
- Test on the field and compare to using `pivot_left_outside` in the same spot—decide which gives better clearance and alignment.

This lesson deepens understanding of left turns by showing how changing which wheel moves (inside vs outside) changes the robot’s path and how it interacts with nearby models.  

---

[Back to Lessons Index](index.html)
