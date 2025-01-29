from PIL import Image

ASCII_CHARS = "@#%*=+-:,. "

def image_to_ascii(image_path, width=100, invert=True):
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
    return ascii_art