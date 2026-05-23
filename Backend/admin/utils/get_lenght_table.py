async def get_lenght_table(connection,column,table):
    async with connection.cursor() as cursor:
        await cursor.execute(f"SELECT COUNT(`{column}`) as count FROM `{table}`")
        data = await cursor.fetchone()
        return {
            "success": True,
            "length": data["count"]
        }