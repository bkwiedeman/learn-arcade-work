"""
Artwork from https://kenney.nl
"""

import random
import arcade
import math
import os

SPRITE_SCALING = 0.5
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_LASER = 0.8
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "FINAL PROJECT"

BULLET_SPEED = 5
MOVEMENT_SPEED = 4
SPRITE_SPEED = 0.5

HEALTHBAR_WIDTH = 25
HEALTHBAR_HEIGHT = 3
HEALTHBAR_OFFSET_Y = -10

HEALTH_NUMBER_OFFSET_X = -10
HEALTH_NUMBER_OFFSET_Y = -25

window = None


class Coin(arcade.Sprite):
    def __init__(self, image, scale, max_health):
        super().__init__(image, scale)

        self.max_health = max_health
        self.cur_health = max_health

    def draw_health_bar(self):
        if self.cur_health < self.max_health:
            arcade.draw_rectangle_filled(center_x=self.center_x,
                                         center_y=self.center_y + HEALTHBAR_OFFSET_Y,
                                         width=HEALTHBAR_WIDTH,
                                         height=3,
                                         color=arcade.color.RED)

        health_width = HEALTHBAR_WIDTH * (self.cur_health / self.max_health)

        arcade.draw_rectangle_filled(center_x=self.center_x - 0.5 * (HEALTHBAR_WIDTH - health_width),
                                     center_y=self.center_y - 10,
                                     width=health_width,
                                     height=HEALTHBAR_HEIGHT,
                                     color=arcade.color.GREEN)

    def follow_sprite(self, player_sprite):

        if self.center_y < player_sprite.center_y:
            self.center_y += min(SPRITE_SPEED, player_sprite.center_y - self.center_y)
        elif self.center_y > player_sprite.center_y:
            self.center_y -= min(SPRITE_SPEED, self.center_y - player_sprite.center_y)

        if self.center_x < player_sprite.center_x:
            self.center_x += min(SPRITE_SPEED, player_sprite.center_x - self.center_x)
        elif self.center_x > player_sprite.center_x:
            self.center_x -= min(SPRITE_SPEED, self.center_x - player_sprite.center_x)


class Player(arcade.Sprite):

    def __init__(self, position_x, position_y, change_x, change_y, max_health, image, scale):
        super().__init__(image, scale)
        self.center_x = position_x
        self.center_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.max_health = max_health
        self.cur_health = max_health

    """ Main application class. """

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

    def draw_health_bar(self):
        if self.cur_health < self.max_health:
            arcade.draw_rectangle_filled(center_x=self.center_x,
                                         center_y=self.center_y - 35,
                                         width=HEALTHBAR_WIDTH,
                                         height=3,
                                         color=arcade.color.RED)

        health_width = HEALTHBAR_WIDTH * (self.cur_health / self.max_health)

        arcade.draw_rectangle_filled(center_x=self.center_x - 0.5 * (HEALTHBAR_WIDTH - health_width),
                                     center_y=self.center_y - 35,
                                     width=health_width,
                                     height=HEALTHBAR_HEIGHT,
                                     color=arcade.color.GREEN)


class MyGame(arcade.Window):

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.bullet_list = None
        self.wall_list = None

        self.physics_engine = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0
        # Load sounds. Sounds from kenney.nl
        self.gun_sound = arcade.sound.load_sound(":resources:sounds/laser1.wav")
        self.hit_sound = arcade.sound.load_sound(":resources:sounds/phaseJump1.wav")
        self.death_sound = arcade.sound.load_sound(":resources:sounds/hit5.wav"
                                                   "")
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):

        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Set up the player
        self.score = 0

        # Image from kenney.nl
        self.player_sprite = Player(50, 70, 0, 0, 5, ":resources:images/animated_characters/female_person/"
                                                     "femalePerson_idle.png", SPRITE_SCALING_PLAYER)
        self.player_list.append(self.player_sprite)

        for x in range(0, 800, 42):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 0
            self.wall_list.append(wall)

        for x in range(0, 800, 42):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 600
            self.wall_list.append(wall)

        for y in range(0, 600, 42):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
            wall.center_x = 0
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(0, 600, 42):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
            wall.center_x = 800
            wall.center_y = y
            self.wall_list.append(wall)

        for i in range(COIN_COUNT):
            coin = Coin(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN, 1)
            coin_placed_successfully = False

            while not coin_placed_successfully:
                coin.center_x = random.randrange(-1000, 1500, 64)
                coin.center_y = random.randrange(-1000, 1500, 64)

                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    coin_placed_successfully = True

            self.coin_list.append(coin)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing
        self.clear()

        # Draw all the sprites.
        self.coin_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()
        self.wall_list.draw()

        for coin in self.coin_list:
            coin.draw_health_bar()

        for player in self.player_list:
            player.draw_health_bar()

        if len(self.coin_list) == 0:
            output = "GAME OVER!"
            arcade.draw_text(output, 400, 300, arcade.color.WHITE, 25)

        if len(self.player_list) == 0:
            output = "YOU DIED!"
            arcade.draw_text(output, 400, 300, arcade.color.WHITE, 25)

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called whenever the mouse button is clicked. """

        # Create a bullet
        bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", SPRITE_SCALING_LASER)

        # Position the bullet at the player's current location
        start_x = self.player_sprite.center_x
        start_y = self.player_sprite.center_y
        bullet.center_x = start_x
        bullet.center_y = start_y

        dest_x = x
        dest_y = y

        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        bullet.angle = math.degrees(angle)

        bullet.change_x = math.cos(angle) * BULLET_SPEED
        bullet.change_y = math.sin(angle) * BULLET_SPEED

        # Add the bullet to the appropriate lists
        self.bullet_list.append(bullet)

    def on_update(self, delta_time):
        self.bullet_list.update()
        self.player_list.update()

        for coin in self.coin_list:
            coin.follow_sprite(self.player_sprite)

        # Loop through each bullet
        for bullet in self.bullet_list:

            # Check this bullet to see if it hit a coin
            hit_list = arcade.check_for_collision_with_list(bullet, self.coin_list)

            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            # For every coin we hit, add to the score and remove the coin
            for coin in hit_list:
                coin.cur_health -= 1

                if coin.cur_health <= 0:
                    coin.remove_from_sprite_lists()
                    self.score += 1
                    arcade.play_sound(self.death_sound)
                else:
                    arcade.play_sound(self.hit_sound)

            # If the bullet flies off-screen, remove it.
            if bullet.bottom > self.width or bullet.top < 0 or bullet.right < 0 or bullet.left > self.width:
                bullet.remove_from_sprite_lists()

        for coin in self.coin_list:

            player_hit_list = arcade.check_for_collision_with_list(coin, self.player_list)

            if len(player_hit_list) > 0:
                coin.remove_from_sprite_lists()

            for player in player_hit_list:
                player.cur_health -= 1

                if player.cur_health <= 0:
                    player.remove_from_sprite_lists()
                    arcade.play_sound(self.death_sound)
                else:
                    arcade.play_sound(self.hit_sound)

        self.physics_engine.update()

    # Move Character
    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.player_sprite.change_y = MOVEMENT_SPEED

        elif key == arcade.key.S:
            self.player_sprite.change_y = -MOVEMENT_SPEED

        elif key == arcade.key.A:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0

        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0


def main():
    game = MyGame()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
