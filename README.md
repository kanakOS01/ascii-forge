# ASCII Forge CLI Tool

## Overview
The ASCII Forge CLI tool is a command-line utility that converts images into ASCII art. It provides various options to customize the output, including width, color, inversion, and file-saving capabilities.

## Features
- Convert images to ASCII art.
- Adjustable output width for clarity.
- Invert ASCII output for different visual effects.
- Choose a color scheme for the output.
- Save output as a `.txt` file.
- Save output as a `.png` file.

## Installation
To install the ASCII Forge CLI tool, use the following command:
```sh
pip install ascii-forge
```

## Usage
To run the tool, use the following command:
```sh
ascii_forge <image_path> [OPTIONS]
```

### Arguments
- `image_path` (required): The path to the image file to be converted.

### Options
| Option | Short Flag | Default | Description |
|--------|------------|---------|-------------|
| `--width` | `-w` | 100 | Width of the ASCII output (affects clarity). |
| `--invert` | `-i` | False | Invert ASCII output. |
| `--color` | `-c` | None | Choose a color scheme from `COLOR_MAP`. The `multi` option works only with `--save-as-png`. |
| `--save-as-txt` | `-st` | None | Save ASCII output to a `.txt` file. |
| `--save-as-png` | `-sp` | None | Save ASCII output to a `.png` file. |

### Example Usage
#### Basic Conversion
```sh
ascii_forge input.jpg
```
#### Adjusting Width
```sh
ascii_forge input.jpg --width 150
```
#### Inverting ASCII Output
```sh
ascii_forge input.jpg --invert
```
#### Saving Output as a Text File
```sh
ascii_forge input.jpg --save-as-txt output.txt
```
#### Saving Output as a PNG
```sh
ascii_forge input.jpg --save-as-png output.png
```
#### Using Color Options
```sh
ascii_forge input.jpg --color red
```

## Running Locally for Development
To set up the development environment locally, follow these steps:

### Directory Structure
```
.
├── ascii_forge
├── ascii_forge.egg-info
├── images
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
└── venv
```

### Steps
1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd ascii_forge
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Run the CLI tool locally:
   ```sh
   pip install --editable .
   ```

5. Make changes and test:
   ```sh
   python -m ascii_forge <image_path>
   ```

## License
This project is licensed under the MIT License.

## Contributions
Contributions are welcome! Feel free to open issues and submit pull requests on GitHub.

## Contact
For any queries or support, reach out via GitHub or email.

