import arcade

column_spacing = 10
row_spacing = 10
left_margin = 5
bottom_margin = 5


def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)


def draw_section_1():
    for row in range(30):
        for column in range(30):
            x = column * column_spacing + left_margin
            y = row * row_spacing + bottom_margin
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_2():
    for row in range(30):
        for column in range(30):
            x = column * column_spacing + left_margin + 300
            y = row * row_spacing + bottom_margin
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            if column % 2 == 1:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)


def draw_section_3():
    for row in range(30):
        for column in range(30):
            x = column * column_spacing + left_margin + 600
            y = row * row_spacing + bottom_margin
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            if row % 2 == 1:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)


def draw_section_4():
    for row in range(30):
        for column in range(30):
            x = column * column_spacing + left_margin + 900
            y = row * row_spacing + bottom_margin
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
            if row % 2 == 0 and column % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_5():
    for column in range(30):
        for row in range(column):
            x = column * column_spacing + left_margin
            y = row * row_spacing + bottom_margin + 300
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_6():
    for row in range(30):
        for column in range(30 - row):
            x = column * column_spacing + left_margin + 300
            y = row * row_spacing + bottom_margin + 300
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_7():
    for row in range(30):
        for column in range(row + 1):
            x = column * column_spacing + left_margin + 600
            y = row * row_spacing + bottom_margin + 300
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_8():
    for row in range(30):
        for column in range(30-(row+1), 30):
            x = column * column_spacing + left_margin + 900
            y = row * row_spacing + bottom_margin+300
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()


main()
