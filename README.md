# Health and Fitness Tracking App Overview

## Introduction

The Health and Fitness Tracking App is designed as a comprehensive tool to assist individuals in monitoring and improving their health and fitness levels. By integrating various health metrics and activity logs, the app provides users with personalized insights and feedback to help them achieve their wellness goals.

## Runnning the Code
1. Create a virtual environment. For macOS/Linux: 
```bash
python3 -m venv venv
```
For Windows:
```bash
python -m venv venv
```

2. Activate the virtual environment. For macOS/Linux:
```bash
source venv/bin/activate
```
For Windows:
```bash
.\venv\Scripts\activate
```
3. Install dependencies.
```bash
pip install -r requirements.txt
```

4. Initialize the database schema.
```bash
python schema.py
```

5. Populate the database with sample data.
```bash
python data.py
```

6. Run the queries and transactions.
```bash
python queries.py
```

7. Test CRUD operations (putting information, retrieving information, updating information and deleting information using the defined schema).
```bash
pytest
```

## Primary Objectives

The primary objectives of the Health and Fitness Tracking App include:

- **Tracking Various Health Metrics**: Including weight, body mass index (BMI), heart rate, and blood pressure.
- **Logging Physical Activities**: Users can log different types of workouts, detailing the duration, intensity, and calories burned.
- **Monitoring Nutrition**: Through detailed nutrition logs, users can track their daily food and caloric intake.
- **Assessing Sleep Patterns**: By recording sleep duration and quality, the app helps users understand their sleep habits and their impact on health and fitness.
- **Providing Personalized Recommendations**: Based on the data collected, the app has the setup required to offer tailored advice on diet, exercise, and lifestyle adjustments to help users meet their fitness and health objectives.

## Target Audience

The Health and Fitness Tracking App is aimed at a broad audience, ranging from fitness enthusiasts and athletes to individuals seeking to start or improve their health and wellness journey. Regardless of fitness level, age, or health goals, the app is designed to provide valuable insights and support to anyone looking to enhance their overall well-being.

## Benefits to Users

By utilizing the Health and Fitness Tracking App, users will be able to:

- Gain a deeper understanding of their physical activities, dietary habits, and sleep patterns.
- Identify areas of improvement and receive guidance on how to address them.
- Track their progress over time towards achieving specific health and fitness goals.
- Make informed decisions about their health and lifestyle choices based on comprehensive data analysis.

# Identifying Data Requirements

For the Health and Fitness Tracking App to provide comprehensive health and fitness management capabilities, it must efficiently store and manage a variety of data elements. These elements are crucial for tracking user progress, generating insights, and offering personalized recommendations.

## Key Data Elements

The application is designed to manage the following key data elements:

### User Data

- **Attributes**: Includes basic personal information such as name, email, age, and gender.
- **Purpose**: Essential for personalizing the app experience and tailoring recommendations to individual user profiles.

### Workout Information

- **Attributes**: Details of each workout session, including the type of workout (e.g., running, cycling), date and time, duration, intensity level, and calories burned.
- **Purpose**: Enables users to track their physical activities, monitor progress, and adjust their fitness routines accordingly.

### Nutrition Logs

- **Attributes**: Information on daily food intake, specifying meal types, food items, quantity, and caloric content.
- **Purpose**: Crucial for understanding dietary habits, managing caloric intake, and providing nutritional advice.

### Sleep Patterns

- **Attributes**: Records of sleep duration and quality, collected on a daily basis.
- **Purpose**: Offers insights into sleep habits, highlights the impact of sleep on health and fitness, and suggests improvements.

### Health Metrics

- **Attributes**: Health-related metrics such as weight, BMI, heart rate, and blood pressure.
- **Purpose**: Tracks overall health status, supports goal setting, and facilitates the monitoring of health improvements over time.

## Relationships Between Data Elements

The success of the Health and Fitness Tracking App hinges on its ability to interrelate these data elements to provide a holistic view of a user's health and fitness journey. Here are some of the critical relationships:

