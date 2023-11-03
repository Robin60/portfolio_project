#!/usr/bin/env python3

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

    def __init__(self, EntryDate, HighBP, HighChol, CholCheck, BMI, Smoker, Stroke, HigHeartDiseaseorAttackhBP,
        PhysActivity, Fruits, Veggies, HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, GenHlth, MentHlth, PhysHlth,
        DiffWalk, Sex, Age, Education, Income, Prediction):
        self.EntryDate = EntryDate
        self.HighBP = HighBP
        self.HighChol = HighChol
        self.CholCheck = CholCheck
        self.BMI = BMI
        self.smoker = Smoker
        self.Stroke = Stroke
        self.HigHeartDiseaseorAttackhBP = HigHeartDiseaseorAttackhBP
        self.PhysActivity = PhysActivity
        self.Fruits = Fruits
        self.Veggies = Veggies
        self.HvyAlcoholConsump = HvyAlcoholConsump
        self.AnyHealthcare = AnyHealthcare
        self.NoDocbcCost = NoDocbcCost
        self.GenHlth = GenHlth
        self.MentHlth = MentHlth
        self.PhysHlth = PhysHlth
        self.DiffWalk = DiffWalk
        self.Sex = Sex
        self.Age = Age
        self.Education = Education
        self.Income = Income
        self.Prediction = Prediction

    def __repr__(self):
        """Representation of database variables"""
        return f"{self.EntryDate}, {self.HighBP}, {self.HighChol}, {self.CholCheck}, {self.BMI}, {self.smoker}, {self.Stroke},
        {self.HigHeartDiseaseorAttackhBP}, {self.PhysActivity}, {self.Fruits}, {self.Veggies}, {self.HvyAlcoholConsump},
        {self.AnyHealthcare}, {self.NoDocbcCost}, {self.GenHlth}, {self.MentHlth}, {self.PhysHlth}, {self.DiffWalk}, {self.Sex},
        {self.Age}, {self.Education}, {self.Income}, {self.Prediction}"

Base.metadata.create_all(engine)
engine.dispose()

