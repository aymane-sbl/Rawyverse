
from shared.errors.admin_errors import AdminError

# check admin
def check_is_admin(payload,lang):
    if payload["role"] != "admin":
        raise AdminError(lang["admin"]["permissions"]["denied"])

async def check_categories_is_exists(connection,category_name):
    async with connection.cursor() as cursor:
       await cursor.execute("SELECT `category_name` FROM categories WHERE `category_name` = %s",(category_name,))
       result=await cursor.fetchone()
       return result is not None

# check books
async def check_books_is_exists(connection,title):
    async with connection.cursor() as cursor:
        await cursor.execute("SELECT `title` FROM books WHERE `title` = %s",(title,))
        result = await cursor.fetchone()
        return result is not None