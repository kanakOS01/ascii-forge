from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="ascii-forge",
    version="0.3",
    author="Kanak Tanwar",
    author_email="kanaktanwarpro@gmail.com",
    description="Turn your images into ASCII art from your terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kanakOS01/ascii-forge",
    project_urls={
        "GitHub Repository": "https://github.com/kanakOS01/ascii-forge",
        "PyPI Project Page": "https://pypi.org/project/ascii-forge/"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
    py_modules=["ascii_forge"],
    install_requires=[
        "Click", 
        "Pillow", 
        "Colorama"
    ],
    keywords="ascii-forge ascii forge ascii-art art",
    entry_points={
        "console_scripts": [
            "ascii-forge=ascii_forge.__main__:cli",
        ],
    },
)
