from sqlalchemy import func, and_, desc, Index, extract
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
from schema import engine, User, Workout, NutritionLog, SleepRecord, HealthMetric

# Connect to session
Session = sessionmaker(bind=engine)
session = Session()

def run_queries():
    """
    Run a series of queries to analyze the data in the database and print the results.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    # Total Calories Burned Per User
    total_calories = session.query(
        User.name,
        func.sum(Workout.calories_burned).label('total_calories')
    ).join(Workout).group_by(User.name).all()

    print("Total Calories Burned Per User:")
    if len(total_calories) == 0:
        print("No workouts found in the database.")
    else:
        for user, calories in total_calories:
            print(f"{user}: {calories} calories")

    # Average Sleep Duration and Quality by Age Group
    average_sleep_by_age = session.query(
        (func.floor(User.age / 10) * 10).label('age_group'),
        func.avg(SleepRecord.duration_hours).label('avg_duration'),
        func.avg(SleepRecord.quality).label('avg_quality')
    ).join(SleepRecord).group_by('age_group').all()

    print("\nAverage Sleep Duration and Quality by Age Group:")
    if len(average_sleep_by_age) == 0:
        print("No sleep records found in the database.")
    else:
        for age_group, duration, quality in average_sleep_by_age:
            print(f"Age Group {age_group}s - Avg Duration: {round(duration, 2)} hours, Avg Quality: {round(quality, 2)}")

    # Most Common Workout Type
    most_common_workout_type = session.query(
        Workout.type,
        func.count(Workout.type).label('count')
    ).group_by(Workout.type).order_by(func.count(Workout.type).desc()).first()

    print("\nMost Common Workout Type:")
    if most_common_workout_type is None:
        print("No workouts found in the database.")
    else:
        print(f"{most_common_workout_type.type} - {most_common_workout_type.count} times")

    # User Progress Over Time (for a specific user)
    user_id_for_progress = 1
    user_progress = session.query(
        HealthMetric.date,
        HealthMetric.weight,
        HealthMetric.bmi
    ).filter(HealthMetric.user_id == user_id_for_progress).order_by(HealthMetric.date).all()
    user = session.query(User).filter(User.id == user_id_for_progress).first()

    print(f"\nUser Progress Over Time for User {user.name}:")
    if len(user_progress) == 0:
        print("No health metrics found in the database.")
    else:
        for record in user_progress:
            print(f"Date: {record.date}, Weight: {record.weight}, BMI: {record.bmi}")

    # Top 5 High Calorie Foods Logged
    top_high_calorie_foods = session.query(
        NutritionLog.food_item,
        func.avg(NutritionLog.calories).label('average_calories')
    ).group_by(NutritionLog.food_item).order_by(func.avg(NutritionLog.calories).desc()).limit(5).all()

    print("\nTop 5 High Calorie Foods Logged:")
    if len(top_high_calorie_foods) == 0:
        print("No nutrition logs found in the database.")
    else:
        for food in top_high_calorie_foods:
            print(f"Food: {food.food_item}, Avg Calories: {round(food.average_calories, 2)}")

    # Users Not Meeting Sleep Quality Goals
    sleep_quality_goal = 3
    users_below_sleep_quality = session.query(
        User.name,
        func.avg(SleepRecord.quality).label('average_sleep_quality')
    ).join(SleepRecord).group_by(User.name).having(func.avg(SleepRecord.quality) < sleep_quality_goal).all()

    print("\nUsers Not Meeting Sleep Quality Goals:")
    if len(users_below_sleep_quality) == 0:
        print(f"All users are meeting the sleep quality goal of {sleep_quality_goal}.")
    else:
        for user in users_below_sleep_quality:
            print(f"User: {user.name}, Avg Sleep Quality: {round(user.average_sleep_quality, 2)}")

    # Workout Frequency by Type for a User
    user_id_for_workout_frequency = 1
    workout_frequency_by_type = session.query(
        Workout.type,
        func.count(Workout.type).label('frequency')
    ).filter(Workout.user_id == user_id_for_workout_frequency).group_by(Workout.type).all()
    user = session.query(User).filter(User.id == user_id_for_workout_frequency).first()

    print(f"\nWorkout Frequency by Type for User {user.name}:")
    if len(workout_frequency_by_type) == 0:
        print(f"No workouts found for the user.")
    else:
        for workout in workout_frequency_by_type:
            print(f"Workout Type: {workout.type}, Frequency: {workout.frequency}")

    # Average Daily Caloric Intake Per User
    average_daily_caloric_intake = session.query(
        User.name,
        func.avg(func.sum(NutritionLog.calories)).over(partition_by=NutritionLog.date).label('average_daily_calories')
    ).join(NutritionLog).group_by(User.name).order_by('average_daily_calories').all()

    print("\nAverage Daily Caloric Intake Per User:")
    if len(average_daily_caloric_intake) == 0:
        print("No nutrition logs found in the database.")
    else:
        for user in average_daily_caloric_intake:
            print(f"User: {user.name}, Avg Daily Calories: {user.average_daily_calories}")

    # Change in Workout Intensity
    user_id_for_intensity_improvement = 1
    workout_intensity_improvement = session.query(
        Workout.date,
        Workout.intensity,
        func.lag(Workout.intensity).over(order_by=Workout.date).label('previous_intensity')
    ).filter(Workout.user_id == user_id_for_intensity_improvement).all()
    user = session.query(User).filter(User.id == user_id_for_intensity_improvement).first()

    print(f"\nChange in Workout Intensity for User {user.name}:")
    if len(workout_intensity_improvement) == 0:
        print(f"No workouts found for the user.")
    else:
        for workout in workout_intensity_improvement:
            print(f"Date: {workout.date}, Intensity: {workout.intensity}, Previous Intensity: {workout.previous_intensity}")

    # Nutritional Deficit or Surplus
    user_id_for_nutritional_analysis = 1
    nutritional_deficit_surplus = session.query(
        NutritionLog.date,
        func.sum(NutritionLog.calories).label('total_daily_calories'),
        (func.sum(NutritionLog.calories) - 2000).label('deficit_surplus')
    ).filter(NutritionLog.user_id == user_id_for_nutritional_analysis).group_by(NutritionLog.date).all()
    user = session.query(User).filter(User.id == user_id_for_nutritional_analysis).first()

    print(f"\nNutritional Deficit or Surplus for User {user.name}:")
    if len(nutritional_deficit_surplus) == 0:
        print(f"No nutrition logs found for the user.")
    else:
        for day in nutritional_deficit_surplus:
            print(f"Date: {day.date}, Total Calories: {day.total_daily_calories}, Deficit/Surplus: {day.deficit_surplus}")

    # User Workout Details
    user_workout_details = session.query(
        User.name,
        Workout.type,
        Workout.duration_minutes
    ).join(Workout).limit(10).all()

    print("\nUser Workout Details:")
    if len(user_workout_details) == 0:
        print("No workouts found in the database.")
    else:
        for detail in user_workout_details:
            print(f"User: {detail.name}, Workout Type: {detail.type}, Duration: {detail.duration_minutes} minutes")

    # Users with Workouts but No Nutrition Logs on the Same Day
    users_with_workouts_no_nutrition = session.query(
        User.name
    ).join(Workout).outerjoin(NutritionLog, and_(
        User.id == NutritionLog.user_id,
        Workout.date == NutritionLog.date
    )).filter(NutritionLog.id == None).group_by(User.id).all()

    print("\nUsers with Workouts but No Nutrition Logs on the Same Day:")
    if len(users_with_workouts_no_nutrition) == 0:
        print("All users have nutrition logs for their workout days.")
    else:
        for user in users_with_workouts_no_nutrition:
            print(user.name)

    # Total Sleep Hours vs Workout Hours Last Month
    sleep_vs_workout_hours = session.query(
        User.name,
        func.sum(SleepRecord.duration_hours).label('total_sleep_hours'),
        func.sum(Workout.duration_minutes / 60).label('total_workout_hours')
    ).join(SleepRecord).join(Workout).filter(SleepRecord.date >= (datetime.now() - timedelta(days=30))).group_by(User.name).all()

    print("\nTotal Sleep Hours vs Workout Hours Last Month:")
    if len(sleep_vs_workout_hours) == 0:
        print("No sleep or workout records found in the database.")
    else:
        for record in sleep_vs_workout_hours:
            print(f"User: {record.name}, Total Sleep Hours: {round(record.total_sleep_hours, 2)}, Total Workout Hours: {round(record.total_workout_hours, 2)}")

    # Users Achieving Calorie Intake Goal
    daily_calorie_goal = 2000
    users_achieving_calorie_goal = session.query(
        User.name
    ).join(NutritionLog).group_by(User.name).having(func.sum(NutritionLog.calories) >= daily_calorie_goal).all()

    print("\nUsers Achieving Calorie Intake Goal:")
    if len(users_achieving_calorie_goal) == 0:
        print(f"No users are achieving the daily calorie intake goal of {daily_calorie_goal}.")
    else:
        for user in users_achieving_calorie_goal:
            print(user.name)

    # Users Who Improved Sleep Quality Over the Past Month
    sleep_quality_improvement_subquery = session.query(
        SleepRecord.user_id,
        func.max(SleepRecord.quality).label('max_quality')
    ).filter(
        SleepRecord.date >= (datetime.now() - timedelta(days=30))
    ).group_by(SleepRecord.user_id).subquery()

    improving_sleep_quality_users = session.query(
        User.name
    ).join(
        sleep_quality_improvement_subquery, User.id == sleep_quality_improvement_subquery.c.user_id
    ).order_by(desc(sleep_quality_improvement_subquery.c.max_quality)).limit(5).all()

    print("\nUsers Who Improved Sleep Quality Over the Past Month:")
    if len(improving_sleep_quality_users) == 0:
        print("No users have improved their sleep quality over the past month.")
    else:
        for user in improving_sleep_quality_users:
            print(user.name)

    # Covering index and query for workouts
    Index('idx_workout_type_calories', Workout.type, Workout.calories_burned)  
    workouts = session.query(Workout.type, 
                             func.avg(Workout.calories_burned)).group_by(Workout.type).all()
    
    print("\nWorkout Type and Average Calories Burned:")
    if len(workouts) == 0:
        print("No workouts found in the database.")
    else:
        for workout in workouts:
            print(f"Workout Type: {workout.type}, Avg Calories: {round(workout[1], 2)}")

    # Covering index and query for health metrics
    Index('idx_health_metric_date_weight', HealthMetric.date, HealthMetric.weight)
    user_id_for_weight_loss = 1
    monthly_weight_records = session.query(
        extract('year', HealthMetric.date).label('year'),
        extract('month', HealthMetric.date).label('month'),
        func.avg(HealthMetric.weight).label('average_weight')
    ).filter(
        HealthMetric.user_id == user_id_for_weight_loss,
        HealthMetric.date.between('2024-01-01', '2024-03-31')
    ).group_by('year', 'month').order_by('year', 'month').all()
    user = session.query(User).filter(User.id == user_id_for_weight_loss).first()

    print(f"\nMonthly Weight Records for user {user.name}:")
    if len(monthly_weight_records) == 0:
        print(f"No weight records found for this user in the database.")
    else:
        for record in monthly_weight_records:
            print(f"Year: {record.year}, Month: {record.month}, Average Weight: {round(record.average_weight, 2)}")

    # Covering index and query for sleep records
    Index('idx_sleep_record_date_quality', SleepRecord.date.desc(), SleepRecord.quality)
    latest_sleep_subquery = session.query(
        SleepRecord.user_id,
        func.max(SleepRecord.date).label('max_date')
    ).group_by(SleepRecord.user_id).subquery()

    latest_high_quality_sleep = session.query(
        latest_sleep_subquery.c.user_id,
        SleepRecord.date,
        SleepRecord.quality
    ).join(SleepRecord, and_(
        SleepRecord.user_id == latest_sleep_subquery.c.user_id,
        SleepRecord.date == latest_sleep_subquery.c.max_date
    )).order_by(SleepRecord.quality.desc()).limit(10).all()

    print("\nLatest High Quality Sleep Records:")
    if len(latest_high_quality_sleep) == 0:
        print("No sleep records found in the database.")
    else:
        for record in latest_high_quality_sleep:
            user = session.query(User).filter(User.id == record.user_id).first()
            print(f"User: {user.name}, Date: {record.date}, Quality: {record.quality}")

def add_new_user_and_health_metrics():
    """
    Add a new user and initial health metrics to the database.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    try:
        new_user = User(name='John Doe', email='johndoe@example.com', age=30, gender='Male')
        session.add(new_user)
        session.flush()
        new_health_metric = HealthMetric(user_id=new_user.id, date=datetime.now(), weight=70, bmi=22, heart_rate=70, blood_pressure='120/80')
        session.add(new_health_metric)
        session.commit()
        print("\nNew user and initial health metrics added successfully.")
    except Exception as e:
        session.rollback()
        print(f"\nTransaction to add new user and initial health metrics failed: {e}")

def update_user_workout_and_add_nutrition_log():
    """
    Update a user's workout and add a nutrition log for the same day.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    """
    try:
        user_id = 1
        update_date = datetime.now().date()
        session.query(Workout).filter(Workout.user_id == user_id, Workout.date == update_date).update({"type": "Yoga", "duration_minutes": 60})
        new_nutrition_log = NutritionLog(user_id=user_id, date=update_date, meal_type="Breakfast", food_item="Oatmeal", quantity=2, calories=300)
        session.add(new_nutrition_log)
        session.commit()
        print("\nUser's workout updated and nutrition log added for the same day successfully.")
    except Exception as e:
        session.rollback()
        print(f"\nTransaction to update user's workout and add nutrition logs for the same day failed: {e}")

if __name__ == "__main__":
    run_queries()
    add_new_user_and_health_metrics()
    update_user_workout_and_add_nutrition_log()