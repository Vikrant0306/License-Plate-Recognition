# License Plate Recognition

## Project Overview

This project involves developing a License Plate Recognition (LPR) system using machine learning techniques in Python. The system is designed to accurately detect and recognize vehicle license plates from images.

## Features

- **License Plate Detection**: Identifies and extracts the license plate from an image.
- **Character Recognition**: Decodes the characters on the license plate using optical character recognition (OCR).
- **Preprocessing**: Includes image preprocessing steps to enhance recognition accuracy.

## Technologies Used

- **Python**: Programming language used for implementing the project.
- **OpenCV**: Library for image processing.
- **Tesseract OCR**: Optical character recognition engine.
- **NumPy**: Library for numerical operations.
- **Matplotlib**: Library for visualizing images.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python packages (listed in `requirements.txt`)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Vikrant0306/License-Plate-Recognition.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd License-Plate-Recognition
   ```

3. **Set Up Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## File Structure

- `recognize_license_plate.py`: Main script for license plate recognition.
- `requirements.txt`: List of Python dependencies.
- `images/`: Directory to store input images.
- `output/`: Directory where results and processed images are saved.
- `README.md`: This file.

## Contributing

Feel free to open issues or submit pull requests to contribute to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [OpenCV](https://opencv.org/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
