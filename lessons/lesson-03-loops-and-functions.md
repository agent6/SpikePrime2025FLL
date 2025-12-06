# Lesson 3 – Loops and Functions

## Lesson Goals

By the end of this lesson, students will be able to:
- Write `while` loops and avoid infinite loops.
- Use `for` loops with `range(...)` to repeat actions.
- Define functions with parameters and return values.
- Build a simple text‑only “robot” that follows rules.

---

## 1. `while` Loops

Explain: *“`while` repeats **while** a condition is True.”*

Example counter:

```python
count = 0

while count < 5:
    print("count is", count)
    count = count + 1
```

Key points:
- The condition (`count < 5`) is checked every time.
- Make sure something **changes** inside the loop or it never ends.

Quick exercise:
- Have students change `5` to `10`.
- Ask: “What happens if we forget `count = count + 1`?”

---

## 2. `for` Loops with `range`

Explain: *“`for` with `range` repeats a known number of times.”*

Example:

```python
for i in range(5):   # 0,1,2,3,4
    print("i is", i)
```

Another example:

```python
for step in range(1, 4):  # 1,2,3
    print("Step", step)
```

Mini‑exercise:
- Print `"Beep!"` 3 times.
- Print `"Mission"` and the numbers 1–5 on separate lines.

---

## 3. Defining Functions

Explain: *“A function is a reusable block of code with a name.”*

Basic function:

```python
def greet():
    print("Hello, team!")

greet()
greet()
```

Function with parameters:

```python
def cheer_for(team_name, points):
    print(f"Go {team_name}! You scored {points} points!")

cheer_for("RoboRockets", 120)
cheer_for("PythonBots", 95)
```

Function with a return value:

```python
def add_points(missions, bonus):
    total = missions + bonus
    return total

score = add_points(60, 20)
print("Total score:", score)
```

Discuss:
- Parameters are “inputs”.
- `return` sends a result back to the caller.

---

## 4. Mini‑Project – Text‑Only “Robot”

Goal: Simulate a robot using print statements and decisions.

Starter idea:

```python
def move_forward(steps):
    for i in range(steps):
        print("Robot moves forward one step")

def turn_left():
    print("Robot turns left 90 degrees")

def turn_right():
    print("Robot turns right 90 degrees")

def run_mission():
    move_forward(3)
    turn_left()
    move_forward(2)
    print("Robot reaches the target!")

run_mission()
```

Have students:
- Change how many steps the robot takes.
- Add a `pick_up()` function that prints `"Pick up model"`.
- Add a simple decision:

```python
def run_mission_with_choice(time_left):
    if time_left > 40:
        print("Plenty of time, running long mission.")
        move_forward(5)
    else:
        print("Short on time, running quick mission.")
        move_forward(2)
```

This mini‑project builds the mental model of **functions** and **loops** that we will later connect directly to real Spike Prime motor functions.  

---

[Back to Lessons Index](index.html)
