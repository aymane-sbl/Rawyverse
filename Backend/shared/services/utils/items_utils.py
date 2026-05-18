# check books
async def check_item_is_exists(connection,title):
    async with connection.cursor() as cursor:
        await cursor.execute("SELECT `title` FROM books WHERE `title` = %s",(title,))
        result = await cursor.fetchone()
        return result is not None

# get Specific items
async def get_specific_items(connection,category_id):
    async with connection.cursor() as cursor:
        await cursor.execute("SELECT id,title,author,category_id,image_url,language,year,pages,file_url,genres,synopsis FROM `books` WHERE `category_id` = %s",(category_id,))
        data = await cursor.fetchall()
        return {
            "success": True,
            "data": data
        }