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
    image = Image.new('1', (epd2in9.EPD_WIDTH, epd2in9.EPD_HEIGHT), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(image)

    # current date and time
    theTime = time.strftime('%H:%M')
    draw.text((0, 50), theTime, font = font24Sans, fill = 0)

    theDate = time.strftime('%d.%m.%Y')
    draw.text((52, 78), theDate, font = font12Sans, fill = 0)

    # horizontal line
    draw.line((0, 90, 128, 90), fill = 0)

    draw.rectangle((0, 0, 10, 10), fill = 0) # upper left corner
    draw.rectangle((118, 0, 128, 10), fill = 0) # upper right corner
    draw.rectangle((0, 286, 10, 296), fill = 0) # lower left corner
    draw.rectangle((118, 282, 128, 292), fill = 0) # lower right corner

    # circles
    draw.chord((10, 130, 30, 150), 0, 360, fill = 0)
    draw.chord((20, 150, 50, 180), 0, 360, fill = 0)
    draw.chord((30, 200, 90, 260), 0, 360, fill = 0)

    # update the display
    epd.clear_frame_memory(0xFF)
    epd.set_frame_memory(image, 0, 0)    # upper left corner coordinates
    epd.display_frame()

    epd.delay_ms(2000)


if __name__ == '__main__':
    main()
