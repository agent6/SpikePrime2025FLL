# Lesson PLO – `pivot_left_outside`

> Environment: Spike App IDE with our FLL robot and `master.py`

## Lesson Goals

By the end of this lesson, students will be able to:
- Explain what `pivot_left_outside(speed, target_angle_degrees)` does.
- Predict which wheel moves and which stays still.
- Tune a left outside pivot angle for accurate field turns.

---

## 1. What `pivot_left_outside` Does

Open `master.py` and find:

```python
def pivot_left_outside(speed, target_angle_degrees):
    """
    Pivot turn to the LEFT using the outside wheel.

    Left turn, outside wheel moves FORWARD:
    - Right motor (port.E) is the outside wheel and moves forward.
    - Left motor (port.A) stays stopped.
    The motion sensor yaw is used as the angle reference.
    """
    motion_sensor.reset_yaw(0)

    while motion_sensor.tilt_angles()[0] < target_angle_degrees:
        motor.run(port.E, speed)

    motor.stop(port.E, stop=motor.BRAKE)
```

Summarize behavior:
- Resets yaw to 0.
- Runs the **right wheel (port.E)** forward.
- Keeps the **left wheel (port.A)** stopped.
- Reads yaw (`tilt_angles()[0]`) until it reaches `target_angle_degrees`.
- Stops the right wheel with brake.

Concept:
- The robot turns **left** around the **left (inside)** wheel.

---

## 2. Inside the Full `pivot_left_outside` Method

Let’s break down what the method is doing step-by-step:

```python
def pivot_left_outside(speed, target_angle_degrees):
    """
    Pivot turn to the LEFT using the outside wheel.

    Left turn, outside wheel moves FORWARD:
    - Right motor (port.E) is the outside wheel and moves forward.
    - Left motor (port.A) stays stopped.
    The motion sensor yaw is used as the angle reference.
    """
    # 1) Reset yaw so 0 = current heading
    motion_sensor.reset_yaw(0)

    # 2) Keep turning until the yaw angle reaches target_angle_degrees
    while motion_sensor.tilt_angles()[0] < target_angle_degrees:
        # Only the right wheel moves; left wheel stays still
        motor.run(port.E, speed)

    # 3) Once we hit the angle, stop the moving wheel
    motor.stop(port.E, stop=motor.BRAKE)
```

Walk-through:
- `motion_sensor.reset_yaw(0)`:
  - Sets the yaw reading to 0 at the start of the pivot.
  - From this point, yaw measures how many degrees we’ve turned left/right from that starting facing.
- The `while` loop:
  - Reads yaw with `motion_sensor.tilt_angles()[0]`.
  - As the robot turns left, this yaw value increases.
  - While yaw is **less than** `target_angle_degrees`, the right wheel keeps running at `speed`.
- Motor commands:
  - `motor.run(port.E, speed)`:
    - Only the right wheel (port E) is powered.
    - The left wheel (port A) stays stopped, acting as the pivot point.
  - This causes the robot to swing left around the left wheel.
- When yaw reaches or exceeds `target_angle_degrees`:
  - The loop exits.
  - `motor.stop(port.E, stop=motor.BRAKE)` brakes the moving wheel to hold the angle.

Key idea:
- `pivot_left_outside` is a **yaw-based “turn until angle” loop** where:
  - We control **one wheel**.
  - The **motion sensor** decides when to stop.

---

## 3. Quick Mental Model

Ask students:
- “If only the right wheel moves forward, which way will the robot turn?”  
  → Left.
- “What is the center of this turn?”  
  → Near the left wheel.

Relate to geometry:
- The path of the moving wheel is a wider arc.
- The stopped wheel marks the approximate rotation center.

---

## 4. Simple Field Test Mission

Create or reuse a mission that calls `pivot_left_outside`:

```python
async def mission_pivot_left_outside_test():
    # Adjust speed and angle on the field
    pivot_left_outside(200, 90)
    return
```

On the field:
1. Place the robot square against base or a line.
2. Run the mission from the selector.
3. Observe:
   - Does the robot pivot around the left wheel?
   - Roughly how far (what angle) does it turn?

---

## 5. Tuning the Pivot Angle

Goal: Achieve a reliable ~90° left pivot for a chosen speed.

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
- Mark a reference line on the mat (or use field graphics) to judge 90°.
- Pick a “standard” left outside pivot angle for your robot and write it down.

---

## 6. Connecting to Real Missions

Ask:
- “Where in our missions do we need a precise left turn around one wheel?”
  - Example: pivot left from base to align with a model or line.

Activity:
- Identify one real situation where `pivot_left_outside` is a good fit.
- Copy your tuned call (speed and angle) into that mission function.
- Test the full mission and confirm the pivot lines the robot up correctly.

This lesson builds intuition for `pivot_left_outside`, which pairs with the other pivot helpers to handle all the directional turns you need on the FLL field.  

---

