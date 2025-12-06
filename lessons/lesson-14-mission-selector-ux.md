# Lesson 14 – Mission Selector UX

> Environment: Spike App IDE with our FLL robot and `master.py`

## Lesson Goals

By the end of this lesson, students will be able to:
- Describe how the `mission_selector()` loop works.
- Use the **RIGHT** button to change missions and the **LEFT** button to run the selected mission.
- Understand how mission numbers and the selector indicator LED are displayed on the hub.

---

## 1. The `mission_selector()` Loop in `master.py`

Open `master.py` and find:

```python
async def mission_selector():
    current = 0
    missions = [
        mission_0,
        mission_1,
        mission_2,
        mission_3,
        mission_4,
        mission_5,
        mission_6,
        mission_7,
        mission_8,
        mission_9,
    ]

    while True:
        # Show current mission number and mark selector mode with top-left LED.
        light_matrix.write(str(current))
        light_matrix.set_pixel(0, 0, 100)

        # Wait for LEFT or RIGHT button press
        await runloop.until(
            lambda: button.pressed(button.LEFT)
            or button.pressed(button.RIGHT)
        )

        # RIGHT moves to next mission, LEFT runs the current mission
        if button.pressed(button.RIGHT):
            current = (current + 1) % len(missions)
        elif button.pressed(button.LEFT):
            await missions[current]()

        # Wait for all buttons to be released (debounce)
        await runloop.until(
            lambda: not (
                button.pressed(button.LEFT)
                or button.pressed(button.RIGHT)
            )
        )
```

Explain:
- `current` – index of the selected mission (0–9).
- `missions` – list mapping numbers to mission functions.
- Infinite `while True` – selector never exits; runs until program stops.

---

## 2. Button UX – LEFT vs RIGHT

Behavior:
- **RIGHT button**:
  - Moves to the next mission: `current = (current + 1) % len(missions)`.
  - `%` wraps from 9 back to 0.
- **LEFT button**:
  - Runs the currently selected mission: `await missions[current]()`.

Call out:
- The green center button always starts/stops the program (firmware behavior) – it does **not** select missions.
- Teams should practice:
  - Start program with green button.
  - Use RIGHT to pick mission number.
  - Use LEFT to run.

---

## 3. Displaying Mission Numbers and the Selector Indicator LED

Each loop iteration:

```python
light_matrix.write(str(current))
light_matrix.set_pixel(0, 0, 100)
```

Explain:
- `light_matrix.write(str(current))` shows the mission number (0–9) on the hub’s LED matrix.
- `light_matrix.set_pixel(0, 0, 100)` turns on the **top-left LED** at full brightness as a “selector mode” indicator.

Activity:
- Run the program and **do not press any buttons**.
- Ask: “What do you see?”
  - A number (selected mission).
  - Top-left LED lit → you are in the selector.

---

## 4. Practice – Driver Workflow

Have each driver practice this sequence:

1. Place robot in base, press the **green button** to start `master.py`.
2. Check:
   - Top-left LED is on.
   - A mission number is shown (start at 0).
3. Tap **RIGHT** until you reach the mission you want (e.g., 3).
4. Press **LEFT** to run that mission.
5. When the mission finishes, the selector returns:
   - Same mission number still shown.
   - Top-left LED still on.
6. Either:
   - Run the same mission again (LEFT), or
   - Change mission (RIGHT) and then run (LEFT).

Debrief:
- Ask drivers which UX details help them feel confident (LED indicator, number display, consistent button behavior).
- Make sure every team member can reliably start, choose, and run missions without looking at the code.  

---

[Back to Lessons Index](index.html)
