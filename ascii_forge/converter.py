from PIL import Image, ImageFile
from ascii_forge.config import ASCII_CHARS, COLOR_MAP

def apply_monochrome_color(ascii_art: str, color: str) -> str:
    return color + ascii_art

def resize_image(image: ImageFile.ImageFile, new_width: int) -> ImageFile.ImageFile:
    aspect_ratio = image.height / image.width
    new_height = int(new_width * aspect_ratio * 0.5)    
    return image.resize((new_width, new_height))

def grayify_image(image):
    return image.convert('L')

def image_to_ascii(image_path: str, width: int = 100, invert: bool = False, color=None) -> str:
    image = Image.open(image_path)
    image = resize_image(image, width)
    image = grayify_image(image)
    
    ASCII_CHARS_USED = ASCII_CHARS[::-1] if invert else ASCII_CHARS

    pixels = image.getdata()
    ascii_str = "".join(ASCII_CHARS_USED[pixel // 25] for pixel in pixels)
    ascii_art = "\n".join(ascii_str[i : i + width] for i in range(0, len(ascii_str), width))
    if color: ascii_art = apply_monochrome_color(ascii_art, COLOR_MAP.get(color))
    return ascii_art