# Lesson 2 – Control Flow (Decisions in Python)

## Lesson Goals

By the end of this lesson, students will be able to:
- Write `if`, `elif`, and `else` blocks.
- Use **comparison** (`==`, `!=`, `<`, `<=`, `>`, `>=`) and **logical** (`and`, `or`, `not`) operators.
- Solve simple problems like grading, even/odd checks, and decision trees.

---

## 1. `if`, `elif`, `else` Basics

Explain: *“Control flow lets the program make decisions.”*

Example:

```python
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: Needs work")
```

Key points:
- Conditions must be **True or False**.
- Indentation (4 spaces) defines the block.

---

## 2. Comparison and Logical Operators

Comparison examples:

```python
mission_points = 30
max_points = 40

print(mission_points == max_points)  # equal?
print(mission_points > 0)            # positive?
print(mission_points >= 35)          # high score?
```

Logical operators:

```python
time_left = 40
has_bonus = True

if time_left > 30 and has_bonus:
    print("Go for the extra mission!")
```

Discuss:
- `and`: both conditions must be True.
- `or`: at least one condition is True.
- `not`: flips True/False.

---

## 3. Small Exercises

### A. Grading
Write a program that:
- Asks for a score (hard‑code a number first).
- Prints a letter grade using `if/elif/else`.

Example targets:
- 90+ → `"A"`
- 80–89 → `"B"`
- 70–79 → `"C"`
- below 70 → `"Try again!"`

### B. Even / Odd Checker

Introduce `%` (modulo = remainder):

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Exercise:
- Test several numbers: 0, 1, 2, 5, 10.
- Ask: “What does `% 2` tell us?”

### C. Simple Decision Tree (Robot Example)

Scenario:
- If **time_left > 60** and **robot_ok == True** → `"Run big mission"`
- Else if **time_left > 30** → `"Run medium mission"`
- Else → `"Run quick mission"`

Starter code:

```python
time_left = 45
robot_ok = True

if time_left > 60 and robot_ok:
    print("Run big mission")
elif time_left > 30:
    print("Run medium mission")
else:
    print("Run quick mission")
```

Have students:
- Change `time_left` and `robot_ok` and predict which line will run before they execute it.

---


