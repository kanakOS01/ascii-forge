from PIL import Image, ImageDraw, ImageFont
from colorama import Style
from ascii_forge.config import ASCII_CHARS, COLOR_MAP


def apply_monochrome_color(ascii_art: str, color: str) -> str:
    """Apply a single color to ASCII Art"""
    return COLOR_MAP.get(color) + ascii_art + Style.RESET_ALL


def image_to_ascii(
    image_path: str,
    width: int = 100,
    invert: bool = False,
    color: str = None,
    save_as_txt: str = "",
    save_as_png: str = "",
) -> str:
    """Main functon to convert image to ASCII"""
    
    if color == "multi" and not save_as_png:
        raise Exception("Use 'multi' option only with '--save-as-png'/'-sp' option")

    image = Image.open(image_path)
    w_orig, h_orig = image.width, image.height

    ASCII_CHARS_USED = ASCII_CHARS[::-1] if invert else ASCII_CHARS
    SCALE = width / w_orig
    INTERVAL = len(ASCII_CHARS) / 256
    CHAR_W, CHAR_H = 4, 8
    FONT_FACTOR = CHAR_W / CHAR_H

    image = image.resize((int(SCALE * w_orig), int(SCALE * h_orig * FONT_FACTOR)))
    w_new, h_new = image.width, image.height

    # logic for text output
    if color != "multi":
        image = image.convert("L")
        pixels = list(image.getdata())

        ascii_str = "".join(ASCII_CHARS_USED[int(pixel * INTERVAL)] for pixel in pixels)
        ascii_art = "\n".join(ascii_str[i : i + w_new] for i in range(0, len(ascii_str), w_new))

        if save_as_txt:
            with open(save_as_txt, "w") as ascii_file:
                ascii_file.write(ascii_art)
            ascii_art = f"Saved ASCII art to {save_as_txt}"
        elif color:
            ascii_art = apply_monochrome_color(ascii_art, color)

        return ascii_art

    # logic for png output
    font = ImageFont.load_default()
    output_img = Image.new("RGBA", (CHAR_W * w_new, CHAR_H * h_new), color=(0, 0, 0, 255))
    draw = ImageDraw.Draw(output_img)

    image = image.convert("RGBA")
    pixels = list(image.getdata())

    for i in range(h_new):
        for j, (r, g, b, a) in enumerate(pixels[i * w_new : (i + 1) * w_new]):
            fill = (r, g, b, a) if color == "multi" else None
            gray = int(r / 3 + g / 3 + b / 3)
            draw.text(
                (j * CHAR_W, i * CHAR_H), font=font, text=ASCII_CHARS_USED[int(gray * INTERVAL)], fill=fill
            )

    output_img.save(save_as_png)
    return f"Saved ASCII art to {save_as_png}"
