# Lesson 15 – Mission Functions (`mission_0`–`mission_9`)

> Environment: Spike App IDE with our FLL robot and `master.py`

## Lesson Goals

By the end of this lesson, students will be able to:
- Explain the structure of `mission_0`–`mission_9` in `master.py`.
- Map each mission to the helper it currently tests.
- Replace a test mission with a **real FLL run** while keeping the selector system.

---

## 1. Mission Function Structure

Open `master.py` and find the mission functions:

```python
async def mission_0():
    """
    Mission 0: test forward drive.
    """
    drive_forward(20, 200, 360)
    return

async def mission_1():
    ...
```

Pattern:
- Each mission is an **async function**: `async def mission_n():`
- Each uses one or more helper functions (drive, pivot, spin, attachments).
- Each ends with `return` so control goes back to `mission_selector()`.

This structure makes it easy to:
- Test helpers individually.
- Swap out the body of any mission for a real FLL run.

---

## 2. What Each Mission Tests Today

Current mapping in `master.py`:

- `mission_0` – `drive_forward(20, 200, 360)`
- `mission_1` – `drive_backward(20, 200, 360)`
- `mission_2` – `pivot_left_outside(200, 45)`
- `mission_3` – `pivot_left_inside(200, 45)`
- `mission_4` – `pivot_right_outside(200, 45)`
- `mission_5` – `pivot_right_inside(200, 45)`
- `mission_6` – `spin_left(200, 90)`
- `mission_7` – `spin_right(200, 90)`
- `mission_8` – left attachment up/down:
  - `left_attachment_up(180, speed=400)`
  - wait for `MotorIsStopped(port.C)`
  - `left_attachment_down(180, speed=400)`
- `mission_9` – right attachment up/down:
  - `right_attachment_up(180, speed=400)`
  - wait for `MotorIsStopped(port.B)`
  - `right_attachment_down(180, speed=400)`

Activity:
- Run through missions 0–9 using the selector.
- For each, have students say which helper they see in action.

---

## 3. Activity – Replace a Test Mission with a Real FLL Run

Goal: Turn one of the test missions (for example `mission_4`) into a real FLL mission.

### Step 1 – Choose a Mission Slot

Pick a mission number that:
- Is easy to reach on the selector (e.g., 2, 3, or 4).
- You’re comfortable “owning” as a specific FLL field run.

Example: we’ll use `mission_4`.

### Step 2 – Plan the FLL Run

On paper, sketch the sequence:
- Drive out of base.
- Turn toward a model.
- Use an attachment.
- Return to base or a safe area.

Example plan:
1. Drive straight to the model.
2. Pivot right to face it.
3. Lift left attachment.
4. Drop it back down.
5. Drive backward to base.

### Step 3 – Implement the Run in `mission_4`

Modify `mission_4` in `master.py`:

```python
async def mission_4():
    """
    Mission 4: real FLL run – example.
    """
    # 1. Drive out of base
    drive_forward(20, 250, 720)

    # 2. Pivot right to face model
    pivot_right_outside(200, 45)

    # 3. Lift attachment to interact with model
    left_attachment_up(180, speed=400)
    await runloop.until(lambda: MotorIsStopped(port.C))

    # 4. Lower attachment
    left_attachment_down(180, speed=400)

    # 5. Drive back to base
    drive_backward(20, 250, 720)

    return
```

### Step 4 – Field Testing and Tuning

On the FLL field:
- Run the newly updated `mission_4` several times.
- Adjust:
  - Drive distances (`target_degrees`).
  - Pivot angles.
  - Attachment degrees.

Encourage:
- Write comments above `mission_4` describing the real mission:  
  `"Mission 4 – Model X delivery run"`.
- Keep a notebook or table of tuned values for each field element.

---

## 4. Next Steps

Once one mission slot is a real FLL run:
- Repeat the process for other missions (e.g., `mission_5` for a different model).
- Keep at least one or two “test missions” (e.g., 0 and 1) for ongoing calibration of straight driving or attachments.

The goal is to end up with:
- A **mission selector** where each number corresponds to a clear, documented FLL run.
- A team that knows which mission number runs which part of the field, and how to re‑tune it if the robot changes.  

---

[Back to Lessons Index](index.html)
