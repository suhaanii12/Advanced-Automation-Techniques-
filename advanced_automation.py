import cv2
import pytesseract
from PIL import Image
import pyocr
import pyocr.builders

# Set the path to the Tesseract executable
# Note: Change the path according to your Tesseract-OCR installation path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to perform OCR using pytesseract
def ocr_pytesseract(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply some pre-processing (if necessary)
    # E.g., thresholding
    _, threshold_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)
    
    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(threshold_image)
    
    return text

# Function to perform OCR using pyocr
def ocr_pyocr(image_path):
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        return None
    tool = tools[0]  # Use the first available tool
    
    # Read the image using PIL
    image = Image.open(image_path)
    
    # Use pyocr to do OCR on the image
    text = tool.image_to_string(image, builder=pyocr.builders.TextBuilder())
    
    return text

def main():
    # Path to the image file
    image_path = 'path_to_your_image.jpg'
    
    # Perform OCR using pytesseract
    text_pytesseract = ocr_pytesseract(image_path)
    print("Recognized Text using pytesseract:")
    print(text_pytesseract)
    
    # Perform OCR using pyocr
    text_pyocr = ocr_pyocr(image_path)
    print("\nRecognized Text using pyocr:")
    print(text_pyocr)

if __name__ == "__main__":
    main()
