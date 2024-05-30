# Exercise 4: Health Reminder App

import time

def health_reminder():
    water_interval = 60 * 60  # 1 hour
    eye_exercise_interval = 60 * 30  # 30 minutes
    physical_exercise_interval = 60 * 60 * 2  # 2 hours

    last_water_time = time.time()
    last_eye_exercise_time = time.time()
    last_physical_exercise_time = time.time()

    while True:
        current_time = time.time()

        if current_time - last_water_time > water_interval:
            print("Time to drink water!")
            last_water_time = current_time

        if current_time - last_eye_exercise_time > eye_exercise_interval:
            print("Time to do eye exercises!")
            last_eye_exercise_time = current_time

        if current_time - last_physical_exercise_time > physical_exercise_interval:
            print("Time for physical exercise!")
            last_physical_exercise_time = current_time

        time.sleep(10)

health_reminder()
