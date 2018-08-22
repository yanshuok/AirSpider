from sqlalchemy import Column, String, Integer, create_engine, DateTime, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import utils.CONST as const
Base = declarative_base()
engine = create_engine(const.database)
DBSession = sessionmaker(bind=engine)
class AirQuality(Base):
    __tablename__ = 'airquality'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    co_0 = Column(Float(), default=-9999)
    co_iaqi = Column(Float(), default=-9999)
    co = Column(Float(), default=-9999)
    no2_0 = Column(Float(), default=-9999)
    no2_iaqi = Column(Float(), default=-9999)
    no2 = Column(Float(), default=-9999)
    so2_0 = Column(Float(), default=-9999)
    so2_iaqi = Column(Float(), default=-9999)
    so2 = Column(Float(), default=-9999)
    o3_0 = Column(Float(), default=-9999)
    o3_iaqi = Column(Float(), default=-9999)
    o3 = Column(Float(), default=-9999)
    pm25_0 = Column(Float(), default=-9999)
    pm25_iaqi = Column(Float(), default=-9999)
    pm25 = Column(Float(), default=-9999)
    pm10_0 = Column(Float(), default=-9999)
    pm10_iaqi = Column(Float(), default=-9999)
    pm10 = Column(Float(), default=-9999)
    aqi = Column(Float(), default=-9999)
    first = Column(String(5))
    grade = Column(Integer())
    station_id = Column(Integer())
    date = Column(DateTime())

class Station(Base):
    __tablename__ = 'airquality_station'
    id = Column(Integer(), primary_key=True)
    station_name = Column(String(10))
    longitude = Column(Float())
    altitude = Column(Float())
    station_detail = Column(String(10))
    district = Column(String(5))
    district_id = Column(Integer())

def insertAirQaulity(airqualities):
    session = DBSession()
    data = [AirQuality(**x) for x in airqualities]
    session.add_all(data)
    session.commit()
    session.close()


def getStationIds():
    session = DBSession()
    stations = session.query(Station, Station.id)
    return [x.id for x in stations]