- **User and Goals**: Each user can set multiple fitness and health goals, allowing for personalized tracking and recommendations.
- **Workouts and Health Metrics**: Analyzing workouts in conjunction with health metrics such as weight and heart rate helps in assessing the effectiveness of exercise routines.
- **Nutrition Logs and Health Metrics**: Dietary habits directly impact health metrics; tracking both allows for nutritional adjustments based on health goals.
- **Sleep Patterns and Workouts**: Understanding the correlation between sleep quality and workout performance can lead to more effective fitness schedules.

## Importance of Capturing These Data Points

Collecting and analyzing these data points are fundamental for the application's ability to:

- Provide a comprehensive health and fitness management platform.
- Offer insights and recommendations that are tailored to the user's unique health profile and goals.
- Enable users to make informed decisions about their health, diet, and fitness routines.
- Facilitate continuous monitoring and adaptation of health and fitness strategies to meet individual user needs effectively.



# Design the SQL Data Schema

The Health and Fitness Tracking App's database schema is meticulously designed to cater to the comprehensive tracking of health and fitness data. This section outlines the schema design, focusing on the structure of tables, their relationships, primary and foreign keys, and the rationale behind specific design decisions.

## Schema Overview

The schema comprises several interconnected tables designed to store information about users, their fitness goals, workout sessions, nutrition logs, sleep records, and health metrics. Below is a detailed explanation of each table and its role within the database.

### Users Table

- **Purpose**: Stores essential information about the app's users.
- **Columns**: Includes `id` (primary key), `name`, `email` (unique), `age`, and `gender`.
- **Design Rationale**: Acts as the central table that connects to other data points through relationships. The uniqueness constraint on the email ensures each user account is unique.

### Goals Table

- **Purpose**: Captures the fitness and health goals of each user.
- **Columns**: `id` (primary key), `user_id` (foreign key), `goal_type`, and `target`.
- **Design Rationale**: Links to the `Users` table via `user_id` to associate each goal with a specific user. Supports tracking of multiple goals per user.

### Workouts Table

- **Purpose**: Records details about each workout session.
- **Columns**: `id`, `user_id`, `date`, `type`, `duration_minutes`, `intensity`, and `calories_burned`.
- **Design Rationale**: `user_id` establishes a relationship with the `Users` table, enabling per-user workout tracking. The table is designed to capture comprehensive details about each workout session.

### NutritionLogs Table

- **Purpose**: Logs daily nutritional intake.
- **Columns**: `id`, `user_id`, `date`, `meal_type`, `food_item`, `quantity`, and `calories`.
- **Design Rationale**: Connected to the `Users` table through `user_id`. It allows detailed tracking of nutritional habits, crucial for dietary management and health monitoring.

### SleepRecords Table

- **Purpose**: Keeps track of sleep patterns.
- **Columns**: `id`, `user_id`, `date`, `duration_hours`, and `quality`.
- **Design Rationale**: Links to `Users` through `user_id`, enabling the analysis of sleep habits and their impact on health and fitness.

### HealthMetrics Table

- **Purpose**: Stores health-related metrics.
- **Columns**: `id`, `user_id`, `date`, `weight`, `bmi`, `heart_rate`, and `blood_pressure`.
- **Design Rationale**: The association with `Users` allows for longitudinal tracking of crucial health indicators, facilitating goal setting and progress tracking.

## Relationships and Constraints

- **Foreign Keys**: Ensure data integrity and establish relationships between user activities, goals, and health metrics.
- **Primary Keys**: Uniquely identify each record across the tables, facilitating efficient data retrieval and updates.
- **Unique Constraints**: Applied to the `email` column in the `Users` table to ensure each user's uniqueness.

## Schema Justification

The design of the SQL data schema is closely aligned with the application's objectives of providing a comprehensive platform for health and fitness tracking. By categorizing data into logically structured tables and establishing relationships between them, the schema supports:

- **Personalized Tracking**: The relational model enables the storage of personalized data across different health and fitness dimensions.
- **Comprehensive Analysis**: By correlating data from various tables, the app can generate holistic insights into a user's health and fitness status.
- **Goal Monitoring**: The goals and health metrics tables allow users to set, monitor, and adjust their health and fitness objectives based on tracked data.


