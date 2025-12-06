# 2025 FLL Spike Prime Program (Firmware v3)

This project contains the Python code for our 2025 FIRST LEGO League robot running on a LEGO Spike Prime hub with **v3 firmware**. The main program for the robot is in `master.py`.

For students and mentors, a lesson site is published at:  
https://agent6.github.io/SpikePrime2025FLL/lessons/

The code is written using the Spike Python runtime (v3), `runloop`, and the built‑in motion sensor and motor APIs.

---

## Hardware Setup

- Hub: LEGO Spike Prime, firmware **v3.x**
- Drive motors:
  - `port.A` – left drive motor
  - `port.E` – right drive motor
- Mechanisms:
  - `port.C` – left attachment motor (controlled by `left_attachment_*` helpers)
  - `port.B` – right attachment motor (controlled by `right_attachment_*` helpers)
- Sensors:
  - Built‑in **motion sensor** used for yaw/tilt and pivot turns.

If you change ports on the physical robot, update the corresponding `port.X` values in `master.py`.

---

## Software Requirements

- LEGO Spike App that supports **Python with firmware v3**.
- Spike Prime hub updated to **v3 firmware**.
- Project file(s) copied to the hub as standard Python files (e.g., `master.py`).

---

## Program Structure (`master.py`)

Key imports:

- `hub`, `motion_sensor`, `light_matrix` – built‑in hub APIs.
- `motor`, `motor_pair` – control individual and paired motors.
- `port` – maps symbolic port names (`port.A`, `port.E`, etc.).
- `runloop` – async event loop used by Spike firmware v3.

Main entry point:

- `async def main()`:
  - Waits until the motion sensor is stable:  
    `await runloop.until(motion_sensor.stable)`
  - Calls the mission selector menu: `await mission_selector()`.
  - The last line of the file runs the program: `runloop.run(main())`.

---

## Movement and Utility Functions

### `drive_forward(min_speed, max_speed, target_degrees, kP=0.5)`

- Purpose: Accelerated, straight‑line drive with a soft start/stop and proportional gyro correction.
- Behavior:
  - Resets yaw and the left motor encoder.
  - Gradually accelerates from `min_speed` up to `max_speed`.
  - Maintains heading using the motion sensor yaw with **proportional** correction (steers by adjusting left/right motor commands based on yaw error).
  - Decelerates back down towards `min_speed` as it approaches the target distance.
  - Stops both drive motors with `motor.BRAKE` when the left motor has turned the requested `target_degrees`.
- Parameters:
  - `min_speed`: Starting/ending speed (low value for gentle start/stop).
  - `max_speed`: Top speed in the middle of the run.
  - `target_degrees`: Target rotation for the left drive motor (distance proxy).
  - `kP`: Proportional gain for gyro correction (default `0.5`).

### `drive_backward(min_speed, max_speed, target_degrees, kP=0.5)`

- Purpose: Accelerated, straight‑line drive **backwards** with proportional gyro correction.
- Behavior:
  - Resets yaw and the left motor encoder.
  - Gradually accelerates from `min_speed` up to `max_speed` while driving backward.
  - Uses the same proportional yaw correction pattern to keep the robot straight.
  - Decelerates back to `min_speed` and stops once the left motor has rotated `target_degrees` backwards.
- Parameters:
  - Same as `drive_forward`: `min_speed`, `max_speed`, `target_degrees`, and optional `kP`.

### Pivot Turn Functions

All pivot functions reset yaw at the start and then spin a single drive motor until the desired yaw (in degrees) is reached, then brake the motor.

- `pivot_left_outside(speed, target_angle_degrees)`
  - Uses the **outside** wheel to turn **left**.
  - Spins the right motor on `port.E` forward while the left motor stays stopped.
  - Stops when yaw reaches `target_angle_degrees`.

- `pivot_right_outside(speed, target_angle_degrees)`
  - Uses the **outside** wheel to turn **right**.
  - Spins the left motor on `port.A` forward while the right motor stays stopped.
  - Stops when yaw reaches `-target_angle_degrees`.

- `pivot_right_inside(speed, target_angle_degrees)`
  - Uses the **inside** wheel to turn **right**.
  - Spins the left motor on `port.A` backward while the right motor stays stopped.
  - Stops when yaw reaches `-target_angle_degrees`.

