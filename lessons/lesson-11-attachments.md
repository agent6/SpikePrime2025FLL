# Lesson 11 – Attachments (Left & Right)

> Environment: Spike App IDE with our FLL robot and `master.py`  
> API reference: <https://tuftsceeo.github.io/SPIKEPythonDocs/SPIKE3.html>

## Lesson Goals

By the end of this lesson, students will be able to:
- Use the left attachment helpers: `left_attachment_up` and `left_attachment_down`.
- Use the right attachment helpers: `right_attachment_up` and `right_attachment_down`.
- Explain how **encoder degrees** give repeatable attachment positions.
- Run a practice mission: hit a model, then safely return the attachment “home”.

---

## 1. Attachment Helpers in `master.py`

Open `master.py` and locate:

```python
def left_attachment_up(degrees, speed=1110):
    ...

def left_attachment_down(degrees, speed=1110):
    ...

def right_attachment_up(degrees, speed):
    ...

def right_attachment_down(degrees, speed):
    ...
```

Port mapping reminder:
- `port.C` – left attachment motor
- `port.B` – right attachment motor

Explain:
- “Up” raises or actuates the mechanism.
- “Down” returns it toward its starting/home position.

---

## 2. Encoder Degrees and Repeatable Positions

Attach a simple arm to each attachment motor (or point to your existing mechanisms).

Explain:
- Motors have encoders that measure **degrees turned** since last reset.
- Running for the same number of degrees each time → **repeatable motion**.

Example behavior (simplified):

```python
left_attachment_up(180, speed=400)    # move up ~half turn
left_attachment_down(180, speed=400)  # move back down ~half turn
```

Activity:
- Mark the attachment’s “home” position with tape.
- Run `left_attachment_up` once.
- Run `left_attachment_down` and check if it returns to the tape mark.
- Adjust `degrees` until it reliably hits the same positions.

---

## 3. Simple Attachment Test Missions

Use or create missions that call the helpers directly, e.g.:

```python
async def mission_left_attachment_test():
    left_attachment_up(180, speed=400)
    await runloop.until(lambda: MotorIsStopped(port.C))
    left_attachment_down(180, speed=400)

async def mission_right_attachment_test():
    right_attachment_up(180, speed=400)
    await runloop.until(lambda: MotorIsStopped(port.B))
    right_attachment_down(180, speed=400)
```

Run these on the robot:
- Watch the arm go out and back.
- Confirm that each cycle returns to roughly the same home position.

---

## 4. Practice – Hit a Model, Then Return Home

On the FLL field:
1. Choose a simple model (or a block/target) in base.
2. Position the robot so an attachment can **reach** the model.

Design a short mission:

```python
async def mission_hit_model():
    # Drive into position (tune these values on the field)
    drive_forward(20, 250, 360)

    # Hit or lift the model with an attachment
    left_attachment_up(180, speed=400)
    await runloop.until(lambda: MotorIsStopped(port.C))

    # Back away and return the attachment home
    drive_backward(20, 250, 360)
    left_attachment_down(180, speed=400)
```

Field activity:
- Start from a consistent base position.
- Run the mission and see if:
  - The attachment reliably reaches and hits/lifts the model.
  - The robot backs away without snagging.
  - The attachment returns to a safe home position.

Adjust:
- Attachment **degrees** for up/down until you get good contact without jamming.
- Drive distances so you approach and leave the model cleanly.

Encourage students to:
- Record working values (degrees and speeds) per mission.
- Use comments in `master.py` or a notebook to label which attachment positions correspond to which models.  

---


