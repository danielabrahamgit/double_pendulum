import arcade
import numpy as np

# Graphics constants
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE  = "Double Pendulum"
FPS = 60

# Physics vairables
theta1 = 0
theta2 = 0
omega1 = 0
omega2 = 0
alpha1 = 0
alpha2 = 0

# Built in arcade function that is called every _delta_time seconds.
def draw(_delta_time):
    arcade.start_render()
    arcade.draw_line(SCREEN_WIDTH//2,SCREEN_HEIGHT//2, SCREEN_WIDTH//2 + 20,SCREEN_HEIGHT//2 + 20 , arcade.color.BLACK, 1)

# Main function that will get taken over by draw right after .run()
def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.GRAY)
    arcade.schedule(draw, 1 / FPS)
    arcade.run()
    arcade.close_window()

if __name__ == "__main__":
    main()