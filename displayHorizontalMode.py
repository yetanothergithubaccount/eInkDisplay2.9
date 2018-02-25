#!/usr/bin/env python2

import epd2in9
import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Display resolution
#EPD_WIDTH       = 128
#EPD_HEIGHT      = 296

def main():

    # prepare e-ink display
    epd = epd2in9.EPD()
    epd.init(epd.lut_full_update)
    epd.reset()

    # font definitions
    font12Sans = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf', 12)
    font24Sans = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf', 24)

    # the image to be drawn on the display (horizontal)
    image = Image.new('1', (epd2in9.EPD_HEIGHT, epd2in9.EPD_WIDTH), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(image)

    # current date and time
    theTime = time.strftime('%H:%M')
    draw.text((10, 30), theTime, font = font24Sans, fill = 0)

    theDate = time.strftime('%d.%m.%Y')
    draw.text((52, 58), theDate, font = font12Sans, fill = 0)

    # horizontal line
    draw.line((0, 90, 128, 90), fill = 0)

    draw.rectangle((0, 0, 10, 10), fill = 0) # upper left corner
    draw.rectangle((286, 0, 296, 10), fill = 0) # upper right corner
    draw.rectangle((0, 118, 10, 128), fill = 0) # lower left corner
    draw.rectangle((282, 118, 292, 128), fill = 0) # lower right corner

    # circles
    draw.chord((130, 10, 150, 30), 0, 360, fill = 0)
    draw.chord((150, 20, 180, 50), 0, 360, fill = 0)
    draw.chord((200, 30, 260, 90), 0, 360, fill = 0)

    # update the display
    epd.clear_frame_memory(0xFF)
    # rotate the image by 90 degrees
    epd.set_frame_memory(image.rotate(90), 0, 0)    # upper left corner coordinates
    epd.display_frame()

    epd.delay_ms(2000)


if __name__ == '__main__':
    main()
