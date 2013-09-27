from PIL import Image, ImageDraw, ImageFont
""" Drawing text that exactly fits inside a rectangle"""

def draw_text(text, size, fill=None):
    font = ImageFont.truetype('/Library/Fonts/Impact.ttf', 30)
    size = font.getsize(text) # Returns the width and height of the given text, as a 2-tuple.
    im = Image.new('RGBA', size, (255, 0, 0, 255)) # Create a blank image with the given size
    draw = ImageDraw.Draw(im)
    draw.text((0, 0), text, font=font, fill=fill) #Draw text
    return im

img = draw_text('Google', 30, (82, 124, 178))
img.save('text_getsize.png')
