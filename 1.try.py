from pytesseract import image_to_string
import pytesseract


if __name__ == '__main__':

    pytesseract.pytesseract.tesseract_cmd = '/home/vishnupriya/projects/shopApp/venv/lib/python3.8/site-packages/tesseract'
    print(pytesseract.image_to_string('/home/riafy.jpg'))
 

    