- `pivot_left_inside(speed, target_angle_degrees)`
  - Uses the **inside** wheel to turn **left**.
  - Spins the right motor on `port.E` backward while the left motor stays stopped.
  - Stops when yaw reaches `target_angle_degrees`.

### Spin Turn Functions

- `spin_right(speed, target_angle_degrees)`
  - Spins the robot in place to the **right**.
  - Uses opposite wheel directions (relative to forward drive) to rotate around the center.
  - Stops when yaw reaches `-target_angle_degrees`.

- `spin_left(speed, target_angle_degrees)`
  - Spins the robot in place to the **left**.
  - Uses opposite wheel directions (relative to forward drive) to rotate around the center.
  - Stops when yaw reaches `target_angle_degrees`.

### Mechanism Functions

- `left_attachment_up(degrees, speed=1110)`
  - Runs the left attachment motor on `port.C` for `degrees` encoder degrees at the given `speed` (default matches legacy behavior).
  - Uses `motor.BRAKE` when finished.
  - Typical use: raising/lowering an elevator or left-side attachment.

- `left_attachment_down(degrees, speed=1110)`
  - Moves the left attachment motor on `port.C` in the **down** direction using encoder feedback.
  - Uses a loop and negative speed to reverse the motion until the requested degrees are reached.
  - Typical use: returning a left-side attachment to its starting (home) position.

- `right_attachment_up(degrees, speed)`
  - Runs the right attachment motor on `port.B` for `degrees` encoder degrees at the given `speed`.
  - Uses `motor.BRAKE` when finished.
  - Typical use: raising or rotating a right-side tower/attachment.

- `right_attachment_down(degrees, speed)`
  - Moves the right attachment motor on `port.B` in the **down** direction using encoder feedback.
  - Uses a loop and negative speed to reverse the motion until the requested degrees are reached.
  - Typical use: lowering or returning a right-side tower/attachment to its starting position.

---

## Using the Program on the Robot

1. **Update firmware**
   - Connect the Spike Prime hub to the LEGO Spike App.
   - Make sure the hub is updated to firmware **v3.x**.

2. **Create/import the project**
   - Open the Spike App and create a **Python** project.
   - Copy the contents of `master.py` into the project or transfer the file directly if your environment allows it.

3. **Connect the motors and check ports**
   - Plug the drive motors into `port.A` and `port.E`.
   - Plug mechanism motors into `port.B` and `port.C` as documented above.
   - Adjust port assignments in `mission1.py` if your build uses different ports.

4. **Run the program**
   - Place the robot on the field in the correct starting position.
   - Start the `master` program on the hub.
   - The robot will wait for the motion sensor to be stable, then enter the **mission selector**:
     - The selected mission number (0–9) is shown on the light matrix.
     - The top-left LED is lit to indicate selector mode.
     - RIGHT button: move to the next mission number.
     - LEFT button: run the currently selected mission.

---

## Customizing for Missions

- To change what a **mission number** does:
  - Edit the corresponding `mission_n` function in `master.py` (e.g., `mission_4`).
  - Chain helpers to build a full run, e.g.:  
    `drive_forward(...)` → `pivot_left_outside(...)` → `left_attachment_up(...)` → `drive_backward(...)` → `left_attachment_down(...)`.

- To tune **turn angles**:
  - Adjust the `target_angle_degrees` parameter in any pivot or spin function call (`pivot_left_outside`, `pivot_left_inside`, `pivot_right_outside`, `pivot_right_inside`, `spin_left`, `spin_right`).
  - Test on the field and refine the degree values until the robot consistently hits/aligns with FLL models.

- To adjust **mechanism movement**:
  - Change `degrees` and `speed` values in calls to `left_attachment_up/down` and `right_attachment_up/down`.
  - Use `MotorIsStopped(port.C)` or `MotorIsStopped(port.B)` with `runloop.until` when you need to wait for an attachment to finish moving.

Keep notes of which parameter sets correspond to specific FLL missions so you can quickly restore working runs during tournaments.

---

## Safety and Reliability Notes

- Always test new parameter changes **off the competition field** first.
- Make sure cables are firmly connected to the documented ports before running.
- Re‑calibrate / re‑zero the robot’s position consistently between runs to keep motion sensor–based turns accurate.
