import json

def convert_chapter_to_array(file_path):
    # Load the JSON data
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Update the chapter field
    for challenge in data:
        if 'chapter' in challenge and isinstance(challenge['chapter'], int):
            challenge['chapter'] = [challenge['chapter']]

    # Save the updated JSON data
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    file_path = "/home/sagreen/Notes/output/challenges.json"
    convert_chapter_to_array(file_path)
    print(f"Updated {file_path} successfully.")
