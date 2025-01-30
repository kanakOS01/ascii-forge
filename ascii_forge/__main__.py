import click
from ascii_forge.converter import image_to_ascii
from ascii_forge.config import COLOR_MAP

@click.command()
@click.argument("image_path", type=click.Path(exists=True))
@click.option("--width", "-w", default=100, type=int, help="Width of ASCII ouput (may improve clarity)")
@click.option("--invert", "-i", is_flag=True, help="Invert ASCII output")
@click.option("--color", "-c", default=None, type=click.Choice(COLOR_MAP.keys()), help="Color of ASCII output")
def cli(image_path, width, invert, color):
    """Convert an IMAGE to ASCII Art"""
    ascii_art = image_to_ascii(image_path, width, invert, color)
    click.echo(ascii_art)