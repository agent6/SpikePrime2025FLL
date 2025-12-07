# Lesson SL – `spin_left`

> Environment: Spike App IDE with our FLL robot and `master.py`

## Lesson Goals

By the end of this lesson, students will be able to:
- Explain what `spin_left(speed, target_angle_degrees)` does.
- Predict how the wheels move during a left spin.
- Tune a left spin angle for quick, in‑place turns on the field.

---

## 1. What `spin_left` Does

Open `master.py` and find:

```python
def spin_left(speed, target_angle_degrees):
    """
    In-place spin to the LEFT using opposite wheel directions.

    - Right motor (port.E) runs forward.
    - Left motor (port.A) runs backward.
    - Stops when yaw reaches target_angle_degrees.
    """
    motion_sensor.reset_yaw(0)

    while motion_sensor.tilt_angles()[0] < target_angle_degrees:
        motor.run(port.A, speed)
        motor.run(port.E, speed)

    motor.stop(port.A, stop=motor.BRAKE)
    motor.stop(port.E, stop=motor.BRAKE)
```

Summarize behavior:
- Resets yaw to 0.
- Runs both wheels in opposite directions (relative to “drive_forward”) to rotate **in place** to the left.
- Uses the motion sensor yaw (`tilt_angles()[0]`) to decide when to stop.

Concept:
- The robot **spins left** without driving forward or backward significantly.

---

## 2. Inside the Full `spin_left` Method

Here is the method with explanation:

```python
def spin_left(speed, target_angle_degrees):
    """
    In-place spin to the LEFT using opposite wheel directions.

    - Right motor (port.E) runs forward.
    - Left motor (port.A) runs backward.
    - Stops when yaw reaches target_angle_degrees.
    """
    # 1) Reset yaw so current facing is 0 degrees
    motion_sensor.reset_yaw(0)

    # 2) Turn until yaw reaches the requested left angle
    while motion_sensor.tilt_angles()[0] < target_angle_degrees:
        # Backward on left, forward on right (relative to drive_forward)
        motor.run(port.A, speed)
        motor.run(port.E, speed)

    # 3) Stop both wheels with brake
    motor.stop(port.A, stop=motor.BRAKE)
    motor.stop(port.E, stop=motor.BRAKE)
```

Walk-through:
- `motion_sensor.reset_yaw(0)`:
  - Sets yaw to 0 at the current heading.
  - After this, yaw tells us how far we’ve turned left/right from that starting orientation.
- Yaw sign convention:
  - Left turns → yaw increases (positive).
  - Right turns → yaw decreases (negative).
- The `while` loop:
  - Reads `yaw = motion_sensor.tilt_angles()[0]`.
  - While `yaw < target_angle_degrees`, the robot keeps spinning left.
- Motor commands:
  - Both `motor.run(port.A, speed)` and `motor.run(port.E, speed)` are used here with signs chosen relative to how `drive_forward` is wired on your robot.
  - Because of that wiring, this pair of commands makes the robot rotate around its center rather than drive straight.
  - Both wheels move, but in such a way that the net translation is small and the main effect is rotation.
- When yaw reaches `target_angle_degrees`:
  - The loop ends.
  - `motor.stop(port.A, ...)` and `motor.stop(port.E, ...)` brake both wheels to hold the final heading.

Key idea:
- `spin_left` is a yaw‑controlled **in‑place rotation**. We:
  - Reset yaw.
  - Continuously command wheel speeds that cause rotation.
  - Stop as soon as yaw hits the target left angle.

---

## 3. Mental Model – Wheels During a Left Spin

Ask students:
- “For a left spin, do we want the robot’s nose to turn left without moving much?”  
  → Yes.

Explain:
- Left wheel and right wheel move in opposite directions relative to forward.
- Combined effect is rotation around the robot’s center.

Compare to pivots:
- Pivot: one wheel moves, one is still.
- Spin: **both** wheels move → tighter turn, more centered.

---

## 4. Simple Field Test Mission

Create or reuse a mission that calls `spin_left`:

```python
async def mission_spin_left_test():
    # Adjust speed and angle on the field
    spin_left(200, 90)
    return
```

On the field:
1. Place the robot in open space.
2. Run the mission from the selector.
3. Observe:
   - Does the robot spin roughly in place?
   - Does it rotate left (counter‑clockwise) as expected?

---

## 5. Tuning the Spin Angle

Goal: Achieve a reliable ~90° left spin at a chosen speed.

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
- Use field graphics or a taped crosshair to judge orientation.
- Keep one “standard” spin_left setting (speed + angle) for quick use in missions.

---

## 6. Connecting `spin_left` to Missions

Ask:
- “When would a left spin be better than a pivot?”
  - Example: in tight spaces where you need to turn without drifting sideways.

Activity:
- Identify a mission step where the robot must quickly turn left in place (e.g., after leaving base to face a different model).
- Insert a tuned `spin_left(speed, angle)` call into that mission.
- Test on the field to ensure the robot ends up facing the correct direction without colliding with nearby models or walls.

This focused practice makes `spin_left` a reliable tool in your mission toolbox for fast orientation changes.  

---

