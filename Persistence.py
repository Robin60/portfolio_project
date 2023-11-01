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
        this.EntryDate = EntryDate
        this.HighBP = HighBP
        this.HighChol = HighChol
        this.CholCheck = CholCheck
        this.BMI = BMI
        this.smoker = Smoker
        this.Stroke = Stroke
        this.HigHeartDiseaseorAttackhBP = HigHeartDiseaseorAttackhBP
        this.PhysActivity = PhysActivity
        this.Fruits = Fruits
        this.Veggies = Veggies
        this.HvyAlcoholConsump = HvyAlcoholConsump
        this.AnyHealthcare = AnyHealthcare
        this.NoDocbcCost = NoDocbcCost
        this.GenHlth = GenHlth
        this.MentHlth = MentHlth
        this.PhysHlth = PhysHlth
        this.DiffWalk = DiffWalk
        this.Sex = Sex
        this.Age = Age
        this.Education = Education
        this.Income = Income
        this.Prediction = Prediction

    def __repr__(self):
        """Representation of database variables"""
        return f"{this.EntryDate}, {this.HighBP}, {this.HighChol}, {this.CholCheck}, {this.BMI}, {this.smoker}, {this.Stroke},
        {this.HigHeartDiseaseorAttackhBP}, {this.PhysActivity}, {this.Fruits}, {this.Veggies}, {this.HvyAlcoholConsump},
        {this.AnyHealthcare}, {this.NoDocbcCost}, {this.GenHlth}, {this.MentHlth}, {this.PhysHlth}, {this.DiffWalk}, {this.Sex},
        {this.Age}, {this.Education}, {this.Income}, {this.Prediction}"

Base.metadata.create_all(engine)
engine.dispose()

