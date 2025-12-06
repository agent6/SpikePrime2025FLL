# Lesson 4 – Lists and Dictionaries (Stretch)

> Environment: Use the online Python playground  
> <https://www.onlineide.pro/playground/python>

## Lesson Goals

By the end of this stretch lesson, students will be able to:
- Use **lists** to store sequences (e.g., scores, mission names).
- Access items by **index** and loop over lists.
- Use **dictionaries** to store named settings (e.g., speeds, distances).

---

## 1. Lists – Sequences of Values

Explain: *“A list is an ordered collection of values in square brackets `[]`.”*

Example:

```python
scores = [25, 40, 35, 50]
teams = ["Alpha", "Bravo", "Charlie"]

print(scores)
print(teams)
```

Indexing (zero‑based):

```python
print(scores[0])   # first score
print(teams[1])    # second team
```

Exercise:
- Add another team to the list and print it.

---

## 2. Loops Over Lists

Loop with index:

```python
scores = [25, 40, 35, 50]

for i in range(len(scores)):
    print("Score", i, "=", scores[i])
```

Loop directly over values:

```python
for score in scores:
    print("Score:", score)
```

Mini‑exercise:
- Given `scores = [10, 20, 30]`, print the **total** using a loop.

```python
scores = [10, 20, 30]
total = 0

for score in scores:
    total = total + score

print("Total:", total)
```

---

## 3. Dictionaries – Named Settings

Explain: *“A dictionary maps **keys** to **values**, using `{}`.”*

Robot settings example:

```python
robot_settings = {
    "drive_speed": 300,
    "turn_speed": 200,
    "left_wheel_port": "A",
    "right_wheel_port": "E",
}

print(robot_settings)
print(robot_settings["drive_speed"])
```

Change a value:

```python
robot_settings["drive_speed"] = 350
print("New drive speed:", robot_settings["drive_speed"])
```

Loop over keys and values:

```python
for key in robot_settings:
    value = robot_settings[key]
    print(key, "=", value)
```

---

## 4. Practice Tasks

1. **Mission Scores List**
   - Create `mission_scores = [15, 25, 10, 30]`.
   - Use a loop to print each mission’s score and the total.

2. **Robot Config Dictionary**
   - Create a dictionary `config` with:
     - `"slow_speed"`, `"normal_speed"`, `"fast_speed"`
   - Print a sentence using one of the speeds, e.g.  
     `print(f"Normal speed is {config['normal_speed']}")`

3. **Combine Lists and Dicts (Optional)**
   - Make a list of team dictionaries:

   ```python
   teams = [
       {"name": "Alpha", "score": 50},
       {"name": "Bravo", "score": 65},
   ]

   for team in teams:
       print(team["name"], "scored", team["score"])
   ```

These ideas will later map to robot code where lists can store sequences of moves, and dictionaries can store named settings for missions and speeds.  

---


