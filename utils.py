from pathlib import Path

from django.conf import settings
from PIL import Image

"""
    Collection of utilities
"""


def cad2hex(id):
    while id > 255:
        id = id - 255
    RGB_list = (
        (0, 0, 0),
        (255, 0, 0),
        (255, 255, 0),
        (0, 255, 0),
        (0, 255, 255),
        (0, 0, 255),
        (255, 0, 255),
        (255, 255, 255),
        (128, 128, 128),
        (192, 192, 192),
        (255, 0, 0),
        (255, 127, 127),
        (165, 0, 0),
        (165, 82, 82),
        (127, 0, 0),
        (127, 63, 63),
        (76, 0, 0),
        (76, 38, 38),
        (38, 0, 0),
        (38, 19, 19),
        (255, 63, 0),
        (255, 159, 127),
        (165, 41, 0),
        (165, 103, 82),
        (127, 31, 0),
        (127, 79, 63),
        (76, 19, 0),
        (76, 47, 38),
        (38, 9, 0),
        (38, 23, 19),
        (255, 127, 0),
        (255, 191, 127),
        (165, 82, 0),
        (165, 124, 82),
        (127, 63, 0),
        (127, 95, 63),
        (76, 38, 0),
        (76, 57, 38),
        (38, 19, 0),
        (38, 28, 19),
        (255, 191, 0),
        (255, 223, 127),
        (165, 124, 0),
        (165, 145, 82),
        (127, 95, 0),
        (127, 111, 63),
        (76, 57, 0),
        (76, 66, 38),
        (38, 28, 0),
        (38, 33, 19),
        (255, 255, 0),
        (255, 255, 127),
        (165, 165, 0),
        (165, 165, 82),
        (127, 127, 0),
        (127, 127, 63),
        (76, 76, 0),
        (76, 76, 38),
        (38, 38, 0),
        (38, 38, 19),
        (191, 255, 0),
        (223, 255, 127),
        (124, 165, 0),
        (145, 165, 82),
        (95, 127, 0),
        (111, 127, 63),
        (57, 76, 0),
        (66, 76, 38),
        (28, 38, 0),
        (33, 38, 19),
        (127, 255, 0),
        (191, 255, 127),
        (82, 165, 0),
        (124, 165, 82),
        (63, 127, 0),
        (95, 127, 63),
        (38, 76, 0),
        (57, 76, 38),
        (19, 38, 0),
        (28, 38, 19),
        (63, 255, 0),
        (159, 255, 127),
        (41, 165, 0),
        (103, 165, 82),
        (31, 127, 0),
        (79, 127, 63),
        (19, 76, 0),
        (47, 76, 38),
        (9, 38, 0),
        (23, 38, 19),
        (0, 255, 0),
        (127, 255, 127),
        (0, 165, 0),
        (82, 165, 82),
        (0, 127, 0),
        (63, 127, 63),
        (0, 76, 0),
        (38, 76, 38),
        (0, 38, 0),
        (19, 38, 19),
        (0, 255, 63),
        (127, 255, 159),
        (0, 165, 41),
        (82, 165, 103),
        (0, 127, 31),
        (63, 127, 79),
        (0, 76, 19),
        (38, 76, 47),
        (0, 38, 9),
        (19, 38, 23),
        (0, 255, 127),
        (127, 255, 191),
        (0, 165, 82),
        (82, 165, 124),
        (0, 127, 63),
        (63, 127, 95),
        (0, 76, 38),
        (38, 76, 57),
        (0, 38, 19),
        (19, 38, 28),
        (0, 255, 191),
        (127, 255, 223),
        (0, 165, 124),
        (82, 165, 145),
        (0, 127, 95),
        (63, 127, 111),
        (0, 76, 57),
        (38, 76, 66),
        (0, 38, 28),
        (19, 38, 33),
        (0, 255, 255),
        (127, 255, 255),
        (0, 165, 165),
        (82, 165, 165),
        (0, 127, 127),
        (63, 127, 127),
        (0, 76, 76),
        (38, 76, 76),
        (0, 38, 38),
        (19, 38, 38),
        (0, 191, 255),
        (127, 223, 255),
        (0, 124, 165),
        (82, 145, 165),
        (0, 95, 127),
        (63, 111, 127),
        (0, 57, 76),
        (38, 66, 76),
        (0, 28, 38),
        (19, 33, 38),
        (0, 127, 255),
        (127, 191, 255),
        (0, 82, 165),
        (82, 124, 165),
        (0, 63, 127),
        (63, 95, 127),
        (0, 38, 76),
        (38, 57, 76),
        (0, 19, 38),
        (19, 28, 38),
        (0, 63, 255),
        (127, 159, 255),
        (0, 41, 165),
        (82, 103, 165),
        (0, 31, 127),
        (63, 79, 127),
        (0, 19, 76),
        (38, 47, 76),
        (0, 9, 38),
        (19, 23, 38),
        (0, 0, 255),
        (127, 127, 255),
        (0, 0, 165),
        (82, 82, 165),
        (0, 0, 127),
        (63, 63, 127),
        (0, 0, 76),
        (38, 38, 76),
        (0, 0, 38),
        (19, 19, 38),
        (63, 0, 255),
        (159, 127, 255),
        (41, 0, 165),
        (103, 82, 165),
        (31, 0, 127),
        (79, 63, 127),
        (19, 0, 76),
        (47, 38, 76),
        (9, 0, 38),
        (23, 19, 38),
        (127, 0, 255),
        (191, 127, 255),
        (82, 0, 165),
        (124, 82, 165),
        (63, 0, 127),
        (95, 63, 127),
        (38, 0, 76),
        (57, 38, 76),
        (19, 0, 38),
        (28, 19, 38),
        (191, 0, 255),
        (223, 127, 255),
        (124, 0, 165),
        (145, 82, 165),
        (95, 0, 127),
        (111, 63, 127),
        (57, 0, 76),
        (66, 38, 76),
        (28, 0, 38),
        (33, 19, 38),
        (255, 0, 255),
        (255, 127, 255),
        (165, 0, 165),
        (165, 82, 165),
        (127, 0, 127),
        (127, 63, 127),
        (76, 0, 76),
        (76, 38, 76),
        (38, 0, 38),
        (38, 19, 38),
        (255, 0, 191),
        (255, 127, 223),
        (165, 0, 124),
        (165, 82, 145),
        (127, 0, 95),
        (127, 63, 111),
        (76, 0, 57),
        (76, 38, 66),
        (38, 0, 28),
        (38, 19, 33),
        (255, 0, 127),
        (255, 127, 191),
        (165, 0, 82),
        (165, 82, 124),
        (127, 0, 63),
        (127, 63, 95),
        (76, 0, 38),
        (76, 38, 57),
        (38, 0, 19),
        (38, 19, 28),
        (255, 0, 63),
        (255, 127, 159),
        (165, 0, 41),
        (165, 82, 103),
        (127, 0, 31),
        (127, 63, 79),
        (76, 0, 19),
        (76, 38, 47),
        (38, 0, 9),
        (38, 19, 23),
        (0, 0, 0),
        (51, 51, 51),
        (102, 102, 102),
        (153, 153, 153),
        (204, 204, 204),
        (255, 255, 255),
    )
    r = RGB_list[id][0]
    g = RGB_list[id][1]
    b = RGB_list[id][2]
    hex = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return hex


def check_wide_image(fb_image):
    """
    Checks if image is suitable for wide version. Performs 'version_generate',
    then controls dimensions. If small, pastes the image on a 1600x800 black
    background replacing original wide version. fb_image is a Fileobject.
    """
    img = fb_image.version_generate("wide")
    if img.width < 1600 or img.height < 800:
        path = Path(settings.MEDIA_ROOT).joinpath(fb_image.version_path("wide"))
        img = Image.open(path)
        back = Image.new(img.mode, (1600, 800))
        position = (
            int((back.width - img.width) / 2),
            int((back.height - img.height) / 2),
        )
        back.paste(img, position)
        back.save(path)
