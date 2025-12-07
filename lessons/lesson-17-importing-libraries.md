# Lesson 17 – Importing Libraries (Connecting Software & Hardware)

> Based on the LEGO Education lesson “Importing Libraries”  
> Original: <https://education.lego.com/en-us/lessons/prime-python-communicating-ideas/importing-libraries/>

## Questions to Investigate

- How can engineers and computer programmers work together to create a way to **communicate ideas** to others?
- Why do we need to **import libraries** in Python to connect software and hardware?

Time: ~45 minutes  
Level: Beginner (Grades 6–8)

---

## Prepare

- Decide groupings (ideally **2 students per SPIKE Prime set**).
- Set expectations for **teamwork** and **materials management**.
- Check that SPIKE Prime hubs are **charged**, especially if using Bluetooth.

---

## 1. Engage – Recipe Analogy

Start a discussion:

- When you follow a **recipe**, you gather:
  - Ingredients (things you use).
  - Tools (stove, oven, mixer, spatula, etc.).
- In Python, before you “cook” (run your program), you must “gather”:
  - The **libraries** (words and modules) that let your code talk to the hardware.

Key idea:

- Importing libraries is like getting the right tools out **before** you start cooking.

---

## 2. Explore – What Is a Library?

Explain:

- Python is **text‑based**: spelling, capitalization, and punctuation all matter.
- For the SPIKE App to talk to the SPIKE Prime hardware, we must **import** the right libraries.

Hands‑on:

1. Have students open their SPIKE Prime sets and remove:
   - 1 hub
   - 3 motors
   - 3 sensors
2. Identify each hardware piece together.
3. Turn on the hub (large center button).
4. Ask: “How do you think we would **import** each piece of hardware into the program?”

Show the **introductory program** in the SPIKE App Python canvas:

```python
from hub import light_matrix
import runloop


async def main():
    # write your code here
    await light_matrix.write("Hi!")


runloop.run(main())
```

Discuss:

- The `from hub import light_matrix` line is importing a **library** from the hub module.
- Ask students to match hardware pieces to typical library names:
  - `light_matrix` – 5×5 grid on the hub front.
  - `button` – three front buttons (left, center, right).
  - `light` – ring light around the center button.
  - `force_sensor` – sensor with a black push button.
  - `motion_sensor` – internal gyro/tilt sensor inside the hub.
  - `speaker` – built‑in speaker on the hub.
  - `color_sensor` – small square sensor with one light.
  - `app` – used to play sounds (software layer).
  - `distance_sensor` – ultrasonic sensor with two “eyes”.
  - `motor` – any single motor.
  - `motor_pair` – two motors working together.

Have students return all hardware neatly to the set trays.

---

## 3. Explain – Why Import First?

Guide questions:

- Why is it important to **import a library** before writing code that uses it?
- What kinds of things can be imported for use with the hub?
- How are **motors** imported differently from `light_matrix`?

Clarify:

- Libraries are usually imported at the **top** of the `.py` file.
- They should be imported **once**, then reused throughout the program.
- The `.py` file is the Python program (you don’t see `.py` on the canvas, but it’s the underlying file).

---

## 4. Elaborate – Practice Importing Libraries

Have students open a **new Python project** in the SPIKE App and connect their hub.

They will see a starter program similar to:

```python
from hub import light_matrix
import runloop


async def main():
    # write your code here
    await light_matrix.write("Hi!")


runloop.run(main())
```

Activities:

1. Ask students:
   - Which libraries have been imported? (Lines 1–2.)
   - Which hardware is used in `await light_matrix.write("Hi!")`?
2. Run the program:
   - The light matrix should scroll “Hi!” across the display.
3. Troubleshooting tips:
   - Check hub connection icon:
     - Green ring = USB connected.
     - Blue ring = Bluetooth connected.
     - Yellow = disconnected.

Introduce the **Knowledge Base** in the SPIKE App:

- Have students open the right‑side panel and read:
  - “1. Introduction to Python”
  - Importing libraries section.
- Discuss the statement:
  - “The imported libraries are located at the beginning of the .py file and should appear only once in the program.”

Experiment:

- Open another new Python project.
- Change the string in `write("Hi!")` to different phrases to see how the behavior changes.
- Optionally add more imports (for example `from hub import button`) and talk about what new hardware becomes available.

---

## 5. Evaluate – Understanding and Reflection

Teacher observation prompts:

- What happened on your hub when you ran the program?
- Which **libraries** did you use in this program?
- Why do you need to **import** different parts of the hub before using them?
- How can engineers and programmers work together so software and hardware **communicate ideas** clearly?

Materials management reminder:

- Parts should **not be shared** between sets.
- If a part is missing, students should tell the teacher right away.

Self‑scoring guide for materials management (1–3):

1. Materials are not all in the correct tray; some parts are still left out or assembled.
2. Materials are in the correct locations, but only **one** partner helped.
3. Both partners worked together and all parts are correctly put away.

Student self‑assessment (journal):

- Why do you need to **import libraries** at the beginning of a Python program?
- What characteristics of a **good teammate** did you show today?
- Rate yourself 1–3 on **time management**.
- Rate yourself 1–3 on **materials (parts) management**.

