import os
import json
from bs4 import BeautifulSoup

def parse_questions(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    chapters = soup.find_all('section')
    challenges = []
    question_id = 1  # Initialize the unique sequential ID

    for chapter in chapters:
        chapter_h2 = chapter.find('h2')  # Find the h2 tag inside the current section
        chapter_title = chapter_h2.text.strip() if chapter_h2 else "Unknown Chapter"  # Extract chapter title
        if "Chapter" in chapter_title and "-" in chapter_title:  # Ensure it's a valid chapter title
            try:
                chapter_title = int(chapter_title.split(' ')[1])  # Extract the chapter number as an integer
            except ValueError:
                print(f"Skipping invalid chapter title: {chapter_title}")
                continue
        else:
            continue  # Skip sections without valid chapter titles
        
        questions = chapter.find_all('li')
        
        for question in questions:
            question_text = question.find('p').text.strip() if question.find('p') else None
            options = [li.text.strip() for li in question.find('ul').find_all('li')] if question.find('ul') else []  # Extract options
            correct_answers_text = question.find('strong', string='Correct Answer:').next_sibling.strip() if question.find('strong', string='Correct Answer:') else None
            correct_answers = []
            if correct_answers_text:
                correct_answers = [options.index(answer.strip()) for answer in correct_answers_text.split(',') if answer.strip() in options]  # Convert to indices
            explanation = question.find('strong', string='Explanation:').next_sibling.strip() if question.find('strong', string='Explanation:') else None
            
            # Ensure all required fields are present
            if question_text and options and correct_answers:
                challenges.append({
                    "id": question_id,  # Add unique sequential ID
                    "type": ["multiple-choice"] if len(correct_answers) == 1 else ["select-all-that-apply"],  # Changed type to an array
                    "chapter": chapter_title,  # Store the chapter number as an integer
                    "challenge": question_text,  # Renamed from question
                    "options": options,
                    "correct_responses": correct_answers,  # Renamed from correct_answers
                    "challenge_source": "Westcott Anatomy and Physiology Course, 2025-03-28",  # Renamed from question_source
                    "explanation": explanation or "",  # Handle missing explanation
                    "explanation_source": "Microsoft Copilot AI-Generated",  # Add explanation source field
                    "hint": "",  # Add hint field
                    "trick": "",  # Add trick field
                    "notes": "",  # Add notes field
                    "difficulty": 0,  # Add difficulty field
                    "streak": 0  # Add streak field
                })
                question_id += 1  # Increment the ID for the next question
            else:
                print(f"Skipping question due to missing fields in chapter {chapter_title}: {question_text}")
    
    return challenges

def save_to_json(data, output_filepath):
    os.makedirs(os.path.dirname(output_filepath), exist_ok=True)  # Ensure the directory exists
    with open(output_filepath, 'w') as file:
        json.dump(data, file, indent=4)

def document_schema():
    schema = {
        "id": "Unique sequential integer identifier for each question.",
        "type": "Array containing the type of question: ['multiple-choice'] for single-answer questions, ['select-all-that-apply'] for multiple-answer questions.",
        "chapter": "Integer representing the chapter number the question belongs to.",
        "challenge": "The text of the challenge (renamed from question).",
        "options": "List of possible answer options for the challenge.",
        "correct_responses": "List of indices (0-based) of the correct responses in the options array (renamed from correct_answers).",
        "challenge_source": "Source of the challenge, typically a course or material reference (renamed from question_source).",
        "explanation": "Detailed explanation of the correct answer.",
        "explanation_source": "Source of the explanation, typically an AI or human-generated reference.",
        "hint": "Optional hint to help answer the challenge (empty by default).",
        "trick": "Optional trick or tip related to the challenge (empty by default).",
        "notes": "Additional notes about the challenge (empty by default).",
        "difficulty": "Integer representing the difficulty level of the challenge (default is 0).",
        "streak": "Integer representing the streak count for the challenge (default is 0)."
    }
    return schema

if __name__ == "__main__":
    input_filepath = "/home/sagreen/Notes/src/routes/+page.svelte"
    output_filepath = "/home/sagreen/Notes/static/output/challenges.json"  # Updated path
    
    questions = parse_questions(input_filepath)
    save_to_json(questions, output_filepath)
    print(f"Questions successfully saved to {output_filepath}")
    print(f"Total number of records: {len(questions)}")  # Output the total number of records
    
    # Calculate and output the total number of records by chapter
    records_by_chapter = {}
    for question in questions:
        chapter = question["chapter"]
        records_by_chapter[chapter] = records_by_chapter.get(chapter, 0) + 1
    
    print("Total number of records by chapter:")
    for chapter, count in sorted(records_by_chapter.items()):
        print(f"Chapter {chapter}: {count} records")
    
    schema = document_schema()
    print("JSON Schema:")
    for field, description in schema.items():
        print(f"{field}: {description}")
