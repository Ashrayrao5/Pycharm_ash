# import sqlite3 as sql
# conn = sql.connect("test.db")
# cursor = conn.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
# # cursor.execute("INSERT INTO users VALUES (1, 'John')")
# # cursor.execute("INSERT INTO users(name) VALUES ('Alice')")
# # cursor.execute("INSERT INTO users(name) VALUES ('Bob')")
# conn.commit()
#
# cursor.execute("SELECT * FROM users")
# print(cursor.fetchall())
# conn.close()
#



# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.orm import declarative_base, sessionmaker
#
# Base = declarative_base()
#
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#
# engine = create_engine('sqlite:///sql_alchemy.db')
# Base.metadata.create_all(engine)
#
# Session = sessionmaker(bind=engine)
# session = Session()

# new_user = User(name='Alice')
# session.add(new_user)
# session.commit()
#
# users = session.query(User).all()
#
#
#
#
# def new_user(name):
#     new_user = User(name=name)
#     session.add(new_user)
#     session.commit()

# new_user(name='Alice')
# new_user(name='Bob')
# new_user(name='Charlie')
#
# name = ['a', 'b', 'c']
# for x in name:
#     new_user(x)
#
# a = session.query(User).all()
#
#
# for user in a:
#     print(user.id, user.name)








