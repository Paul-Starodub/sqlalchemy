from sqlalchemy import create_engine, text


# print(sqlalchemy.__version__)  # version
engine = create_engine("sqlite:///sample.db", echo=True)  # echo show sql query


with engine.connect() as conn:  # create cursor with sample.db
    pass
    # conn.execute(text("SELECT 'Hello'"))  # create sample.db
