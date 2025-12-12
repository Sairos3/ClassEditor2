import re

def add_timestamp_to_schedule(input_file, output_file):
    time_pattern = re.compile(r'\d{1,2}:\d{2}\s*-\s*\d{1,2}:\d{2}')

    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    updated_lines = []

    for line in lines:
        updated_lines.append(line.strip())

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("\n".join(updated_lines))
