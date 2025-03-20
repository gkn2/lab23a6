my_image = assets.image("""g""")

image_width = my_image.width
screen_width = screen.width

x_position = image_width / 2

while x_position < screen_width:
    my_sprite = sprites.create(my_image, SpriteKind.player)
    my_sprite.x = x_position
    my_sprite.y = my_sprite.height / 2
    x_position += image_width