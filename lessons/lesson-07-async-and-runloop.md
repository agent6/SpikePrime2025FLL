# Lesson 7 – Async and `runloop`

> Environment: Spike App IDE with a Spike Prime hub connected  
> Reference docs: https://tuftsceeo.github.io/SPIKEPythonDocs/SPIKE3.html

## Lesson Goals

By the end of this lesson, students will be able to:
- Explain what `async` and `await` do on the Spike hub.
- Use `runloop.run(main)` to start an async program.
- Use `await runloop.until(...)` to wait for events (tilt, button press).

---

## 1. What `async` and `await` Mean

Explain:
- **`async`** marks a function that can pause and resume.
- **`await`** tells the hub “wait here until this thing is done.”
- The Spike hub runs an **event loop** (`runloop`) that schedules async work.

Minimal example:

```python
import runloop

async def main():
    print("Hello from async main!")

runloop.run(main())
```

---

## 2. `runloop.run(main)` and Waiting with `sleep_ms`

Time‑based wait:

```python
import runloop

async def main():
    print("Start")
    await runloop.sleep_ms(1000)    # wait 1 second
    print("One second later")

runloop.run(main())
```

Key idea:
- `await runloop.sleep_ms(...)` is a non‑blocking delay; the hub can do other work in between.

---

## 3. `await runloop.until(...)` – Waiting for Events

Pattern:

```python
await runloop.until(lambda: <condition that is True/False>)
```

### A. Wait for Button Press

```python
from hub import button, light_matrix
import runloop

async def main():
    light_matrix.write("L")  # show hint for left button

    # Wait until LEFT button is pressed
    await runloop.until(lambda: button.pressed(button.LEFT))

    light_matrix.write("Go")

runloop.run(main())
```

### B. Wait for a Tilt

```python
from hub import motion_sensor, light_matrix
import runloop

async def main():
    motion_sensor.reset_yaw(0)
    light_matrix.write("Tilt")

    # Wait until yaw passes 30 degrees
    await runloop.until(lambda: motion_sensor.tilt_angles()[0] > 30)

    light_matrix.write("Done")

runloop.run(main())
```

Discuss:
- `button.pressed(...)` and `motion_sensor.tilt_angles()` both return values we can use in conditions.
- `runloop.until` keeps checking the condition until it becomes `True`.

This same pattern is used in `master.py` (e.g., waiting for the motion sensor to be stable and in mission selection to wait for button presses).  

---

[Back to Lessons Index](index.html)
