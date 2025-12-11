import os
import re

def extract_schedules(input_file):
    weekdays = ["1_Montag", "2_Dienstag", "3_Mittwoch", "4_Donnerstag", "5_Freitag"]
    
    # Match "-16:00" up to "-23:59" (hour 16–23, any minutes)
    # allows optional spaces after the dash: "-16:00", "- 16:00"
    end_time_pattern = re.compile(r'-\s*(1[6-9]|2[0-3]):[0-5]\d')

    if not os.path.exists("days"):
        os.makedirs("days")
    
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    schedule_chunks = []
    current_schedule = []

    for line in lines:
        current_schedule.append(line)

        # End of chunk if line contains a time -16:00 to -23:59
        if end_time_pattern.search(line):
            schedule_chunks.append(current_schedule)
            current_schedule = []
    
    for i, schedule in enumerate(schedule_chunks):
        weekday_name = weekdays[i % len(weekdays)]
        with open(f"days/{weekday_name}_schedule.txt", 'w') as f:
            f.writelines(schedule)
