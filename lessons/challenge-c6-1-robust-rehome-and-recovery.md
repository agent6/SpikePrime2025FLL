# Challenge C6.1 – Robust Re-home &amp; Recovery (Robustness &amp; Recovery)

> Environment: Spike App IDE with our FLL robot and `master.py`

## Challenge Goal

Build a **recovery mission** that:

- Safely re-homes one or more attachments.
- Puts the robot in a known, repeatable state after something goes wrong.

You’ll use `MotorIsStopped` and attachment helpers to make the motion **self-correcting**.

---

## Setup

1. Choose an attachment that sometimes:
   - Gets bumped.
   - Ends in a strange position after a failed run.
2. Decide what the **“home” position** should be:
   - All the way up?
   - All the way down?
3. Pick a mission slot to use as your **Recovery Mission** (for example, `mission_9`).

---

## Required Methods from `master.py`

- `MotorIsStopped(motor_port, samples=100)`
- Attachment helpers (pick the side you’re re-homing):
  - `left_attachment_up/down`
  - `right_attachment_up/down`
- `await runloop.until(lambda: MotorIsStopped(port.X))`

---

## Step 1 – Design a Safe Re-home Sequence

Example for a left attachment that should end **down**:

```python
async def mission_c6_rehome_left():
    # Move up until the mechanism stops (hits a hard stop or limit)
    left_attachment_up(360, speed=400)
    await runloop.until(lambda: MotorIsStopped(port.C))

    # Then move down to a known encoder-based position
    left_attachment_down(360, speed=400)
    await runloop.until(lambda: MotorIsStopped(port.C))
    return
```

Adjust degrees and direction for your robot and attachment design.

---

## Step 2 – Test “Bad Starts”

Manually move the attachment to different wrong positions:

- Halfway up.
- Almost fully down.
- Slightly jammed against a model (gently).

Then run the recovery mission:

- Does it always end in the same home position?
- Does the motion stop cleanly when the attachment can’t move farther?

If it fails or struggles:

- Reduce speed.
- Adjust the movement degrees.
- Add an extra re-home step if needed (for example, up → down → up).

---

## Step 3 – Integrate with Other Missions

Decide how your team will use the recovery mission:

- As a **separate mission slot** you can run between matches.
- As a **first step** in other missions if needed:
  - Example: run re-home at the very start of a long mission.

Make sure everyone on the team knows:

- Which mission number is the recovery mission.
- When to use it in practice and at tournaments.

---

## Success Criteria

You’ve completed this challenge when:

- From many different starting attachment positions, running the recovery mission:
  - Moves the mechanism safely.
  - Ends in the same, known home position every time.
- Your team has a **standard procedure**: “If something looks wrong, run mission X to re-home.”

This makes your robot more **robust** and easier to use under competition pressure.

