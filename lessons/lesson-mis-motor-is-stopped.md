# Lesson MIS – `MotorIsStopped`

> Environment: Spike App IDE with our FLL robot and `master.py`

## Lesson Goals

By the end of this lesson, students will be able to:
- Explain what `MotorIsStopped(motor_port, samples=100)` does.
- Describe how encoder readings show **motion vs stop**.
- Use `await runloop.until(lambda: MotorIsStopped(port.C))` (or `port.B`) to wait for a mechanism to finish moving before the next action.

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
- Reads the motor encoder once (`first_position`), waits briefly, then keeps checking.
- If the position stops changing (current equals first), it prints a message and returns `True`.
- It **never returns `False`**; it just keeps checking until the motor appears stopped.

---

## 2. Encoders: Motion vs Stop

Remind students:
- `motor.relative_position(port.X)` returns how many degrees the motor has turned since its last reset.
- While the motor is **moving**, this number changes over time.
- When the motor is **stopped**, the number stays the same between samples.

Mini‑demo:
- In a small test mission, print `motor.relative_position(port.C)` every 0.1 seconds while the attachment moves, then after it stops.
- Show how the values change during motion and become constant when stopped.

---

## 3. Using `MotorIsStopped` with `runloop.until`

Pattern:

```python
await runloop.until(lambda: MotorIsStopped(port.C))
```

This means:
- Keep calling `MotorIsStopped(port.C)` until it returns `True`.
- Once it returns `True`, continue with the next line in the mission.

Example with the left attachment:

```python
async def mission_left_with_wait():
    left_attachment_up(180, speed=400)
    await runloop.until(lambda: MotorIsStopped(port.C))
    left_attachment_down(180, speed=400)
    return
```

In words:
- Move the left attachment up.
- Wait until motor C appears stopped (encoder stable).
- Then move the attachment back down.

---

## 4. Practice – Wait for a Mechanism to Settle

Field activity:
1. Use a mission that:
   - Lifts an attachment to hit or lift a model.
   - Waits for `MotorIsStopped` on that port.
   - Then starts the next move (backing away or lowering).
2. Watch:
   - The console output (first position, samples, and final `True`).
   - The physical mechanism: does it stop bouncing before the next action starts?

Example snippet for the right attachment:

```python
async def mission_right_hit_and_settle():
    right_attachment_up(180, speed=400)
    await runloop.until(lambda: MotorIsStopped(port.B))
    right_attachment_down(180, speed=400)
```

Discuss:
- How is this more robust than using a fixed time delay (e.g., `await runloop.sleep_ms(500)`)?
  - It adapts to battery level, load, and small changes in mechanism friction.

Encourage students to:
- Use `MotorIsStopped` anywhere a mechanism must finish moving and settle before the next drive or turn.
- Reduce “mystery timing” in missions by using actual motor feedback instead of guessed delays.  

---


