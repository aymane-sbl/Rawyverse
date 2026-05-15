async def create_categories_table(connection):
    async with connection.cursor() as cursor:
        await cursor.execute("""CREATE TABLE IF NOT EXISTS categories( 
                                `categories_id` INTEGER PRIMARY KEY AUTO_INCREMENT,
                                `category_name` VARCHAR(300) NOT NULL UNIQUE 
                                )
                                """)