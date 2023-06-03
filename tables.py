from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
)


meta_obj = MetaData()
users_table = Table(
    "users",
    meta_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(25), nullable=False),
    Column("fullname", Text(25), nullable=False),
)
comments_table = Table(
    "comments",
    meta_obj,
    Column("id", Integer, primary_key=True),
    Column("comment", Text, nullable=False),
    Column("user_id", ForeignKey("users.id")),
)
