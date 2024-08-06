import sqlite3



def init_db():
    conn = sqlite3.connect("pokemontam.db")
    cursor = conn.cursor()

    # Create a table to store card information and quantity
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pokemons (
            id TEXT PRIMARY KEY,
            name TEXT,
            height TEXT,
            weight TEXT,
            types TEXT,
            abilites TEXT,
            quntity INT 
        )
    ''')

    conn.commit()
    conn.close()
init_db()
