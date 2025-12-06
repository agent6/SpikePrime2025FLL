import hub, sys, time
from hub import light_matrix
from hub import motion_sensor
from hub import button
import motor_pair
import motor
from hub import port
import runloop

motor.BRAKE

#Define Systems

#Functions go here:


def drive_forward(min_speed, max_speed, target_degrees, kP=0.5):
    """
    Accelerate to max_speed, hold, then decelerate back to min_speed
    while using proportional gyro correction to stay on heading.
    """
    ACCELERATE = 1
    CRUISE = 2
    DECELERATE = 3
    FINISH = 4

    motion_sensor.reset_yaw(0)

    left_speed = min_speed
    right_speed = min_speed
    phase = ACCELERATE
    speed_step_counter = 1
    accel_degrees = 0

    motor.reset_relative_position(port.A, 0)

    while True:
        distance_travelled = -1 * motor.relative_position(port.A)

        if phase == ACCELERATE:
            speed_step_counter += 1
            if speed_step_counter == 4:
                right_speed += 1
                left_speed += 1
                speed_step_counter = 1

            if distance_travelled >= (target_degrees / 2):
                print("Skipping max speed, start decel")
                phase = DECELERATE

            if left_speed >= max_speed:
                phase = CRUISE
                right_speed = max_speed
                left_speed = max_speed
                accel_degrees = distance_travelled
                print("Accel distance ", accel_degrees)

        elif phase == CRUISE:
            if distance_travelled >= (target_degrees - (2 * accel_degrees)):
                phase = DECELERATE
                print("Start decel")

        elif phase == DECELERATE:
            if speed_step_counter == 4:
                right_speed -= 1
                left_speed -= 1
                speed_step_counter = 1
                print("Decel speed ", right_speed)
            speed_step_counter += 1
            if left_speed <= min_speed:
                left_speed = min_speed
                right_speed = min_speed
                phase = FINISH

        if phase == FINISH:
            left_speed = min_speed
            right_speed = min_speed

        yaw = motion_sensor.tilt_angles()[0]
        correction = int(kP * yaw)

        left_command = left_speed + correction
        right_command = right_speed - correction

        max_command = max_speed
        if left_command > max_command:
            left_command = max_command
        if left_command < -max_command:
            left_command = -max_command
        if right_command > max_command:
            right_command = max_command
        if right_command < -max_command:
            right_command = -max_command

        motor.run(port.A, -1 * left_command)
        motor.run(port.E, right_command)

        if distance_travelled >= target_degrees:
            motor.stop(port.A, stop=motor.BRAKE)
            motor.stop(port.E, stop=motor.BRAKE)
            return False


def drive_backward(min_speed, max_speed, target_degrees, kP=0.5):
    """
    Accelerate to max_speed, hold, then decelerate back to min_speed
    while driving backward, using proportional gyro correction to stay on heading.
    """
    ACCELERATE = 1
    CRUISE = 2
    DECELERATE = 3
    FINISH = 4

    motion_sensor.reset_yaw(0)

    left_speed = min_speed
    right_speed = min_speed
    phase = ACCELERATE
    speed_step_counter = 1
    accel_degrees = 0

    motor.reset_relative_position(port.A, 0)

    while True:
        distance_travelled = motor.relative_position(port.A)

        if phase == ACCELERATE:
            speed_step_counter += 1
            if speed_step_counter == 4:
                right_speed += 1
                left_speed += 1
                speed_step_counter = 1

            if distance_travelled >= (target_degrees / 2):
                print("Backward: skipping max speed, start decel")
                phase = DECELERATE

            if left_speed >= max_speed:
                phase = CRUISE
                right_speed = max_speed
                left_speed = max_speed
                accel_degrees = distance_travelled
                print("Backward accel distance ", accel_degrees)

        elif phase == CRUISE:
            if distance_travelled >= (target_degrees - (2 * accel_degrees)):
                phase = DECELERATE
                print("Backward start decel")

        elif phase == DECELERATE:
            if speed_step_counter == 4:
                right_speed -= 1
                left_speed -= 1
                speed_step_counter = 1
                print("Backward decel speed ", right_speed)
            speed_step_counter += 1
            if left_speed <= min_speed:
                left_speed = min_speed
                right_speed = min_speed
                phase = FINISH

        if phase == FINISH:
            left_speed = min_speed
            right_speed = min_speed

        yaw = motion_sensor.tilt_angles()[0]
        correction = int(kP * yaw)

        left_command = left_speed + correction
        right_command = right_speed - correction

        max_command = max_speed
        if left_command > max_command:
            left_command = max_command
        if left_command < -max_command:
            left_command = -max_command
        if right_command > max_command:
            right_command = max_command
        if right_command < -max_command:
            right_command = -max_command

        # Backward drive: reverse base directions compared to drive_forward
        motor.run(port.A, left_command)
        motor.run(port.E, -1 * right_command)

        if distance_travelled >= target_degrees:
            motor.stop(port.A, stop=motor.BRAKE)
            motor.stop(port.E, stop=motor.BRAKE)
            return False


