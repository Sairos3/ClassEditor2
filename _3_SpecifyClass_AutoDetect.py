import re

def remove_teams_and_plus_lines(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        keywords = set()

        # 1) AUTO-DETECT class keywords FROM THE Klass LINES
        for line in lines:
            clean = line.replace("\xa0", " ")

            match = re.search(r'\b([A-Za-zÄÖÜäöü]+)\s+(\d{2})\b.*\bmin\b', clean)
            if match:
                name, year = match.groups()
                keywords.add(f"{name} {year}")

        filtered_lines = [
            line for line in lines
            if not any(keyword in line for keyword in keywords)
        ]

        with open(output_file, 'w', encoding='utf-8') as file:
            file.writelines(filtered_lines)

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
