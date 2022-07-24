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
    result_dir = os.path.join(os.path.dirname(file), 'result')
    file_name = os.path.basename(file)
    if not os.path.exists(result_dir) or (os.path.exists(result_dir) and os.path.isfile(result_dir)):
        os.makedirs(result_dir)
    with open(os.path.join(result_dir, f'{file_name}.txt'), 'w') as txt:
        txt.write(string)


def massive_ocr(source):
    for (subdir, _, files) in os.walk(source):
        files_count = len(files)
        file_counter = 0
        for file in files:
            full_path = os.path.join(subdir, file)
            error_msg = ''
            try:
                ocr(full_path)
            except Exception as e:
                error_msg = str(e)
            file_counter += 1
            yield subdir, file, file_counter, files_count, error_msg


if __name__ == '__main__':

    if len(sys.argv) == 1:
        targets = ["./example"]
    else:
        targets = sys.argv[1:]

    abs_targets = []
    for target in targets:
        abs_targets.append(os.path.abspath(target))

    for target in abs_targets:
        current_folder = ''
        for step in massive_ocr(target):
            if current_folder != step[0]:
                if current_folder != '':
                    print(f'{current_folder}: 100% done')
                current_folder = step[0]
            # print(f'\r{step[0]} : {step[1]} : {step[2]} of {step[3]} files. {step[4]}', end='', flush=False)
            print(f'{step[0]}: {step[1]} : {step[2]} of {step[3]} files. {step[4]}')
        if current_folder != '':
            print(f'{current_folder}: 100% done')
        print(f'')

