import tesserocr
from PIL import Image



image1 = Image.open('code1.jpg')
result1= tesserocr.image_to_text(image1)
image2 = Image.open('code4.jpg')
result2= tesserocr.image_to_text(image2)
print(result2)
# image_l = image2. convert('L')
# image2.show()
# result3= tesserocr.image_to_text(image2)
# print(result1)
# print(result2)


image2 = image2. convert('L')
threshold= 128
table= []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image2 = image2.point(table,'1')
image2.show()
result22= tesserocr.image_to_text(image2)
print(result22)