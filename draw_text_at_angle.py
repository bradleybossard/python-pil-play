from PIL import Image, ImageDraw, ImageFont

def draw_text(text, size, angle=0, fill=None):
  #font = ImageFont.truetype( 'path/to/font.ttf', size)
  font = ImageFont.truetype('/Library/Fonts/Impact.ttf', 30)
  size = font.getsize(text) # Returns the width and height of the given text, as a 2-tuple.
  im = Image.new('RGBA', size, (0, 0, 0, 0)) # Create a blank image with the given size
  draw = ImageDraw.Draw(im)
  draw.text((0, 0), text, font=font, fill=fill) #Draw text
  return im.rotate(angle, expand=True)

img = draw_text('Google', 30, 45, (82, 124, 178))
img.save('text_at_angle.png')