# SQL Query Scenarios

The Health and Fitness Tracking App leverages a robust SQL database to store and manage a wide array of health and fitness data. To extract meaningful insights and support various app functionalities, we have devised a series of SQL queries that span across different scenarios. These scenarios encompass workout tracking, nutrition analysis, sleep pattern assessment, user progress monitoring, and personalized recommendations.

## Overview of Scenarios

The following list outlines the queries implemented, providing a glimpse into the app's data interaction capabilities:

- **Total Calories Burned Per User**: Aggregates total calories burned from workouts for each user.
- **Average Sleep Duration and Quality by Age Group**: Calculates the average sleep duration and quality, grouped by age.
- **Most Common Workout Type**: Identifies the most frequently logged workout type across all users.
- **User Progress Over Time**: Tracks changes in health metrics for a specific user over time.
- **Top 5 High Calorie Foods Logged**: Lists the top five food items with the highest average calorie count logged by users.
- **Users Not Meeting Sleep Quality Goals**: Finds users whose average sleep quality is below a predefined goal.
- **Workout Frequency by Type for a User**: Counts how often each workout type is performed by a specific user.
- **Average Daily Caloric Intake Per User**: Computes the average daily caloric intake for each user.
- **Improvement in Workout Intensity**: Analyzes changes in the intensity of workouts for a user over time.
- **Nutritional Deficit or Surplus**: Evaluates days when a user's caloric intake was significantly above or below their dietary goals.
- **User Workout Details**: Displays details of recent workouts for users, including type and duration.
- **Users with Workouts but No Nutrition Logs on the Same Day**: Identifies users who have logged workouts but have not logged nutrition information on the same day.
- **Total Sleep Hours vs. Workout Hours Last Month**: Compares total hours slept to total hours spent working out for users in the last month.
- **Users Achieving Calorie Intake Goal**: Identifies users who meet or exceed a specified daily calorie intake goal.
- **Users Who Improved Sleep Quality Over the Past Month**: Lists users who have shown improvement in sleep quality over the past month.
- **Workout Type and Average Calories Burned**: Aggregates workouts by type and calculates the average calories burned for each type.
- **Monthly Weight Records for User**: Shows average weight records by month for a specific user, providing insights into their weight trends.
- **Latest High Quality Sleep Records**: Lists users with their most recent high-quality sleep records, focusing on sleep quality and date.

## **Transactions**

In the Health and Fitness Tracking App, transactions are crucial for maintaining data integrity during operations that involve multiple, related changes to the database. Here's how transactions are employed in the app:

### **Adding New User and Health Metrics**

A transaction is used when adding a new user along with their initial health metrics to the database. This ensures that either both the user and their health metrics are successfully added, or neither is, preventing partial updates that could lead to data inconsistency.

### **Updating User Workout and Adding Nutrition Log**

Another transaction updates a user's workout information and adds a nutrition log entry for the same day. This atomic operation ensures that workout updates and nutrition log additions are always synchronized, reflecting a comprehensive view of the user's fitness activities and dietary intake for that day.

These transactions are implemented with careful exception handling, where any failure in the operation leads to a rollback, preserving the integrity of the database.

## **Indices**

The application utilizes covering indices to optimize query performance for frequent and critical data retrieval operations. Here are the indices used:

### **Workout Type and Average Calories Burned**

The **`idx_workout_type_calories`** index on the **`Workout`** table, covering **`type`** and **`calories_burned`**, enhances the performance of queries aggregating workouts by type and calculating the average calories burned. This index speeds up data access for these common queries, improving the app's responsiveness.

### **Health Metric Trends**

The **`idx_health_metric_date_weight`** index on the **`HealthMetric`** table, covering **`date`** and **`weight`**, optimizes queries analyzing weight trends over time for a given user. By facilitating quicker access to health metrics based on dates, this index supports efficient tracking of user progress and health changes.

### **Sleep Record Analysis**

For sleep records, the **`idx_sleep_record_date_quality`** index, covering **`date`** desc and **`quality`**, significantly improves the performance of queries fetching the latest high-quality sleep records. It allows the database to quickly sort and filter sleep data, enabling the app to provide timely insights into sleep patterns.

