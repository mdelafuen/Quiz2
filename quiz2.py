import arcade

def main():
    temperature_data = [65,72,52]
    new_data = int(input("what is the high temperature today?"))
    temperature_data.append(new_data)
    today_temp = temperature_data[0] + new_data
    print("Today's temperature is", today_temp)

def arcadeloop():
    arcade.open_window(800, 800, "Vertical Pattern")
    arcade.set_background_color(arcade.color.WHITE)
    width = arcade.get_window().width
    height = arcade.get_window().height

    arcade.start_render()
    # start drawing here
    for x in range(0, 801, 80):
        arcade.draw_rectangle_filled(x, 400, 40, height, arcade.color.BLACK)


    arcade.finish_render()

    arcade.run()

arcadeloop()
#main()
