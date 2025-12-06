# Lesson 12 – Async Motion Helpers & Parallel Tasks

> Environment: Spike App IDE with our FLL robot and `master.py`  
> API reference: <https://tuftsceeo.github.io/SPIKEPythonDocs/SPIKE3.html>

## Lesson Goals

By the end of this lesson, students will be able to:
- Use the async motion helpers in `master.py`:
  - `async_drive_forward`, `async_drive_backward`
  - `async_left_attachment_up/down`
  - `async_right_attachment_up/down`
- Explain the idea of **parallel tasks** with `runloop.create_task`.
- Write a mission that drives while raising an attachment.

---

## 1. Async Motion Helpers in `master.py`

Open `master.py` and find:

```python
async def async_drive_forward(speed, target_degrees, kP=0.5):
    ...

async def async_drive_backward(speed, target_degrees, kP=0.5):
    ...

async def async_left_attachment_up(degrees, speed=1110):
    ...

async def async_left_attachment_down(degrees, speed=1110):
    ...

async def async_right_attachment_up(degrees, speed):
    ...

async def async_right_attachment_down(degrees, speed):
    ...
```

Key ideas:
- These functions are marked `async` and use `await runloop.sleep_ms(...)` inside.
- That means they **yield** control regularly, so other tasks can run in between.

Compare to blocking helpers:
- `drive_forward`, `left_attachment_up`, etc. run in tight loops and block until done.
- The async versions are designed for **parallel** movement.

---

## 2. Concept: Parallel Tasks with `runloop.create_task`

Explain:
- A **task** is like a separate “mini‑program” running alongside others.
- `runloop.create_task(async_function(...))` starts it and returns a handle (task object).
- We can `await` that handle to wait until the task is finished.

Pattern:

```python
task = runloop.create_task(async_drive_forward(150, 720))
# other code can run here
await task   # wait until driving is done
```

---

## 3. Example – Drive While Raising an Arm

Goal: Robot drives forward while lifting the left attachment.

Example mission:

```python
import runloop
from hub import port

async def mission_drive_and_lift():
    # Start driving and lifting at the same time
    drive_task = runloop.create_task(async_drive_forward(150, 720))
    arm_task = runloop.create_task(async_left_attachment_up(180, speed=400))

    # Wait for both to complete
    await drive_task
    await arm_task
```

Discussion:
- Both tasks run together because each uses `await runloop.sleep_ms(...)` inside.
- If you used the blocking versions (`drive_forward` + `left_attachment_up`), one would fully finish before the other starts.

---

## 4. Practice Variations

Field exercises:

1. **Drive forward while raising, then drive back while lowering**  

   ```python
   async def mission_drive_lift_return():
       # Forward + lift
       drive_forward_task = runloop.create_task(async_drive_forward(150, 720))
       lift_task = runloop.create_task(async_left_attachment_up(180, speed=400))
       await drive_forward_task
       await lift_task

       # Backward + lower
       drive_back_task = runloop.create_task(async_drive_backward(150, 720))
       lower_task = runloop.create_task(async_left_attachment_down(180, speed=400))
       await drive_back_task
       await lower_task
   ```

2. **Right attachment in parallel**  
   - Swap `async_left_attachment_*` for `async_right_attachment_*`.
   - Adjust degrees and speed until the timing matches what you want.

3. **Experiment with timing**  
   - Try different `target_degrees` for drive vs attachment.
   - Ask: “Do we want the arm up **before** we reach the model, or exactly when we hit it?”

Encourage students to:
- Use parallel tasks carefully and only when needed.
- Keep missions simple and predictable—test each combined action on the field before using it in a tournament run.  

---

[Back to Lessons Index](index.html)
