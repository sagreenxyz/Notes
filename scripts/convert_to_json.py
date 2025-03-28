import os
import json
from bs4 import BeautifulSoup

def parse_questions(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    chapters = soup.find_all('section')
    challenges = []

    for chapter in chapters:
        chapter_title = chapter.find('h2').text.strip()  # Extract chapter title from the h2 tag inside the section
        if "Chapter" in chapter_title and "-" in chapter_title:
            chapter_title = int(chapter_title.split(' ')[1])  # Extract and convert the chapter number to an integer
        questions = chapter.find_all('li')
        
        for question in questions:
            question_text = question.find('p').text.strip() if question.find('p') else None
            options = [li.text.strip() for li in question.find('ul').find_all('li')] if question.find('ul') else []  # Extract options
            correct_answers_text = question.find('strong', text='Correct Answer:').next_sibling.strip() if question.find('strong', text='Correct Answer:') else None
            correct_answers = [options.index(answer.strip()) for answer in correct_answers_text.split(',') if answer.strip() in options] if correct_answers_text else []  # Convert to indices
            explanation = question.find('strong', text='Explanation:').next_sibling.strip() if question.find('strong', text='Explanation:') else None
            
            if question_text and correct_answers and explanation:
                challenges.append({
                    "chapter": chapter_title,  # Store the chapter as an integer
                    "question": question_text,
                    "options": options,
                    "correct_answers": correct_answers,  # Store indices of correct answers
                    "explanation": explanation
                })
    
    return challenges

def save_to_json(data, output_filepath):
    os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
    with open(output_filepath, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    input_filepath = "/home/sagreen/Notes/src/routes/+page.svelte"
    output_filepath = "/home/sagreen/Notes/output/challenges.json"
    
    questions = parse_questions(input_filepath)
    save_to_json(questions, output_filepath)
    print(f"Questions successfully saved to {output_filepath}")
