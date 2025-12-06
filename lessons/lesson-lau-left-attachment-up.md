# Lesson LAU – `left_attachment_up`

> Environment: Spike App IDE with our FLL robot and `master.py`

## Lesson Goals

By the end of this lesson, students will be able to:
- Explain what `left_attachment_up(degrees, speed)` does.
- Choose appropriate `degrees` and `speed` values for a left-side mechanism.
- Use `left_attachment_up` reliably as part of a mission step.

---

## 1. What `left_attachment_up` Does

Open `master.py` and find:

```python
def left_attachment_up(degrees, speed=1110):
    """
    Move the left attachment UP for a given encoder distance.

    - Left attachment motor is on port.C.
    - Positive degrees values move the mechanism up.
    """
    motor.run_for_degrees(port.C, degrees, speed, stop=motor.BRAKE)
```

Summarize behavior:
- Uses `motor.run_for_degrees` on `port.C` (left attachment motor).
- Runs the motor for `degrees` encoder degrees at `speed`.
- Stops with `motor.BRAKE` at the end.

Concept:
- “Up” means **move the left attachment mechanism in the lifting/engaging direction** for a fixed, repeatable distance.

---

## 2. Choosing `degrees` and `speed`

Explain:
- **`degrees`** controls *how far* the attachment moves.
  - Small degree values → small motion.
  - Larger degree values → larger motion.
- **`speed`** controls *how fast* it moves.
  - Lower speeds are safer and more precise.
  - Higher speeds can be faster but may overshoot or stress the mechanism.

Suggested starting values:
- `degrees = 180` (about half a turn).
- `speed = 400` (moderate speed).

Activity:
- With robot in base, run a test mission that calls `left_attachment_up(180, 400)` and watch how far it moves.
- Adjust `degrees` until the attachment reaches the desired “up” position without hitting anything too hard.

---

## 3. Simple Test Mission

Create or reuse a mission that calls `left_attachment_up`:

```python
async def mission_left_attachment_up_test():
    left_attachment_up(180, speed=400)
    return
```

Run on the robot:
- Observe the motion.
- Mark the “home” and “up” positions with tape or a marker.

Next, combine with `left_attachment_down` (from Lesson LAD) to go up and then back down.

---

## 4. Using `left_attachment_up` in Real Missions

Typical uses:
- Lifting a lever on a model.
- Raising an arm to push or flip something.
- Raising a gate or latch.

Activity:
- Pick one FLL model where the left attachment is the main actor.
- Decide:
  - “How far up does the attachment need to go?”
  - “How fast should it move for safe contact?”
- Use a mission like:

```python
async def mission_left_model():
    # Drive into position (tuned separately)
    drive_forward(20, 250, 360)

    # Lift left attachment to interact with the model
    left_attachment_up(180, speed=400)

    # Optional: wait for MotorIsStopped if you want extra safety
    # await runloop.until(lambda: MotorIsStopped(port.C))
```

Test on the field:
- Adjust `degrees` and `speed` until:
  - The model is consistently triggered.
  - The mechanism does not jam or strain.

Encourage students to:
- Record the final `degrees` and `speed` that work for each model where `left_attachment_up` is used.
- Add short comments above mission code describing what the attachment is doing.  

---


