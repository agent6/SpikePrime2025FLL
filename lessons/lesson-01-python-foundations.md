# Lesson 1 – Python Foundations (Off‑Robot)

## Lesson Goals

By the end of this lesson, students will be able to:
- Explain what a **variable** is and name four basic types: `int`, `float`, `bool`, `str`.
- Use variables in simple **expressions and operators**.
- Use `print()` and basic **string formatting** to show results.

Keep this lesson **off‑robot** (laptop or Chromebook) so everyone can focus on Python, not hardware.

---

## 1. Variables & Types

Explain: *“A variable is a named box that holds a value.”*

Show and run:

```python
team_number = 123        # int
robot_speed = 0.5        # float
is_ready = True          # bool
team_name = "RoboRockets"  # str
```

Quick check:
- Ask: “Which of these are numbers? Which are text? Which is True/False?”
- Have students change the values and re‑run.

---

## 2. Expressions and Operators

Show numeric expressions:

```python
start = 10
added = start + 5
half = added / 2
double = added * 2
```

Show comparisons and booleans:

```python
score = 80
passed = score >= 60      # True or False?
```

Mini‑exercise:
- Ask students to compute how many **points** they’d have with 3 missions worth 10 points each, plus a 20‑point bonus.

---

## 3. `print()` and Simple Formatting

Start simple:

```python
team_name = "RoboRockets"
score = 50

print(team_name)
print(score)
```

Then connect variables into one line:

```python
print("Team:", team_name, "Score:", score)
```

Introduce f‑strings (if environment supports Python 3.6+; Spike 3 does):

```python
print(f"Team {team_name} scored {score} points!")
```

---

## 4. Practice Tasks

Have students write small scripts that:
1. Store their **name**, **age**, and **favorite robot part** in variables and print a sentence using all three.
2. Compute the **total score** for:
   - 2 missions × 25 points
   - 1 bonus worth 15 points  
   Then print: `"Total score = X"`.
3. Change the values and re‑run to see how the output changes.

Encourage pair‑programming: one “driver” at the keyboard, one “navigator” reading the code and spotting mistakes.

---


