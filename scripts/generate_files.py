import json
from bs4 import BeautifulSoup
import os

# Ensure you have the BeautifulSoup library installed.
# Install it using: pip install beautifulsoup4

# It is recommended to use a virtual environment to manage dependencies.
# Create a virtual environment using: python3 -m venv venv
# Activate it using: source venv/bin/activate
# Then install dependencies: pip install beautifulsoup4

# Input file path
input_file = "/home/sagreen/Notes/src/routes/+page.svelte"

# Output file paths
json_output_file = "/home/sagreen/Notes/output/page_data.json"
html_output_file = "/home/sagreen/Notes/output/updated_page.svelte"

# Ensure the output directory exists
output_dir = "/home/sagreen/Notes/output"
os.makedirs(output_dir, exist_ok=True)

# Read the input file
with open(input_file, "r") as file:
    content = file.read()

# Parse the HTML content
soup = BeautifulSoup(content, "html.parser")

# Read existing JSON data if the file exists
existing_data = {}
if os.path.exists(json_output_file):
    with open(json_output_file, "r") as json_file:
        existing_data = json.load(json_file)

# Extract data for JSON representation
data = []
for section in soup.find_all("section"):
    section_data = {
        "title": section.find("h2").text if section.find("h2") else None,
        "questions": []
    }
    for article in section.find_all("article"):
        # Extract the full question text
        question_tag = article.find("h3")
        question = question_tag.find_next_sibling("p").text.strip() if question_tag and question_tag.find_next_sibling("p") else None
        
        # Extract list of options
        options = [li.text for li in article.find_all("li")]

        # Extract correct_answer as an index
        correct_answer = None
        for p in article.find_all("p"):
            if "Correct Answer:" in p.text:
                correct_answer_text = p.text.replace("Correct Answer:", "").strip()
                if correct_answer_text in options:
                    correct_answer = options.index(correct_answer_text)
                break
        
        # Extract explanation
        explanation = None
        for p in article.find_all("p"):
            if "Explanation:" in p.text:
                explanation = p.text.replace("Explanation:", "").strip()
                break

        # Preserve existing notes if available
        notes = ""
        if existing_data:
            for existing_section in existing_data:
                if existing_section["title"] == section_data["title"]:
                    for existing_question in existing_section.get("questions", []):
                        if existing_question["question"] == question:
                            notes = existing_question.get("notes", "")
                            break

        section_data["questions"].append({
            "type": "multiple-choice",
            "question": question,
            "options": options,
            "correct_answer": correct_answer,
            "explanation": explanation,
            "notes": notes  # Preserve existing notes if not empty
        })
    data.append(section_data)

# Write JSON representation to file
with open(json_output_file, "w") as json_file:
    json.dump(data, json_file, indent=4)

# Add a <p> element for "Notes" to each article
for article in soup.find_all("article"):
    notes_paragraph = soup.new_tag("p")
    notes_paragraph.string = "Notes"
    article.append(notes_paragraph)

# Write updated HTML content to file
with open(html_output_file, "w") as html_file:
    html_file.write(str(soup))
