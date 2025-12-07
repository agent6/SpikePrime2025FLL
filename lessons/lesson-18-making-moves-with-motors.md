# Lesson 18 – Making Moves with Motors (Dance Party)

> Based on the LEGO Education lesson “Making Moves with Motors”  
> Original: <https://education.lego.com/en-us/lessons/get-moving-with-motors/making-moves-with-motors/>

## Question to Investigate

- How can engineers and programmers work together to **make something move**?

Time: ~45 minutes  
Level: Beginner (Grades 6–8)

---

## Prepare

- Ensure SPIKE Prime hubs are **charged**, especially if connecting via Bluetooth.
- Each pair of students should have:
  - 1 SPIKE Prime hub.
  - At least **2 motors** (one large, one medium is fine).
  - Bricks to attach to motors for the “dance party”.

---

## 1. Engage – Humans as Motors

Get students thinking about movement and timing:

1. Have students stand in a line and “act as motors”.
2. Ask them to walk **5 steps forward** together.
   - Repeat a couple of times.
   - Ask: “Why didn’t everyone move exactly the same distance?”
3. Ask them to raise their **right arm** when you say “Raise.”
   - Repeat a few times.
   - Ask: “Why didn’t everyone move at the exact same time?”
4. Ask them to **clap** when you say “Clap.”
   - Again, timing will differ.

Discuss:

- Humans react with **delay** and **variation**.
- A group of robots running the **same code** on the **same command** will move much more consistently.
- When is this consistency useful? (FLL missions, factory robots, etc.)

---

## 2. Explore – Single Motor Basics

Students will work with a single motor on **port A**.

1. In the SPIKE App, direct students to the Knowledge Base:
   - GETTING STARTED → “4. Controlling Motors”.
2. Then open a **new Python project**:
   - Clear any existing code.
   - Connect the hub.
3. Plug a **large motor** into `port.A` on the hub.

Talk through **pseudocode** for running a motor for 2 rotations:

- Import `motor`.
- Turn motor on.
- Move clockwise for 2 rotations.

Explain that pseudocode is just **words** describing what we want; the actual Python will look slightly different.

### Sample Code – Run Motor for Degrees

Have students type and run:

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

- What does `360` mean? (Degrees of rotation; 360° ≈ 1 full turn.)
- What does `720` mean? (Speed in degrees per second.)

Have students experiment:

- Change `360` to other values (e.g., 90, 180, 720).
- Change `720` to other speeds (e.g., 360, 1000).

Troubleshooting:

- Make sure the motor is actually on **port A**, or change `port.A` to the correct port.

---

## 3. Explore – Two Motors

Now add a **second motor** on `port.B`.

Discuss:

- What types of robots need **two motors**? (Drive bases, arms, etc.)
- How can we make both motors run in a program?

Update the pseudocode:

- Turn motor A for some angle and speed.
- Turn motor B for some angle and speed.
- Then think about **timing** (one after another vs both at once).

### Sample Code – Two Motors with Awaits

```python
import motor
from hub import port
import runloop


async def main():
    # Run a motor on port A for 360 degrees at 720 degrees per second.
    await motor.run_for_degrees(port.A, 360, 720)
    # Run a motor on port B for 360 degrees at 720 degrees per second.
    await motor.run_for_degrees(port.B, 360, 720)


runloop.run(main())
```

Ask:

- What did you see? (Motor A runs, then Motor B runs.)

Now change the code so that **only the second await is removed**:

```python
async def main():
    await motor.run_for_degrees(port.A, 360, 720)
    motor.run_for_degrees(port.B, 360, 720)
```

Run again and compare:

- What changed?
- Did Motor A and Motor B run **at the same time** or one after another?

Explain:

- An `await` waits for an **awaitable** to finish before moving on.
- Without `await`, the program can start another action sooner.
- For deeper info, point to Getting Started → “4. Controlling Motors” for awaitables.

---

## 4. Explain – Parameters and Directions

Discuss with students:

- Did the motors turn in the **same** or **opposite** directions?
- How did different combinations of **degrees** and **speed** change the motion?
- How do you choose **which motor** to move when multiple motors are attached? (By port: `port.A`, `port.B`, etc.)

Key points:

- Importing libraries:
  - `import motor` – gives access to `motor.run_for_degrees`, etc.
  - `from hub import port` – lets us use `port.A`, `port.B`, etc.
- Motor parameters:
  - Degrees (how far).
  - Speed (degrees per second, integer from –1000 to 1000).
  - Sign of speed or degrees can reverse direction, depending on the API call.

Questions to ask:

- Explain the difference between importing just `motor` and adding other libraries (like `light_matrix`, `sound`, etc.) for your dance party.
- What parameters can you change to make motors move in different ways?
- How can you **debug** when a motor doesn’t move? (Check ports, imports, typos.)

---

## 5. Elaborate – Motor Dance Party

Challenge: create a **motor dance party** with two motors.

Ideas:

- Both motors spinning the same direction.
- Motors spinning opposite directions.
- Mixing speeds and durations to create a **pattern**.

Encourage students to:

- Attach bricks or decorations to their motors.
- Add:
  - Sounds (using the `app`/`sound` library).
  - Hub lights (`light_matrix` and hub `light`) for extra effect.
- Think about which **libraries** they need to import to support these features.

Have groups share their dancing robots and **explain their programs**:

- Which ports are used?
- How did they choose speeds and degrees?
- How did they time their motions?

Afterward, disconnect motors and return all parts to the correct locations.

---

## 6. Evaluate – Reflection and Teamwork

Teacher observation prompts:

- What happened on the hub and motors when the program ran?
- Which **libraries** did students import and use?
- How can engineers and computer programmers work together to make something move?
- How did students troubleshoot motor issues (wrong port, wrong import, etc.)?

Student self‑assessment (journal):

- How do you determine **which motor** you are programming when multiple motors are attached?
- What characteristics of a **good teammate** did you display today?
- Rate yourself 1–3 on **time management**.
- Rate yourself 1–3 on **materials (parts) management**.

