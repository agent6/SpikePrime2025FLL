# Lesson 8 – Straight Driving with `drive_forward` / `drive_backward`

> Environment: Spike App IDE with our FLL robot and `master.py`  
> API reference: <https://tuftsceeo.github.io/SPIKEPythonDocs/SPIKE3.html>  
> Example programs: LEGO SPIKE Python Programs (Feb 2024 PDF)

## Lesson Goals

By the end of this lesson, students will be able to:
- Use `drive_forward` and `drive_backward` from `master.py`.
- Explain how **proportional correction** uses yaw to keep the robot straight.
- Tune speeds and distances on the **actual field**.

---

## 1. Review the Helpers in `master.py`

Open `master.py` and locate:

```python
def drive_forward(min_speed, max_speed, target_degrees, kP=0.5):
    ...

def drive_backward(min_speed, max_speed, target_degrees, kP=0.5):
    ...
```

Key ideas:
- `min_speed` – gentle start/finish speed.
- `max_speed` – top speed in the middle.
- `target_degrees` – how far the **left motor** should turn.
- `kP` – proportional gain for heading correction.

Explain the motion:
- Accelerate from `min_speed` → `max_speed`.
- Cruise.
- Decelerate back to `min_speed`.
- Stop when the left motor encoder reaches `target_degrees`.

---

## 2. Proportional Correction Using Yaw

Inside `drive_forward`, we use yaw:

```python
yaw = motion_sensor.tilt_angles()[0]
correction = int(kP * yaw)

left_command = left_speed + correction
right_command = right_speed - correction
```

Explain in words:
- If the robot drifts to one side, yaw becomes positive or negative.
- We multiply yaw by `kP` to get a **correction**.
- We **add** correction to one wheel and **subtract** from the other to steer back.

Activity:
- Set `kP` very low (e.g., `0.1`) and observe drift.
- Set `kP` higher (e.g., `0.7`) and see if the robot “wiggles” while correcting.
- Discuss: too low = drift; too high = over‑correction.

---

## 3. Simple Test Missions for Straight Driving

Use the existing missions or add a new one to test:

```python
async def mission_forward_test():
    drive_forward(20, 300, 720)  # ~ two wheel turns

async def mission_backward_test():
    drive_backward(20, 300, 720)
```

Or temporarily replace one of the `mission_n` functions with these calls.

Remember:
- Select the mission in the selector.
- Start the program from the hub and run the mission.

---

## 4. Field Practice – Tuning Speeds and Distances

On the FLL field:
1. Pick a **straight line** (edge of the base or tape) as reference.
2. Start with a safe configuration, e.g.:
   - `drive_forward(20, 250, 720, kP=0.5)`
3. Observe:
   - Does it stop where you expect?
   - Does it drift left or right?

Adjust:
- **Distance**: change `target_degrees` until the robot stops at the same spot consistently.
- **Speed**: raise `max_speed` once it’s reliable at lower speed.
- **kP**: nudge up/down to reduce drift without causing oscillation.

Write down a table in a notebook:

| Test | min_speed | max_speed | degrees | kP  | Result / Notes             |
|------|-----------|-----------|---------|-----|----------------------------|
| 1    | 20        | 250       | 720     | 0.5 | Slight drift left          |
| 2    | 20        | 250       | 720     | 0.7 | Straighter, small wiggle   |
| 3    | 20        | 300       | 720     | 0.7 | Faster, still acceptable   |

This tuning process is exactly what you will repeat for real FLL missions.  

---

[Back to Lessons Index](index.html)
