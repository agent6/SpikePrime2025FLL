# Lesson ADB – `async_drive_backward`

> Environment: Spike App IDE with our FLL robot and `master.py`

## Lesson Goals

By the end of this lesson, students will be able to:
- Explain what `async_drive_backward(speed, target_degrees, kP)` does.
- Understand how it differs from the blocking `drive_backward`.
- Use `async_drive_backward` in parallel with other async tasks using `runloop.create_task`.

---

## 1. What `async_drive_backward` Does

Open `master.py` and find:

```python
async def async_drive_backward(speed, target_degrees, kP=0.5):
    """
    Simple backward drive with proportional gyro correction that can run in parallel
    with other async tasks.
    """
    motion_sensor.reset_yaw(0)
    motor.reset_relative_position(port.A, 0)

    while True:
        distance = motor.relative_position(port.A)
        if distance >= target_degrees:
            motor.stop(port.A, stop=motor.BRAKE)
            motor.stop(port.E, stop=motor.BRAKE)
            return

        yaw = motion_sensor.tilt_angles()[0]
        correction = int(kP * yaw)

        left_command = speed + correction
        right_command = speed - correction

        motor.run(port.A, left_command)
        motor.run(port.E, -right_command)

        await runloop.sleep_ms(10)
```

Summarize behavior:
- Drives **backward** at a constant base speed (`speed`), with proportional yaw correction.
- Stops when the left motor has turned `target_degrees` in reverse.
- Uses `await runloop.sleep_ms(10)` to yield and allow other tasks to run.

Key difference from `drive_backward`:
- `drive_backward` is blocking and has its own accel/decel logic.
- `async_drive_backward` is simpler and **non‑blocking**, designed for parallel use.

---

## 2. Why the `await runloop.sleep_ms(10)` Matters

Explain:
- The `while True` loop continuously updates motor commands and checks distance.
- `await runloop.sleep_ms(10)`:
  - Lets other async tasks run between updates.
  - Keeps backward motion smooth while sharing time with attachments or other actions.

Ask:
- “What would happen if there were no `await` inside the loop?”  
  → The drive task would hog all the time; other async helpers would struggle to run.

---

## 3. Basic Usage – Solo Reverse Drive

You can use `async_drive_backward` by itself and `await` it:

```python
async def mission_async_backward_test():
    await async_drive_backward(150, 720, kP=0.5)
    return
```

On the field:
- Compare to `drive_backward`:
  - Constant speed vs. accel/decel.
  - Both use yaw to stay straight in reverse.

---

## 4. Parallel Use – Back Up While Moving an Attachment

The main strength of `async_drive_backward` is parallel motion.

Example: back away while lowering the left attachment:

```python
async def mission_back_and_lower():
    back_task = runloop.create_task(async_drive_backward(150, 720))
    lower_task = runloop.create_task(async_left_attachment_down(180, speed=400))

    await back_task
    await lower_task
```

Explain:
- Both tasks run together because they each include `await runloop.sleep_ms(...)` internally.
- This allows you to back away while resetting an attachment, saving time in missions.

---

## 5. Practice – Tuning `async_drive_backward`

Field practice:
1. Start with `speed = 150`, `target_degrees = 720`, `kP = 0.5`.
2. Run several times and note:
   - How far back the robot travels.
   - How straight it moves in reverse.
3. Adjust:
   - `speed` for slower/faster backing.
   - `target_degrees` for distance.
   - `kP` to reduce drift without causing oscillation.

Then:
- Combine with an async attachment motion (e.g., lowering an arm) and check if the timing matches your mission needs.

Encourage students to:
- Use `async_drive_backward` only in missions where parallel behavior is worth the added complexity.
- Prefer the simpler blocking `drive_backward` when no parallel action is needed, to keep mission code easier to read.  

---


