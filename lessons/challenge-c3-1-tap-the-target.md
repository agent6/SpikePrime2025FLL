# Challenge C3.1 – Tap the Target (Attachments &amp; Models)

> Environment: Spike App IDE with our FLL robot and `master.py`

## Challenge Goal

Use an attachment helper to **tap or push a target model**, then safely return the attachment to its starting position.

You will tune attachment degrees and speeds so the motion is repeatable and gentle.

---

## Setup

1. Place a simple “target model” in front of the robot:
   - A small box, a LEGO lever, or an FLL model you can safely touch.
2. Position the robot in base so the **attachment** is lined up with the target.
3. Decide which attachment you will use:
   - Left attachment on `port.C`, or
   - Right attachment on `port.B`.

---

## Required Methods from `master.py`

- Left attachment:
  - `left_attachment_up(degrees, speed=1110)`
  - `left_attachment_down(degrees, speed=1110)`
- Right attachment:
  - `right_attachment_up(degrees, speed)`
  - `right_attachment_down(degrees, speed)`
- Optional safety helper:
  - `MotorIsStopped(motor_port)` with `await runloop.until(...)`

Pick **one side** (left or right) for this challenge.

---

## Step 1 – Build a Simple Tap Mission

Example using the **left** attachment:

```python
async def mission_c3_tap_target():
    # First guess – small, gentle movement
    tap_degrees = 180
    tap_speed = 400

    left_attachment_up(tap_degrees, speed=tap_speed)
    left_attachment_down(tap_degrees, speed=tap_speed)
    return
```

If you use the right attachment, switch to `right_attachment_up/down` on `port.B`.

Add this mission to `master.py` and hook it into `mission_selector`.

---

## Step 2 – Tune the “Reach” of the Attachment

Run the mission several times and observe:

- Does the attachment **reach** the target?
- Does it **push too hard** or overshoot?

Adjust `tap_degrees`:

- Increase degrees if it stops **before** hitting the target.
- Decrease degrees if it **crashes** or pushes too far.

Keep `tap_speed` fairly low (300–500) for control.

---

## Step 3 – Check the Return Motion

Watch the motion as it returns:

- Does the attachment come back to a **safe home position**?
- Does anything get stuck or hit on the way back?

If the return feels rough:

- Lower the speed slightly.
- Reduce degrees a little to avoid binding.

Optional: add a short delay or use `MotorIsStopped` before starting the return motion to let the mechanism settle.

---

## Success Criteria

You’ve completed this challenge when:

- Starting from a consistent base position, the robot:
  - Moves the attachment to gently tap or push the target.
  - Returns the attachment to a safe home position every time.
- Your team has recorded good values for:
  - `tap_degrees` and `tap_speed`.

These values become starting points for real missions that need **precise attachment movements** on the FLL field.

