# Lesson SEL – `mission_selector`

> Environment: Spike App IDE with our FLL robot and `master.py`

## Lesson Goals

By the end of this lesson, students will be able to:
- Explain how the `mission_selector()` function works internally.
- Describe how it maps mission numbers (0–9) to mission functions.
- Understand how the selector loop uses buttons and the light matrix to manage missions.

---

## 1. The `mission_selector` Function in `master.py`

Open `master.py` and find:

```python
async def mission_selector():
    """
    Mission selector menu.

    Uses LEFT/RIGHT/CENTER buttons to select and run missions 0–9.
    The selector loop never exits.
    """
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

Key parts:
- `current` – the index of the currently selected mission (0–9).
- `missions` – a list of mission functions; `missions[current]` is the selected mission.
- Infinite `while True` loop – the selector never exits; it keeps waiting for driver input.

---

## 2. Mapping Mission Numbers to Functions

Explain:
- The `missions` list is a **dispatch table**:

```python
missions = [
    mission_0,  # index 0
    mission_1,  # index 1
    ...
    mission_9,  # index 9
]
```

- `current` is the mission number shown on the hub.
- `await missions[current]()` calls the function at that index.

Thought exercise:
- If `current = 3`, which function will run?  
  → `mission_3`.

Changing missions:

```python
current = (current + 1) % len(missions)
```

- Increments `current`.
- `% len(missions)` wraps around from 9 back to 0.

---

## 3. Buttons and Light Matrix Behavior

Inside the loop:

```python
light_matrix.write(str(current))
light_matrix.set_pixel(0, 0, 100)
```

Explain:
- Displays the current mission number (`0`–`9`) on the hub.
- Lights the **top-left LED** as a “selector mode” indicator.

Waiting for input:

```python
await runloop.until(
    lambda: button.pressed(button.LEFT)
    or button.pressed(button.RIGHT)
)
```

- This pauses until either LEFT or RIGHT is pressed.

Handling input:

```python
if button.pressed(button.RIGHT):
    current = (current + 1) % len(missions)
elif button.pressed(button.LEFT):
    await missions[current]()
```

- RIGHT → change selection.
- LEFT → run the selected mission.

Debounce:

```python
await runloop.until(
    lambda: not (
        button.pressed(button.LEFT)
        or button.pressed(button.RIGHT)
    )
)
```

- Wait until all buttons are released before accepting another input.

---

## 4. Practice – Modify and Extend the Selector

Ideas:
- Add a simple **startup animation** before the loop begins (e.g., show “GO”).
- Add a “mission description” comment above each mission function so students know what mission number does what.

Challenge activity:
- Add a **“test mode”** where a special mission (e.g., mission_9) runs a short self-test (drive forward then back).
- Make sure it still fits into the same `missions` list and is selectable like the others.

Discuss:
- How the selector design separates **UI** (buttons + display) from **behavior** (mission functions).
- How easy it is to swap what mission number does by editing `mission_n` code without changing the selector logic.  

---


