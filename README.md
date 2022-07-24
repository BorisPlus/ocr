# OCR on Python

Установим зависимости (долго):

```shell
pip3 install -r ./requirements.txt
```

Запустим:

```shell
python3 app.py ./src
```

Рядом с распознанным будет лежать в созданной поддиректории `result` файл `.txt`.

Может пригодиться

```shell
python3 -m pip install --upgrade pip

sudo apt-get install libleptonica-dev tesseract-ocr tesseract-ocr-dev libtesseract-dev python3-pil tesseract-ocr-eng tesseract-ocr-script-latn
```