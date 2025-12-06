# Lesson ARAU – `async_right_attachment_up`

> Environment: Spike App IDE with our FLL robot and `master.py`

## Lesson Goals

By the end of this lesson, students will be able to:
- Explain what `async_right_attachment_up(degrees, speed)` does.
- Understand how it differs from the blocking `right_attachment_up`.
- Use `async_right_attachment_up` in parallel with driving using `runloop.create_task`.

---

## 1. What `async_right_attachment_up` Does

Open `master.py` and find:

```python
async def async_right_attachment_up(degrees, speed):
    """
    Move the right attachment up in a non-blocking way for use in parallel tasks.
    """
    motor.reset_relative_position(port.B, 0)

    while motor.relative_position(port.B) < degrees:
        motor.run(port.B, speed)
        await runloop.sleep_ms(10)

    motor.stop(port.B, stop=motor.BRAKE)
```

Summarize behavior:
- Resets the encoder on `port.B` (right attachment motor) to 0.
- Runs the motor in the **upward** direction until `relative_position(port.B)` reaches `degrees`.
- Uses `await runloop.sleep_ms(10)` in the loop so other tasks can run.
- Stops the motor with brake when done.

Key difference from `right_attachment_up`:
- `right_attachment_up` is blocking (`run_for_degrees`).
- `async_right_attachment_up` is **non-blocking**, meant for parallel use.

---

## 2. Why Use an Async “Up” Helper?

Explain:
- We often want the right attachment to move while the robot is moving:
  - For example, raising a tower as we drive toward a model.
- With a blocking helper, the sequence must be:
  - Drive, then move attachment, or
  - Move attachment, then drive.
- With `async_right_attachment_up`, we can:
  - Start driving and lifting at the same time.

Reinforce:
- The `await runloop.sleep_ms(10)` call inside the loop is what allows other async tasks to run.

---

## 3. Basic Usage – Solo Async Lift

You can test `async_right_attachment_up` by itself:

```python
async def mission_async_right_up_test():
    await async_right_attachment_up(180, speed=400)
    return
```

On the robot:
- Confirm that the right attachment moves to the expected “up” position.
- Compare behavior and final position to `right_attachment_up(180, 400)`.

---

## 4. Parallel Use – Drive While Raising the Right Attachment

Example: drive forward while raising the right attachment:

```python
async def mission_drive_and_lift_right():
    drive_task = runloop.create_task(async_drive_forward(150, 720))
    tower_task = runloop.create_task(async_right_attachment_up(180, speed=400))

    await drive_task
    await tower_task
```

Explain:
- Both tasks start at the same time.
- The robot moves while the right attachment lifts.
- When both `await` calls finish, the robot should be at its target position with the right attachment up.

Field activity:
- Adjust `target_degrees` and `degrees` so that:
  - The attachment reaches the correct height at the right time.
  - The robot is in the right place to use the attachment effectively.

---

## 5. Good Practices

Suggestions:
- Use `async_right_attachment_up` when parallel motion saves time or simplifies alignment.
- Prefer `right_attachment_up` when no parallel action is needed, to keep missions simple.
- Test combined drive + lift missions many times on the field:
  - Watch for collisions while driving and lifting.
  - Tune both speeds and degrees until the sequence is smooth and reliable.  

---

[Back to Lessons Index](index.html)
