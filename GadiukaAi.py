import colorama
colorama.init()

print(colorama.Fore.BLACK)
print(colorama.Back.LIGHTWHITE_EX)

print("""               Привіт!
          Про що поговоримо?""")

input = input('Я:')

if input == 'покажи змію':
 import cv2

snake_img_path = 'thumb-article-420x300-tyc8.jpg'

img = cv2.imread(snake_img_path)

print(snake_img_path)
print('Ось змія.')

cv2.imshow('Snake', img)
cv2.waitKey()
