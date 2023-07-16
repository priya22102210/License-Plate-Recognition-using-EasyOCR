# License Plate Recognition using EasyOCR

License Plate Recognition using EasyOCR is a Python project that demonstrates the implementation of Optical Character Recognition (OCR) for license plate detection. This project aims to provide a simple and efficient solution for extracting and recognizing license plate numbers from images.

## Installation

To run this project, you need to install the required packages. Run the following command to install the dependencies:

```shell
pip install -r requirements.txt
```

## Usage

To use this project, follow these steps:

1. Import the necessary libraries:
   - `cv2`: OpenCV library for image processing.
   - `pyttsx3`: Text-to-speech library for speech output.
   - `easyocr`: OCR library for text detection and recognition.
   - `imutils`: Convenience functions for image processing tasks.

2. Load the input image using `cv2.imread()`.

3. Preprocess the image by applying filters and edge detection techniques to enhance the license plate region.

4. Use EasyOCR to perform text recognition on the license plate region.

5. Display the recognized license plate number and any additional visualizations.

## Examples

Here are some examples of how to use the project:

```python
# Import libraries
import cv2
import pyttsx3
import easyocr
import imutils

# Load image
img = cv2.imread("image.jpg")

# Preprocess the image

# Perform license plate recognition

# Display the results
```

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to contribute, report issues, and submit pull requests to enhance the project.

## Credits

This project utilizes the following libraries:

- [EasyOCR](https://github.com/JaidedAI/EasyOCR)
- [OpenCV](https://opencv.org/)
- [pyttsx3](https://github.com/nateshmbhat/pyttsx3)
- [imutils](https://github.com/jrosebr1/imutils)


