import click
from ascii_forge.converter import image_to_ascii

@click.command()
@click.argument("image_path", type=click.Path(exists=True))
@click.option("--width", "-w", default=100, type=int, help="Width of ASCII ouput")
@click.option("--invert", "-i", is_flag=True, help="Invert ASCII characters")
def cli(image_path, width, invert):
    """Convert an IMAGE to ASCII Art"""
    ascii_art = image_to_ascii(image_path, width, invert)

    click.echo(ascii_art)