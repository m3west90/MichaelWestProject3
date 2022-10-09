import arcade

myWindow = arcade.open_window(800, 800, "My Flag!")

arcade.set_background_color(arcade.color.LIGHT_GRAY)
arcade.start_render()

#Drawing the base of the flag
arcade.draw_lrtb_rectangle_filled(50, 750, 700, 300, arcade.color.REDWOOD)

#Drawing flag lines
arcade.draw_line(50, 300, 50, 700, arcade.color.LAVENDER, 5)
arcade.draw_line(750, 300, 750, 700, arcade.color.LAVENDER, 5)
arcade.draw_line(50, 700, 750, 700, arcade.color.LAVENDER, 5)
arcade.draw_line(50, 650, 750, 650, arcade.color.LAVENDER, 5)
arcade.draw_line(50, 600, 750, 600, arcade.color.LAVENDER, 5)
arcade.draw_line(50, 550, 750, 550, arcade.color.LAVENDER, 5)
arcade.draw_line(50, 500, 750, 500, arcade.color.LAVENDER, 5)
arcade.draw_line(50, 450, 750, 450, arcade.color.LAVENDER, 5)
arcade.draw_line(50, 400, 750, 400, arcade.color.LAVENDER, 5)
arcade.draw_line(50, 350, 750, 350, arcade.color.LAVENDER, 5)
arcade.draw_line(50, 300, 750, 300, arcade.color.LAVENDER, 5)

#Drawing the logo of the flag
arcade.draw_lrtb_rectangle_filled(200, 600, 600, 400, arcade.color.LAVENDER)
arcade.draw_xywh_rectangle_filled(250, 350, 300, 300, arcade.color.LAVENDER)
arcade.draw_circle_filled(400, 500, 150, arcade.color.LIGHT_CORNFLOWER_BLUE)
arcade.draw_triangle_filled(400, 600, 500, 440, 300, 440, arcade.color.BLACK)
arcade.draw_arc_filled(400, 500, 100, 100, arcade.color.GREEN, 30, 340)

#Drawing signature
signature = arcade.Text("My Flag by\nMichael West", 10, 710, arcade.color.BLACK, 20)
signature.draw()

arcade.finish_render()

arcade.run()