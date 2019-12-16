#!/usr/bin/env python3
import base64
import os
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont


def draw_image(new_img, text, font_size=20, fill_text_color=(0, 0, 0), show_image=False):
    draw = ImageDraw.Draw(new_img)
    img_size = new_img.size
    # draw.line((0, 0) + img_size, fill=128)
    # draw.line((0, img_size[1], img_size[0], 0), fill=128)

    fnt = ImageFont.truetype(os.path.realpath('.') + '/src/resources/arialuni.ttf', font_size)
    fnt_size = fnt.getsize(text)
    # while fnt_size[0] > img_size[0]:
    #     font_size -= 2
    #     fnt = ImageFont.truetype(os.path.realpath('.') + '/src/resources/arialuni.ttf', font_size)
    #     fnt_size = fnt.getsize(text)

    x = (img_size[0] - fnt_size[0]) / 2
    y = (img_size[1] - fnt_size[1]) / 2
    draw.multiline_text((30, 30), text, font=fnt, fill=fill_text_color)

    if show_image:
        new_img.show()
    del draw


def new_image(width, height, text, color=(255, 255, 255, 255), font_size=20, show_image=False, save_image_path=None):
    new_img = Image.new('RGB', (int(width), int(height)), color)
    draw_image(new_img, text, font_size=font_size, show_image=show_image)
    if save_image_path is not None and save_image_path != '':
        new_img.save(save_image_path)
    output_buffer = BytesIO()
    new_img.save(output_buffer, format='JPEG')
    byte_data = output_buffer.getvalue()
    base64_str = base64.b64encode(byte_data)
    del new_img
    return byte_data


def new_image_with_file(fn):
    with open(fn, encoding='utf-8') as f:
        for l in f:
            l = l.strip()
            if l:
                ls = l.split(',')
                if '#' == l[0] or len(ls) < 2:
                    continue

                new_image(*ls)


if '__main__' == __name__:
    new_image(1200, 800, 'hello world any size\n哈哈哈哈 hello world any size\n哈哈哈哈 hello world any size\n哈哈哈哈 hello world any size\n哈哈哈哈 hello world any size\n哈哈哈哈 hello world any size\n哈哈哈哈 hello world any size\n哈哈哈哈 hello world any size\n哈哈哈哈 ', font_size=12, show_image=True)
    # new_image_with_file('image_data.txt')
