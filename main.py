import sys
import arcade
import numpy as np

# Graphics constants
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE  = "Double Pendulum"
FPS = 60

# Makes life a little easier
sin = np.sin
cos = np.cos
PI = np.pi

# Physics vairables
state1 = [
    0,          # theta (angle)
    0           # omega (angular velocity)
]
state2 = [
    0,          # theta (angle)
    0           # omega (angular velocity)
]

# Physics constants
phys_const = [
    1,          # mass 1
    1,          # mass 2
    10,         # radius 1
    10,         # radius 2
    200,        # length 1
    150,        # length 2
    0.5         # gravity
]


# This is the large phsyics equation that gets alpha1 and alpha2
def get_angular_accel(theta1, theta2, omega1, omega2):
    global phys_const
    # unpack physics constants
    m1, m2, _, _, l1, l2, g = phys_const

    # common denomenator
    denom = (2 * m1 + m2 - m2 * cos(2 * theta1 - 2 * theta2))
    # mega equation for alpha1
    a1 = (-g * (2 * m1 + m2) * sin(theta1)) - (m2 * g * sin(theta1 - 2*theta2))
    a1 -= 2 * sin(theta1 - theta2) * m2 * ((l2 * omega2 ** 2) + (l1 * cos(theta1 - theta2) * omega1 ** 2))
    a1 /= l1 * denom
    # mega equation for alpha2
    a2 = 2 * sin(theta1 - theta2) * ((l1 * (m1 + m2) * omega1 ** 2) + (g * (m1 + m2) * cos(theta1)) + \
    (cos(theta1 - theta2) * m2 * l2 * omega2 ** 2))
    a2 /= l2 * denom

    return a1, a2

def update_and_draw():
    global state1, state2, phys_const

    # Unpack physics constants
    r1, r2, l1, l2 = phys_const[2:-1]
    # Unpack physics variables
    theta1, omega1 = state1
    theta2, omega2 = state2

    # Calculate new accelerations
    alpha1_new, alpha2_new = get_angular_accel(theta1, theta2, omega1, omega2)

    # update anuglar velocities
    state1[1] += alpha1_new
    state2[1] += alpha2_new

    # update angular positions
    state1[0] += state1[1]
    state2[0] += state2[1]

    # Nice names :)
    theta1 = state1[0]
    theta2 = state2[0]

    # Defines "hinge" or center
    center = np.array([SCREEN_WIDTH//2, 2 * SCREEN_HEIGHT//3])

    # Draw first pendulum
    pend1 = center - l1 * np.array([sin(theta1), cos(theta1)])
    arcade.draw_line(center[0], center[1], pend1[0], pend1[1], arcade.color.BLACK)
    arcade.draw_circle_filled(pend1[0], pend1[1], r1, arcade.color.BLACK)

    # Draw second pendulum
    pend2 = pend1 - l2 * np.array([sin(theta2), cos(theta2)])
    arcade.draw_line(pend1[0], pend1[1], pend2[0], pend2[1], arcade.color.BLACK)
    arcade.draw_circle_filled(pend2[0], pend2[1], r2, arcade.color.BLACK)
    


# Built in arcade function that is called every _delta_time seconds.
def draw(_delta_time):
    global state1, state2
    arcade.start_render()

    update_and_draw()

# Main function that will get taken over by draw right after .run()
def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.GRAY)
    arcade.schedule(draw, 1 / FPS)
    arcade.run()
    arcade.close_window()

if __name__ == "__main__":
    assert len(sys.argv) == 3
    state1[0] = float(sys.argv[1])
    state2[0] = float(sys.argv[2])
    main()