def pivot_right_outside(speed, target_angle_degrees):
    """
    Pivot turn to the RIGHT using the outside wheel.

    Right turn, outside wheel moves FORWARD:
    - Left motor (port.A) is the outside wheel and moves forward.
    - Right motor (port.E) stays stopped.
    The motion sensor yaw is used as the angle reference.
    """
    motion_sensor.reset_yaw(0)

    while motion_sensor.tilt_angles()[0] > -target_angle_degrees:
        motor.run(port.A, speed)

    motor.stop(port.A, stop=motor.BRAKE)


def pivot_left_outside(speed, target_angle_degrees):
    """
    Pivot turn to the LEFT using the outside wheel.

    Left turn, outside wheel moves FORWARD:
    - Right motor (port.E) is the outside wheel and moves forward.
    - Left motor (port.A) stays stopped.
    The motion sensor yaw is used as the angle reference.
    """
    motion_sensor.reset_yaw(0)

    while motion_sensor.tilt_angles()[0] < target_angle_degrees:
        motor.run(port.E, speed)

    motor.stop(port.E, stop=motor.BRAKE)

def pivot_right_inside(speed, target_angle_degrees):
    """
    Pivot turn to the RIGHT using the inside wheel.

    Right turn, inside wheel moves BACKWARD:
    - Left motor (port.A) is the inside wheel and moves backward.
    - Right motor (port.E) stays stopped.
    The motion sensor yaw is used as the angle reference.
    """
    motion_sensor.reset_yaw(0)

    while motion_sensor.tilt_angles()[0] > -target_angle_degrees:
        motor.run(port.A, -speed)

    motor.stop(port.A, stop=motor.BRAKE)


def pivot_left_inside(speed, target_angle_degrees):
    """
    Pivot turn to the LEFT using the inside wheel.

    Left turn, inside wheel moves BACKWARD:
    - Right motor (port.E) is treated as the inside wheel and moves backward.
    - Left motor (port.A) stays stopped.
    The motion sensor yaw is used as the angle reference.
    """
    motion_sensor.reset_yaw(0)

    while motion_sensor.tilt_angles()[0] < target_angle_degrees:
        motor.run(port.E, -speed)

    motor.stop(port.E, stop=motor.BRAKE)


def spin_right(speed, target_angle_degrees):
    """
    In-place spin to the RIGHT using opposite wheel directions.

    - Left motor (port.A) runs forward.
    - Right motor (port.E) runs backward.
    - Stops when yaw reaches -target_angle_degrees.
    """
    motion_sensor.reset_yaw(0)

    while motion_sensor.tilt_angles()[0] > -target_angle_degrees:
        # Forward on left, backward on right (relative to drive_forward)
        motor.run(port.A, -speed)
        motor.run(port.E, -speed)

    motor.stop(port.A, stop=motor.BRAKE)
    motor.stop(port.E, stop=motor.BRAKE)


