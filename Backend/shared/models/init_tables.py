from shared.models.books_tables import create_books_table
from shared.models.categories_table import create_categories_table
from shared.models.users_table import create_table_users


async def init_tables(connection):
    await create_table_users(connection=connection)
    await create_categories_table(connection=connection)
    await create_books_table(connection=connection)