from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="ascii-forge",
    version="1.0.0",
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
    packages=find_packages(),
    install_requires=[
        "Click", 
        "Pillow", 
        "Colorama"
    ],
    keywords="ascii-forge ascii forge ascii-art art",
    entry_points={
        "console_scripts": [
            "ascii-forge=ascii_forge:cli",
        ],
    },
)
