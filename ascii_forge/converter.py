from PIL import Image, ImageFile
from ascii_forge.config import ASCII_CHARS, COLOR_MAP

def apply_monochrome_color(ascii_art, color):
    return color + ascii_art

def image_to_ascii(image_path: str, width: int = 100, invert: bool = False, color=None) -> ImageFile.ImageFile:
    image = Image.open(image_path)
    aspect_ratio = image.height / image.width
    new_height = int(width * aspect_ratio * 0.5)

    image = image.resize((width, new_height)).convert('L')
    
    if invert:
        ASCII_CHARS_USED = ASCII_CHARS[::-1]
    else:
        ASCII_CHARS_USED = ASCII_CHARS

    pixels = image.getdata()
    ascii_str = "".join(ASCII_CHARS_USED[pixel // 25] for pixel in pixels)
    ascii_art = "\n".join(ascii_str[i : i + width] for i in range(0, len(ascii_str), width))
    if color: ascii_art = apply_monochrome_color(ascii_art, COLOR_MAP.get(color))
    return ascii_art