
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random

# MySQL 데이터베이스에 연결하기 위한 엔진 생성
engine = create_engine('mysql+pymysql://root:oz-password@localhost:3306/airportdb')


# 테이블별로 다른 더미 데이터를 생성하기 위한 함수 정의

def generate_airport_data(session, num_data, delete_existing_data=False):
    metadata = MetaData()
    metadata.reflect(bind=engine)
    table = metadata.tables['airport']
    if delete_existing_data:
        session.execute(table.delete())
    for _ in range(num_data):
        fake_iata = fake.bothify(text='???')
        fake_icao = fake.bothify(text='????')
        fake_name = fake.name()
        session.execute(table.insert().values(iata=fake_iata, icao=fake_icao, name=fake_name))

def generate_airline_data(session, num_data, delete_existing_data=False):
    metadata = MetaData()
    metadata.reflect(bind=engine)
    table = metadata.tables['airline']
    if delete_existing_data:
        session.execute(table.delete())
    for _ in range(num_data):
        fake_iata = fake.bothify(text='??')
        fake_airlinename = fake.word()
        fake_base_airport = random.randint(1,1000)
        session.execute(table.insert().values(iata=fake_iata, airlinename=fake_airlinename, base_airport=fake_base_airport))

def generate_airplane_type_data(session, num_data, delete_existing_data=False):
    metadata = MetaData()
    metadata.reflect(bind=engine)
    table = metadata.tables['airplane_type']
    if delete_existing_data:
        session.execute(table.delete())
    for _ in range(num_data):
        fake_identifier = fake.word()
        fake_description = fake.sentence()
        session.execute(table.insert().values(identifer=fake_identifier, description=fake_description))
        
def generate_airplane_data(session, num_data, delete_existing_data=False):
    metadata = MetaData()
    metadata.reflect(bind=engine)
    table = metadata.tables['airplane']
    if delete_existing_data:
        session.execute(table.delete())
    for _ in range(num_data):
        fake_capacity = random.randint(1,32000)
        fake_type_id = random.randint(1,32000)
        fake_airline_id = random.randint(1,32000)
        session.execute(table.insert().values(capacity=fake_capacity, type_id=fake_type_id, airline_id=fake_airline_id))

def generate_airport_geo_data(session, num_data, delete_existing_data=False):
    metadata = MetaData()
    metadata.reflect(bind=engine)
    table = metadata.tables['airport_geo']
    if delete_existing_data:
        session.execute(table.delete())
    for _ in range(num_data):
        fake_airport_id = random.randint(1,32000)
        fake_name = fake.name()
        fake_city = fake.city()
        fake_country = fake.country()
        fake_latitude = fake.latitude()
        fake_longitude = fake.longitude()
        session.execute(table.insert().values(airport_id=fake_airport_id, name=fake_name, city=fake_city, country=fake_country, latitude=fake_latitude, longitude=fake_longitude))

def generate_airplane_reachable_data(session, num_data, delete_existing_data=False):
    metadata = MetaData()
    metadata.reflect(bind=engine)
    table = metadata.tables['airplane_reachable']
    if delete_existing_data:
        session.execute(table.delete())
    for _ in range(num_data):
        fake_airport_id = random.randint(1,32000)
        fake_hops = random.randint(1,32000)
        session.execute(table.insert().values(airport_id = fake_airport_id, hops = fake_hops))

def generate_booking_data(session, num_data, delete_existing_data=False):
    metadata = MetaData()
    metadata.reflect(bind=engine)
    table = metadata.tables['booking']
    if delete_existing_data:
        session.execute(table.delete())
    for _ in range(num_data):
        fake_flight_id = random.randint(1,32000)
        fake_seat = fake.bothify(text='????')
        fake_passenger_id = random.randint(1,32000)
        fake_price = round(random.uniform(10, 1000), 2)
        session.execute(table.insert().values(flight_id = fake_flight_id, seat = fake_seat, passenger_id = fake_passenger_id, price = fake_price))

def generate_employee_data(session, num_data, delete_existing_data=False):
    metadata = MetaData()
    metadata.reflect(bind=engine)
    table = metadata.tables['employee']
    if delete_existing_data:
        session.execute(table.delete())
    for _ in range(num_data):
        fake_employee_id = random.randint(1,32000)
        fake_firstname = fake.firstname()
        fake_lastname = fake.lastname()
        fake_birthdate = fake.date()
        fake_sex = random.choice(["f","m"])
        fake_street = fake.street()
        fake_city = fake.city()
        fake_zip = fake.zip()
        fake_country = fake.country()
        fake_emailaddress = fake.email()
        fake_telephoneno = fake.phone_number()
        fake_salary = round(random.uniform(5000,20000),2)
        fake_department = random.choice(["Marketing","Buchhaltung","Management","Logistik","Flugfeld"])
        fake_username = fake.name()
        fake_password = fake.password()
        session.execute(table.insert().values(employee_id = fake_employee_id, firstname = fake_firstname, lastname = fake_lastname, birthdate = fake_birthdate, sex = fake_sex, street = fake_street, city = fake_city, zip = fake_zip, country = fake_country, emailaddress = fake_emailaddress, telephoneno = fake_telephoneno, salary = fake_salary, department = fake_department, username = fake_username, password = fake_password))

def generate_booking_data(session, num_data, delete_existing_data=False):
    metadata = MetaData()
    metadata.reflect(bind=engine)
    table = metadata.tables['booking']
    if delete_existing_data:
        session.execute(table.delete())
    for _ in range(num_data):
        fake_flight_id = random.randint(1,32000)
        fake_seat = fake.bothify(text='????')
        fake_passenger_id = random.randint(1,32000)
        fake_price = round(random.uniform(10, 1000), 2)
        session.execute(table.insert().values(flight_id = fake_flight_id, seat = fake_seat, passenger_id = fake_passenger_id, price = fake_price))
        

# 세션 생성
Session = sessionmaker(bind=engine)
session = Session()

# 데이터베이스와 로드된 테이블에서 테이블 목록 가져오기
table_names = metadata.tables.keys()

# 변경 내용 커밋
session.commit()

# 세션 닫기
session.close()
