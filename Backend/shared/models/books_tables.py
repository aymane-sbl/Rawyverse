async def create_books_table(connection):
    async with connection.cursor() as cursor:
        await cursor.execute("""
                                CREATE TABLE IF NOT EXISTS books (
                                `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
                                `title` VARCHAR(300) UNIQUE NOT NULL,
                                `author` TEXT,
                                `synopsis` TEXT,
                                `category_id` INT,
                                `image_url` TEXT,
                                `file_url` TEXT,
                                `language` TEXT,
                                `year` YEAR,
                                `pages` INT,
                                `genres` TEXT,
                                FOREIGN KEY (`category_id`) REFERENCES categories(`categories_id`)
                                    ON DELETE CASCADE 
                                    ON UPDATE CASCADE
                                )
                                
                             """)