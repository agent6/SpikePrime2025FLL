# Lesson SR – `spin_right`

> Environment: Spike App IDE with our FLL robot and `master.py`

## Lesson Goals

By the end of this lesson, students will be able to:
- Explain what `spin_right(speed, target_angle_degrees)` does.
- Predict how the wheels move during a right spin.
- Tune a right spin angle for quick, in‑place turns on the field.

---

## 1. What `spin_right` Does

Open `master.py` and find:

```python
def spin_right(speed, target_angle_degrees):
    """
    In-place spin to the RIGHT using opposite wheel directions.

    - Left motor (port.A) runs forward.
    - Right motor (port.E) runs backward.
    - Stops when yaw reaches -target_angle_degrees.
    """
    motion_sensor.reset_yaw(0)

    while motion_sensor.tilt_angles()[0] > -target_angle_degrees:
        # Forward on left, backward on right (relative to drive_forward)
        motor.run(port.A, -speed)
        motor.run(port.E, -speed)

    motor.stop(port.A, stop=motor.BRAKE)
    motor.stop(port.E, stop=motor.BRAKE)
```

Summarize behavior:
- Resets yaw to 0.
- Drives both wheels so the robot rotates **in place** to the right.
- Uses the motion sensor yaw (`tilt_angles()[0]`) reaching `-target_angle_degrees` as the stop condition.

Concept:
- The robot **spins right** without significantly moving forward or backward.

---

## 2. Inside the Full `spin_right` Method

Here is the method again, with explanation:

```python
def spin_right(speed, target_angle_degrees):
    """
    In-place spin to the RIGHT using opposite wheel directions.

    - Left motor (port.A) runs forward.
    - Right motor (port.E) runs backward.
    - Stops when yaw reaches -target_angle_degrees.
    """
    # 1) Reset yaw so current heading is 0 degrees
    motion_sensor.reset_yaw(0)

    # 2) Turn until yaw reaches the requested right angle (negative)
    while motion_sensor.tilt_angles()[0] > -target_angle_degrees:
        # Forward on left, backward on right (relative to drive_forward)
        motor.run(port.A, -speed)
        motor.run(port.E, -speed)

    # 3) Stop both wheels with brake
    motor.stop(port.A, stop=motor.BRAKE)
    motor.stop(port.E, stop=motor.BRAKE)
```

Walk-through:
- `motion_sensor.reset_yaw(0)`:
  - Sets yaw to 0 at the current orientation.
  - From here, yaw reports how far we’ve turned from that starting heading.
- Yaw sign convention:
  - Right turns make yaw **negative**.
  - Left turns make yaw **positive**.
- The `while` loop:
  - Reads `yaw = motion_sensor.tilt_angles()[0]`.
  - While `yaw > -target_angle_degrees`, the robot keeps spinning right.
  - As we turn right, yaw decreases from 0 toward the negative target.
- Motor commands:
  - `motor.run(port.A, -speed)` and `motor.run(port.E, -speed)` are chosen to produce an in‑place spin to the right given the wiring used in `drive_forward`.
  - Both wheels move with equal magnitude but opposite effective directions relative to straight driving, so the robot rotates rather than translating.
- When yaw reaches `-target_angle_degrees`:
  - The loop exits.
  - `motor.stop(port.A, ...)` and `motor.stop(port.E, ...)` brake both wheels to hold the final heading.

Key idea:
- `spin_right` is a yaw‑controlled **in‑place rotation** to the right: we reset yaw, drive both wheels in a pattern that causes rotation, and stop exactly when yaw hits the negative target angle.

---

## 3. Mental Model – Wheels During a Right Spin

Ask students:
- “For a right spin, do we want the robot’s nose to turn right without drifting sideways?”  
  → Yes.

Explain:
- Left and right wheels run in opposite directions (relative to a straight drive).
- Combined effect is rotation around the robot’s center.

Compare to pivots:
- Pivot: one wheel moves, one is still.
- Spin: **both** wheels move → tight, centered turn.

---

## 4. Simple Field Test Mission

Create or reuse a mission that calls `spin_right`:

```python
async def mission_spin_right_test():
    # Adjust speed and angle on the field
    spin_right(200, 90)
    return
```

On the field:
1. Place the robot in open space.
2. Run the mission from the selector.
3. Observe:
   - Does the robot spin roughly in place?
   - Does it rotate right (clockwise) as expected?

---

## 5. Tuning the Spin Angle

Goal: Achieve a reliable ~90° right spin at a chosen speed.

Steps:
1. Start with `speed = 200`, `target_angle_degrees = 90`.
2. Run several times and see where the robot ends up facing.
3. If it **under‑spins** (less than 90°):
   - Increase `target_angle_degrees` (e.g., 92–100).
4. If it **over‑spins**:
   - Decrease `target_angle_degrees` (e.g., 80–88).

Suggested tuning table:

| Test | speed | target_angle | Result / Notes                 |
|------|-------|--------------|--------------------------------|
| 1    | 200   | 90           | Slightly less than 90°        |
| 2    | 200   | 96           | Closer to desired angle       |
| 3    | 200   | 96           | Repeatable, acceptable error  |

Encourage:
- Use field markings or a taped reference to judge orientation.
- Choose a “standard” `spin_right` setting (speed + angle) once it’s reliable.

---

## 6. Connecting `spin_right` to Missions

Ask:
- “When would a right spin be better than a right pivot?”
  - Example: in tight spaces where you must rotate without bumping nearby models.

Activity:
- Identify a mission step where the robot must quickly turn right in place (e.g., after scoring on one model and facing another).
- Insert a tuned `spin_right(speed, angle)` call into that mission.
- Test on the field to ensure the robot ends up facing the correct direction and clears all nearby objects.

This lesson makes `spin_right` a dependable tool for fast, in‑place orientation changes in your competition runs.  

---

