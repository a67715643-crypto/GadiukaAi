import colorama
colorama.init()

print(colorama.Fore.BLACK)
print(colorama.Back.LIGHTWHITE_EX)

print("""               Привіт!
          Про що поговоримо?""")

input()
if input() == 'намалюй змію':
    print("""
                       _____________________
                      |  _________________oo|__
    __________________/ /
   |___________________/""")

if input() == 'намалюй кота':
    print("""
              ||     ||
             | _| _ |_ |
            |           |
            |  O     O  |
             \    Y    /
              \ X W X /
               \_____/
    """)