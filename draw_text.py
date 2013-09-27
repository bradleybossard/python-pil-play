from PIL import Image, ImageDraw, ImageFont

im = Image.new('RGBA', (100, 100), (255, 0, 0, 255)) # Create a blank image
draw = ImageDraw.Draw(im)
font = ImageFont.truetype('/Library/Fonts/Impact.ttf', 30)
draw.text((10, 50), 'Logo', font=font, fill="blue")
im.save('text.png')
