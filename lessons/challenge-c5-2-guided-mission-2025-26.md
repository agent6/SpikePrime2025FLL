# Challenge C5.2 – Guided Mission 2025‑26 (Competition Ready)

> Environment: SPIKE App IDE, official FLL mat with the **Guided Mission 2025‑26** model, and your `master.py` helpers.

## 1. Prepare

- Read the student material for the Guided Mission in the SPIKE App.
- Build the **Driving Base with Color Sensor**.
- Build the **Guided Mission 2025‑26 model** and place it on the mat:
  - Check the Robot Game Rulebook for the correct position.
  - Make sure the model is built correctly and moves as it should.
  - Carefully apply Dual Lock so it stays in place.
- Confirm your robot wiring matches your team standard:
  - Drive motors on `port.A` and `port.E`.
  - Color sensor on the correct port for line following.

You’ll focus on **strategy, consistency, and teamwork**, not just code.

---

## 2. Engage (Discussion + Video)

Ignite a discussion using questions like:

- What is the robot doing in this mission?
- How does the robot **reach** the model?
- How does the robot **activate** the model?
- What is the ideal balance between **speed and accuracy** here?

Then have students watch the Guided Mission video in the SPIKE App so they know what they’re about to build.

---

## 3. Explore (Build and Program)

On the field:

1. Set up the Guided Mission model on the official mat.
2. Follow the SPIKE App instructions to write a program that:
   - Drives from the launch area.
   - Uses line following and/or turns to reach the model.
   - Activates the model to raise the connector.

In your `master.py`, create a new `mission_n`, for example:

Create a new `mission_n` in `master.py`, for example:

```python
async def mission_c5_guided_2025_26():
    # 1) Launch and approach the line
    # 2) Follow the line toward the Guided Mission model
    # 3) Activate the model (using an attachment or precise stop)
    # 4) Exit to a safe area
    #
    # TODO: Fill in with your team's distances, turns,
    #       and line-follow segments.
    return
```

Hook this mission into the `missions` list in `mission_selector` so you can launch it from the hub.

---

## 4. Explain (Make the Robot’s Job Clear)

Pause coding and talk about:

- Which parts of the robot are most important for triggering the model.
- How the program makes the robot:
  - Reach the model.
  - Activate it reliably (attachment, bumper, or precise stopping).

Have students describe, in words, **how their code makes the model raise the connector**.

---

## 5. Elaborate (Practice, Lines, and Strategy)

Give teams time to **practice launches**:

1. Line up the robot in base the same way every time.
2. Send it on the mission to activate the model.
3. After several runs, ask:
   - Did you notice anything important, like starting in the **left** launch area and ending in the **right**?
   - Does your path pass other missions on the way?
   - What have you learned about **following lines** that could help you reach other missions?

Encourage teams to adjust:

- Starting position and orientation.
- Line‑following gains or thresholds.
- Speeds to balance speed and accuracy.

Leave time at the end for **cleanup** of the field and models.

---

## 6. Evaluate (Rubrics and Reflection)

Use a simple observation checklist (for example: 1 = partially accomplished, 2 = fully accomplished, 3 = overachieved) and rate:

- Students worked well as a team to complete the mission.
- Students chained more than one mission in the same run (if attempted).
- Students can present their robot, program, and mission strategy.

### Self‑Assessment (Bricks)

Have each student choose a brick:

- **Blue**: I’ve successfully completed one mission.
- **Yellow**: I’ve successfully completed more than one mission.
- **Violet**: Our team presented our robot, program, and strategy, and everyone spoke.

### Peer‑Assessment

Invite students to:

- Score a teammate’s performance using the same brick scale.
- Give **constructive feedback** on how their partners can improve the next run.

---

## Differentiation Ideas

- To **simplify**:
  - Review a line‑following lesson (like a “Training Camp 3” style activity) showing color mode vs reflected light intensity.
- To **extend**:
  - Change the program to start from the **right** launch area.
  - Add another FLL mission before or after the Guided Mission in the same run.

