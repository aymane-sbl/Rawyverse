# check books
async def check_books_is_exists(connection,title):
    async with connection.cursor() as cursor:
        await cursor.execute("SELECT `title` FROM books WHERE `title` = %s",(title,))
        result = await cursor.fetchone()
        return result is not None