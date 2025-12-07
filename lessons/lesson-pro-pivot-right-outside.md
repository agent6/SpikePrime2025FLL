# Lesson PRO – `pivot_right_outside`

> Environment: Spike App IDE with our FLL robot and `master.py`

## Lesson Goals

By the end of this lesson, students will be able to:
- Explain what `pivot_right_outside(speed, target_angle_degrees)` does.
- Predict which wheel moves and which stays still.
- Tune a right outside pivot angle for accurate field turns.

---

## 1. What `pivot_right_outside` Does

Open `master.py` and find:

```python
def pivot_right_outside(speed, target_angle_degrees):
    """
    Pivot turn to the RIGHT using the outside wheel.

    Right turn, outside wheel moves FORWARD:
    - Left motor (port.A) is the outside wheel and moves forward.
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
- Runs the **left wheel (port.A)** forward (relative to our drive direction).
- Keeps the **right wheel (port.E)** stopped.
- Reads yaw (`tilt_angles()[0]`) until it reaches `-target_angle_degrees`.
- Stops the left wheel with brake.

Concept:
- The robot turns **right** around the **right (inside)** wheel; the left wheel is the outside wheel moving forward.

---

## 2. Inside the Full `pivot_right_outside` Method

Here is the method again with a step-by-step explanation:

```python
def pivot_right_outside(speed, target_angle_degrees):
    """
    Pivot turn to the RIGHT using the outside wheel.

    Right turn, outside wheel moves FORWARD:
    - Left motor (port.A) is the outside wheel and moves forward.
    - Right motor (port.E) stays stopped.
    The motion sensor yaw is used as the angle reference.
    """
    # 1) Reset yaw so current heading is 0 degrees
    motion_sensor.reset_yaw(0)

    # 2) Turn until yaw reaches -target_angle_degrees
    while motion_sensor.tilt_angles()[0] > -target_angle_degrees:
        # Left wheel (outside) moves, right wheel stays stopped
        motor.run(port.A, -speed)

    # 3) Stop the left wheel when the angle is reached
    motor.stop(port.A, stop=motor.BRAKE)
```

Walk-through:
- `motion_sensor.reset_yaw(0)`:
  - Sets yaw to 0 at the starting heading.
  - All subsequent yaw readings measure how far we’ve turned from that starting pose.
- Yaw sign convention in this code:
  - For right turns, yaw becomes **negative**.
  - For left turns, yaw becomes **positive**.
- The `while` loop:
  - Reads `yaw = motion_sensor.tilt_angles()[0]`.
  - While `yaw > -target_angle_degrees`, it keeps running the left motor.
  - As the robot turns right, yaw decreases from 0 down toward `-target_angle_degrees`.
- `motor.run(port.A, -speed)`:
  - Commands the left wheel to move in the “forward” direction for a right outside pivot (relative to how `drive_forward` is wired in this robot).
  - The right wheel on `port.E` remains stopped, acting as the pivot point.
- When yaw reaches `-target_angle_degrees`:
  - The loop exits.
  - `motor.stop(port.A, stop=motor.BRAKE)` brakes the moving wheel to hold the final orientation.

Key idea:
- `pivot_right_outside` is a yaw‑controlled pivot where the **outside wheel** (left) moves and the inside wheel (right) stays still. The motion sensor decides when to stop based on reaching a negative yaw angle.

---

## 3. Quick Mental Model

Ask students:
- “If only the left wheel moves forward and the right stays still, which way do we turn?”  
  → Right.
- “Where is the center of this turn?”  
  → Near the right wheel.

Relate to geometry:
- The moving left wheel travels a wider arc.
- The right wheel marks the approximate pivot point.

---

## 4. Simple Field Test Mission

Create or reuse a mission that calls `pivot_right_outside`:

```python
async def mission_pivot_right_outside_test():
    # Adjust speed and angle on the field
    pivot_right_outside(200, 90)
    return
```

On the field:
1. Place the robot square against base or along a mat line.
2. Run the mission from the selector.
3. Observe:
   - Does the robot pivot around the right wheel?
   - Roughly how far (what angle) does it turn?

---

## 5. Tuning the Pivot Angle

Goal: Achieve a reliable ~90° right outside pivot at a chosen speed.

Steps:
1. Start with `speed = 200`, `target_angle_degrees = 90`.
2. Run several times and check where the robot ends up.
3. If it **under-turns** (less than 90°):
   - Increase `target_angle_degrees` slightly (e.g., 92–95).
4. If it **over-turns**:
   - Decrease `target_angle_degrees` slightly (e.g., 85–88).

Suggested tuning table:

| Test | speed | target_angle | Result / Notes                   |
|------|-------|--------------|----------------------------------|
| 1    | 200   | 90           | Slightly short of 90°           |
| 2    | 200   | 94           | Closer to 90°, acceptable       |
| 3    | 200   | 94           | Repeatable within small error   |

Encourage:
- Use mat lines or robot base edge as visual guides.
- Pick a “standard” right outside pivot angle for your robot and record it.

---

## 6. Connecting to Real Missions

Ask:
- “Where in our missions do we need a precise right turn around one wheel?”
  - Example: pivot right from base to face a specific model or line.

Activity:
- Identify one mission where `pivot_right_outside` is appropriate.
- Insert your tuned call (speed and angle) into that mission.
- Test on the field and confirm the pivot lines the robot up correctly for the next action (e.g., a straight drive or attachment use).

This lesson complements the left outside pivot (PLO) and helps build a complete set of reliable right‑turn maneuvers for FLL runs.  

---

