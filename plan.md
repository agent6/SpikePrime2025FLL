# 2025 FLL Spike Prime – Motion & Attachment Plan (v3 firmware)

This plan describes the movement and attachment API we want for our 2025 FLL Spike Prime robot (v3 firmware). It shows what exists in `mission1.py` today and what still needs to be implemented or refactored.

Status legend:
- ✅ Implemented (or easily wrapped)
- 🛠️ Needs refactor / rename
- ⏳ Not implemented yet

---

## 📌 Driving

Goal: Simple, readable functions for straight driving with encoder distance and gyro assist.

### `drive_forward()`
- Status: ✅
- Behavior:
  - Move **forward** a given distance using encoder degrees.
  - Use gyro assist to keep the robot straight (adjust left/right motor speeds based on yaw).
- Current code:
  - `drive_forward(min_speed, max_speed, target_degrees, kP=0.5)` already:
    - Uses encoder degrees for distance.
    - Uses motion sensor yaw with **proportional** correction to stay straight.
  - Plan:
    - Optionally add a thin wrapper with a simpler signature (e.g., `drive_forward(distance_degrees)`) that uses tuned default speeds and `kP`.

### `drive_backward()`
- Status: ✅
- Behavior:
  - Move **backward** a given distance using encoder degrees.
  - Use gyro assist to stay straight.
- Current code:
  - `drive_backward(min_speed, max_speed, target_degrees, kP=0.5)`:
    - Mirrors `drive_forward` but runs the motors in reverse.
    - Uses encoder degrees for distance and proportional yaw correction to stay straight.
  - Plan:
    - Tune default values for `min_speed`, `max_speed`, `target_degrees`, and `kP` for common backward moves.

---

## 📌 Pivot Turns (one motor moves)

Goal: Use clear inside/outside naming with gyro assist and one motor moving.

Turning **RIGHT**:

### `pivot_right_outside()`
- Status: ✅
- Behavior:
  - Turn right.
  - **Outside motor** moves forward; inside motor stays still.
  - Use gyro assist (target yaw angle).
- Current code:
  - `pivot_right_outside(speed, target_angle_degrees)`:
    - Resets yaw and runs the left motor on `port.A` forward while the right motor stays stopped.
    - Stops when yaw reaches `-target_angle_degrees`.
  - Plan:
    - Optionally add proportional yaw-based speed shaping if we need smoother starts/stops on outside right pivots.

### `pivot_right_inside()`
- Status: ✅
- Behavior:
  - Turn right.
  - **Inside motor** moves backward; outside motor stays still.
  - Use gyro assist.
- Current code:
  - `pivot_right_inside(speed, target_angle_degrees)`:
    - Resets yaw and runs the left motor on `port.A` backward while the right motor stays stopped.
    - Stops when yaw reaches `-target_angle_degrees`.
  - Plan:
    - Optionally add proportional yaw-based speed shaping if we need smoother starts/stops on inside pivots.

Turning **LEFT**:

### `pivot_left_outside()`
- Status: ✅
- Behavior:
  - Turn left.
  - **Outside motor** moves forward; inside motor stays still.
  - Use gyro assist.
- Current code:
  - `pivot_left_outside(speed, target_angle_degrees)`:
    - Resets yaw and runs the right motor on `port.E` forward while the left motor stays stopped.
    - Stops when yaw reaches `target_angle_degrees`.
  - Plan:
    - Optionally add proportional yaw-based speed shaping if we need smoother starts/stops on outside left pivots.

### `pivot_left_inside()`
- Status: ✅
- Behavior:
  - Turn left.
  - **Inside motor** moves backward; outside motor stays still.
  - Use gyro assist.
- Current code:
  - `pivot_left_inside(speed, target_angle_degrees)`:
    - Resets yaw and runs the right motor on `port.E` backward while the left motor stays stopped.
    - Stops when yaw reaches `target_angle_degrees`.
  - Plan:
    - Optionally add proportional yaw-based speed shaping if we need smoother starts/stops on inside left pivots.

General pivot notes:
- All current pivot functions reset yaw and spin one motor until a yaw target is reached.
- For the new API:
  - Standardize signatures: e.g., `pivot_*_*(speed, angle_degrees)`.
  - Use consistent positive angles (e.g., always pass `angle_degrees > 0` and let the function handle sign).

---

## 📌 Spin Turns (both motors move opposite directions)

Goal: In‑place spins using opposite motor directions with gyro assist.

### `spin_right()`
- Status: ✅
- Behavior:
  - Robot spins in place to the **right**.
  - Left motor moves forward, right motor moves backward.
  - Uses yaw to stop at the requested angle.
- Current code:
  - `spin_right(speed, target_angle_degrees)`:
    - Resets yaw.
    - Runs the left motor on `port.A` forward and the right motor on `port.E` backward.
    - Stops when yaw reaches `-target_angle_degrees`.
  - Plan:
    - Optionally add acceleration/deceleration shaping if needed for more precise spins.

### `spin_left()`
- Status: ✅
- Behavior:
  - Robot spins in place to the **left**.
  - Right motor moves forward, left motor moves backward.
  - Uses yaw to stop at the requested angle.