def spin_left(speed, target_angle_degrees):
    """
    In-place spin to the LEFT using opposite wheel directions.

    - Right motor (port.E) runs forward.
    - Left motor (port.A) runs backward.
    - Stops when yaw reaches target_angle_degrees.
    """
    motion_sensor.reset_yaw(0)

    while motion_sensor.tilt_angles()[0] < target_angle_degrees:
        # Backward on left, forward on right (relative to drive_forward)
        motor.run(port.A, speed)
        motor.run(port.E, speed)

    motor.stop(port.A, stop=motor.BRAKE)
    motor.stop(port.E, stop=motor.BRAKE)

def left_attachment_up(degrees, speed=1110):
    """
    Move the left attachment UP for a given encoder distance.

    - Left attachment motor is on port.C.
    - Positive degrees values move the mechanism up.
    """
    motor.run_for_degrees(port.C, degrees, speed, stop=motor.BRAKE)


def left_attachment_down(degrees, speed=1110):
    """
    Move the left attachment DOWN for a given encoder distance.

    - Left attachment motor is on port.C.
    - Positive degrees values command a downward move.
    """
    motor.reset_relative_position(port.C, 0)
    while -motor.relative_position(port.C) < degrees:
        motor.run(port.C, -speed)
    motor.stop(port.C, stop=motor.BRAKE)

def right_attachment_up(degrees, speed):
    """
    Move the right attachment UP for a given encoder distance.

    - Right attachment motor is on port.B.
    - Positive degrees values move the mechanism up.
    """
    motor.run_for_degrees(port.B, degrees, speed, stop=motor.BRAKE)


def right_attachment_down(degrees, speed):
    """
    Move the right attachment DOWN for a given encoder distance.

    - Right attachment motor is on port.B.
    - Positive degrees values command a downward move.
    """
    motor.reset_relative_position(port.B, 0)
    while -motor.relative_position(port.B) < degrees:
        motor.run(port.B, -speed)
    motor.stop(port.B, stop=motor.BRAKE)


def MotorIsStopped(motor_port, samples=100):
    """
    Return True if the motor on the given port appears stopped.

    Waits a short time, then keeps checking the encoder position.
    Once the position stops changing, returns True.
    """
    first_position = motor.relative_position(motor_port)
    print("MotorIsStopped start:", motor_port, "first_position:", first_position)

    # Initial wait so we do not immediately report "stopped"
    time.sleep(0.25)

    while True:
        current = motor.relative_position(motor_port)
        print("MotorIsStopped sample:", motor_port, "current:", current)
        if current == first_position:
            print("MotorIsStopped:", motor_port, "-> True")
            return True
        # Update reference and delay before next check
        first_position = current
        time.sleep(0.01)


# Async helpers for running driving and attachments in parallel.

async def async_drive_forward(speed, target_degrees, kP=0.5):
    """
    Simple forward drive with proportional gyro correction that can run in parallel
    with other async tasks (attachments, etc.).
    """
    motion_sensor.reset_yaw(0)
    motor.reset_relative_position(port.A, 0)

    while True:
        distance = -motor.relative_position(port.A)
        if distance >= target_degrees:
            motor.stop(port.A, stop=motor.BRAKE)
            motor.stop(port.E, stop=motor.BRAKE)
            return

        yaw = motion_sensor.tilt_angles()[0]
        correction = int(kP * yaw)

        left_command = speed + correction
        right_command = speed - correction

        motor.run(port.A, -left_command)
        motor.run(port.E, right_command)

        await runloop.sleep_ms(10)


async def async_drive_backward(speed, target_degrees, kP=0.5):
    """
    Simple backward drive with proportional gyro correction that can run in parallel
    with other async tasks.
    """
    motion_sensor.reset_yaw(0)
    motor.reset_relative_position(port.A, 0)

    while True:
        distance = motor.relative_position(port.A)
        if distance >= target_degrees:
            motor.stop(port.A, stop=motor.BRAKE)
            motor.stop(port.E, stop=motor.BRAKE)
            return

        yaw = motion_sensor.tilt_angles()[0]
        correction = int(kP * yaw)

        left_command = speed + correction
        right_command = speed - correction

        motor.run(port.A, left_command)
        motor.run(port.E, -right_command)

        await runloop.sleep_ms(10)


