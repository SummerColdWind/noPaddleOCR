from nopaddleocr import OCR

ocr = OCR('./models')
res = ocr('./multi.png', text_only=False)
print(res)
res = ocr('./single.png')
print(res)
res = ocr('./none.png')
print(res)





