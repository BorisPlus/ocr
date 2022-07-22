import sys
import os
#
import pytesseract
import cv2
# import matplotlib.pyplot as plt
# from PIL import Image


def ocr(file):
    image = cv2.imread(file)
    string = pytesseract.image_to_string(image)
    with open(f'{file}.txt', 'w') as txt:
        txt.write(string)


def massive_ocr(source):
    for (subdir, _, files) in os.walk(source):
        for file in files:
            full_path = os.path.join(subdir, file)
            try:
                ocr(full_path)
            except Exception as e:
                print(f'Error of {full_path}: {e}')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sources_dirs = ["./src"]
    else:
        sources_dirs = sys.argv[1:]

    for source in sources_dirs:
        massive_ocr(source)

