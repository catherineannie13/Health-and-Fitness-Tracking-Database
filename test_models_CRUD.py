import pytest
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from schema import Base, User, Goal, Workout, NutritionLog, SleepRecord, HealthMetric

# Setup a fixture for the database session
@pytest.fixture(scope="module")
def session():
    """
    Create a new database session and return it to the test function. 
    After the test is run, the session is closed and the mappers are cleared.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    yield session
    session.close()
    clear_mappers()

# Test User model
def test_user_model(session):
    """
    Test the User model by adding a new user to the database and asserting its attributes.
    
    Parameters
    ----------
    session : SQLAlchemy session
        The session object used to interact with the database.

    Returns
    -------
    None
    """
    user = User(name='Test User', email='test@example.com', age=30, gender='Male')
    session.add(user)
    session.commit()

    retrieved_user = session.query(User).filter_by(email='test@example.com').first()
    assert retrieved_user.name == 'Test User'
    assert retrieved_user.email == 'test@example.com'
    assert retrieved_user.age == 30
    assert retrieved_user.gender == 'Male'

    # Update the user
    session.query(User).filter_by(email='test@example.com').update({'name': 'Updated Test User'})
    session.commit()

    updated_user = session.query(User).filter_by(email='test@example.com').first()
    assert updated_user.name == 'Updated Test User'

    # Delete the user
    session.delete(updated_user)
    session.commit()

    deleted_user = session.query(User).filter_by(email='test@example.com').first()
    assert deleted_user is None

# Test Goal model
def test_goal_model(session):
    """
    Test the Goal model by adding a new goal to the database and asserting its attributes.

    Parameters
    ----------
    session : SQLAlchemy session
        The session object used to interact with the database.

    Returns
    -------
    None
    """
    goal = Goal(user_id=1, goal_type='Weight Loss', target='Lose 5 kg in 3 months')
    session.add(goal)
    session.commit()

    retrieved_goal = session.query(Goal).first()
    assert retrieved_goal.goal_type == 'Weight Loss'
    assert retrieved_goal.target == 'Lose 5 kg in 3 months'

    # Update the goal
    session.query(Goal).filter_by(goal_type='Weight Loss').update({'target': 'Lose 10 kg in 6 months'})
    session.commit()

    updated_goal = session.query(Goal).first()
    assert updated_goal.target == 'Lose 10 kg in 6 months'

    # Delete the goal
    session.delete(updated_goal)
    session.commit()
    
    deleted_goal = session.query(Goal).first()
    assert deleted_goal is None

# Test Workout model
def test_workout_model(session):
    """
    Test the Workout model by adding a new workout to the database and asserting its attributes.

    Parameters
    ----------
    session : SQLAlchemy session
        The session object used to interact with the database.

    Returns
    -------
    None
    """
    workout = Workout(user_id=1, date=datetime.now(), type='Running', duration_minutes=30, intensity='High', calories_burned=300)
    session.add(workout)
    session.commit()

    retrieved_workout = session.query(Workout).first()
    assert retrieved_workout.type == 'Running'
    assert retrieved_workout.duration_minutes == 30
    assert retrieved_workout.intensity == 'High'
    assert retrieved_workout.calories_burned == 300

    # Update the workout
    session.query(Workout).filter_by(type='Running').update({'duration_minutes': 45})
    session.commit()
    
    updated_workout = session.query(Workout).first()
    assert updated_workout.duration_minutes == 45

    # Delete the workout
    session.delete(updated_workout)
    session.commit()

    deleted_workout = session.query(Workout).first()
    assert deleted_workout is None

# Test NutritionLog model
def test_nutrition_log_model(session):
    """
    Test the NutritionLog model by adding a new nutrition log to the database and asserting its attributes.

    Parameters
    ----------
    session : SQLAlchemy session
        The session object used to interact with the database.

    Returns
    -------
    None
    """
    nutrition_log = NutritionLog(user_id=1, date=datetime.now(), meal_type='Breakfast', food_item='Oatmeal', quantity=2, calories=150)
    session.add(nutrition_log)
    session.commit()

    retrieved_log = session.query(NutritionLog).first()
    assert retrieved_log.meal_type == 'Breakfast'
    assert retrieved_log.food_item == 'Oatmeal'
    assert retrieved_log.quantity == 2
    assert retrieved_log.calories == 150

    # Update the nutrition log
    session.query(NutritionLog).filter_by(meal_type='Breakfast').update({'quantity': 3})
    session.commit()

    updated_log = session.query(NutritionLog).first()
    assert updated_log.quantity == 3

    # Delete the nutrition log
    session.delete(updated_log)
    session.commit()

    deleted_log = session.query(NutritionLog).first()
    assert deleted_log is None

# Test SleepRecord model
def test_sleep_record_model(session):
    """
    Test the SleepRecord model by adding a new sleep record to the database and asserting its attributes.

    Parameters
    ----------
    session : SQLAlchemy session
        The session object used to interact with the database.

    Returns
    -------
    None
    """
    sleep_record = SleepRecord(user_id=1, date=datetime.now(), duration_hours=8, quality='Good')
    session.add(sleep_record)
    session.commit()

    retrieved_record = session.query(SleepRecord).first()
    assert retrieved_record.duration_hours == 8
    assert retrieved_record.quality == 'Good'

    # Update the sleep record
    session.query(SleepRecord).filter_by(quality='Good').update({'duration_hours': 7})
    session.commit()

    updated_record = session.query(SleepRecord).first()
    assert updated_record.duration_hours == 7

    # Delete the sleep record
    session.delete(updated_record)
    session.commit()

    deleted_record = session.query(SleepRecord).first()
    assert deleted_record is None

# Test HealthMetric model
def test_health_metric_model(session):
    """
    Test the HealthMetric model by adding a new health metric to the database and asserting its attributes.

    Parameters
    ----------
    session : SQLAlchemy session
        The session object used to interact with the database.

    Returns
    -------
    None
    """
    health_metric = HealthMetric(user_id=1, date=datetime.now(), weight=70, bmi=22, heart_rate=70, blood_pressure='120/80')
    session.add(health_metric)
    session.commit()

    retrieved_metric = session.query(HealthMetric).first()
    assert retrieved_metric.weight == 70
    assert retrieved_metric.bmi == 22
    assert retrieved_metric.heart_rate == 70
    assert retrieved_metric.blood_pressure == '120/80'

    # Update the health metric
    session.query(HealthMetric).filter_by(weight=70).update({'weight': 75})
    session.commit()

    updated_metric = session.query(HealthMetric).first()
    assert updated_metric.weight == 75

    # Delete the health metric
    session.delete(updated_metric)
    session.commit()

    deleted_metric = session.query(HealthMetric).first()
    assert deleted_metric is None