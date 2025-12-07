# Challenge C2.1 – Square Path with Pivots (Turning & Alignment)

> Environment: Spike App IDE with our FLL robot and `master.py`

## Challenge Goal

Use straight drives and pivot helpers to make the robot drive a clean **square path**:

- Four straight segments using `drive_forward`
- Four 90° turns using `pivot_*_outside` or `pivot_*_inside`

The robot should finish close to where it started and face the original direction.

---

## Setup

1. On the mat, mark a **square** with tape or use printed lines.
2. Choose a side length (for example, 40–50 cm).
3. Mark the **start corner** and robot orientation.

---

## Required Methods from `master.py`

- `drive_forward(min_speed, max_speed, target_degrees, kP=0.5)`
- One or more pivot helpers:
  - `pivot_left_outside(speed, target_angle_degrees)`
  - `pivot_right_outside(speed, target_angle_degrees)`
  - or the corresponding `pivot_*_inside` versions
- `mission_selector()` and a mission slot to run your test.

---

## Step 1 – Create a “Square Path” Mission

Pick an unused mission slot and create a first draft:

```python
async def mission_c2_square_path():
    # Rough starting guesses – you will tune these
    side_degrees = 720      # distance for one side (adjust on field)
    turn_speed = 200        # pivot speed
    turn_angle = 90         # target yaw angle

    for _ in range(4):
        drive_forward(20, 200, side_degrees, kP=0.5)
        pivot_right_outside(turn_speed, turn_angle)
    return
```

Add this function to `master.py` and hook it into `mission_selector` (either as a new mission or by temporarily replacing one of the existing test missions).

---

## Step 2 – Tune the Side Distance

On the field:

1. Place the robot in the start corner, facing along the first side.
2. Run `mission_c2_square_path()` from the mission selector.
3. Watch the **first side**:
   - If the robot stops **short**, increase `side_degrees`.
   - If it goes **too far**, decrease `side_degrees`.

Once the first side looks right, run the whole square a few times and adjust slightly if needed.

---

## Step 3 – Tune the Pivot Angle

Now focus on the turns:

- If the robot **cuts inside** the square:
  - Decrease `turn_angle` a little (e.g., 90 → 85).
- If it **turns too far** and the square “bulges” out:
  - Increase `turn_angle` a little (e.g., 90 → 95).

You can also experiment with:

- Using `pivot_left_outside` instead of `pivot_right_outside` (reverse the square direction).
- Trying `pivot_*_inside` to see how inside-wheel pivots feel different.

---

## Step 4 – Check Alignment at the End

You know the challenge is close when:

- After 4 sides and 4 pivots, the robot:
  - Ends near the original corner.
  - Faces almost the same direction as at the start.

If it **drifts away** from the start:

- Re-check side distance (too long/short adds up over 4 sides).
- Re-check angle (even 2–3° error per turn is visible after 4 turns).

---

## Success Criteria

You’ve completed this challenge when:

- The robot consistently:
  - Drives a square path that visually matches your tape square.
  - Ends within a small area (about a robot-width) of the starting corner.
  - Faces the original direction within a few degrees.
- Your team has written down tuned values for:
  - `side_degrees`, `turn_speed`, and `turn_angle`.

These tuned values become a building block for missions that require **drive–turn–drive** patterns and precise alignment with models.

