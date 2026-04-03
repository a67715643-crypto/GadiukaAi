import colorama
colorama.init()

print(colorama.Fore.BLACK)
print(colorama.Back.LIGHTWHITE_EX)

print("""               Привіт!
          Про що поговоримо?""")

import cv2

cat_img_path = 'cat-underwater.png'

img = cv2.imread(cat_img_path)

print(cat_img_path)

cv2.imshow('Cat', img)
cv2.waitKey()