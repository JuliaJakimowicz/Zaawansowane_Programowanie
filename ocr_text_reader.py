

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def read_text_from_image(image_path):
    """
    Funkcja do odczytywania tekstu z obrazu.
    :param image_path: Ścieżka do pliku obrazu
    :return: Odczytany tekst
    """
    img = cv2.imread(image_path)

    if img is None:
        return f"Błąd: Nie udało się wczytać obrazu z {image_path}"

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray_img, lang='eng')  # 'eng' można zmienić na inny język
    return text

image_paths = [
    'C:/Users/jakim/Downloads/257-682.jpg',
]

for img_path in image_paths:
    print(f'Tekst z obrazu {img_path}:')
    print(read_text_from_image(img_path))
    print('-' * 50)
