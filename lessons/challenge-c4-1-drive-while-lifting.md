# Challenge C4.1 – Drive While Lifting (Combined Motion)

> Environment: Spike App IDE with our FLL robot and `master.py`

## Challenge Goal

Use **async helpers** so the robot can **drive forward while raising an attachment**.

You will coordinate:

- `async_drive_forward(...)` for motion, and
- An async attachment helper for lifting during the drive.

---

## Setup

1. Choose an attachment to lift:
   - Left (`port.C`) or right (`port.B`).
2. Mark a straight path on the mat where the robot can safely drive.
3. Make sure the attachment has room to move up without hitting anything.

---

## Required Methods from `master.py`

- Driving:
  - `async_drive_forward(speed, target_degrees, kP=0.5)`
- Attachments (pick one side):
  - `async_left_attachment_up(degrees, speed=1110)`
  - `async_right_attachment_up(degrees, speed)`
- `runloop.create_task(...)` to run tasks in parallel.

---

## Step 1 – Create a Parallel Motion Mission

Example with the **left** attachment:

```python
async def mission_c4_drive_while_lifting():
    drive_degrees = 720     # how far to drive
    drive_speed = 200
    lift_degrees = 270
    lift_speed = 500

    drive_task = runloop.create_task(
        async_drive_forward(drive_speed, drive_degrees, kP=0.5)
    )
    lift_task = runloop.create_task(
        async_left_attachment_up(lift_degrees, speed=lift_speed)
    )

    # Wait for both to finish
    await drive_task
    await lift_task
    return
```

If you use the right attachment, switch to `async_right_attachment_up`.

Add this mission to `master.py` and wire it into `mission_selector`.

---

## Step 2 – Tune the Timing

On the field:

1. Start from a consistent base position.
2. Run the mission and observe:
   - Does the attachment finish lifting **before**, **during**, or **after** the drive?

Adjust:

- `drive_degrees` / `drive_speed` for drive duration.
- `lift_degrees` / `lift_speed` for lift duration.

Goal: the arm should be **mostly up by the time the robot reaches** a specific point on the mat (for example, near a model).

---

## Step 3 – Add a Return Motion (Optional)

Extend the mission to:

- Drive backward using `async_drive_backward`.
- Lower the attachment with `async_left_attachment_down` or `async_right_attachment_down`.

Use the same pattern:

```python
back_task = runloop.create_task(
    async_drive_backward(drive_speed, drive_degrees, kP=0.5)
)
down_task = runloop.create_task(
    async_left_attachment_down(lift_degrees, speed=lift_speed)
)
await back_task
await down_task
```

---

## Success Criteria

You’ve completed this challenge when:

- The robot:
  - Drives a chosen distance.
  - Raises the attachment in parallel (not one after the other).
  - Finishes in a safe position without dragging the attachment.
- Your team understands how `runloop.create_task` and `await` let multiple actions happen at the same time.

