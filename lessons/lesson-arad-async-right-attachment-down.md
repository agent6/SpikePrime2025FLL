# Lesson ARAD – `async_right_attachment_down`

> Environment: Spike App IDE with our FLL robot and `master.py`

## Lesson Goals

By the end of this lesson, students will be able to:
- Explain what `async_right_attachment_down(degrees, speed)` does.
- Understand how it differs from the blocking `right_attachment_down`.
- Use `async_right_attachment_down` in parallel with other async tasks (for example, driving back while lowering the right attachment).

---

## 1. What `async_right_attachment_down` Does

Open `master.py` and find:

```python
async def async_right_attachment_down(degrees, speed):
    """
    Move the right attachment down in a non-blocking way for use in parallel tasks.
    """
    motor.reset_relative_position(port.B, 0)

    while -motor.relative_position(port.B) < degrees:
        motor.run(port.B, -speed)
        await runloop.sleep_ms(10)

    motor.stop(port.B, stop=motor.BRAKE)
```

Summarize behavior:
- Resets the encoder on `port.B` (right attachment motor) to 0.
- Runs the motor in the **downward** direction (negative speed).
- Keeps moving until the encoder change reaches `degrees`.
- Uses `await runloop.sleep_ms(10)` in the loop so other tasks can run.
- Stops the motor with brake at the end.

Key difference from `right_attachment_down`:
- `right_attachment_down` is a blocking helper.
- `async_right_attachment_down` is **non-blocking**, intended for use alongside other async tasks.

---

## 2. Why Use an Async “Down” Helper?

Explain:
- Missions often need to **reset the right attachment while something else happens**, like backing away from a model.
- Blocking helpers force you to:
  - Finish driving, then lower the attachment, or
  - Finish lowering, then drive.
- With `async_right_attachment_down`, you can:
  - Start retreating and lowering at the same time.

Reinforce:
- `await runloop.sleep_ms(10)` inside the loop is what allows sharing time with other async tasks.

---

## 3. Basic Usage – Solo Async Lower

You can test `async_right_attachment_down` by itself:

```python
async def mission_async_right_down_test():
    # First move up using the blocking helper
    right_attachment_up(180, speed=400)

    # Then move down using the async helper
    await async_right_attachment_down(180, speed=400)
    return
```

On the robot:
- Confirm that the right attachment returns to (or very near) its original “home” position.
- Compare behavior and final position to `right_attachment_down(180, 400)`.

---

## 4. Parallel Use – Back Away While Lowering

Example: drive backward while lowering the right attachment:

```python
async def mission_back_and_lower_right():
    # Assume the right attachment is already up
    back_task = runloop.create_task(async_drive_backward(150, 720))
    lower_task = runloop.create_task(async_right_attachment_down(180, speed=400))

    await back_task
    await lower_task
```

Explain:
- Both tasks start together.
- The robot backs away while the right attachment lowers.
- When both `await` calls finish, the robot should be in position with the attachment down.

Field activity:
- Test different `target_degrees` for driving and `degrees` for lowering.
- Make sure the attachment is fully down and clear before the next action in your mission.

---

## 5. Good Practices

Suggestions:
- Use `async_right_attachment_down` when parallel motion saves mission time or reduces stationary moments near models.
- Stick with `right_attachment_down` when the mission is simpler and doesn’t need parallel actions.
- Always test new combined drive + lower sequences many times:
  - Watch for collisions as the robot moves and lowers.
  - Tune speeds, degrees, and distances until the motion is smooth, safe, and repeatable.  

---

[Back to Lessons Index](index.html)
