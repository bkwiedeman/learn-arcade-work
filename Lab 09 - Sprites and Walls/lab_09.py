"""
Artwork from https://kenney.nl
"""

from pyglet.math import Vec2
import arcade
import random


SPRITE_SCALING = 0.5
SPRITE_SCALING_PARTS = 0.8

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"
VIEWPORT_MARGIN = 220
CAMERA_SPEED = 0.1
PLAYER_MOVEMENT_SPEED = 7
NUMBER_OF_PARTS = 75


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.parts_list = None
        self.upgrade_sound = arcade.load_sound("upgrade.wav")

        # Set up the player
        self.player_sprite = None
        self.score = 0

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.parts_list = arcade.SpriteList()
        self.score = 0

        # Set up the player
        self.player_sprite = arcade.Sprite("spaceAstronauts_004.png",
                                           scale=1)
        self.player_sprite.center_x = 256
        self.player_sprite.center_y = 512
        self.player_list.append(self.player_sprite)

        # walls
        for x in range(0, 2000, 42):
            wall = arcade.Sprite("spaceBuilding_001.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 0
            self.wall_list.append(wall)

        for x in range(0, 2000, 42):
            wall = arcade.Sprite("spaceBuilding_001.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 2000
            self.wall_list.append(wall)

        for y in range(0, 2000, 42):
            wall = arcade.Sprite("spaceBuilding_001.png", SPRITE_SCALING)
            wall.center_x = 0
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(0, 2000, 42):
            wall = arcade.Sprite("spaceBuilding_001.png", SPRITE_SCALING)
            wall.center_x = 2000
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(64, 1000, 64):
            for y in range(64, 1000, 64):
                wall = arcade.Sprite("spaceBuilding_007.png", SPRITE_SCALING)
                wall.center_x = random.randrange(64, 1936)
                wall.center_y = random.randrange(64, 1936)
                self.wall_list.append(wall)

        for i in range(NUMBER_OF_PARTS):
            parts = arcade.Sprite("spaceParts_069.png", SPRITE_SCALING_PARTS)
            parts_placed_successfully = False

            while not parts_placed_successfully:
                parts.center_x = random.randrange(64, 2000, 64)
                parts.center_y = random.randrange(64, 2000, 64)

                wall_hit_list = arcade.check_for_collision_with_list(parts, self.wall_list)
                parts_hit_list = arcade.check_for_collision_with_list(parts, self.parts_list)

                if len(wall_hit_list) == 0 and len(parts_hit_list) == 0:
                    parts_placed_successfully = True

            self.parts_list.append(parts)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.GRAY_BLUE)

    def on_draw(self):

        self.clear()

        self.camera_sprites.use()

        self.wall_list.draw()
        self.player_list.draw()
        self.parts_list.draw()

        self.camera_gui.use()

        # GUI
        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.ALMOND)

        text = f"Score: {self.score}"
        arcade.draw_text(text, 10, 10, arcade.color.BLACK, 20)

        if len(self.parts_list) == 0:
            output = "GAME OVER!"
            arcade.draw_text(output, 400, 300, arcade.color.WHITE, 25)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def on_update(self, delta_time):

        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

        self.physics_engine.update()

        if len(self.parts_list) > 0:
            self.parts_list.update()

        parts_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.parts_list)

        for parts in parts_hit_list:
            parts.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.upgrade_sound)

        # Scroll the screen to the player

        self.scroll_to_player()

    def scroll_to_player(self):

        position = Vec2(self.player_sprite.center_x - self.width / 2,
                        self.player_sprite.center_y - self.height / 2)

        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):

        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
