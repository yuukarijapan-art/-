import os
from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap

def make_image(path, text, width=1080, height=1350, font_path=None):
    img = Image.new("RGB", (width, height), (245, 245, 245))
    draw = ImageDraw.Draw(img)
    for i in range(height):
        shade = 245 - int(i * 120 / height)
        draw.line([(0, i), (width, i)], fill=(shade, shade, 255 if i % 3 == 0 else shade))

    if font_path and os.path.exists(font_path):
        font = ImageFont.truetype(font_path, size=56)
        font_small = ImageFont.truetype(font_path, size=32)
    else:
        font = ImageFont.load_default()
        font_small = ImageFont.load_default()

    max_chars = 16
    lines = []
    for line in text.splitlines():
        if not line.strip():
            lines.append("")
            continue
        lines.extend(wrap(line, width=max_chars))

    y = height // 3
    for ln in lines:
        w, h = draw.textsize(ln, font=font)
        draw.text(((width - w)//2, y), ln, fill=(20, 20, 20), font=font)
        y += h + 12

    footer = "Auto • Daily"
    fw, fh = draw.textsize(footer, font=font_small)
    draw.text((width - fw - 24, height - fh - 24), footer, fill=(40,40,40), font=font_small)

    img.save(path, "JPEG", quality=92)
    return path
