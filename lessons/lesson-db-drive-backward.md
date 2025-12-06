# Lesson DB – `drive_backward`

> Environment: Spike App IDE with our FLL robot and `master.py`

## Lesson Goals

By the end of this lesson, students will be able to:
- Explain what `drive_backward(min_speed, max_speed, target_degrees, kP)` does.
- Choose reasonable values for `min_speed`, `max_speed`, `target_degrees`, and `kP` when driving backward.
- Tune a straight **reverse** drive on the field for a specific distance.

---

## 1. Where `drive_backward` Lives and What It Does

Open `master.py` and find:

```python
def drive_backward(min_speed, max_speed, target_degrees, kP=0.5):
    ...
```

Summarize behavior:
- Resets yaw and the left motor encoder.
- Accelerates from `min_speed` up to `max_speed` while driving **backward**.
- Holds speed, then decelerates back down to `min_speed`.
- Uses **proportional correction** with yaw to stay straight in reverse.
- Stops when the left motor has turned `target_degrees` backwards.

Parameter meanings (same as forward):
- `min_speed` – gentle starting/ending speed.
- `max_speed` – highest speed during the run.
- `target_degrees` – how far the left wheel should rotate (distance proxy).
- `kP` – proportional gain; how strongly yaw error changes the wheel speeds.

---

## 2. Proportional Correction in Reverse

Inside `drive_backward`, we still use yaw:

```python
yaw = motion_sensor.tilt_angles()[0]
correction = int(kP * yaw)

left_command = left_speed + correction
right_command = right_speed - correction
```

Key idea:
- The robot is moving backward, but yaw still tells us if we are drifting.
- We adjust left/right speeds to steer back to the intended heading.

Thought exercise:
- Why is backward driving harder to keep straight than forward?
- How might that affect your choice of `max_speed` and `kP`?

---

## 3. Simple Field Test for `drive_backward`

Create or reuse a mission that calls `drive_backward`:

```python
async def mission_drive_backward_test():
    # Tune these numbers on the field
    drive_backward(20, 200, 720, kP=0.5)
    return
```

On the field:
1. Place the robot squarely against base facing into the field.
2. Run the mission via the selector.
3. Observe:
   - How far backward does it travel?
   - Does it drift left or right as it reverses?

---

## 4. Tuning `drive_backward` – Distance and Straightness

Adjusting **distance**:
- Increase `target_degrees` to go farther backward.
- Decrease `target_degrees` to go shorter.
- Record values that correspond to backing out of specific locations.

Adjusting **speeds**:
- Start conservative:
  - `min_speed = 20`
  - `max_speed = 150–200` (often lower than forward).
- Increase `max_speed` only after backward runs are reliable.

Adjusting **kP**:
- Start with `kP = 0.5`.
- If reverse drifts, try `0.6` or `0.7`.
- If it wiggles, lower `kP`.

Suggested tuning table:

| Test | min_speed | max_speed | degrees | kP  | Result / Notes             |
|------|-----------|-----------|---------|-----|----------------------------|
| 1    | 20        | 150       | 720     | 0.5 | Small drift right          |
| 2    | 20        | 150       | 720     | 0.6 | Straighter                 |
| 3    | 20        | 180       | 720     | 0.6 | Faster, still controllable |

---

## 5. Connecting to Real Missions

Backward moves are common when:
- Leaving a model after interacting.
- Backing up to base without turning around.

Activity:
- Pick one mission where the robot should **retreat backward** instead of turning first.
- Use `mission_drive_backward_test` to tune the reverse leg until it returns reliably to the desired location.
- Copy the tuned `drive_backward` call into the corresponding mission function (e.g., after a model hit in `mission_4` or `mission_5`).  

---

[Back to Lessons Index](index.html)
