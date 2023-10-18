from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func


db_url = "postgresql://dras_db_7ke9_user:rjbBj2JXRshov9Kkbvpz8snTKEt6MmDN@dpg-ckn4olv83ejs739li02g-a.oregon-postgres.render.com/dras_db_7ke9"
engine = create_engine(db_url)

Base = declarative_base()

class DrasTable(Base):
    """Class representation of the dras table"""
    __tablename__ = "dras_table"
    usid = Column(Integer, primary_key=True)
    EntryDate = Column(Date, default=func.now())
    HighBP = Column(Integer)
    HighChol = Column(Integer)
    CholCheck = Column(Integer)
    BMI = Column(Integer)
    Smoker = Column(Integer)
    Stroke = Column(Integer)
    HigHeartDiseaseorAttackhBP = Column(Integer)
    PhysActivity = Column(Integer)
    Fruits = Column(Integer)
    Veggies = Column(Integer)
    HvyAlcoholConsump = Column(Integer)
    AnyHealthcare = Column(Integer)
    NoDocbcCost = Column(Integer)
    GenHlth = Column(Integer)
    MentHlth = Column(Integer)
    PhysHlth = Column(Integer)
    DiffWalk = Column(Integer)
    Sex = Column(Integer)
    Age = Column(Integer)
    Education = Column(Integer)
    Income = Column(Integer)
    Prediction = Column(Integer)

Base.metadata.create_all(engine)
engine.dispose()

