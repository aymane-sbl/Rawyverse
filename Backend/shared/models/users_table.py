async def create_table_users(connection):
    async with connection.cursor() as cursor:
        await cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS users(
            `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
            `user_name` VARCHAR(255) UNIQUE,
            `email` VARCHAR(255) UNIQUE NOT NULL,
            `password` TEXT,
            `is_verified` BOOLEAN NOT NULL DEFAULT FALSE  ,
            `role` ENUM("user","admin") NOT NULL DEFAULT  "user",
            `created_at` TIMESTAMP NOT NULL DEFAULT  CURRENT_TIMESTAMP
            
            )
        """)