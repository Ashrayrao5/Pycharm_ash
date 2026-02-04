# movieId	title	genres
# 1	Toy Story (1995)	Adventure|Animation|Children|Comedy|Fantasy
# 2	Jumanji (1995)	Adventure|Children|Fantasy
# 3	Grumpier Old Men (1995)	Comedy|Romance
# 4	Waiting to Exhale (1995)	Comedy|Drama|Romance
# 5	Father of the Bride Part II (1995)	Comedy
# 6	Heat (1995)	Action|Crime|Thriller


# "C:\Users\ashri\OneDrive\Desktop\Pandas_Assign\Output\top_rated_movies_report.csv"


import csv
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


# DEFINE TABLE USING A CLASS

class Movie(Base):
    __tablename__ = "movies"

    movie_id = Column(Integer, primary_key=True)
    title = Column(String)
    genre = Column(String)


    def __repr__(self):
        return f"Movie(id={self.movie_id}, title='{self.title}', genre={self.genre})"


engine = create_engine("sqlite:///movies_orm.db")

Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


def load_movies_from_csv(csv_file, session):

    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            movie = Movie(
                movie_id=int(row["movieId"]),
                title=row["title"],
                genre=row["genres"]
            )

            session.add(movie)

        session.commit()

# load_movies_from_csv("C:\\Users\\ashri\\OneDrive\\Desktop\\Pandas_Assign\\Raw Data\\ movies.csv", session)


movies = session.query(Movie).all()

print("\nInserted Movies:")
for movie in movies:
    print(movie)

# print("\nInserted Genres:")
# for movie in movies:
#     print(movie.title)