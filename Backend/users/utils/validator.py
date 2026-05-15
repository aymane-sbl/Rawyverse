async def check_user_exists(username,connection):
    async with connection.cursor() as cursor:
        await cursor.execute("SELECT `user_name` FROM `users` WHERE `user_name`=%s",(username,))
        result = await cursor.fetchone()
        return result is not None

async def check_email_exists(email,connection):
    async with connection.cursor() as cursor:
        await cursor.execute("SELECT `email` FROM `users` WHERE `email`=%s",(email,))
        result = await cursor.fetchone()
        return result is not None