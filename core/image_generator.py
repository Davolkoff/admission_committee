from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os


def generate_ticket(ticket_number):
    X = 490
    Y = 900
    TEXT = 'Талон номер'

    img = Image.open(os.path.abspath(f"core/img/original.png"))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(os.path.abspath(f"core/static/fonts/Roboto-Medium.ttf"), 62)

    draw.text((310, 825), TEXT, font=font, fill=(0, 0, 0))

    tmp = ticket_number
    i = 0

    while tmp > 0:
        i += 1
        tmp = tmp//10

    X = X - i * 15

    draw.text((X, Y), str(ticket_number), font=font, fill=(0, 0, 0))

    # img.show()
    img.save(os.path.abspath(f"core/img/pic1.png"))

def generate_expert_ticket(ticket_number):
    X = 490
    Y = 750
    TEXT = 'Талон номер'

    img = Image.open(os.path.abspath(f"core/img/pic.png"))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(os.path.abspath(f"core/static/fonts/Roboto-Medium.ttf"), 62)

    draw.text((310, 675), TEXT, font=font, fill=(0, 0, 0))

    tmp = ticket_number
    i = 0

    while tmp > 0:
        i += 1
        tmp = tmp//10

    X = X - i * 15

    draw.text((X, Y), str(ticket_number), font=font, fill=(0, 0, 0))

    # img.show()
    img.save(os.path.abspath(f"core/img/pic2.png"))

# generate_expert_ticket(1)