# Lesson 13 – Detecting Motor Stop with `MotorIsStopped`

> Environment: Spike App IDE with our FLL robot and `master.py`  
> API reference: https://tuftsceeo.github.io/SPIKEPythonDocs/SPIKE3.html

## Lesson Goals

By the end of this lesson, students will be able to:
- Use `MotorIsStopped(motor_port, samples=100)` to detect when a motor has stopped moving.
- Explain how encoder readings show **motion vs stop**.
- Use `await runloop.until(lambda: MotorIsStopped(port.C))` inside a mission.
- Wait for a mechanism to “settle” before starting the next action.

---

## 1. The `MotorIsStopped` Helper in `master.py`

Open `master.py` and find:

```python
def MotorIsStopped(motor_port, samples=100):
    """
    Return True if the motor on the given port appears stopped.

    Waits a short time, then keeps checking the encoder position.
    Once the position stops changing, returns True.
    """
    first_position = motor.relative_position(motor_port)
    print("MotorIsStopped start:", motor_port, "first_position:", first_position)

    # Initial wait so we do not immediately report "stopped"
    time.sleep(0.25)

    while True:
        current = motor.relative_position(motor_port)
        print("MotorIsStopped sample:", motor_port, "current:", current)
        if current == first_position:
            print("MotorIsStopped:", motor_port, "-> True")
            return True
        # Update reference and delay before next check
        first_position = current
        time.sleep(0.01)
```

Explain:
- It reads the motor **encoder position** repeatedly.
- If the encoder value stops changing, it assumes the motor has stopped and returns `True`.
- It prints debug information (positions and final result) to the console.

---

## 2. Encoders: Motion vs Stop

Remind students:
- `motor.relative_position(port.X)` returns how many degrees the motor has turned since last reset.
- When a motor is **moving**, this number changes over time.
- When a motor is **stopped**, the number stays the same.

Quick demo:
- Write a short script that:
  - Resets an encoder.
  - Runs a motor for a short time.
  - Prints several `relative_position` values to show the change.

---

## 3. Using `await runloop.until(lambda: MotorIsStopped(port.C))`

Pattern in missions:

```python
from hub import port
import runloop

async def mission_example():
    left_attachment_up(180, speed=400)
    await runloop.until(lambda: MotorIsStopped(port.C))
    left_attachment_down(180, speed=400)
```

Explain:
- `runloop.until` keeps calling `MotorIsStopped(port.C)` until it returns `True`.
- Once the motor appears stopped (encoder stable), the mission continues.
- This is more reliable than using a fixed time delay, especially if load or battery changes.

---

## 4. Practice – Wait for a Mechanism to Settle

Field exercise:
1. Use an attachment that hits or lifts a model.
2. In a mission:
   - Activate the attachment (up).
   - Wait for `MotorIsStopped` on the correct port (`port.C` or `port.B`).
   - Then either:
     - Back away, or
     - Return the attachment home.

Example:

```python
async def mission_hit_and_settle():
    # Move into position
    drive_forward(20, 250, 360)

    # Hit model with left attachment
    left_attachment_up(180, speed=400)
    await runloop.until(lambda: MotorIsStopped(port.C))

    # Back away and return attachment home
    drive_backward(20, 250, 360)
    left_attachment_down(180, speed=400)
```

Have students:
- Watch the console output for `MotorIsStopped` to see encoder values and True result.
- Compare behavior with and without the `await runloop.until(...)` line.
- Notice how waiting for the mechanism to settle reduces jamming or misalignment before the next move.  

---

[Back to Lessons Index](index.html)
