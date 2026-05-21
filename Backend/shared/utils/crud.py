async def update_any_column(table,column_name,new_value,unique_column,value_unique_column,connection,result):
    async with connection.cursor() as cursor:
        await cursor.execute("""UPDATE FROM %s SET %s = %s WHERE %s = %s""",(table,column_name,new_value,unique_column,value_unique_column))
        await connection.commit()
        return {
            "status":True,
            "msg":result
        }