async def async_left_attachment_up(degrees, speed=1110):
    """
    Move the left attachment up in a non-blocking way for use in parallel tasks.
    """
    motor.reset_relative_position(port.C, 0)

    while motor.relative_position(port.C) < degrees:
        motor.run(port.C, speed)
        await runloop.sleep_ms(10)

    motor.stop(port.C, stop=motor.BRAKE)


async def async_left_attachment_down(degrees, speed=1110):
    """
    Move the left attachment down in a non-blocking way for use in parallel tasks.
    """
    motor.reset_relative_position(port.C, 0)

    while -motor.relative_position(port.C) < degrees:
        motor.run(port.C, -speed)
        await runloop.sleep_ms(10)

    motor.stop(port.C, stop=motor.BRAKE)


async def async_right_attachment_up(degrees, speed):
    """
    Move the right attachment up in a non-blocking way for use in parallel tasks.
    """
    motor.reset_relative_position(port.B, 0)

    while motor.relative_position(port.B) < degrees:
        motor.run(port.B, speed)
        await runloop.sleep_ms(10)

    motor.stop(port.B, stop=motor.BRAKE)


async def async_right_attachment_down(degrees, speed):
    """
    Move the right attachment down in a non-blocking way for use in parallel tasks.
    """
    motor.reset_relative_position(port.B, 0)

    while -motor.relative_position(port.B) < degrees:
        motor.run(port.B, -speed)
        await runloop.sleep_ms(10)

    motor.stop(port.B, stop=motor.BRAKE)

async def mission_0():
    """
    Mission 0: test forward drive.
    """
    drive_forward(20, 200, 360)
    return


async def mission_1():
    """
    Mission 1: test backward drive.
    """
    drive_backward(20, 200, 360)
    return


async def mission_2():
    """
    Mission 2: test left outside pivot.
    """
    pivot_left_outside(200, 45)
    return


async def mission_3():
    """
    Mission 3: test left inside pivot.
    """
    pivot_left_inside(200, 45)
    return


async def mission_4():
    """
    Mission 4: test right outside pivot.
    """
    pivot_right_outside(200, 45)
    return


async def mission_5():
    """
    Mission 5: test right inside pivot.
    """
    pivot_right_inside(200, 45)
    return


async def mission_6():
    """
    Mission 6: test left spin.
    """
    spin_left(200, 90)
    return


async def mission_7():
    """
    Mission 7: test right spin.
    """
    spin_right(200, 90)
    return


async def mission_8():
    """
    Mission 8: test left attachment up and down.
    """
    left_attachment_up(180, speed=400)
    await runloop.until(lambda: MotorIsStopped(port.C))
    left_attachment_down(180, speed=400)
    return


async def mission_9():
    """
    Mission 9: test right attachment up and down.
    """
    right_attachment_up(180, speed=400)
    await runloop.until(lambda: MotorIsStopped(port.B))
    right_attachment_down(180, speed=400)
    return


async def mission_selector():
    """
    Mission selector menu.

    Uses LEFT/RIGHT/CENTER buttons to select and run missions 0–9.
    The selector loop never exits.
    """
    current = 0
    missions = [
        mission_0,
        mission_1,
        mission_2,
        mission_3,
        mission_4,
        mission_5,
        mission_6,
        mission_7,
        mission_8,
        mission_9,
    ]

    while True:
        # Show current mission number and mark selector mode with top-left LED.
        light_matrix.write(str(current))
        light_matrix.set_pixel(0, 0, 100)

        # Wait for LEFT or RIGHT button press
        await runloop.until(
            lambda: button.pressed(button.LEFT)
            or button.pressed(button.RIGHT)
        )

        # RIGHT moves to next mission, LEFT runs the current mission
        if button.pressed(button.RIGHT):
            current = (current + 1) % len(missions)
        elif button.pressed(button.LEFT):
            await missions[current]()

        # Wait for all buttons to be released (debounce)
        await runloop.until(
            lambda: not (
                button.pressed(button.LEFT)
                or button.pressed(button.RIGHT)
            )
        )


async def main():
    await runloop.until(motion_sensor.stable)
    await mission_selector()


runloop.run(main())
