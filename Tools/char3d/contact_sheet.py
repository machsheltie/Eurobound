"""Small review sheet from rendered frames (PIL only, <=1024 px): python tools/char3d/contact_sheet.py <out.png> <cols> <img> [img ...]
Each 640 px frame is cropped to the figure (x 140..500, y 40..620) and shown at half size on grey; images fill rows left to right."""
import sys
from PIL import Image
out, cols, files = sys.argv[1], int(sys.argv[2]), sys.argv[3:]
tw, th = 180, 290
rows = (len(files) + cols - 1) // cols
sheet = Image.new("RGB", (cols * tw, rows * th), (140, 140, 140))
for i, f in enumerate(files):
    im = Image.open(f).convert("RGBA").crop((140, 40, 500, 620)).resize((tw, th), Image.LANCZOS)
    sheet.paste(im, ((i % cols) * tw, (i // cols) * th), im)
sheet.save(out)
print("SHEET", out, sheet.size)
