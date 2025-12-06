# Lesson LAD – `left_attachment_down`

> Environment: Spike App IDE with our FLL robot and `master.py`

## Lesson Goals

By the end of this lesson, students will be able to:
- Explain what `left_attachment_down(degrees, speed)` does.
- Use it to return the left attachment from “up” back to a safe “home” position.
- Combine `left_attachment_up` and `left_attachment_down` for reliable out‑and‑back motions.

---

## 1. What `left_attachment_down` Does

Open `master.py` and find:

```python
def left_attachment_down(degrees, speed=1110):
    """
    Move the left attachment DOWN for a given encoder distance.

    - Left attachment motor is on port.C.
    - Positive degrees values command a downward move.
    """
    motor.reset_relative_position(port.C, 0)
    while -motor.relative_position(port.C) < degrees:
        motor.run(port.C, -speed)
    motor.stop(port.C, stop=motor.BRAKE)
```

Summarize behavior:
- Resets the encoder on `port.C` to 0.
- Runs the left attachment motor **in the opposite direction** (negative speed).
- Stops once the encoder has changed by `degrees` in the downward direction.

Concept:
- This is the counterpart to `left_attachment_up` and should bring the mechanism back to its starting or “home” position (if `degrees` match).

---

## 2. Matching `up` and `down` Degrees

Explain:
- If `left_attachment_up` moves the motor `+degrees`, then `left_attachment_down` should move it **back** by a similar amount.
- Using the same `degrees` for up and down is a good starting point.

Example pair:

```python
left_attachment_up(180, speed=400)
left_attachment_down(180, speed=400)
```

Activity:
- Mark the “home” position of the attachment with tape.
- Run the up/down pair and check if the mechanism returns to the mark.
- Adjust `degrees` slightly if needed so the home position is consistent.

---

## 3. Simple Test Mission – Up Then Down

Create or reuse a mission combining both helpers:

```python
async def mission_left_attachment_up_down_test():
    # Move up
    left_attachment_up(180, speed=400)

    # Wait until motor C appears stopped (optional but recommended)
    await runloop.until(lambda: MotorIsStopped(port.C))

    # Move down
    left_attachment_down(180, speed=400)
    return
```

Run on the robot:
- Watch the attachment move up, pause, then return down.
- Confirm that it returns to the same resting position each time.

---

## 4. Using `left_attachment_down` Safely in Missions

Typical uses:
- After lifting or pushing a model with `left_attachment_up`, use `left_attachment_down` to:
  - Clear the model.
  - Avoid dragging or jamming when driving away.
  - Reset the attachment for the next run.

Example mission snippet:

```python
async def mission_left_model_safe():
    # Approach model
    drive_forward(20, 250, 360)

    # Lift to interact
    left_attachment_up(180, speed=400)
    await runloop.until(lambda: MotorIsStopped(port.C))

    # Back away
    drive_backward(20, 250, 360)

    # Return attachment home
    left_attachment_down(180, speed=400)
```

Discussion:
- Why is it important to always return the attachment home?
  - Consistent starting state.
  - Less chance of collisions on the next run.

Encourage students to:
- Treat `left_attachment_down` as a standard part of any mission that uses the left attachment.
- Record the tuned `degrees` and `speed` that reliably return the mechanism to its home position without slamming or stalling.  

---


