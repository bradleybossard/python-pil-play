from PIL import Image, ImageDraw

im = Image.new('RGBA', (100, 100), (0, 0, 0, 0)) # Create a blank image
draw = ImageDraw.Draw(im) # Create a draw object
draw.ellipse((0, 0, 100, 100), fill=(255, 255, 255)) # Draw a circle
im.save('ellipse.png')
