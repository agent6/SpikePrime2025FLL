# Lesson Mx – `mission_0`–`mission_9` (Full Missions)

> Environment: Spike App IDE with our FLL robot and `master.py`

## Lesson Goals

By the end of this lesson, students will be able to:
- Understand how `mission_0`–`mission_9` are organized in `master.py`.
- Build a **full FLL mission** using our helper functions.
- Test and refine missions using the mission selector.

---

## 1. Mission Functions as Building Blocks

Open `master.py` and locate the mission functions:

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

Common structure:
- Each mission is `async def mission_n():`.
- Each mission calls one or more helpers (drive, pivots, spins, attachments).
- Each ends with `return` to hand control back to `mission_selector()`.

The selector uses these functions as entries in its mission list; updating a mission changes behavior for that mission number in the UI.

---

## 2. Current Mission Mapping (Test Missions)

As configured now, missions are simple tests:

- `mission_0` – `drive_forward`
- `mission_1` – `drive_backward`
- `mission_2` – `pivot_left_outside`
- `mission_3` – `pivot_left_inside`
- `mission_4` – `pivot_right_outside`
- `mission_5` – `pivot_right_inside`
- `mission_6` – `spin_left`
- `mission_7` – `spin_right`
- `mission_8` – left attachment up/down
- `mission_9` – right attachment up/down

These are great for:
- Calibrating movement.
- Teaching helpers.
- Debugging robot behavior.

But real FLL missions will often string several actions together.

---

## 3. Designing a Full Mission (On Paper First)

Pick a model on the field and answer:
- Where does the robot start?
- What path does it need to drive?
- What turns and attachment motions are needed?
- How does it return (if at all)?

Write a **step list**:
1. Drive from base to a line in front of the model.
2. Pivot to face the model.
3. Drive up to the model.
4. Use left or right attachment to interact.
5. Back away and optionally return to base.

---

## 4. Implementing the Mission in Code

Pick a mission slot (for example, `mission_4`) and write the steps using helpers:

```python
async def mission_4():
    """
    Mission 4: Example full FLL run to Model X.
    """
    # 1. Drive out of base
    drive_forward(20, 250, 720)

    # 2. Pivot right to face model
    pivot_right_outside(200, 45)

    # 3. Drive closer to the model
    drive_forward(20, 200, 360)

    # 4. Use left attachment
    left_attachment_up(180, speed=400)
    await runloop.until(lambda: MotorIsStopped(port.C))

    # 5. Back away and reset attachment
    drive_backward(20, 250, 720)
    left_attachment_down(180, speed=400)

    return
```

Notes:
- Use helpers you already tuned in previous lessons.
- Add comments to label what each step is doing.

---

## 5. Testing and Refining Missions with the Selector

Use `mission_selector()` to test:
- Start `master.py` with the green button.
- Use RIGHT to select the mission number you edited.
- Use LEFT to run it.

Refinement loop:
1. Run the mission and observe behavior on the field.
2. Adjust parameters:
   - `target_degrees` in `drive_forward` / `drive_backward`.
   - Angles in pivots/spins.
   - Attachment degrees and speeds.
3. Run again.
4. Repeat until the mission is reliable.

Encourage:
- Keep a simple tuning log for each mission:

| Mission | Step      | Helper & Params                        | Notes                  |
|---------|-----------|-----------------------------------------|------------------------|
| 4       | Drive 1   | `drive_forward(20, 250, 720, 0.6)`      | to front of Model X    |
| 4       | Pivot     | `pivot_right_outside(200, 45)`          | line up with ramp      |
| 4       | Attach up | `left_attachment_up(180, 400)`          | lift latch fully       |

---

## 6. Best Practices for Team Missions

Guidelines:
- Give each mission a clear **purpose** and write it in the docstring.
- Avoid cramming too many models into a single mission—keep them manageable.
- Use test missions (0/1/8/9) as calibration tools and leave them mostly intact.
- Make sure multiple team members know:
  - Which mission number runs which FLL run.
  - Roughly what the robot should do when that mission is selected.

This lesson ties together all helpers and the selector into full FLL missions that the whole team can understand, test, and refine.  

---


