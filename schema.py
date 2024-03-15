from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
    """
    A class used to represent a user in the database. Each user has a personal information
    such as name, age, gender and email. They also have a list of goals, workouts, nutrition logs,
    sleep records, and health metrics.

    Attributes
    ----------
    id : int
        The unique identifier for the user.
    name : str
        The name of the user.
    email : str
        The email address of the user.
    age : int
        The age of the user.
    gender: str
        The gender of the user.

    Relationships
    -------------
    goals : Goal
        The goals associated with the user.
    workouts : Workout
        The workouts associated with the user.
    nutrition_logs : NutritionLog
        The nutrition logs associated with the user.
    sleep_records : SleepRecord
        The sleep records associated with the user.
    health_metrics : HealthMetric
        The health metrics associated with the user.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    age = Column(Integer)
    gender = Column(String)
    goals = relationship('Goal', back_populates='user')
    workouts = relationship('Workout', back_populates='user')
    nutrition_logs = relationship('NutritionLog', back_populates='user')
    sleep_records = relationship('SleepRecord', back_populates='user')
    health_metrics = relationship('HealthMetric', back_populates='user')

class Goal(Base):
    """
    A class used to represent a goal in the database. Each goal is associated with a 
    user and has a type and target.

    Attributes
    ----------
    id : int
        The unique identifier for the goal.
    user_id : int
        The foreign key referencing the user that the goal belongs to.
    goal_type : str
        The type of the goal.
    target : str
        The target of the goal.

    Relationships
    -------------
    user : User
        The user that the goal belongs to.
    """
    __tablename__ = 'goals'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    goal_type = Column(String, nullable=False)
    target = Column(String, nullable=False)
    user = relationship('User', back_populates='goals')

class Workout(Base):
    """
    A class used to represent a workout in the database. Each workout has a user_id, date, type,
    duration_minutes, intensity, and calories_burned. It is associated with a user.

    Attributes
    ----------
    id : int
        The unique identifier for the workout.
    user_id : int
        The foreign key referencing the user's id.
    date : DateTime
        The date of the workout.
    type : str
        The type of the workout.
    duration_minutes : float
        The duration of the workout in minutes.
    intensity : str
        The intensity of the workout.
    calories_burned : float
        The number of calories burned during the workout.

    Relationships
    -------------
    user : User
        The user associated with the workout.
    """
    __tablename__ = 'workouts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    date = Column(DateTime, nullable=False)
    type = Column(String, nullable=False)
    duration_minutes = Column(Float, nullable=False)
    intensity = Column(String)
    calories_burned = Column(Float)
    user = relationship('User', back_populates='workouts')

class NutritionLog(Base):
    """
    A class used to represent a nutrition log in the database. Each nutrition log
    contains information about a user's meal, including the date, meal type, food item,
    quantity, and calories.

    Attributes
    ----------
    id : int
        The unique identifier for the nutrition log.
    user_id : int
        The foreign key referencing the user associated with the nutrition log.
    date : datetime
        The date of the nutrition log.
    meal_type : str
        The type of meal (e.g., breakfast, lunch, dinner).
    food_item : str
        The name of the food item.
    quantity : float
        The quantity of the food item consumed.
    calories : float
        The number of calories in the food item.

    Relationships
    -------------
    user : User
        The user associated with the nutrition log.
    """
    __tablename__ = 'nutrition_logs'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    date = Column(DateTime, nullable=False)
    meal_type = Column(String, nullable=False)
    food_item = Column(String, nullable=False)
    quantity = Column(Float, nullable=False)
    calories = Column(Float, nullable=False)
    user = relationship('User', back_populates='nutrition_logs')

class SleepRecord(Base):
    """
    A class used to represent a sleep record in the database. Each sleep record has a unique identifier,
    a user ID, a date, a duration in hours, and a quality rating.

    Attributes
    ----------
    id : int
        The unique identifier for the sleep record.
    user_id : int
        The ID of the user associated with the sleep record.
    date : datetime
        The date of the sleep record.
    duration_hours : float
        The duration of the sleep in hours.
    quality : str
        The quality rating of the sleep.

    Relationships
    -------------
    user : User
        The user associated with the sleep record.
    """
    __tablename__ = 'sleep_records'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    date = Column(DateTime, nullable=False)
    duration_hours = Column(Float, nullable=False)
    quality = Column(String, nullable=False)
    user = relationship('User', back_populates='sleep_records')

class HealthMetric(Base):
    """
    A class used to represent a health metric in the database. Each health metric has a unique identifier,
    a user ID, a date, a weight, a BMI, a heart rate, and a blood pressure.

    Attributes
    ----------
    id : int
        The unique identifier for the health metric.
    user_id : int
        The ID of the user associated with the health metric.
    date : datetime
        The date of the health metric.
    weight : float
        The weight of the user.
    bmi : float
        The body mass index of the user.
    heart_rate : int
        The heart rate of the user.
    blood_pressure : str
        The blood pressure of the user.
    
    Relationships
    -------------
    user : User
        The user associated with the health metric.
    """
    __tablename__ = 'health_metrics'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    date = Column(DateTime, nullable=False)
    weight = Column(Float)
    bmi = Column(Float)
    heart_rate = Column(Integer)
    blood_pressure = Column(String)
    user = relationship('User', back_populates='health_metrics')

# Create an engine that stores data in the local directory's database
engine = create_engine('sqlite:///health_and_fitness_tracking.db')

# Create all tables in the engine
Base.metadata.create_all(engine)