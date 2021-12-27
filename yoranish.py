from time import sleep
intro = """
 __   _____  ____      _    _   _ ___ ____  _   _    ___   _ 
 \ \ / / _ \|  _ \    / \  | \ | |_ _/ ___|| | | |  / _ \ / |
  \ V / | | | |_) |  / _ \ |  \| || |\___ \| |_| | | | | || |
   | || |_| |  _ <  / ___ \| |\  || | ___) |  _  | | |_| || |
   |_| \___/|_| \_\/_/   \_\_| \_|___|____/|_| |_|  \___(_)_|

Joranština je jazyk vytvořený Lukášem Tomáškem. Verze slovníku: 0.1
Pro překlad nejprve zvolte žádaný směr (1 nebo 2), následně zadejte hledané slovo.
Slovník je case-insensitive.
"""


def divide_chunks(input_list, n):
    for i in range(0, len(input_list), n):
        yield input_list[i:i + n]


def translate(word, direction):
    for phrase in dictionary:
        if word == phrase[direction]:
            return phrase[1 - direction]
    return "---NENALEZENO---"


def prompt_user():
    direction = int(input("Pro překlad zvolte žádaný směr:\n1) Joranština --> Čeština\n2) Čeština --> Joranština\n")) - 1
    if direction != 0 and direction != 1:
        print("Překlad možný pouze ve dvou nabízených směrech!")
        prompt_user()
    else:
        user_input = input("Slovo: ").lower()
        print(f"Překlad: {translate(user_input, direction)}")


# z txt seznamu, kde je na každém řádku jedno slovo vytvoří mega-list, kde každá položka je list-dvojice joranština-čeština
yoranish_content = open("yoranish.txt", "r", encoding="utf-8-sig")
content_read = yoranish_content.read()
content_list = content_read.split("\n")
dictionary = list(divide_chunks(content_list, 2))

# print(intro)

# while True:
#     prompt_user()
#     user_answer = input("Přejete si hledat další slovo? (A/N)\n").lower()
#     if user_answer != "a":
#        print("Ukončuji program. Nashledanou. Diowiedia ")
#        break

# sleep(3)
