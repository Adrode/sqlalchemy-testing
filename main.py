from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, Date, ForeignKey

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
  Column('year', Integer),
  Column('owner', Integer, ForeignKey('people.id'), unique=True)
)

meta.create_all(engine)

conn = engine.connect()

statement = cars.insert().values([
    {'make': 'Ford', 'model': 'Mustang', 'year': 1969, 'owner': 1},
    {'make': 'Opel', 'model': 'Astra', 'year': 2005, 'owner': 3},
    {'make': 'Toyota', 'model': 'Camry', 'year': 2024, 'owner': 4},
  ]
)
result = conn.execute(statement)

conn.commit()