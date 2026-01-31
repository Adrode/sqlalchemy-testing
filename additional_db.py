from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey

engine = create_engine('postgresql+psycopg2://app_user:app_password@localhost:5432/app_add_db', echo=True)

meta = MetaData()

authors = Table(
  'authors',
  meta,
  Column('id', Integer, primary_key=True),
  Column('name', String, nullable=False)
)

books = Table(
  'books',
  meta,
  Column('id', Integer, primary_key=True),
  Column('title', String, nullable=False)
)

authors_books = Table(
  'authors_books',
  meta,
  Column('author_id', Integer, ForeignKey('authors.id')),
  Column('book_id', Integer, ForeignKey('books.id'))
)

meta.create_all(engine)

conn = engine.connect()

join_statement = authors.join(authors_books, authors.c.id == authors_books.c.author_id).join(books, books.c.id == authors_books.c.book_id) 
select_statement = authors.select().with_only_columns(authors.c.name, books.c.title).select_from(join_statement)

result = conn.execute(select_statement)

for row in result.fetchall():
  print(row)