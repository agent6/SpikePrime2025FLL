# Challenge C1.1 – Hit the Line (Straight-Line Accuracy)

> Environment: Spike App IDE with our FLL robot and `master.py`

## Challenge Goal

Use `drive_forward` to drive straight out of base and stop with the front of the robot *exactly* on a marked line on the mat.

You’ll tune `min_speed`, `max_speed`, `target_degrees`, and `kP` to make the distance and heading reliable.

---

## Setup

1. On the FLL mat (or practice mat), choose a clear straight path from base.
2. Place a strip of tape or use an existing mat line as your **target line**.
3. Mark a consistent **starting position** in base:
   - Front bumper against the base wall.
   - Robot centered on a known reference.

---

## Required Methods from `master.py`

- `drive_forward(min_speed, max_speed, target_degrees, kP=0.5)`
- `mission_selector()` and a `mission_n` (for example, `mission_0` or a new mission) to run your test.

---

## Step 1 – Create a Test Mission

Pick a mission slot and create a simple test mission:

```python
async def mission_c1_hit_line():
    # Initial guess – tune these values on the field
    drive_forward(20, 250, 720, kP=0.5)
    return
```

Add this to `master.py`, and then add it into the `missions` list in `mission_selector` (or temporarily swap it into an existing mission number you’re not using yet).

---

## Step 2 – First Field Trials

On the field:

1. Place the robot in the marked start position.
2. Start the `master` program on the hub.
3. Use the selector to choose your challenge mission number.
4. Press LEFT to run it.

Observe:
- Does the robot reach the line, fall short, or overshoot?
- Does it drift left or right?

---

## Step 3 – Tuning Distance (`target_degrees`)

Adjust `target_degrees` until the front of the robot stops on the line:

- If it stops **short** of the line:
  - Increase `target_degrees` (e.g., 720 → 760 → 800).
- If it stops **past** the line:
  - Decrease `target_degrees` (e.g., 720 → 680 → 650).

Record your trials:

| Test | min_speed | max_speed | target_degrees | kP  | Result / Notes            |
|------|-----------|-----------|----------------|-----|---------------------------|
| 1    | 20        | 250       | 720            | 0.5 | Stopped 5 cm before line  |
| 2    | 20        | 250       | 780            | 0.5 | Slight overshoot          |
| 3    | 20        | 250       | 760            | 0.5 | Front bumper on the line  |

---

## Step 4 – Tuning Straightness (`kP` and Speeds)

If the robot drifts left or right on the way to the line:

- Increase `kP` slightly (e.g., 0.5 → 0.6 → 0.7) to apply stronger yaw correction.
- If it starts to “wiggle” or oscillate, reduce `kP` a bit.

Once the path is straight and the distance is correct:
- Try increasing `max_speed` to make the run faster.
- Keep `min_speed` low (e.g., 20) for gentle start/stop.

Update your table with new tests:

| Test | min_speed | max_speed | target_degrees | kP  | Result / Notes          |
|------|-----------|-----------|----------------|-----|-------------------------|
| 4    | 20        | 250       | 760            | 0.6 | Straighter, good stop   |
| 5    | 20        | 300       | 760            | 0.6 | Faster, still accurate  |

---

## Success Criteria

You’ve completed this challenge when:

- Starting from the marked base position, the robot:
  - Drives straight using `drive_forward`.
  - Stops with its front bumper consistently on or within ~1–2 cm of the target line.
- You’ve written down the tuned parameters that work reliably with your robot.

These tuned values become a building block for real missions that require precise “drive to here” segments.