- Current code:
  - `spin_left(speed, target_angle_degrees)`:
    - Resets yaw.
    - Runs the right motor on `port.E` forward and the left motor on `port.A` backward.
    - Stops when yaw reaches `target_angle_degrees`.
  - Plan:
    - Optionally add acceleration/deceleration shaping if needed for more precise spins.

Implementation notes:
- Keep the API consistent with pivots (`speed`, `angle_degrees`).
- Use yaw to control the stopping point and allow for easy tuning of spin angles.

---

## 📌 Attachments

Goal: Simple up/down helpers for left and right attachments, using encoder degrees.

### Left Attachment

#### `left_attachment_up()`
- Status: ✅
- Behavior:
  - Moves the left attachment **up** for a given encoder distance.
- Current code:
  - `left_attachment_up(degrees, speed=1110)`:
    - Uses `motor.run_for_degrees(port.C, degrees, speed, stop=motor.BRAKE)`.
  - Plan:
    - Tune default `speed` if needed for more delicate attachments on the left side.

#### `left_attachment_down()`
- Status: ✅
- Behavior:
  - Moves the left attachment **down** for a given encoder distance.
- Current code:
  - `left_attachment_down(degrees, speed=1110)`:
    - Uses `motor.run_for_degrees(port.C, -degrees, speed, stop=motor.BRAKE)`.
    - Mirrors `left_attachment_up` but reverses the sign of `degrees` internally.
  - Plan:
    - Tune default `speed` and degree values per mission so the attachment reliably returns to home without overshooting.

### Right Attachment

#### `right_attachment_up()`
- Status: ✅
- Behavior:
  - Moves the right attachment **up** for a given encoder distance.
- Current code:
  - `right_attachment_up(degrees, speed)`:
    - Uses `motor.run_for_degrees(port.B, degrees, speed, stop=motor.BRAKE)`.
    - Corresponds to a “tower” or arm mechanism on the right side.
  - Plan:
    - Choose a good default `speed` for typical tower movements and document it in mission code.

#### `right_attachment_down()`
- Status: ✅
- Behavior:
  - Moves the right attachment **down** for a given encoder distance.
- Current code:
  - `right_attachment_down(degrees, speed)`:
    - Uses `motor.run_for_degrees(port.B, -degrees, speed, stop=motor.BRAKE)`.
    - Mirrors `right_attachment_up` but reverses the sign of `degrees` internally.
  - Plan:
    - Tune default `speed` and degree values per mission so the right attachment returns to home consistently.

General attachment notes:
- Decide and document:
  - Which ports correspond to left/right attachments (likely `port.C` and `port.B`).
  - Direction conventions for “up” and “down”.
- Expose movement in **degrees**, with:
  - Clear defaults for speed/power.
  - The option to adjust per mission.

---

## Implementation Checklist

- [x] Confirm physical motor assignments:
  - [x] Left drive motor port (currently `port.A`).
  - [x] Right drive motor port (currently `port.E`).
  - [x] Left attachment motor port (currently `port.C`).
  - [x] Right attachment motor port (currently `port.B`).
- [x] Finalize sign conventions for yaw and angles (right vs left turns).
- [x] Add `drive_forward()` and `drive_backward()` helpers using encoder distance and proportional gyro assist.
- [x] Standardize pivot functions to the `pivot_*_*(speed, angle_degrees)` API with inside/outside naming.
- [x] Add `spin_right()` and `spin_left()` using opposite motor directions and yaw‑based stopping.
- [x] Add attachment helpers:
  - [x] `left_attachment_up()` / `left_attachment_down()`
  - [x] `right_attachment_up()` / `right_attachment_down()`
- [x] Update `README.md` once APIs are implemented so team members know how to call each function in missions.

---

# Mission Selector System (SPIKE Prime Python 3)

## 📌 Goal

Create a reusable **Mission Selector** that runs automatically when the robot starts. The system will:

- Display a launch selection menu (missions **0–9**).
- Allow the user to choose a mission using buttons.
- Execute the selected mission.
- Return to the selector menu after the mission completes.
- Keep the current highlighted mission when returning.
- Provide a clear structure for adding or modifying missions.

## 📌 Key Components

1. Mission selector loop.
2. Button-based menu navigation.
3. 10 preset mission functions (`mission_0` → `mission_9`).
4. Main controller that calls mission functions and returns to the menu.
5. Optional display feedback (matrix numbers or text).

## 🧩 Behavior Overview

- On startup, `mission_selector()` loads with `current = 0`.
- LEFT button decrements selection; RIGHT increments; CENTER confirms and runs the mission.
- Selection wraps around (9 → 0 and 0 → 9).
- After a mission finishes, control returns to `mission_selector()` at the same mission number.
- The selector loop never exits; it runs until the hub is powered off.

## 🧱 Implementation Steps

1. Add 10 async mission functions (`mission_0` … `mission_9`), initially as placeholders that `return` cleanly.
2. Build an async selector loop that:
   - Tracks the current mission index.
   - Displays the current index on the light matrix.
   - Uses LEFT/RIGHT/CENTER buttons to change or confirm the selection.
3. Create a mission dispatch table:
   - `missions = [mission_0, mission_1, ..., mission_9]`
   - Call with `await missions[current]()`.
4. Use `runloop.until` for clean button press/release detection (debouncing).
5. Ensure the selector loop never exits so drivers can quickly re-run missions during practice and competition.
