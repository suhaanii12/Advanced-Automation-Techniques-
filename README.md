# Advanced-Automation-Techniques-

This example includes image loading, pre-processing, and text extraction:

1. Import Libraries:

       ¤ cv2 for OpenCV operations.

       ¤ pytesseract for OCR operations.

       ¤ PIL (Python Imaging Library) for handling image operations.

       ¤ pyocr for another OCR tool.


2. Set Tesseract Path:

       ¤ pytesseract.pytesseract.tesseract_cmd: Set this to the path where Tesseract OCR is installed.


3. Function ocr_pytesseract:

       ¤ Read the image using OpenCV.

       ¤ Convert the image to grayscale for better OCR accuracy.

       ¤ Apply thresholding to create a binary image.

       ¤ Use pytesseract.image_to_string() to extract text from the pre-processed image.


4. Function ocr_pyocr:

       ¤ Use pyocr.get_available_tools() to get the available OCR tools.

       ¤ Read the image using PIL.

       ¤ Use tool.image_to_string() with pyocr.builders.TextBuilder() to extract text from the image.


5. Main Function:

       ¤ Define the path to your image file.

       ¤ Call both ocr_pytesseract and ocr_pyocr functions to get the recognized text using both methods.

       ¤ Print the extracted text to the console.
