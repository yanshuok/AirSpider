from sqlalchemy import Column, String, Integer, create_engine, DateTime, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import utils.CONST as const
Base = declarative_base()

engine = create_engine(const.database)
DBSession = sessionmaker(bind=engine)

class Weather(Base):
    __tablename__ = 'weather24h'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    temperature = Column(Float(), default=-99)
    humidity = Column(Float(), default=-99)
    rain = Column(Float(), default=-99)
    wind_force = Column(Float(), default=-99)
    wind_direction = Column(Float(), default=-99)
    station_id = Column(Integer())
    date = Column(DateTime())
    dur = Column(Integer())

class Station(Base):
    __tablename__ = 'weather_station'
    id = Column(Integer(), primary_key=True)
    station_name = Column(String(10))
    href = Column(String(128))


def getUrls():
    session = DBSession()
    stations = session.query(Station, Station.id, Station.href).filter(Station.href!=None).all()
    session.close()
    return stations

def insertWeahter24h(weathers):
    session = DBSession()
    data = [Weather(**x) for x in weathers]
    session.add_all(data)
    session.commit()
    session.close()

if __name__ == '__main__':
    for x in getUrls():
        print(x)
