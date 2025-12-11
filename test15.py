import os
import math

def parse_duration(duration_str):
    hours, minutes = map(int, duration_str.replace('h', '').replace('min', '').split())
    return hours + math.ceil(minutes / 60)

def calculate_day_hours_in_folder(folder_path, max_hours=8):
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            calculate_day_hours(file_path, max_hours)

def calculate_day_hours(file_path, max_hours=8):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    schedule = []
    total_hours = 0
    
    for line in lines:
        if "Class:" in line and "Duration:" in line:
            class_info, duration_str = line.split("| Duration:")
            duration = parse_duration(duration_str.strip())
            schedule.append([class_info.strip(), duration])
            total_hours += duration
    
    if schedule:
        diff = total_hours - max_hours
        
        if diff > 0:
            max_index = max(range(len(schedule)), key=lambda i: schedule[i][1])
            schedule[max_index][1] = max(0, schedule[max_index][1] - diff)
            total_hours = max_hours
        
        elif diff < 0:
            min_index = max(range(len(schedule)), key=lambda i: schedule[i][1])
            schedule[min_index][1] += abs(diff)
            total_hours = max_hours
    
    updated_lines = [
        f"{class_info} | Duration: {duration}\n"
        for class_info, duration in schedule
    ]
    
    with open(file_path, 'w') as file:
        file.writelines(updated_lines)
