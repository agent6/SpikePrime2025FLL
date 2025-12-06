# Lesson PRI – `pivot_right_inside`

> Environment: Spike App IDE with our FLL robot and `master.py`

## Lesson Goals

By the end of this lesson, students will be able to:
- Explain what `pivot_right_inside(speed, target_angle_degrees)` does.
- Predict which wheel moves and which stays still.
- Tune a right **inside** pivot angle for accurate field turns.

---

## 1. What `pivot_right_inside` Does

Open `master.py` and find:

```python
def pivot_right_inside(speed, target_angle_degrees):
    """
    Pivot turn to the RIGHT using the inside wheel.

    Right turn, inside wheel moves BACKWARD:
    - Left motor (port.A) is the inside wheel and moves backward.
    - Right motor (port.E) stays stopped.
    The motion sensor yaw is used as the angle reference.
    """
    motion_sensor.reset_yaw(0)

    while motion_sensor.tilt_angles()[0] > -target_angle_degrees:
        motor.run(port.A, -speed)

    motor.stop(port.A, stop=motor.BRAKE)
```

Summarize behavior:
- Resets yaw to 0.
- Runs the **left wheel (port.A)** **backward**.
- Keeps the **right wheel (port.E)** stopped.
- Reads yaw (`tilt_angles()[0]`) until it reaches `-target_angle_degrees`.
- Stops the left wheel with brake.

Concept:
- The robot turns **right** using the **inside** wheel backing up, with the right wheel acting as the pivot point.

---

## 2. Quick Mental Model

Ask students:
- “If the left wheel moves backward and the right wheel is stopped, which way do we turn?”  
  → Right.
- “Is this different from `pivot_right_outside`?”  
  → Yes: outside pivot moves the left wheel forward; inside pivot moves it backward.

Compare:
- Outside right pivot: wider arc, left wheel forward.
- Inside right pivot: tighter, backing motion around the inside.

---

## 3. Simple Field Test Mission

Create or reuse a mission that calls `pivot_right_inside`:

```python
async def mission_pivot_right_inside_test():
    # Adjust speed and angle on the field
    pivot_right_inside(200, 45)
    return
```

On the field:
1. Place the robot square against base or along a line.
2. Run the mission from the selector.
3. Observe:
   - Does the left wheel back up while the right stays in place?
   - How big is the turn compared to `pivot_right_outside`?

---

## 4. Tuning the Inside Pivot Angle

Goal: Achieve a reliable right inside pivot for a chosen speed (e.g., ~45° or 90°).

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
- Compare tuned angles for `pivot_right_inside` vs `pivot_right_outside`.
- Decide which pivot is better for each specific mission situation.

---

## 5. Connecting to Real Missions

Ask:
- “Where might a right inside pivot be safer or more precise?”
  - Example: backing around a model without swinging the far side of the robot too much.

Activity:
- Identify a mission step where a small right turn is needed near models or walls.
- Try both `pivot_right_outside` and `pivot_right_inside` with tuned angles.
- Choose the one that gives better clearance and alignment, and keep that call in your mission function.

This lesson completes the pivot set by solidifying how to use inside right pivots alongside outside and left pivots for full control of robot orientation on the FLL field.  

---


