from PIL import Image, ImageDraw

im = Image.new('RGBA', (100, 100), (0, 0, 0, 0)) # Create a blank image
draw = ImageDraw.Draw(im)
lines = [(50, 0), (0, 40), (20, 100), (80, 100), (100, 40)]
draw.polygon(lines, fill="black")
im.save('polygon.png')
