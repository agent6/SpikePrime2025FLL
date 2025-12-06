# Lesson RAU – `right_attachment_up`

> Environment: Spike App IDE with our FLL robot and `master.py`

## Lesson Goals

By the end of this lesson, students will be able to:
- Explain what `right_attachment_up(degrees, speed)` does.
- Choose appropriate `degrees` and `speed` values for the right-side mechanism.
- Use `right_attachment_up` reliably as part of a mission step.

---

## 1. What `right_attachment_up` Does

Open `master.py` and find:

```python
def right_attachment_up(degrees, speed):
    """
    Move the right attachment UP for a given encoder distance.

    - Right attachment motor is on port.B.
    - Positive degrees values move the mechanism up.
    """
    motor.run_for_degrees(port.B, degrees, speed, stop=motor.BRAKE)
```

Summarize behavior:
- Uses `motor.run_for_degrees` on `port.B` (right attachment motor).
- Runs the motor for `degrees` encoder degrees at `speed`.
- Stops with `motor.BRAKE` at the end.

Concept:
- “Up” means **move the right attachment in the lifting/engaging direction** for a fixed, repeatable distance.

---

## 2. Choosing `degrees` and `speed`

Explain:
- **`degrees`** controls *how far* the attachment moves.
  - Small values → small motion.
  - Larger values → further reach or lift.
- **`speed`** controls *how fast* it moves.
  - Lower speeds are safer and easier on the mechanism.
  - Higher speeds are faster but may overshoot or strain.

Suggested starting values:
- `degrees = 180`
- `speed = 400`

Activity:
- With the robot in base, run a test mission that calls `right_attachment_up(180, 400)` and watch the motion.
- Adjust `degrees` until it reaches the desired “up” position without slamming into anything.

---

## 3. Simple Test Mission

Create or reuse a mission that calls `right_attachment_up`:

```python
async def mission_right_attachment_up_test():
    right_attachment_up(180, speed=400)
    return
```

Run on the robot:
- Observe the movement of the right-side mechanism.
- Mark the “home” and “up” positions with tape or a pen.

Later, combine with `right_attachment_down` (Lesson RAD) to go up and back down.

---

## 4. Using `right_attachment_up` in Real Missions

Typical uses:
- Lifting or pushing a model from the right side.
- Rotating a tower or arm to hook, lift, or drop an object.

Activity:
- Pick one FLL model where the **right** attachment should do the work.
- Decide:
  - “How far up should the mechanism move?”
  - “How fast should it move for safe contact?”

Example mission snippet:

```python
async def mission_right_model():
    # Approach model (tuned separately)
    drive_forward(20, 250, 360)

    # Use right attachment to interact with the model
    right_attachment_up(180, speed=400)

    # Optional: wait for MotorIsStopped if needed
    # await runloop.until(lambda: MotorIsStopped(port.B))
```

Field testing:
- Tune `degrees` and `speed` until:
  - The model is reliably triggered.
  - The attachment does not jam or overstress the mechanism.

Encourage students to:
- Record final `degrees` and `speed` values used for each model.
- Add comments in the mission code describing what the right attachment is doing at each step.  

---

[Back to Lessons Index](index.html)
