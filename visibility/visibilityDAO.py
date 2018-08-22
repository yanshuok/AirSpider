from sqlalchemy import Column, String, Integer, create_engine, DateTime, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import utils.CONST as const
Base = declarative_base()
engine = create_engine(const.database)
DBSession = sessionmaker(bind=engine)


class Station(Base):
    __tablename__ = 'weather_station'
    id = Column(Integer(), primary_key=True)
    station_name = Column(String(10))
    href = Column(String(128))


class Visibility(Base):
    __tablename__ = 'visibility'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    feel_temperature = Column(Float())
    temperature = Column(Float())
    weather = Column(Integer())
    wind_direction = Column(Float())
    wind_power = Column(Float())
    humidity = Column(Float())
    precipitation = Column(Float())
    press = Column(Float())
    visibility = Column(Float())
    cloud = Column(Float())
    date = Column(DateTime())
    district_id = Column(Integer())


def insert_visibility(visibilities):
    session = DBSession()
    data = [Visibility(**x) for x in visibilities]
    session.add_all(data)
    session.commit()
    session.close()


def get_districts():
    session = DBSession()
    stations = session.query(Station, Station.id, Station.station_name).all()
    session.close()
    return stations
