import arcade

import random

# ---Constants---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COW = 0.2
SPRITE_SCALING_ROCKET = 0.5
COW_COUNT = 50
ROCKET_COUNT = 25

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Cow(arcade.Sprite):
    def update(self):
        self.center_y -= 1

        if self.center_y < -20:
            self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                             SCREEN_HEIGHT + 100)
            self.center_x = random.randrange(SCREEN_WIDTH)


class Rocket(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "SPRITE EXAMPLE")

        # Sprite Variables
        self.center_y = None
        self.center_x = None
        self.player_list = None
        self.cow_list = None
        self.rocket_list = None
        self.upgrade_sound = arcade.load_sound("upgrade.wav")
        self.explosion_sound = arcade.load_sound("explosion.wav")

        # Player Info
        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):

        # Sprite Lists
        self.player_list = arcade.SpriteList()
        self.cow_list = arcade.SpriteList()
        self.rocket_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("shipGreen_manned.png", SPRITE_SCALING_PLAYER)

        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(COW_COUNT):
            # Character image from kenney.nl
            cow = Cow("cow.png", SPRITE_SCALING_COW)

            cow.center_x = random.randrange(SCREEN_WIDTH)
            cow.center_y = random.randrange(SCREEN_HEIGHT)

            self.cow_list.append(cow)

        for i in range(ROCKET_COUNT):
            # Character image from kenney.nl
            rocket = Rocket("spaceMissiles_003.png", SPRITE_SCALING_ROCKET)

            rocket.center_x = random.randrange(SCREEN_WIDTH)
            rocket.center_y = random.randrange(SCREEN_HEIGHT)
            rocket.change_x = random.randrange(-3, 4)
            rocket.change_y = random.randrange(-3, 4)

            self.rocket_list.append(rocket)

    def on_draw(self):
        arcade.start_render()

        self.cow_list.draw()
        self.player_list.draw()
        self.rocket_list.draw()

        output = "Score: " + str(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 15)

        if len(self.cow_list) == 0:
            output = "GAME OVER!"
            arcade.draw_text(output, 300, 400, arcade.color.WHITE, 25)

    def on_mouse_motion(self, x, y, dx, dy):
        if len(self.cow_list) > 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def update(self, delta_time):
        if len(self.cow_list) > 0:
            self.cow_list.update()
            self.rocket_list.update()

        cow_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                            self.cow_list)
        rocket_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                               self.rocket_list)

        for cow in cow_hit_list:
            cow.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.upgrade_sound)

        for rocket in rocket_hit_list:
            self.score -= 1
            arcade.play_sound(self.explosion_sound)

            rocket.center_x = random.randrange(SCREEN_WIDTH)
            rocket.center_y = random.randrange(SCREEN_HEIGHT)
            rocket.change_x = random.randrange(-3, 4)
            rocket.change_y = random.randrange(-3, 4)


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
