import ddddocr

ocr = ddddocr.DdddOcr(old=True)

with open("20210715203841893.png", 'rb') as f:
    image = f.read()

res = ocr.classification(image)
print(res)