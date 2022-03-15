import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3


def draw_grass():
    """Draw the Ground."""
    arcade.draw_lrtb_rectangle_filled(0, 800, 400, 0, arcade.color.DARK_GREEN)


def draw_campfire():
    """Draw the camp fire."""
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


def draw_sky():
    """Draw the sky"""
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


def draw_cloud():
    arcade.draw_circle_filled(150, 515, 15, arcade.color.GRAY_BLUE)
    arcade.draw_circle_filled(170, 500, 20, arcade.color.GRAY_BLUE)
    arcade.draw_circle_filled(190, 500, 18, arcade.color.GRAY_BLUE)
    arcade.draw_circle_filled(210, 510, 25, arcade.color.GRAY_BLUE)
    arcade.draw_circle_filled(210, 530, 20, arcade.color.GRAY_BLUE)
    arcade.draw_circle_filled(170, 515, 30, arcade.color.GRAY_BLUE)
    arcade.draw_circle_filled(140, 490, 20, arcade.color.GRAY_BLUE)


def ufo():
    arcade.draw_circle_filled(0, 600, 100, arcade.color.GRAY)
    arcade.draw_circle_filled(0, 600, 75, arcade.color.DARK_BLUE)
    arcade.draw_circle_filled(0, 600, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(0, 600, 25, arcade.color.GRAY_BLUE)


def draw_marshmallow():
    """Draw the marshmallow."""

    # The Marshmallow
    arcade.draw_ellipse_filled(475, 410, 150, 86, arcade.color.WHITE)
    arcade.draw_ellipse_filled(476, 396.2, 138, 54, arcade.color.LIGHT_BROWN)


class Marshmallow:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y

    def draw(self):
        arcade.draw_ellipse_filled(self.position_x,
                                   self.position_y,
                                   150,
                                   86,
                                   arcade.color.WHITE)

        arcade.draw_ellipse_filled(self.position_x,
                                   self.position_y,
                                   138,
                                   54,
                                   arcade.color.LIGHT_BROWN)


class Ufo:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

        self.laser_sound = arcade.load_sound("laser.wav")

    def draw(self):
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  100,
                                  arcade.color.GRAY)

        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  75,
                                  arcade.color.DARK_BLUE)

        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  50,
                                  arcade.color.WHITE)

        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  25,
                                  arcade.color.GRAY_BLUE)

    def update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < self.radius:
            self.position_x = self.radius
            arcade.play_sound(self.laser_sound)

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
            arcade.play_sound(self.laser_sound)

        if self.position_y < self.radius:
            self.position_y = self.radius
            arcade.play_sound(self.laser_sound)

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
            arcade.play_sound(self.laser_sound)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7-User Control")
        self.set_mouse_visible(False)
        self.laser_sound = arcade.load_sound("laser.wav")
        self.coin_sound = arcade.load_sound("coin5.wav")

        self.marshmallow = Marshmallow(400, 300)
        self.ufo = Ufo(675, 475, 0, 0, 100, arcade.color.LIGHT_BLUE)

    def on_draw(self):
        arcade.start_render()
        draw_grass()
        draw_campfire()
        draw_sky()
        self.marshmallow.draw()
        draw_cloud()
        self.ufo.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.marshmallow.position_x = x
        self.marshmallow.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.coin_sound)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            arcade.play_sound(self.coin_sound)

    def update(self, delta_time):
        self.ufo.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.ufo.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ufo.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ufo.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ufo.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ufo.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ufo.change_y = 0


def main():
    window = MyGame()
    arcade.run()


main()
