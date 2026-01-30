from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, Date

engine = create_engine('postgresql+psycopg2://app_user:app_password@localhost:5432/app_db', echo=True)

meta = MetaData()

people = Table(
  "people",
  meta,
  Column('id', Integer, primary_key=True),
  Column('name', String, nullable=False),
  Column('age', Integer)
)

cars = Table(
  "cars",
  meta,
  Column('id', Integer, primary_key=True),
  Column('make', String),
  Column('model', String),
  Column('year', Date)
)

meta.create_all(engine)

conn = engine.connect()

insert_statement = people.insert().values(name='Adrian', age=26)
result = conn.execute(insert_statement)

conn.commit()