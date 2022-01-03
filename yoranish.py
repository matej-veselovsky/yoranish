def divide_chunks(input_list, n):
    for i in range(0, len(input_list), n):
        yield input_list[i:i + n]


def translate(word, direction):
    for phrase in dictionary:
        if word.lower() == phrase[direction].lower():
            return phrase[1 - direction]
    return "---NENALEZENO---"


# z txt seznamu, kde je na každém řádku jedno slovo vytvoří mega-list, kde každá položka je list-dvojice joranština-čeština
with open("yoranish.txt", "r", encoding="utf-8-sig") as file:
    content_list = file.read().split("\n")
    dictionary = list(divide_chunks(content_list, 2))
