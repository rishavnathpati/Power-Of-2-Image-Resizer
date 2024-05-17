# Power Of 2 Image Resizer

Power Of 2 Image Resizer is a tool that resizes images to the nearest power of 2 dimensions, making them suitable for use in game engines.

## Features

- Resize images to the nearest power of 2
- Center images and expand to fit the canvas without distortion
- Batch processing of images
- Configurable settings for threshold and compression
- GUI for ease of use

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/rishavnathpati/Power-Of-2-Image-Resizer.git
   cd Power-Of-2-Image-Resizer
   ```

2. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the application:
   ```sh
   python src/main.py
   ```

## Usage

1. **Open the Application**:
    - Navigate to the directory where you cloned the repository.
    - Run the application using:
      ```sh
      python src/main.py
      ```

2. **Select a File or Directory**:
    - Use the "Browse File" button to select a single image file.
    - Use the "Browse Directory" button to select a directory containing multiple image files.

3. **Start Processing**:
    - Click the "Start Processing" button to begin resizing the selected images.
    - The status and progress of the processing will be displayed in the application.

![Screenshot](docs/screenshot.png)

## Configuration

### Configuration via `config.txt`

You can configure Power Of 2 Image Resizer by editing the `config.txt` file in the root directory. The following settings are available:

- **THRESHOLD**: The threshold for resizing. This determines how close the image size should be to the power of 2 size before resizing (default is `0.25`).
- **COMPRESSION**: The compression level for saving images. This affects the output quality of the resized images (default is `0`).

Example `config.txt` file:
```plaintext
THRESHOLD=0.25
COMPRESSION=0
```

### Configuration via GUI

1. **Open Settings**:
    - Click the "Settings" button in the main application window.

2. **Adjust Settings**:
    - Modify the threshold and compression settings as needed.
    - Click "Save" to apply the new settings.

## Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork the Repository**:
    - Click the "Fork" button at the top right of the repository page on GitHub.

2. **Clone Your Fork**:
    ```sh
    git clone https://github.com/yourusername/Power-Of-2-Image-Resizer.git
    cd Power-Of-2-Image-Resizer
    ```

3. **Create a Branch**:
    ```sh
    git checkout -b feature/your-feature-name
    ```

4. **Make Your Changes**:
    - Implement your feature or bug fix.
    - Write tests to cover your changes (if applicable).

5. **Run Tests**:
    ```sh
    pytest
    ```

6. **Commit Your Changes**:
    ```sh
    git commit -m "Description of your changes"
    ```

7. **Push to Your Fork**:
    ```sh
    git push origin feature/your-feature-name
    ```

8. **Create a Pull Request**:
    - Go to the original repository on GitHub.
    - Click "New Pull Request" and follow the instructions.

Please read the [contributing guidelines](docs/CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Credits

- Developed by Rishav Nath Pati
- Uses the Pillow and Pygame libraries