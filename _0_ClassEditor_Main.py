import os
import tkinter as tk
from _1_Select_PDF import main as step1_main
from _2_ExtractDates import step2_main
from _3_SpecifyClass_AutoDetect import remove_teams_and_plus_lines
from _4_Transform_txtControl import add_newline_after_uhr
from _5_Remove_Uhr import remove_word_from_file
from _6_Remove_SpecificLines import remove_lines_with_keywords
from _7_Clean_Breaks import clean_schedule
from _8_Transform_MergeLines import merge_LEK_with_next_line
from _9_Transform_TeacherNames import merge_teacher_names
from _10_Add_TimeControl import add_timestamp_to_schedule
from _11_Extract_WeekDays import extract_schedules
from _12_Process_TimeCalculations import process_all_files_in_days_folder
from _13_Transform_Time import merge_class_durations
from _14_Remove_Breaks import remove_mittagspause_lines
from _15_Limit_MinMaxHours import calculate_day_hours_in_folder
from _16_Remove_0Timestamps import remove_zero_duration_lines
from _17_Create_WordFile import create_schedule_document
from _01_Create_GUI import ThemeEditorApp

def process_schedule_steps():
    steps = [
        ('schedule2.txt', 'schedule3.txt', remove_teams_and_plus_lines),
        ('schedule3.txt', 'schedule4.txt', add_newline_after_uhr),
        ('schedule4.txt', 'schedule5.txt', lambda i, o: remove_word_from_file(i, o, 'Uhr')),
        ('schedule5.txt', 'schedule6.txt', lambda i, o: remove_lines_with_keywords(i, o, ["Theorieunterricht", "Konsultation"])),
        ('schedule6.txt', 'schedule7.txt', clean_schedule),
        ('schedule7.txt', 'schedule8.txt', merge_LEK_with_next_line),
        ('schedule8.txt', 'schedule9.txt', merge_teacher_names),
        ('schedule9.txt', 'schedule10.txt', add_timestamp_to_schedule),
    ]

    for input_file, output_file, func in steps:
        func(input_file, output_file)
        os.remove(input_file)

def finalize_schedule():
    extract_schedules('schedule10.txt')
    os.remove('schedule10.txt')
    process_all_files_in_days_folder()
    merge_class_durations('days')
    remove_mittagspause_lines('days')
    calculate_day_hours_in_folder('days')
    remove_zero_duration_lines('days')
    create_schedule_document(input_file='schedule.txt', folder_path='days', output_file='Weekly_Class_Schedules.docx')

if __name__ == "__main__":
    step1_main()
    step2_main()
    process_schedule_steps()
    finalize_schedule()

    root = tk.Tk()
    app = ThemeEditorApp(root)
    root.mainloop()