These indices play a vital role in ensuring that the app can retrieve and analyze health and fitness data efficiently, offering users fast and reliable access to their information and insights.

## Data Normalization and Schema Design

The database schema adheres to the Third Normal Form (3NF) to ensure data integrity, reduce redundancy, and simplify data management:

- **Elimination of Duplication**: Each piece of information is stored only once, reducing redundancy and potential inconsistencies. For instance, user details are stored in a single `Users` table and referenced elsewhere via foreign keys.
- **Dependency on Primary Key**: All attributes in each table are directly dependent on the primary key, ensuring that each table contains data related to a single entity.
- **Transitive Dependency Removal**: There are no transitive dependencies in any table, meaning that non-key attributes do not depend on other non-key attributes.

By adhering to these principles, the schema ensures efficient data storage, ease of data retrieval, and flexibility for future enhancements.

# Data Population

To thoroughly test the Health and Fitness Tracking App's functionality and ensure the SQL queries return meaningful insights, we've implemented a process for generating and populating the database with sample data. This step is crucial for simulating real-world usage scenarios and validating the application's data handling capabilities.

## Overview

The data population process involves creating fake, yet realistic, records across various categories:

- **User Profiles**: A diverse set of user profiles to represent the app's wide target audience.
- **Workout Sessions**: Different types of workout sessions, varying in intensity, duration, and calories burned.
- **Nutrition Logs**: Detailed logs of daily food intake, including meal types, food items, quantities, and caloric content.
- **Sleep Patterns**: Records of sleep duration and quality, reflecting typical variations in user sleep habits.
- **Health Metrics**: Key health metrics such as weight, BMI, heart rate, and blood pressure, captured over time to enable progress tracking.

## Implementation

Using the Python `Faker` library, we generate sample data that closely mimics real user inputs. Here's a breakdown of the steps involved in the data population process:

1. **Create Fake Users**: Generates user profiles with varied names, ages, genders, and email addresses.
2. **Log Workout Sessions**: For each user, logs a range of workout sessions with details such as date, type, duration, and calories burned.
3. **Record Nutrition Logs**: Adds daily nutrition logs for users, including meal types and detailed food item entries.
4. **Capture Sleep Patterns**: Inputs records of sleep, detailing the duration and quality for different nights.
5. **Track Health Metrics**: Generates entries for health metrics, reflecting changes in weight, BMI, heart rate, and blood pressure over time.

This approach ensures a comprehensive dataset that supports extensive testing of the app's functionalities, from basic data retrieval to complex analytical queries.

## Benefits

Populating the database with sample data has several key benefits:

- **Query Testing**: Allows for the thorough testing of SQL queries under various scenarios, ensuring accurate and efficient data retrieval.
- **Feature Validation**: Supports the validation of app features, particularly those relying on data analysis and personalized recommendations.
- **User Experience Simulation**: Facilitates the simulation of real-world user experiences, helping identify potential improvements in the app's design and functionality.

# **Extended Model Testing with `test_models_CRUD.py`**

The **`test_models_CRUD.py`** file in our project has been enhanced to cover a comprehensive testing strategy, ensuring robustness in the application's data management. This file now includes tests for CRUD (Create, Read, Update, Delete) operations for each model within the Health and Fitness Tracking App. Here’s a breakdown of the new functionalities tested:

## **CRUD Operations:**

- **Create**: Tests now include adding new records to the database for each model (**`User`**, **`Goal`**, **`Workout`**, **`NutritionLog`**, **`SleepRecord`**, **`HealthMetric`**), ensuring that data is correctly persisted.
- **Read**: After creating records, tests retrieve these records from the database to verify that the data stored matches the expected values. This ensures the integrity of the data retrieval processes.
- **Update**: For each model, tests have been added to modify existing records (e.g., updating a user's name, changing the duration of a workout). These tests confirm that updates are correctly applied and persisted in the database.
- **Delete**: Finally, each test includes steps to delete the records created during the test. This ensures that deletion operations correctly remove data from the database, maintaining the cleanliness and accuracy of the dataset.