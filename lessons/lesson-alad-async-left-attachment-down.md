# Lesson ALAD – `async_left_attachment_down`

> Environment: Spike App IDE with our FLL robot and `master.py`

## Lesson Goals

By the end of this lesson, students will be able to:
- Explain what `async_left_attachment_down(degrees, speed)` does.
- Understand how it differs from the blocking `left_attachment_down`.
- Use `async_left_attachment_down` in parallel with other async tasks (for example, driving back while lowering the arm).

---

## 1. What `async_left_attachment_down` Does

Open `master.py` and find:

```python
async def async_left_attachment_down(degrees, speed=1110):
    """
    Move the left attachment down in a non-blocking way for use in parallel tasks.
    """
    motor.reset_relative_position(port.C, 0)

    while -motor.relative_position(port.C) < degrees:
        motor.run(port.C, -speed)
        await runloop.sleep_ms(10)

    motor.stop(port.C, stop=motor.BRAKE)
```

Summarize behavior:
- Resets the encoder on `port.C` (left attachment motor) to 0.
- Runs the motor in the **downward** direction (negative speed).
- Keeps moving until the encoder change reaches `degrees`.
- Uses `await runloop.sleep_ms(10)` in the loop so other tasks can run.
- Stops the motor with brake at the end.

Key difference from `left_attachment_down`:
- `left_attachment_down` is a blocking helper.
- `async_left_attachment_down` is **non-blocking**, meant for use with `runloop.create_task` in parallel with other motion.

---

## 2. Why Use an Async “Down” Helper?

Explain:
- Often you want to **reset the arm while something else is happening**, like driving away.
- Blocking down-motions force you to:
  - Finish driving, then lower the arm, or
  - Finish lowering the arm, then drive.
- With `async_left_attachment_down`, you can:
  - Start the retreat drive and the arm reset at the same time.

Mini‑discussion:
- “Why do we still need `await runloop.sleep_ms(10)` in the loop?”  
  → To allow other async tasks (like driving) to get CPU time.

---

## 3. Basic Usage – Solo Async Lower

You can test `async_left_attachment_down` alone:

```python
async def mission_async_left_down_test():
    # First move up using the blocking helper
    left_attachment_up(180, speed=400)

    # Then move down using the async helper
    await async_left_attachment_down(180, speed=400)
    return
```

On the robot:
- Confirm that the attachment returns to (or very near) its original “home” position.
- Compare behavior to using `left_attachment_down(180, 400)` directly.

---

## 4. Parallel Use – Back Away While Lowering

Example: drive backward while lowering the left attachment:

```python
async def mission_back_and_lower_left():
    # Assume the arm is already up
    back_task = runloop.create_task(async_drive_backward(150, 720))
    lower_task = runloop.create_task(async_left_attachment_down(180, speed=400))

    await back_task
    await lower_task
```

Explain:
- Both tasks start together.
- The robot retreats while the arm lowers.
- When both `await` calls finish, the robot should be back and the arm should be down.

Field activity:
- Test different `target_degrees` for driving and `degrees` for lowering.
- Ensure the arm is fully down before you need it clear for the next action.

---

## 5. Good Practices

Suggestions:
- Use `async_left_attachment_down` when you want to **save time** by resetting the arm during other motion.
- Use the blocking `left_attachment_down` when clarity is more important and no parallel action is needed.
- Always test new parallel actions carefully on the field:
  - Watch for unwanted collisions while backing and lowering at the same time.
  - Adjust speeds and degrees so the motion is smooth and safe.  

---

[Back to Lessons Index](index.html)
