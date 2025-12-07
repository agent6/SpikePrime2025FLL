# Lesson 20 – New Moves with Motors (Degrees & Positions)

> Based on the LEGO Education lesson “New Moves with Motors”  
> Original: <https://education.lego.com/en-us/lessons/get-moving-with-motors/new-moves-with-motors/>

## Question to Investigate

- How do robots move **precisely**?

Time: ~45 minutes  
Level: Beginner (Grades 6–8)

---

## Prepare

- Ensure SPIKE Prime hubs are **charged**, especially if using Bluetooth.
- Students should have already built the **Getting Started 2: Motors and Sensors** model (through step 19, used in “Making Moves with Motors”).
- Each group needs:
  - Hub with at least one motor on `port.A`.
  - A wheel (5.6 cm diameter) attached to the motor.

Note: A 5.6 cm wheel travels about **17.6 cm per 360° rotation**.

---

## 1. Engage – How Far Is One Rotation?

Using a SPIKE tire, ask:

- How could we measure how far the tire travels in **one rotation**?
- What different methods could we use?

Prompt students to think of the wheel as a **circle**:

- Circumference = π × diameter.
- For a 5.6 cm wheel, one rotation ≈ 17.6 cm.

Discuss:

- If we have a robot with wheels, how can we code the motors to move a **specific distance**, not just “for 2 seconds”?
- How might we program:
  - 0.5 rotation (180°),
  - 1 rotation (360°),
  - 2 rotations (720°)?

---

## 2. Explore – Run Single Motor for Degrees

Goal: use **degrees** to control how far a motor turns.

Pseudocode for one full circle:

- Import motor.
- Turn motor on.
- Move motor **360 degrees**.

Steps:

1. Open a new Python project in the SPIKE App.
2. Clear any existing code and connect the hub.
3. Plug a motor into `port.A`.

### Sample Code – Degrees

```python
import motor
from hub import port
import runloop


async def main():
    # Run a motor on port A for 360 degrees at 720 degrees per second.
    await motor.run_for_degrees(port.A, 360, 720)


runloop.run(main())
```

Discuss:

- Show students the **position marker** on the motor.
- Line the marker up at a visible “0°” starting point.
- Run the program and see if it returns to the same position.

Experiment:

- Try different degree values (small and large).
- Try **negative** degrees:

```python
# Run a motor on port A for -360 degrees at 720 degrees per second.
await motor.run_for_degrees(port.A, -360, 720)
```

Ask:

- What changed when you used a negative value? (Direction reversed.)
- What happens when you use a degree value **greater than 360**?

Discuss what students discovered.

---

## 3. Explore – Run Single Motor to Position

Now use **absolute position** instead of “move this many degrees”.

1. Align the motor marker to **0°**.
2. Discuss: How can we program the motor to move to a **specific position** and stop exactly there?

### Sample Code – To Absolute Position

```python
import motor
from hub import port
import runloop


async def main():
    # Run a motor on port A to 0 degrees at 720 degrees per second.
    await motor.run_to_absolute_position(port.A, 0, 720)


runloop.run(main())
```

If the motor starts at 0°, it won’t move.

Ask students to:

- Move the motor away from 0°.
- Run the program:
  - The motor moves back to 0° along the **shortest path**.

Run several times from different starting positions and observe:

- The motor does not always rotate the same direction/amount.
- It always takes the **shortest path** back to the target.

Ask:

- What is the **longest** move a motor can make to return to 0° along the shortest path?

### Sample Code – Multiple Positions

```python
import motor
from hub import port
import runloop


async def main():
    # Run a motor on port A to 0 degrees at 720 degrees per second.
    await motor.run_to_absolute_position(port.A, 0, 720)
    await runloop.sleep_ms(2000)
    # Move to 90 degrees in the clockwise direction.
    await motor.run_to_absolute_position(port.A, 90, 720, direction=motor.CLOCKWISE)


runloop.run(main())
```

Let students change the **target positions** (e.g., 180°, 270°, 360°) and see:

- How direction is chosen.
- How absolute positions can represent precise angles for mechanisms.

Remind: errors are normal while exploring—use the console messages.

---

## 4. Explain – Precision and When to Use Degrees vs Position

Have students share example programs for both **run_for_degrees** and **run_to_absolute_position**.

Discussion prompts:

- How does `motor.run_for_degrees` work? When is it useful?
- When would you prefer `run_for_degrees` vs `run_to_absolute_position`?
- Why do degrees/positions give more **precision** than programming for a number of seconds?
- What happened when you used a degree value larger than 360?
- How can you **calculate** degrees needed for a certain distance? (Use wheel circumference and ratios.)
- Why does the motor not move if you start at 0° and command it to go to 0°?
- How can you program the motor to move in the **opposite direction**? (Negative degrees, or `direction=`.)

---

## 5. Elaborate – Debugging Challenges

Work together to debug the following snippets. Have students run each one and read the **console errors** (or observed behavior).

### Debug 1 – What Is Missing?

```python
import motor
import runloop


async def main():
    # Run a motor on port A to 0 degrees at 720 degrees per second.
    await motor.run_to_absolute_position(port.A, 0, 720)
    await runloop.sleep_ms(2000)
    await motor.run_to_absolute_position(port.A, 90, 720, direction=motor.CLOCKWISE)


runloop.run(main())
```

Issue:

- `port` is not defined.
- Fix: add `from hub import port`.

### Debug 2 – What Number Is Wrong?

```python
import motor
from hub import port
import runloop


async def main():
    # Run a motor on port A to 0 degrees at 7200 degrees per second.
    await motor.run_to_absolute_position(port.A, 0, 7200)
    await runloop.sleep_ms(2000)
    await motor.run_to_absolute_position(port.A, 90, 720, direction=motor.CLOCKWISE)


runloop.run(main())
```

Issue:

- Velocity `7200` is outside the allowed range (–1000 to 1000).
- No error is thrown, but the motor speed is clamped to within the valid range.

### Debug 3 – What Is Wrong?

```python
import motor
from hub import port
import runloop


async def main():
    # Run a motor on port A to 0 degrees at 720 degrees per second.
    await Motor.run_to_absolute_position(port.A, 0, 720)


runloop.run(main())
```

Issue:

- `Motor` is capitalized; Python is **case‑sensitive**.
- Error: `NameError: name 'Motor' isn't defined`.
- Fix: use `motor.run_to_absolute_position(...)`.

---

## 6. Evaluate – Precision and Teamwork

Teacher observation:

- What different ways did students program their motors to move?
- Which methods (time, degrees, position) allow for the most **precise** movements?
- How did they use positions for exact stops?

Student self‑assessment (journal):

- What did you learn today that will help you program robots to move with **precision**?
- What characteristics of a **good teammate** did you show?
- Rate yourself 1–3 on **time management**.
- Rate yourself 1–3 on **materials (parts) management**.

