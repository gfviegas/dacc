#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import cv2

base = cv2.imread('./base.png', 1)
base_rgb = cv2.cvtColor(base, cv2.COLOR_BGR2RGB)


font_name = ImageFont.truetype('Assistant-Bold.otf', 32)
font_type = ImageFont.truetype('Assistant-Bold.otf', 14)

data = [
    {'name': 'Gustavo Viegas', 'type': 'Graduando'},
    {'name': 'Marcos da Silva Junior', 'type': 'Alumni'}
]

for d in data:
    base_copy = cv2.cvtColor(base.copy(), cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(base_copy)
    draw = ImageDraw.Draw(pil_img)

    # Draw the text
    draw.text((140, 770), d['name'], font=font_name, fill=(0,0,0))
    draw.text((550, 830), d['type'], font=font_type, fill=(0,0,0))

    # Get back the image to OpenCV
    processed = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

    # cv2.putText(baseCopy, d['name'], (140,800), font, 1, (0, 0, 0), 1)
    # cv2.putText(baseCopy, d['type'], (550,850), font, 0.5, (0, 0, 0), 1)
    cv2.imwrite('images/{}.png'.format(d['name']), processed)
