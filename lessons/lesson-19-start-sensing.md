# Lesson 19 – Start Sensing (Force Sensor & Conditions)

> Based on the LEGO Education lesson “Start Sensing”  
> Original: <https://education.lego.com/en-us/lessons/spike-python-u3-sensor-control/spike-python-u3l1-start-sensing/>

## Question to Investigate

- How can **sensors** interact with or control **motors**?

Time: ~45 minutes  
Level: Beginner (Grades 6–8)

---

## Prepare

- Ensure SPIKE Prime hubs are **charged**, especially if using Bluetooth.
- Each group needs:
  - 1 hub
  - 1 motor (e.g., on `port.A`)
  - 1 **force sensor** (e.g., on `port.B`)

---

## Engage – Freeze Dance with a Sensor (5 min)

Whole class activity:

1. Play a quick **freeze dance** game.
2. Hold up a **force sensor** and explain:
   - Students can only move when you are **pressing** the sensor button.
   - They must **freeze** when you **release** it.
3. Make it obvious when you push and release the button.

Discuss:

- The sensor is providing **information** that changes behavior.
- Ask: “How do you think sensors work?” and “How could a sensor control a robot’s movement?”

---

## Explore – Push, Start, Stop (20 min)

Students will control a motor using the force sensor.

1. In the SPIKE App Knowledge Base, open:
   - GETTING STARTED → **7. Sensor Control** (force sensor intro).
2. Open a **new Python project** and clear the canvas.
3. Connect the hub:
   - Plug the motor into `port.A`.
   - Plug the force sensor into `port.B` (or another port; adjust code as needed).

Brainstorm **pseudocode**:

- Import force sensor, motor, and hub.
- Wait for **sensor press**.
- Turn motor on.
- Wait for **sensor release**.
- Turn motor off.

### Sample Code – Press to Start, Release to Stop

Have students type and run:

```python
import runloop
import motor
import force_sensor
from hub import port


def is_force_sensor_pressed():
    # collect input from force sensor
    return force_sensor.pressed(port.B)


def is_force_sensor_not_pressed():
    # collect input from force sensor
    return not force_sensor.pressed(port.B)


async def main():
    # wait until the force sensor is pressed
    await runloop.until(is_force_sensor_pressed)

    motor.run(port.A, 750)

    # wait until the force sensor is not pressed
    await runloop.until(is_force_sensor_not_pressed)

    motor.stop(port.A)


runloop.run(main())
```

Discuss:

- When the force sensor is **pressed**, the motor starts at 750 degrees/second.
- It continues until the sensor is **released**, then the motor stops.
- Walk through each line so students see how sensor input triggers motor actions.

Now **invert** the logic: motor runs first, then stops on button press.

### Sample Code – Run Until Pressed

```python
import runloop
import motor
import force_sensor
from hub import port


def is_force_sensor_pressed():
    # collect input from force sensor
    return force_sensor.pressed(port.B)


async def main():
    # turn on motor
    motor.run(port.A, 1000)

    # wait until the force sensor is pressed
    await runloop.until(is_force_sensor_pressed)

    # stop motor
    motor.stop(port.A)


runloop.run(main())
```

Key idea:

- Moving `motor.run(...)` **before** the `await runloop.until(...)` call changes the behavior:
  - Motor starts immediately.
  - Program waits for the **press** to stop it.
- The “not pressed” helper is no longer needed in this version.

Let students experiment:

- Different ports (`port.C`, `port.D`, etc.).
- Different speeds (positive/negative values).

---

## Explain – Using Sensors to Control Motors (5 min)

Whole class questions:

- How can you use a **sensor** to control a motor’s actions?
- What are different ways to use or program a **force sensor**?
- Why don’t we set a **time** or **distance** for the motor here?
  - (Hint: the sensor acts as the **stop condition**.)
- What kinds of **errors** might happen (wrong port, missing import, etc.)?

Clarify:

- The force sensor is read using `force_sensor.pressed(port.B)`.
- `runloop.until(...)` waits for a **condition function** to return `True`.
- Sensors + conditions let us replace fixed timings with **real feedback**.

---

## Elaborate – Print Messages & Simple Games (10 min)

Introduce printing to the **console**.

Start from the second example and add a `print()` line:

```python
import runloop
import motor
import force_sensor
from hub import port


def is_force_sensor_pressed():
    # collect input from force sensor
    return force_sensor.pressed(port.B)


async def main():
    # turn on motor
    motor.run(port.A, 1000)

    # wait until the force sensor is pressed
    await runloop.until(is_force_sensor_pressed)

    # stop motor
    motor.stop(port.A)

    # print Hello! in the console
    print("Hello!")


runloop.run(main())
```

Discuss:

- What happens when `"Hello!"` is printed?
- How can print messages help:
  - Explain what the program is doing.
  - Make the program more fun.
  - Debug (see where the program got to).

Debugging reminder:

- Printed text must be in **quotes** and inside parentheses:
  - `print("text")` or `print('text')`.

Challenge:

- Create a **question‑and‑answer game**:
  - One student pushes the button to answer.
  - The correct answer appears in the console (or multiple messages print).

---

## Evaluate – Reflection (5 min)

Teacher observation:

- What are some ways students programmed the force sensor to work?
- How did the sensor and motor **interact**?
- What creative uses of `print()` did they come up with?

Student self‑assessment (journal):

- What did you learn today about using a **force sensor**?
- When is it useful to use the `print()` function?
- What characteristics of a **good teammate** did you display today?
- Rate yourself 1–3 on **time management**.
- Rate yourself 1–3 on **materials (parts) management**.

