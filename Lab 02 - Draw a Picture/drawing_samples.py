"""
Hopefully this will look like a marshmallow being roasted over a fire.
Let's see how this goes...
"""

# Import the Arcade library
import arcade

# Open a Window
arcade.open_window(800, 600, "CAMPFIRE")

# Set the Background Color
arcade.set_background_color(arcade.color.BLACK)

# Get ready to draw
arcade.start_render()

# Draw the Grass
arcade.draw_lrtb_rectangle_filled(0, 800, 400, 0, arcade.color.DARK_GREEN)

# --- Draw the Fire ---

# The Log
arcade.draw_lrtb_rectangle_filled(200, 600, 50, 0, arcade.color.DARK_BROWN)
arcade.draw_line(200, 45, 250, 45, arcade.color.BLACK)
arcade.draw_line(225, 35, 425, 35, arcade.color.BLACK)
arcade.draw_line(250, 20, 357, 20, arcade.color.BLACK)
arcade.draw_line(300, 40, 500, 40, arcade.color.BLACK)
arcade.draw_line(287, 28, 596, 28, arcade.color.BLACK)
arcade.draw_line(350, 15, 469, 15, arcade.color.BLACK)
arcade.draw_line(200, 5, 600, 5, arcade.color.BLACK)

# The Fire
arcade.draw_triangle_filled(225, 50, 575, 50, 400, 300, arcade.color.ORANGE_RED)
arcade.draw_triangle_filled(275, 50, 525, 50, 400, 250, arcade.color.YELLOW)
arcade.draw_triangle_filled(325, 50, 475, 50, 400, 200, arcade.color.RED)

# The Marshmallow
arcade.draw_ellipse_filled(475, 410, 150, 86, arcade.color.WHITE)
arcade.draw_ellipse_filled(476, 394.2, 138, 54, arcade.color.LIGHT_BROWN)

# Roasting Stick
arcade.draw_lrtb_rectangle_filled(550, 800, 415, 405, arcade.color.GRAY)

# The Moon
arcade.draw_circle_filled(0, 600, 150, arcade.color.LIGHT_BLUE)

# Stars
arcade.draw_circle_filled(150, 450, 5, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(225, 500, 5, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(275, 550, 5, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(200, 425, 5, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(350, 575, 5, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(644, 478, 5, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(365, 513, 5, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(296, 568, 5, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(500, 597, 5, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(730, 516, 5, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(437, 576, 5, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(727, 583, 5, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(636, 448, 5, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(797, 522, 5, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(542, 503, 5, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(594, 564, 5, arcade.color.LIGHT_BLUE)

# --- Finish Drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()

