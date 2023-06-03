from tables import users_table
from connect import engine
from sqlalchemy import select


# statement = select(users_table)
# print(statement)  # u can see ur query
# with engine.connect() as conn:  # retrieve all users
#     result = conn.execute(statement)
#     for row in result:
#         print(f"User name: {row.name}")


# print(users_table.c.name)  # access to column in db
statement = select(users_table).where(users_table.c.name == "Joe")
with engine.connect() as conn:  # retrieve specify user with condition
    result = conn.execute(statement)
    for row in result:
        print(f"User name: {row.name}")
