# Lesson DB – `drive_backward`

> Environment: Spike App IDE with our FLL robot and `master.py`

## Lesson Goals

By the end of this lesson, students will be able to:
- Explain what `drive_backward(min_speed, max_speed, target_degrees, kP)` does.
- Choose reasonable values for `min_speed`, `max_speed`, `target_degrees`, and `kP` when driving backward.
- Tune a straight **reverse** drive on the field for a specific distance.

---

## 1. Where `drive_backward` Lives and What It Does

Open `master.py` and find:

```python
def drive_backward(min_speed, max_speed, target_degrees, kP=0.5):
    ...
```

Summarize behavior:
- Resets yaw and the left motor encoder.
- Accelerates from `min_speed` up to `max_speed` while driving **backward**.
- Holds speed, then decelerates back down to `min_speed`.
- Uses **proportional correction** with yaw to stay straight in reverse.
- Stops when the left motor has turned `target_degrees` backwards.

Parameter meanings (same as forward):
- `min_speed` – gentle starting/ending speed.
- `max_speed` – highest speed during the run.
- `target_degrees` – how far the left wheel should rotate (distance proxy).
- `kP` – proportional gain; how strongly yaw error changes the wheel speeds.

---

## 2. Inside the Full `drive_backward` Method

Here is a simplified version of the full method in `master.py`:

```python
def drive_backward(min_speed, max_speed, target_degrees, kP=0.5):
    ACCELERATE = 1
    CRUISE = 2
    DECELERATE = 3
    FINISH = 4

    motion_sensor.reset_yaw(0)
    motor.reset_relative_position(port.A, 0)

    left_speed = min_speed
    right_speed = min_speed
    phase = ACCELERATE
    speed_step_counter = 1
    accel_degrees = 0

    while True:
        distance_travelled = motor.relative_position(port.A)

        # 1) Phase state machine: accelerate → cruise → decelerate → finish
        if phase == ACCELERATE:
            # Slowly ramp up both wheel speeds
            speed_step_counter += 1
            if speed_step_counter == 4:
                left_speed += 1
                right_speed += 1
                speed_step_counter = 1

            # If we have already gone at least half the distance,
            # skip the cruise phase and start decelerating early.
            if distance_travelled >= (target_degrees / 2):
                phase = DECELERATE

            # When we hit max_speed, move to CRUISE and remember
            # how many degrees acceleration took.
            if left_speed >= max_speed:
                phase = CRUISE
                left_speed = max_speed
                right_speed = max_speed
                accel_degrees = distance_travelled

        elif phase == CRUISE:
            # Stay at max speed until we are close enough to the target
            # that it's time to decelerate. We use accel_degrees to
            # roughly mirror the distance spent accelerating.
            if distance_travelled >= (target_degrees - (2 * accel_degrees)):
                phase = DECELERATE

        elif phase == DECELERATE:
            # Gradually ramp speeds back down toward min_speed
            speed_step_counter += 1
            if speed_step_counter == 4:
                left_speed -= 1
                right_speed -= 1
                speed_step_counter = 1
            if left_speed <= min_speed:
                left_speed = min_speed
                right_speed = min_speed
                phase = FINISH

        if phase == FINISH:
            # Hold at min_speed until we reach the final distance
            left_speed = min_speed
            right_speed = min_speed

        # 2) Heading correction using yaw and kP
        yaw = motion_sensor.tilt_angles()[0]
        correction = int(kP * yaw)

        left_command = left_speed + correction
        right_command = right_speed - correction

        # 3) Clamp motor commands so they never exceed max_speed
        max_cmd = max_speed
        left_command = max(-max_cmd, min(max_cmd, left_command))
        right_command = max(-max_cmd, min(max_cmd, right_command))

        # 4) Send commands to motors, reversed relative to drive_forward
        motor.run(port.A, left_command)
        motor.run(port.E, -right_command)

        # 5) Stop when the distance target is reached
        if distance_travelled >= target_degrees:
            motor.stop(port.A, stop=motor.BRAKE)
            motor.stop(port.E, stop=motor.BRAKE)
            return False
```

Walk-through:
- Uses the same **phase** state machine as `drive_forward` (ACCELERATE/CRUISE/DECELERATE/FINISH).
- `distance_travelled` now uses the left motor encoder in the **forward** direction, but we reverse the motor commands to drive backward.
- In ACCELERATE, both wheel speeds ramp up gradually until:
  - Either we reach half the target distance (skip CRUISE → DECELERATE), or
  - We reach `max_speed` (enter CRUISE and remember `accel_degrees`).
- CRUISE keeps `left_speed`/`right_speed` at `max_speed` until we are “2 × accel_degrees” from the target, then switches to DECELERATE.
- DECELERATE ramps speeds down step-by-step back to `min_speed`.
- Yaw-based correction (`kP * yaw`) runs every loop, just like in `drive_forward`, but the base directions are reversed.
- Commands are clamped to `±max_speed` to keep speeds under control.
- The loop ends when `distance_travelled >= target_degrees` and brakes both motors.

---

## 3. Proportional Correction in Reverse

Inside `drive_backward`, we still use yaw:

```python
yaw = motion_sensor.tilt_angles()[0]
correction = int(kP * yaw)

left_command = left_speed + correction
right_command = right_speed - correction
```

Key idea:
- The robot is moving backward, but yaw still tells us if we are drifting.
- We adjust left/right speeds to steer back to the intended heading.

Thought exercise:
- Why is backward driving harder to keep straight than forward?
- How might that affect your choice of `max_speed` and `kP`?

---

## 4. Simple Field Test for `drive_backward`

Create or reuse a mission that calls `drive_backward`:

```python
async def mission_drive_backward_test():
    # Tune these numbers on the field
    drive_backward(20, 200, 720, kP=0.5)
    return
```

On the field:
1. Place the robot squarely against base facing into the field.
2. Run the mission via the selector.
3. Observe:
   - How far backward does it travel?
   - Does it drift left or right as it reverses?

---

## 5. Tuning `drive_backward` – Distance and Straightness

Adjusting **distance**:
- Increase `target_degrees` to go farther backward.
- Decrease `target_degrees` to go shorter.
- Record values that correspond to backing out of specific locations.

Adjusting **speeds**:
- Start conservative:
  - `min_speed = 20`
  - `max_speed = 150–200` (often lower than forward).
- Increase `max_speed` only after backward runs are reliable.

Adjusting **kP**:
- Start with `kP = 0.5`.
- If reverse drifts, try `0.6` or `0.7`.
- If it wiggles, lower `kP`.

Suggested tuning table:

| Test | min_speed | max_speed | degrees | kP  | Result / Notes             |
|------|-----------|-----------|---------|-----|----------------------------|
| 1    | 20        | 150       | 720     | 0.5 | Small drift right          |
| 2    | 20        | 150       | 720     | 0.6 | Straighter                 |
| 3    | 20        | 180       | 720     | 0.6 | Faster, still controllable |

---

## 6. Connecting to Real Missions

Backward moves are common when:
- Leaving a model after interacting.
- Backing up to base without turning around.

Activity:
- Pick one mission where the robot should **retreat backward** instead of turning first.
- Use `mission_drive_backward_test` to tune the reverse leg until it returns reliably to the desired location.
- Copy the tuned `drive_backward` call into the corresponding mission function (e.g., after a model hit in `mission_4` or `mission_5`).  

---

