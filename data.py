from faker import Faker
import random
from sqlalchemy.orm import sessionmaker
from schema import engine, User, Workout, NutritionLog, SleepRecord, HealthMetric

# Initialize Faker
fake = Faker()

# Connect to session
Session = sessionmaker(bind=engine)
session = Session()

def create_fake_users(n=10):
    """
    Create a given number of fake users for the database.

    Parameters
    ----------
    n : int, optional
        The number of users to create. Default is 10.

    Returns
    -------
    None
    """
    for _ in range(n):
        user = User(
            name=fake.name(),
            email=fake.email(),
            age=random.randint(18, 65),
            gender=random.choice(['Male', 'Female', 'Other'])
        )
        session.add(user)
    session.commit()

def create_fake_workouts(n=50):
    """
    Create a given number of fake workouts for all users in the database.

    Parameters
    ----------
    n : int, optional
        The number of workouts to create. Default is 50.

    Returns
    -------
    None
    """
    user_ids = session.query(User.id).all()
    for _ in range(n):
        workout = Workout(
            user_id=random.choice(user_ids)[0],
            date=fake.date_time_this_year(before_now=True, after_now=False),
            type=random.choice(['Running', 'Cycling', 'Swimming', 'Gym', 'Yoga']),
            duration_minutes=random.randint(15, 120),
            intensity=random.choice(['Low', 'Medium', 'High']),
            calories_burned=random.randint(100, 1000)
        )
        session.add(workout)
    session.commit()

def create_fake_nutrition_logs(n=100):
    """
    Create a given number of fake nutrition logs for all users in the database.

    Parameters
    ----------
    n : int, optional
        The number of nutrition logs to create. Default is 100.

    Returns
    -------
    None
    """
    user_ids = session.query(User.id).all()
    for _ in range(n):
        nutrition_log = NutritionLog(
            user_id=random.choice(user_ids)[0],
            date=fake.date_time_this_year(before_now=True, after_now=False),
            meal_type=random.choice(['Breakfast', 'Lunch', 'Dinner', 'Snack']),
            food_item=random.choice(['Pasta', 'Rice', 'Chicken Breast', 'Salmon', 
                                     'Broccoli', 'Spinach Salad', 'Beef Steak', 
                                     'Scrambled Eggs', 'Greek Yogurt', 'Protein Shake']),
            quantity=random.randint(1, 5),
            calories=random.randint(50, 700)
        )
        session.add(nutrition_log)
    session.commit()

def create_fake_sleep_records(n=50):
    """
    Create a given number of fake sleep records for all users in the database.

    Parameters
    ----------
    n : int, optional
        The number of sleep records to create. Default is 50.

    Returns
    -------
    None
    """
    user_ids = session.query(User.id).all()
    for _ in range(n):
        sleep_record = SleepRecord(
            user_id=random.choice(user_ids)[0],
            date=fake.date_time_this_year(before_now=True, after_now=False),
            duration_hours=round(random.uniform(4.0, 12.0), 2),
            quality=random.randint(1, 5)
        )
        session.add(sleep_record)
    session.commit()

def create_fake_health_metrics(n=50):
    """
    Create a given number of fake health metrics for all users in the database.

    Parameters
    ----------
    n : int, optional
        The number of health metrics to create. Default is 50.

    Returns
    -------
    None
    """
    user_ids = session.query(User.id).all()
    for _ in range(n):
        health_metric = HealthMetric(
            user_id=random.choice(user_ids)[0],
            date=fake.date_time_this_year(before_now=True, after_now=False),
            weight=round(random.uniform(50.0, 100.0), 2),
            bmi=round(random.uniform(18.5, 30.0), 2),
            heart_rate=random.randint(60, 100),
            blood_pressure=f"{random.randint(90, 120)}/{random.randint(60, 80)}"
        )
        session.add(health_metric)
    session.commit()

if __name__ == "__main__":
    create_fake_users(10) 
    create_fake_workouts(50)
    create_fake_nutrition_logs(100)  
    create_fake_sleep_records(50)
    create_fake_health_metrics(50)