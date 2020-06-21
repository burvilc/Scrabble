#!/usr/bin/env python3 

import argparse
from PIL import Image, ImageDraw, ImageFont

def DrawLines(draw, axis, line_start, line_end, num_lines, step_size):

    for i in range(0, num_lines, step_size):
        if axis == "x":
            line = ((i, line_start), (i, line_end))
        elif axis == "y":
            line = ((line_start, i), (line_end, i))
        draw.line(line, fill=128)

def WriteLetter(draw, col_and_row_numbers, text):
    # get a font
    fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 16)
    #fnt = ImageFont.load_default()
    draw.text( (7,5), "TWS", font=fnt, align="center", fill=0 )
    #draw.text( (5,5), "D", font=fnt, fill=0 )
    return

def GetParams():
    """ Get parameters
    """
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("width", help="width of image in pixels",
                        type=int)
    parser.add_argument("height", help="height of image in pixels",
                        type=int)
    parser.add_argument("step_count", help="how many steps across the grid",
                        type=int)
    args = parser.parse_args()
    """

    step_count = 15 
    height = 582 
    width = 800 
    return height, width, step_count

def InitBlankBoardImage(height, width, step_count):
    image = Image.new(mode='L', size=(width, height), color=255)

    y_start = 0
    y_end = image.height
    draw = ImageDraw.Draw(image)
    x_start = 0
    x_end = image.width
    step_size = int(image.width / step_count)
    return image, x_start, y_start, x_end, y_end, draw, step_size

def SaveBoardImage(width, height, step_count):

    filename = "grid-{}-{}-{}.png".format(width, height, step_count)
    print("Saving {}".format(filename))
    image.save(filename)
    image.show()
    return filename

###############
if __name__ == '__main__':

    height, width, step_count = GetParams()
    image, x_start, y_start, x_end, y_end, draw, step_size = InitBlankBoardImage(height, width, step_count)

    # Draw a grid
    DrawLines(draw, "x", y_start, y_end, image.width, step_size)
    DrawLines(draw, "y", x_start, x_end, image.height, step_size)
    WriteLetter(draw, (1,1), "TWS")
    
    del draw
    filename = SaveBoardImage(width, height, step_count)


