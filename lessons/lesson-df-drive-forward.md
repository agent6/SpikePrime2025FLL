# Lesson DF – `drive_forward`

> Environment: Spike App IDE with our FLL robot and `master.py`

## Lesson Goals

By the end of this lesson, students will be able to:
- Explain what `drive_forward(min_speed, max_speed, target_degrees, kP)` does.
- Choose reasonable values for `min_speed`, `max_speed`, `target_degrees`, and `kP`.
- Tune a straight drive on the field for a specific distance.

---

## 1. Where `drive_forward` Lives and What It Does

Open `master.py` and find:

```python
def drive_forward(min_speed, max_speed, target_degrees, kP=0.5):
    ...
```

Summarize behavior:
- Resets yaw and the left motor encoder.
- Accelerates from `min_speed` up to `max_speed`.
- Holds speed, then decelerates back down to `min_speed`.
- Uses **proportional correction** with yaw to stay straight.
- Stops when the left motor has turned `target_degrees`.

Parameter meanings:
- `min_speed` – gentle starting/ending speed (safer, less wheel slip).
- `max_speed` – highest speed during the run.
- `target_degrees` – how far the left wheel should rotate (distance proxy).
- `kP` – proportional gain; how strongly yaw error changes the wheel speeds.

---

## 2. Proportional Correction Recap

Key lines inside the function:

```python
yaw = motion_sensor.tilt_angles()[0]
correction = int(kP * yaw)

left_command = left_speed + correction
right_command = right_speed - correction
```

Explain in simple terms:
- If yaw is not 0, the robot is drifting off its intended heading.
- We multiply yaw by `kP` to get a correction amount.
- We adjust left/right speeds in **opposite** directions to steer back.

Thought exercise:
- What happens if `kP` is 0? (No correction → more drift.)
- What happens if `kP` is too large? (Robot “wiggles” or oscillates.)

---

## 3. Simple Field Test for `drive_forward`

Create or reuse a mission that calls `drive_forward`:

```python
async def mission_drive_forward_test():
    # Tune these numbers on the field
    drive_forward(20, 250, 720, kP=0.5)
    return
```

On the field:
1. Place the robot squarely against base or along a mat line.
2. Run the mission via the selector.
3. Observe:
   - How far does it travel?
   - Does it drift left or right?

---

## 4. Tuning `drive_forward` – Distance and Straightness

Adjusting **distance**:
- Increase `target_degrees` to go farther.
- Decrease `target_degrees` to go shorter.
- Record values that correspond to specific field distances (e.g., “to model X”).

Adjusting **speeds**:
- Start with conservative values:
  - `min_speed = 20`
  - `max_speed = 200–250`
- Once the run is reliable, increase `max_speed` in steps (e.g., 50 at a time).

Adjusting **kP**:
- Start with `kP = 0.5`.
- If the robot drifts, try `0.6` or `0.7`.
- If it wiggles or oscillates, reduce `kP`.

Suggested tuning table (students fill in):

| Test | min_speed | max_speed | degrees | kP  | Result / Notes           |
|------|-----------|-----------|---------|-----|--------------------------|
| 1    | 20        | 200       | 720     | 0.5 | Drifted slightly left    |
| 2    | 20        | 200       | 720     | 0.6 | Straighter               |
| 3    | 20        | 250       | 720     | 0.6 | Faster, still acceptable |

---

## 5. Connecting to Real Missions

Ask:
- “Which FLL mission needs a reliable straight drive?”
- “Can we use one `drive_forward` call to get from base to that model?”

Activity:
- Pick one real mission and identify the main straight leg.
- Use a test mission with `drive_forward` to tune that leg until it lands consistently where you need it.
- Then copy those tuned values into the real mission function (e.g., `mission_4`).  

---


