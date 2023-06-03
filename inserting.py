from sqlalchemy import insert
from tables import users_table
from connect import engine

# statement = insert(users_table)
# print(statement)  # u can see query of this statement

# statement = insert(users_table).values(
#     name="paul",
#     fullname="starodub pavlo",
# )

# with engine.connect() as conn:  # insert single row
#     conn.execute(statement)
#     conn.commit()


statement = insert(users_table)

with engine.connect() as conn:
    conn.execute(
        statement,
        [
            {"name": "Joe", "fullname": "Joe Bidden"},
            {"name": "Sponge", "fullname": "Sponge Bob"},
        ],
    )
    conn.commit()
