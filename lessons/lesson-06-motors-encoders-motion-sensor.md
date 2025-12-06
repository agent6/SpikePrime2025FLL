# Lesson 6 – Motors, Encoders, and Motion Sensor

> Environment: Spike App IDE with a Spike Prime hub connected  
> Reference docs: <https://tuftsceeo.github.io/SPIKEPythonDocs/SPIKE3.html>

## Lesson Goals

By the end of this lesson, students will be able to:
- Use `motor.run`, `motor.run_for_degrees`, and `motor.stop` on a real robot.
- Read `motor.relative_position` and explain why we reset encoders.
- Read `motion_sensor.tilt_angles()` and understand yaw for turning.

---

## 1. Basic Motor Commands

Open a new Spike Python project and add:

```python
import motor
from hub import port
import runloop

async def main():
    motor.run(port.A, 300)          # run left motor forward
    await runloop.sleep_ms(1000)    # wait 1 second
    motor.stop(port.A)              # stop motor

runloop.run(main())
```

Discuss:
- `motor.run(port.A, speed)` – keeps running until you stop it.
- `motor.stop(port.A)` – uses default braking.

Now try `run_for_degrees`:

```python
async def main():
    motor.run_for_degrees(port.A, 360, 300)

runloop.run(main())
```

Watch the wheel turn about one full rotation.

---

## 2. Encoders and `motor.relative_position`

Explain: *“Each motor has an encoder that counts degrees turned.”*

Example:

```python
async def main():
    from hub import port

    motor.reset_relative_position(port.A, 0)
    motor.run(port.A, 300)
    await runloop.sleep_ms(1000)
    motor.stop(port.A)

    pos = motor.relative_position(port.A)
    print("Motor A position:", pos)

runloop.run(main())
```

Key ideas:
- `reset_relative_position(port.A, 0)` sets “zero” where we want.
- `relative_position` tells us how far we’ve turned since the reset.
- Our helpers (like `drive_forward`) use this to know when to stop.

Mini‑exercise:
- Change the sleep time and see how the reported position changes.

---

## 3. Motion Sensor and Yaw (`tilt_angles`)

Explain: *“The hub has a built‑in motion sensor that can tell us how much we’ve turned.”*

Example:

```python
from hub import motion_sensor
import runloop

async def main():
    motion_sensor.reset_yaw(0)

    while True:
        angles = motion_sensor.tilt_angles()
        yaw = angles[0]
        print("Yaw:", yaw)
        await runloop.sleep_ms(200)

runloop.run(main())
```

Activity:
- Run this and slowly rotate the hub left and right.
- Observe how yaw increases/decreases.

Connect to our code:
- Our `pivot_*` and `spin_*` functions:
  - Reset yaw: `motion_sensor.reset_yaw(0)`
  - Use `motion_sensor.tilt_angles()[0]` to decide when to stop turning.

Show one example from `master.py`:

```python
motion_sensor.reset_yaw(0)
while motion_sensor.tilt_angles()[0] < target_angle_degrees:
    motor.run(port.E, speed)
```

Explain: *“We turn until yaw reaches the target angle, then stop for a precise turn.”*  

---


