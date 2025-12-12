import re

def clean_schedule(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            schedule_text = file.read()

        cleaned_text = re.sub(
            r'(Teilnehmende|Probe-Prüfung|Unterrichtsfrei|Sonderveranstaltung|Praxisunterricht|Mittagspause|Lernzeit m. Lernzeitbegleitung)\d*\s*min?', 
            r'\1', 
            schedule_text
        )

        cleaned_text = re.sub(
            r'(Praxisunterricht)t?\b.*?\d*\s*mins?', 
            r'\1', 
            cleaned_text, 
            flags=re.IGNORECASE
        )

        cleaned_text = re.sub(
            r'(?mi)^[^:\n]*:\s*\d+\s*mins?\b.*$|^\s*\d+\s*mins?\b.*$',
            'Praxisunterricht',
            cleaned_text
        )
        
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(cleaned_text)

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
