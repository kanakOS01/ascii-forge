from setuptools import setup

setup(
    name="ascii-forge",
    version="0.1",
    py_modules=["ascii_forge"],
    install_requires=["Click", "Pillow", "Colorama"],
    entry_points={
        "console_scripts": [
            "ascii-forge=ascii_forge.__main__:cli",
        ],
    },
)