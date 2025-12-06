# Lesson ADF – `async_drive_forward`

> Environment: Spike App IDE with our FLL robot and `master.py`

## Lesson Goals

By the end of this lesson, students will be able to:
- Explain what `async_drive_forward(speed, target_degrees, kP)` does.
- Understand how it differs from the blocking `drive_forward`.
- Use `async_drive_forward` in parallel with other async tasks using `runloop.create_task`.

---

## 1. What `async_drive_forward` Does

Open `master.py` and find:

```python
async def async_drive_forward(speed, target_degrees, kP=0.5):
    """
    Simple forward drive with proportional gyro correction that can run in parallel
    with other async tasks (attachments, etc.).
    """
    motion_sensor.reset_yaw(0)
    motor.reset_relative_position(port.A, 0)

    while True:
        distance = -motor.relative_position(port.A)
        if distance >= target_degrees:
            motor.stop(port.A, stop=motor.BRAKE)
            motor.stop(port.E, stop=motor.BRAKE)
            return

        yaw = motion_sensor.tilt_angles()[0]
        correction = int(kP * yaw)

        left_command = speed + correction
        right_command = speed - correction

        motor.run(port.A, -left_command)
        motor.run(port.E, right_command)

        await runloop.sleep_ms(10)
```

Summarize behavior:
- Drives forward at a **constant base speed** (`speed`), with proportional yaw correction.
- Stops when the left motor has turned `target_degrees`.
- Uses `await runloop.sleep_ms(10)` to pause briefly each loop.

Key difference from `drive_forward`:
- `drive_forward` is blocking and has its own acceleration profile.
- `async_drive_forward` is simpler and **non‑blocking**, designed for parallel use.

---

## 2. Why the `await runloop.sleep_ms(10)` Matters

Explain:
- Without the `await`, the `while True` loop would hog the processor for that task.
- `await runloop.sleep_ms(10)`:
  - Gives time for other tasks (like async attachments) to run.
  - Makes `async_drive_forward` a good citizen in a multi‑tasking system.

Mini‑exercise:
- Ask students what would happen if we removed the `await` (answer: other async tasks would struggle to run smoothly).

---

## 3. Basic Usage – Solo Run

You can use `async_drive_forward` by itself and `await` it:

```python
async def mission_async_forward_test():
    await async_drive_forward(150, 720, kP=0.5)
    return
```

On the field:
- Compare behavior to `drive_forward`:
  - Constant speed vs. accel/decel profile.
  - Both use yaw to stay straight.

---

## 4. Parallel Use – Drive While Doing Something Else

The main reason to use `async_drive_forward` is to **run it in parallel** with other async tasks.

Example: drive forward while raising the left attachment:

```python
async def mission_forward_and_lift():
    drive_task = runloop.create_task(async_drive_forward(150, 720))
    arm_task = runloop.create_task(async_left_attachment_up(180, speed=400))

    await drive_task
    await arm_task
```

Explain:
- `runloop.create_task(...)` starts each async function as a separate task.
- Because both functions use `await runloop.sleep_ms(...)` internally, they can take turns running.
- `await drive_task` and `await arm_task` ensure both complete before the mission returns.

---

## 5. Practice – Tuning `async_drive_forward`

Field practice:
1. Start with `speed = 150`, `target_degrees = 720`, `kP = 0.5`.
2. Run several times and observe distance and straightness.
3. Adjust:
   - `speed` for faster/slower motion.
   - `target_degrees` for longer/shorter distance.
   - `kP` to reduce drift without causing wobble.

Then:
- Combine with an async attachment task and see if the timing matches your mission needs (for example, arm finishes lifting just before you reach the model).

Encourage students to:
- Use `async_drive_forward` only when they truly need parallel actions; otherwise, keep missions simple with the blocking helpers.  

---

[Back to Lessons Index](index.html)
