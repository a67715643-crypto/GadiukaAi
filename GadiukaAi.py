import cv2
import colorama

while True:

 colorama.init()

 print(colorama.Fore.BLACK)
 print(colorama.Back.LIGHTWHITE_EX)

 print("""               Привіт!
          Про що поговоримо?""")

 user_input = input('Я:')

 if user_input == 'привіт':
  print('Привіт! З чим допомогти?')

 else:

   if user_input == 'як в тебе справи':
    print('У мене все добре, а в тебе як?')
   elif user_input == 'в мене теж все добре':
    print('Супер! Може щось підказати?')
   elif user_input == 'мені сумно':
    print('Не сумуй, все добре, просто заспокойся😉!')

   else:

    if user_input == 'пока':
     print('Пока!')

    else:

     if user_input == 'дякую':
      print('Нема за що😄!')

 if user_input == 'напиши табличку множення':
   for i in range(2, 10):
    for j in range(2, 10):
     print(f'{i} x {j} = {i * j}')
     print('----------')

 else:

  if user_input == 'намалюй змію':
       print("""
                         ____________________ 
                        |  ________________oo|~
       _________________/ /
      |__________________/""")

  else:

       if user_input == 'намалюй кота':
        print("""
           /\    /\ 
          /  \__/  \ 
          | ()   ()|
           \   Y  /
            \____/
           """)

       else:

        if user_input == 'покажи змію':

         snake_img_path = 'thumb-article-420x300-tyc8.jpg'

         img = cv2.imread(snake_img_path)

         print(snake_img_path)
         print('Ось змія.')

       cv2.imshow('Snake', img)
       cv2.waitKey()

       break