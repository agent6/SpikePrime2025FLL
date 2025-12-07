# Challenge C5.2 – Guided Mission 2025‑26 (Competition Ready)

> Environment: SPIKE App IDE, official FLL mat with the **Guided Mission 2025‑26** model, and your `master.py` helpers.

## Challenge Goal

Coach your team through a **full FIRST® LEGO® League–style mission** using the official Guided Mission model:

- Start from base with a consistent launch.
- Drive to the Guided Mission model (often using line following).
- Activate the model reliably.
- Return to a safe position.

You’ll focus on **strategy, consistency, and teamwork**, not just code.

---

## Setup

1. Build the **Driving Base with Color Sensor** (from the SPIKE app).
2. Build the **Guided Mission 2025‑26 model** and place it on the mat:
   - Follow the Robot Game Rulebook for the exact position.
   - Use Dual Lock and check that the model moves correctly.
3. Make sure your robot ports match your team standard:
   - Drive motors on `port.A` and `port.E`.
   - Color sensor on the correct port from your build (for line following).

---

## Required Tools and Helpers

- Your choice of driving and turning helpers from `master.py`:
  - `drive_forward`, `drive_backward`
  - `pivot_*` or `spin_*` helpers (if needed)
- Color sensor line‑following logic (from earlier line‑following lessons).
- `mission_selector()` and a dedicated `mission_n` for this Guided Mission.

---

## Step 1 – Discuss the Mission

As a team, answer:

- What is the robot supposed to **do** at the model?
- Where does the robot **start** and where should it **end**?
- What obstacles or other models are nearby?
- What is more important for this run: **speed** or **accuracy**?

Write down your answers on a whiteboard or worksheet.

---

## Step 2 – Build the First Program

Create a new `mission_n` in `master.py`, for example:

```python
async def mission_c5_guided_2025_26():
    # 1) Launch and approach the line
    # 2) Follow the line toward the Guided Mission model
    # 3) Activate the model (using an attachment or precise stop)
    # 4) Exit to a safe area
    #
    # TODO: Fill in with your team's distances, turns,
    #       and line-follow segments.
    return
```

Hook this mission into the `missions` list in `mission_selector` so you can launch it from the hub.

---

## Step 3 – Practice and Refine

Have each team:

1. Practice **lining up** the robot in base the same way every time.
2. Run the Guided Mission from the mission selector.
3. Observe:
   - Does it reach the model consistently?
   - Does it activate the model every time?
   - Where does it stop at the end?

Use your earlier line‑following knowledge (color or reflected light modes) to improve the approach path.

---

## Step 4 – Strategy and Optimization

Ask the team:

- Can we start in the **right launch area** instead of the left?
- Can we chain **another mission** before or after this one?
- What is the best **balance between speed and reliability**?

Tune:

- Speeds and distances in your drive helpers.
- Line‑following gains and thresholds.
- Final stopping point so the robot ends ready for the next mission.

---

## Assessment & Reflection

Use checklists or colored bricks (blue/yellow/violet) to rate:

- Did the team **work together** to complete the Guided Mission?
- Did they chain **more than one mission** in a single run?
- Can they **present** their robot, program, and mission strategy to a coach?

Optional extension:

- Have students prepare a short presentation explaining how they:
  - Designed their strategy.
  - Balanced speed vs. accuracy.
  - Improved their run over time.

