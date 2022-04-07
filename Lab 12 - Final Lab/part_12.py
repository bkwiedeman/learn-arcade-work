# CITE WEBSITE ABOVE IMAGE AND SOUNDS
import random
import arcade
import math


SPRITE_SCALING = 0.8
SPRITE_SCALING_PLAYER = 0.3
SPRITE_SCALING_PLANE = 0.8
SPRITE_SCALING_LASER = 0.4
PLANE_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "FINAL PROJECT"

BULLET_SPEED = 15
MOVEMENT_SPEED = 4
SPRITE_SPEED = 0.6

HEALTHBAR_WIDTH = 25
HEALTHBAR_HEIGHT = 3
HEALTHBAR_OFFSET_Y = -10

HEALTH_NUMBER_OFFSET_X = -10
HEALTH_NUMBER_OFFSET_Y = -25

window = None


class InstructionView(arcade.View):
    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.BLACK)

    def on_draw(self):
        """ Draw this view """
        self.window.clear()
        arcade.draw_text("Instructions", self.window.width / 2, self.window.height / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("W,A,S,D to move.", self.window.width / 2, self.window.height / 2 - 70,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("Mouse to aim.", self.window.width / 2, self.window.height / 2 - 100,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("Right click mouse to shoot", self.window.width / 2, self.window.height / 2 - 130,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("Destroy all of the enemy ships", self.window.width / 2, self.window.height / 2 - 200,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("Don't Die. Good Luck", self.window.width / 2, self.window.height / 2 - 230,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("Click to Continue..", self.window.width / 2, self.window.height / 2 - 290,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)


class GameOverView(arcade.View):
    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.BLACK)

    def on_draw(self):
        """ Draw this view """
        self.window.clear()
        arcade.draw_text("You have Died.", self.window.width / 2, self.window.height / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Click to Try Again...", self.window.width / 2, self.window.height / 2 - 70,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)


class Plane(arcade.Sprite):
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


class GameView(arcade.View):

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__()

        # Variables that will hold sprite lists
        self.player_list = None
        self.plane_list = None
        self.bullet_list = None
        self.wall_list = None

        self.level = 1

        self.physics_engine = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0
        # Load sounds. Sounds from kenney.nl
        self.hit2_sound = arcade.sound.load_sound("arcade_resources_sounds_hit3.wav")
        self.death_sound = arcade.sound.load_sound("arcade_resources_sounds_explosion2.wav")
        self.hit_sound = arcade.sound.load_sound("arcade_resources_sounds_gameover2.wav")

    def level_1(self):
        for i in range(PLANE_COUNT):
            plane = Plane("ship_0005.png", SPRITE_SCALING_PLANE, 1)
            plane.center_x = random.randrange(-1000, 1500, 64)
            plane.center_y = random.randrange(-1000, 1500, 64)

            self.plane_list.append(plane)

    def level_2(self):
        for i in range(PLANE_COUNT):
            plane = Plane("ship_0005.png", SPRITE_SCALING_PLANE, 3)
            plane.center_x = random.randrange(-1000, 1500, 64)
            plane.center_y = random.randrange(-1000, 1500, 64)

            self.plane_list.append(plane)

    def level_3(self):
        for i in range(PLANE_COUNT):
            plane = Plane("ship_0005.png", SPRITE_SCALING_PLANE, 5)
            plane.center_x = random.randrange(-1000, 1500, 64)
            plane.center_y = random.randrange(-1000, 1500, 64)

            self.plane_list.append(plane)

    def setup(self):

        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.plane_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.level = 1

        # Image from kenney.nl
        self.player_sprite = Player(50, 70, 0, 0, 10, "tanks_tankGrey1.png", SPRITE_SCALING_PLAYER)
        self.player_list.append(self.player_sprite)

        for x in range(0, 800, 42):
            wall = arcade.Sprite("tanks_crateWood.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 0
            self.wall_list.append(wall)

        for x in range(0, 800, 42):
            wall = arcade.Sprite("tanks_crateWood.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 600
            self.wall_list.append(wall)

        for y in range(0, 600, 42):
            wall = arcade.Sprite("tanks_crateWood.png", SPRITE_SCALING)
            wall.center_x = 0
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(0, 600, 42):
            wall = arcade.Sprite("tanks_crateWood.png", SPRITE_SCALING)
            wall.center_x = 800
            wall.center_y = y
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.TAN)

        self.level_1()

    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing
        self.window.clear()

        # Draw all the sprites.
        self.plane_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()
        self.wall_list.draw()

        for plane in self.plane_list:
            plane.draw_health_bar()

        for player in self.player_list:
            player.draw_health_bar()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        output = f"Level: {self.level}"
        arcade.draw_text(output, 10, 35, arcade.color.WHITE, 14)

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called whenever the mouse button is clicked. """

        # Create a bullet
        bullet = arcade.Sprite("tank_bulletFly3.png", SPRITE_SCALING_LASER)

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

        for plane in self.plane_list:
            plane.follow_sprite(self.player_sprite)

        # Loop through each bullet
        for bullet in self.bullet_list:

            # Check this bullet to see if it hit a coin
            hit_list = arcade.check_for_collision_with_list(bullet, self.plane_list)

            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            # For every coin we hit, add to the score and remove the coin
            for plane in hit_list:
                plane.cur_health -= 1

                if plane.cur_health <= 0:
                    plane.remove_from_sprite_lists()
                    self.score += 1
                    arcade.play_sound(self.death_sound)
                else:
                    arcade.play_sound(self.hit2_sound)

                    # See if we should go to level 2
            if len(self.plane_list) == 0 and self.level == 1:
                self.level += 1
                self.level_2()
                # See if we should go to level 3
            elif len(self.plane_list) == 0 and self.level == 2:
                self.level += 1
                self.level_3()

            # If the bullet flies off-screen, remove it.
            if bullet.bottom > self.window.width or bullet.top < 0 or bullet.right < 0 or bullet.left > self.window.width:
                bullet.remove_from_sprite_lists()

        for plane in self.plane_list:

            player_hit_list = arcade.check_for_collision_with_list(plane, self.player_list)

            if len(player_hit_list) > 0:
                plane.remove_from_sprite_lists()

            for player in player_hit_list:
                player.cur_health -= 1

                if player.cur_health <= 0:
                    view = GameOverView()
                    self.window.show_view(view)
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
    """ Main function """

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
