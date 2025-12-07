# Lesson 16 – Controlling Motion with Tilt (Motion Sensor & Conditions)

> Based on the LEGO Education lesson “Controlling Motion with Tilt”  
> Original: <https://education.lego.com/en-us/lessons/spike-python-u5-playing-games-with-simple-conditions/spike-python-u5l1-controlling-motion-with-tilt/>

## Goals

- Explore **conditional statements** in Python using the hub motion sensor.
- Understand how the motion sensor detects **gestures** and **orientation**.
- Use `if` logic to react to taps and tilts with images, sounds, and text.

Time: ~45 minutes  
Level: Beginner (Grades 6–8)

---

## Prepare

- Make sure SPIKE Prime hubs are charged (especially when using Bluetooth).
- Each group needs:
  - A SPIKE Prime hub.
  - Access to the SPIKE App Python canvas.
  - A small set of bricks for the warm‑up:
    - 1 magenta frame.
    - 3 different yellow elements.
    - 3 different red elements.

---

## Engage – Condition Warm‑Up (5 min)

1. Place the **magenta frame** on a sheet of paper. Spread the yellow and red elements **outside** the frame.
2. Explain: elements **inside** the frame are **true** (match the condition), outside the frame are **false**.
3. Run rounds with different conditions, clearing the frame each time:
   - Round 1: “The condition is **red**.”
   - Round 2: “The condition is **larger than a 2×2 brick**.”
   - Round 3: “The condition is **not a traditional brick shape**.”
4. Discuss:
   - What is a **conditional statement**?
   - Introduce **Boolean** values: `True` and `False`.

---

## Explore – Tap for Action (Gestures, 20 min)

Students will create simple conditional statements using the motion sensor.

1. Open a **new Python project** in the SPIKE App and clear the canvas.
2. Connect the hub.
3. Discuss: “How can we move the hub in our hand?” (tap, double tap, shake, etc.)
4. Write **pseudocode** for a “tap to show image” program:
   - Import motion sensor.
   - If hub is tapped → show an image on the light matrix.

### Sample Code – Tap to Show Image

Have students type and run:

```python
from hub import light_matrix, motion_sensor
import runloop

def if_tapped():
    # If the hub is tapped, return True
    return motion_sensor.gesture() == motion_sensor.TAPPED

async def main():
    # Wait until the hub is tapped to show a sad face
    await runloop.until(if_tapped)
    light_matrix.show_image(light_matrix.IMAGE_SAD)
    print("Stop Please")

runloop.run(main())
```

Discuss:

- This is a **conditional** program: “if the hub is tapped, then show a sad face.”
- `==` is a **comparison**, not an assignment.
- If the condition is never met, the image never appears.

Ask students to experiment with different gestures:

- `motion_sensor.TAPPED`
- `motion_sensor.DOUBLE_TAPPED`
- `motion_sensor.SHAKEN`
- `motion_sensor.FALLING`
- `motion_sensor.UNKNOWN`

They can refer to the Tufts SPIKE 3 docs:  
<https://tuftsceeo.github.io/SPIKEPythonDocs/SPIKE3.html>

---

## Explore – Tilt for Action (Orientation, 15 min)

Now students will use **orientation** instead of gestures.

### Sample Code – Tilt to Show Arrow

```python
from hub import light_matrix, motion_sensor
from app import sound
import runloop

def face_up():
    # Return True if the hub is oriented USB port up
    return motion_sensor.up_face() == motion_sensor.BACK

async def main():
    await runloop.until(face_up)
    light_matrix.show_image(light_matrix.IMAGE_ARROW_N)
    print("I am awake")
    await sound.play("Applause 1")

runloop.run(main())
```

Discuss:

- The condition is “hub USB side is facing up”.
- Only when that condition is **true** do we see the arrow, print text, and play a sound.
- If the hub already starts in that orientation, the action may trigger immediately.

Orientation options (which side is facing up):

- Speaker side → `motion_sensor.FRONT`
- USB side → `motion_sensor.BACK`
- A/C/E ports → `motion_sensor.LEFT`
- B/D/F ports → `motion_sensor.RIGHT`
- Light matrix side → `motion_sensor.TOP`
- Battery side → `motion_sensor.BOTTOM`

Encourage students to change the orientation condition and add:

- Different images.
- Different sounds.
- Extra `print()` messages.

---

## Explain – Make the Logic Visible (5 min)

Whole‑group questions:

- What is a **conditional statement** in a program?
- What does `if` do?
- Why are the lines after `if` **indented**?
- How does the **motion sensor** work?
- What different conditions can you set for the motion sensor?

Let a few students show their favorite versions on the hub.

---

## Elaborate – Story Game with Motion (10 min)

Challenge: create a **short story game** that uses the motion sensor to fill in a blank.

Example as pseudocode:

- `print("One day Jane was walking through the park. She looked up.")`
- Player tilts the hub up.
- Ghost image appears.
- Sound plays.
- `print("Then she woke up and realized it was a dream.")`

Guidelines:

- Write the story first as **pseudocode**.
- Use `print()` for the story text.
- Use at least one **gesture or orientation** condition.
- Include code **comments** explaining what each part does.

Have groups share their story games and reflect on different ways the motion sensor can be used.

---

## Evaluate – Reflection and Checklist (5 min)

Teacher observation:

- How do conditional statements work in students’ programs?
- How are they using the motion sensor (gestures, orientation)?
- Are they reading and fixing console error messages?

Student self‑assessment (journal or discussion):

- What did you learn today about using **conditional statements**?
- What **good teammate** behaviors did you show?
- Rate yourself 1–3 on **time management**.
- Rate yourself 1–3 on **materials/parts management**.

