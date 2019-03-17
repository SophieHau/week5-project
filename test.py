import sqlite3


DB_FILE_PATH = 'data/data.db'

connection = sqlite3.connect(DB_FILE_PATH)
cursor = connection.cursor()
connection.row_factory = sqlite3.Row

recipe_id = 10 
user_id = 1

query = ''' DELETE FROM recipe
                    WHERE recipe.recipe_id = (?) 
                    AND recipe.user_id = (?) '''
cursor.execute(query, (recipe_id, user_id))
connection.commit()
connection.close()