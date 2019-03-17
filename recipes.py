import sqlite3

DB_FILE_PATH = 'data/data.db'


def tuples_to_dictionnary(tuples_list):
    new_list = []
    for row in tuples_list:
        new_dict_item = {
            'recipe_id': row[0],
            'user_id': row[1],
            'title': row[2],
            'image_URL': row[3],
            'category': row[4],
            'description': row[5],
            'ingredients': row[6],
            'count': row[7],
        }
        new_list.append(new_dict_item)
    return new_list

class Recipes:
    def __init__(self):
        '''Set up necessary database objects that will be reused by
        other functions of this class.'''
        self.connection = sqlite3.connect(DB_FILE_PATH)
        self.cursor = self.connection.cursor()
        self.connection.row_factory = sqlite3.Row


    def get_recipes(self, user_id):
        '''Get a list of dictionaries(!) representing recipes that belong
        to the given user.'''
        query = ''' 
            SELECT * FROM recipe
            JOIN user 
            ON user.user_id = recipe.user_id 
            WHERE recipe.user_id = (?)
            ORDER BY count DESC '''
        self.cursor.execute(query, (user_id,))
        recipes_tuples = self.cursor.fetchall()
        recipes = tuples_to_dictionnary(recipes_tuples)
        self.connection.close()
        return recipes


    def get_recipe(self, recipe_id):
        '''Get a dictionary(!) of the data for the dictionary whose ID
        matches the given ID.'''
        query = ''' SELECT * FROM recipe 
                WHERE recipe.recipe_id = (?)'''
        self.cursor.execute(query, (recipe_id,))
        recipe_tuple = self.cursor.fetchall()
        recipe = tuples_to_dictionnary(recipe_tuple)
        return recipe[0]
        self.connection.close()

        
    def add_recipe(self, data, user_id):
        '''Add a recipe to the database. Use the given dictionary of data
        as well as the given user ID as data for the new row.'''
        new_tuple = (user_id, data['title'], data['image_URL'], data['category'], data['description'], data['ingredients'])
        query = "INSERT INTO recipe (user_id, title, image_URL, category, description, ingredients) VALUES(?, ?, ?, ?, ?, ?)"
        self.cursor.execute(query, new_tuple)
        self.connection.commit()
        self.connection.close()

    def delete_recipe(self, recipe_id, user_id):
        query = ''' DELETE FROM recipe
                    WHERE recipe.recipe_id = (?) 
                    AND recipe.user_id = (?) '''
        self.cursor.execute(query, (recipe_id, user_id))
        self.connection.commit()
        self.connection.close()

    def get_all_recipes(self):
            '''Get a list of dictionaries(!) representing recipes that belong
            to the given user.'''
            query = ''' 
                SELECT * FROM recipe
                '''
            self.cursor.execute(query)
            recipes_tuples = self.cursor.fetchall()
            recipes = tuples_to_dictionnary(recipes_tuples)
            self.connection.close()
            return recipes

    def add_recipe_count(self, recipe_id):
        query = ''' INSERT INTO popularity(recipe_id)
                    VALUES (?)
                '''
        self.cursor.execute(query, (recipe_id,))
        self.connection.commit()

    def get_recipe_count(self, recipe_id):
        query = ''' SELECT count(recipe_id)
                    FROM popularity
                    WHERE recipe_id = (?) '''
        self.cursor.execute(query, (recipe_id,))
        count = self.cursor.fetchone()
        return count[0]

    def add_recipe_count_to_recipe_db(self, recipe_id):
        count = self.get_recipe_count(recipe_id)
        query = ''' UPDATE recipe 
                    SET count = (?)
                    WHERE recipe_id = (?) '''
        self.cursor.execute(query, (count, recipe_id))
        self.connection.commit()


