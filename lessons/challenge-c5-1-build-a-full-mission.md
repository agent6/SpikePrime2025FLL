# Challenge C5.1 – Build a Full Model Mission (Mission Builder &amp; Optimization)

> Environment: Spike App IDE with our FLL robot and `master.py`

## Challenge Goal

Turn one of your **test missions** into a **real FLL-style mission** for a specific model:

- Drive out from base.
- Turn or align as needed.
- Use attachments to interact with the model.
- Return to a safe area or back to base.

Then, tune it for **speed and reliability**.

---

## Setup

1. Pick one FLL model that:
   - Is reachable from base with a few moves.
   - Can be safely touched by your attachment(s).
2. Decide which mission slot you will use (for example, `mission_2` or `mission_8`).
3. Sketch the run on paper:
   - Drive distances.
   - Turns.
   - Attach actions.

---

## Required Methods from `master.py`

Use any helpers you need:

- Driving: `drive_forward`, `drive_backward`
- Turning: `pivot_*`, `spin_left`, `spin_right`
- Attachments: `left_attachment_*`, `right_attachment_*`
- Async: `async_drive_*`, async attachment helpers (optional)
- Mission structure: `mission_0`–`mission_9`, `mission_selector()`

---

## Step 1 – Build the First Version

Create or replace a `mission_n` in `master.py`:

```python
async def mission_c5_model_run():
    # Example structure – replace distances/angles with your own
    drive_forward(20, 200, 720)          # out of base
    pivot_right_outside(200, 45)         # aim at model
    drive_forward(20, 200, 360)          # approach
    left_attachment_down(180, speed=400) # interact with model
    drive_backward(20, 200, 720)         # return toward base
    return
```

Hook this mission into the `missions` list used by `mission_selector`.

---

## Step 2 – Test for Reliability

Run the mission at least **5–10 times** from:

- The same starting position and orientation.

Record:

- How often it hits the model correctly.
- Where it fails (too short/long, wrong angle, attachment timing).

Adjust:

- Distances (`target_degrees`).
- Angles (`target_angle_degrees`).
- Attachment degrees and speeds.

Focus first on **reliability** (high success rate), not speed.

---

## Step 3 – Optimize for Time

Once the mission is reliable:

- Increase `max_speed` in `drive_forward` / `drive_backward`.
- Reduce unnecessary pauses or extra movements.
- Consider using async helpers for **drive + attach** sections.

After each change:

- Re-test reliability.
- Make sure faster still means **consistent**.

---

## Success Criteria

You’ve completed this challenge when:

- You have a mission that:
  - Starts from base.
  - Reaches and interacts with a real model.
  - Ends in a safe, known state for the next run.
- It succeeds **most of the time** (aim for 8/10 or better) at competition-like speed.
- Your team can explain which helpers you used and why.

