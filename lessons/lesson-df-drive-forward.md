# Lesson DF – `drive_forward`

> Environment: Spike App IDE with our FLL robot and `master.py`

## Lesson Goals

By the end of this lesson, students will be able to:
- Explain what `drive_forward(min_speed, max_speed, target_degrees, kP)` does.
- Choose reasonable values for `min_speed`, `max_speed`, `target_degrees`, and `kP`.
- Tune a straight drive on the field for a specific distance.

---

## 1. Where `drive_forward` Lives and What It Does

Open `master.py` and find:

```python
def drive_forward(min_speed, max_speed, target_degrees, kP=0.5):
    ...
```

Summarize behavior:
- Resets yaw and the left motor encoder.
- Accelerates from `min_speed` up to `max_speed`.
- Holds speed, then decelerates back down to `min_speed`.
- Uses **proportional correction** with yaw to stay straight.
- Stops when the left motor has turned `target_degrees`.

Parameter meanings:
- `min_speed` – gentle starting/ending speed (safer, less wheel slip).
- `max_speed` – highest speed during the run.
- `target_degrees` – how far the left wheel should rotate (distance proxy).
- `kP` – proportional gain; how strongly yaw error changes the wheel speeds.

---

## 2. Inside the Full `drive_forward` Method

Here is a simplified version of the full method in `master.py`:

```python
def drive_forward(min_speed, max_speed, target_degrees, kP=0.5):
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
        distance_travelled = -motor.relative_position(port.A)

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

        # 4) Send commands to motors (note: left motor direction is flipped)
        motor.run(port.A, -left_command)
        motor.run(port.E, right_command)

        # 5) Stop when the distance target is reached
        if distance_travelled >= target_degrees:
            motor.stop(port.A, stop=motor.BRAKE)
            motor.stop(port.E, stop=motor.BRAKE)
            return False
```

Walk-through:
- It uses a **phase** variable (ACCELERATE/CRUISE/DECELERATE/FINISH) to manage speed changes over time.
- `distance_travelled` comes from the left motor encoder; this is the main distance reference.
- In ACCELERATE, speeds ramp up slowly to avoid sudden jumps.
- If more than half the distance is already covered during acceleration, the code **skips the cruise phase** and goes straight to deceleration (useful for shorter moves).
- `accel_degrees` remembers how much distance was spent accelerating so CRUISE and DECELERATE can roughly mirror it.
- In DECELERATE, speeds ramp down gradually back to `min_speed`.
- Yaw-based correction (`kP * yaw`) is applied every loop to keep the robot on heading.
- Motor commands are clamped to avoid exceeding `max_speed`.
- The loop ends when the encoder shows the left wheel has turned `target_degrees`.

---

## 3. Proportional Correction Recap

Key lines inside the function:

```python
yaw = motion_sensor.tilt_angles()[0]
correction = int(kP * yaw)

left_command = left_speed + correction
right_command = right_speed - correction
```

Explain in simple terms:
- If yaw is not 0, the robot is drifting off its intended heading.
- We multiply yaw by `kP` to get a correction amount.
- We adjust left/right speeds in **opposite** directions to steer back.

Thought exercise:
- What happens if `kP` is 0? (No correction → more drift.)
- What happens if `kP` is too large? (Robot “wiggles” or oscillates.)

---

## 4. Simple Field Test for `drive_forward`

Create or reuse a mission that calls `drive_forward`:

```python
async def mission_drive_forward_test():
    # Tune these numbers on the field
    drive_forward(20, 250, 720, kP=0.5)
    return
```

On the field:
1. Place the robot squarely against base or along a mat line.
2. Run the mission via the selector.
3. Observe:
   - How far does it travel?
   - Does it drift left or right?

---

## 5. Tuning `drive_forward` – Distance and Straightness

Adjusting **distance**:
- Increase `target_degrees` to go farther.
- Decrease `target_degrees` to go shorter.
- Record values that correspond to specific field distances (e.g., “to model X”).

Adjusting **speeds**:
- Start with conservative values:
  - `min_speed = 20`
  - `max_speed = 200–250`
- Once the run is reliable, increase `max_speed` in steps (e.g., 50 at a time).

Adjusting **kP**:
- Start with `kP = 0.5`.
- If the robot drifts, try `0.6` or `0.7`.
- If it wiggles or oscillates, reduce `kP`.

Suggested tuning table (students fill in):

| Test | min_speed | max_speed | degrees | kP  | Result / Notes           |
|------|-----------|-----------|---------|-----|--------------------------|
| 1    | 20        | 200       | 720     | 0.5 | Drifted slightly left    |
| 2    | 20        | 200       | 720     | 0.6 | Straighter               |
| 3    | 20        | 250       | 720     | 0.6 | Faster, still acceptable |

---

## 6. Connecting to Real Missions

Ask:
- “Which FLL mission needs a reliable straight drive?”
- “Can we use one `drive_forward` call to get from base to that model?”

Activity:
- Pick one real mission and identify the main straight leg.
- Use a test mission with `drive_forward` to tune that leg until it lands consistently where you need it.
- Then copy those tuned values into the real mission function (e.g., `mission_4`).  

---

