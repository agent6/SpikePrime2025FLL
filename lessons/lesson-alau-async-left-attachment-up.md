# Lesson ALAU – `async_left_attachment_up`

> Environment: Spike App IDE with our FLL robot and `master.py`

## Lesson Goals

By the end of this lesson, students will be able to:
- Explain what `async_left_attachment_up(degrees, speed)` does.
- Understand how it differs from the blocking `left_attachment_up`.
- Use `async_left_attachment_up` in parallel with driving using `runloop.create_task`.

---

## 1. What `async_left_attachment_up` Does

Open `master.py` and find:

```python
async def async_left_attachment_up(degrees, speed=1110):
    """
    Move the left attachment up in a non-blocking way for use in parallel tasks.
    """
    motor.reset_relative_position(port.C, 0)

    while motor.relative_position(port.C) < degrees:
        motor.run(port.C, speed)
        await runloop.sleep_ms(10)

    motor.stop(port.C, stop=motor.BRAKE)
```

Summarize behavior:
- Resets the encoder on `port.C` (left attachment motor) to 0.
- Runs the motor until `relative_position(port.C)` reaches `degrees`.
- Uses `await runloop.sleep_ms(10)` in the loop so other tasks can run.
- Stops the motor with brake when done.

Key difference from `left_attachment_up`:
- `left_attachment_up` is a **blocking** helper using `run_for_degrees`.
- `async_left_attachment_up` is **non-blocking**, designed to run in parallel with other async tasks (like async driving).

---

## 2. Why This Helper is Async

Explain:
- Missions often need to **move an attachment while the robot is driving**.
- With a blocking helper, the robot would:
  - Either finish driving, then move the arm, or
  - Finish moving the arm, then drive.
- With `async_left_attachment_up`:
  - We can start lifting and driving at the same time.
  - Each loop iteration moves the motor a bit and then yields with `await runloop.sleep_ms(10)`.

Mini‑discussion:
- “What happens if we remove the `await` inside the loop?”  
  → The attachment task would hog time, and other async tasks would struggle to run smoothly.

---

## 3. Basic Usage – Solo Async Lift

You can test `async_left_attachment_up` by itself:

```python
async def mission_async_left_up_test():
    await async_left_attachment_up(180, speed=400)
    return
```

On the robot:
- Confirm the left attachment moves up the expected amount.
- Compare behavior to `left_attachment_up(180, 400)`:
  - They should end at similar positions.
  - The async version just yields to `runloop` while moving.

---

## 4. Parallel Use – Drive While Lifting the Left Attachment

Example: drive forward while raising the left attachment:

```python
async def mission_drive_and_lift_left():
    drive_task = runloop.create_task(async_drive_forward(150, 720))
    arm_task = runloop.create_task(async_left_attachment_up(180, speed=400))

    await drive_task
    await arm_task
```

Explain:
- Both tasks start at the same time.
- Each task uses `await runloop.sleep_ms(...)` internally, so they share time.
- By the time the robot reaches the model, the arm may already be up.

Field activity:
- Try different `target_degrees` for driving and different `degrees` for the arm.
- Adjust so that the arm is fully up just before the robot reaches the contact point.

---

## 5. Good Practices

Suggestions:
- Use `async_left_attachment_up` only when you actually need parallel movement.
- For simple missions where actions can happen one after another, prefer the blocking `left_attachment_up` to keep code easier to read.
- Always test combined actions (drive + lift) many times on the field to ensure there are no surprises before using them in competition.  

---

[Back to Lessons Index](index.html)
