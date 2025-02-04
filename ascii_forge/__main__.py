import click
from ascii_forge.converter import image_to_ascii
from ascii_forge.config import COLOR_MAP


@click.command()
@click.argument("image_path", type=click.Path(exists=True))
@click.option("--width", "-w", default=100, type=int, help="Width of ASCII ouput (may improve clarity)")
@click.option("--invert", "-i", is_flag=True, help="Invert ASCII output")
@click.option(
    "--color",
    "-c",
    default=None,
    type=click.Choice(COLOR_MAP.keys()),
    help="Color of ASCII output. 'multi' value only works with '--save-as-png' option",
)
@click.option("--save-as-txt", "-st", type=click.Path(), help="Save ASCII output to a .txt file")
@click.option("--save-as-png", "-sp", type=click.Path(), help="Save ASCII output to a .png file")
def cli(image_path, width, invert, color, save_as_txt, save_as_png):
    """Convert an IMAGE to ASCII Art"""
    try:
        ascii_art = image_to_ascii(image_path, width, invert, color, save_as_txt, save_as_png)
        click.echo(ascii_art)
    except Exception as e:
        print(str(e))