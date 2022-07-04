import sqlite3

def translate(word, direction):
    with sqlite3.connect("yoranish.db") as con:
        cur = con.cursor()

        if direction == 0:
            query = "SELECT czech_word FROM czech_words WHERE reference_id IN (SELECT yorani_id FROM yorani_words WHERE yorani_word IS (?) COLLATE NOCASE);"
        else:
            query = "SELECT yorani_word FROM yorani_words WHERE yorani_id IN (SELECT reference_id FROM czech_words WHERE czech_word IS (?) COLLATE NOCASE);"
            
        cur.execute(query, [word])
        answer = cur.fetchall()
        if answer:
            return answer
        else:
            return 0
