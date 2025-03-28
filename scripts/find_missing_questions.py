import json
import re

def extract_questions_from_svelte(file_path):
    """Extract questions from the Svelte file."""
    with open(file_path, 'r') as file:
        content = file.read()
    questions = re.findall(r'<p>(.*?)</p>', content)
    return [q.strip() for q in questions if not q.startswith("<strong>")]

def extract_questions_from_json(file_path):
    """Extract questions from the JSON file."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return [item['challenge'] for item in data]

def find_missing_questions(svelte_questions, json_questions):
    """Find questions in the Svelte file that are not in the JSON file."""
    return [q for q in svelte_questions if q not in json_questions]

if __name__ == "__main__":
    svelte_file = "/home/sagreen/Notes/static/chapter-2p.svelte"
    json_file = "/home/sagreen/Notes/static/output/challenges.json"
    output_file = "/home/sagreen/Notes/static/output/missing_questions.log"

    svelte_questions = extract_questions_from_svelte(svelte_file)
    json_questions = extract_questions_from_json(json_file)

    missing_questions = find_missing_questions(svelte_questions, json_questions)

    with open(output_file, 'a') as file:
        if missing_questions:
            for question in missing_questions:
                file.write(f"{svelte_file}: {question}\n")
        else:
            file.write(f"{svelte_file}: All questions are present in the JSON file.\n")
