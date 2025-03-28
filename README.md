## Ideas
- question hints, explanations, and memorization ideas
- question type should be array. multiple-choice, flashcard, select-all-that-apply.

---

2025-03-27: I would copy a quiz into the landing page "./routes/+page.svelte" then tell Copilot to perform formatting of that data. I would then preserve the results after ensuring the 20 questions were processed.

This is my conversation with Copilot to preserve the instructions:

What is your understanding of what needs to be done when I would tell you, "fresh data - 20 questions"?

GitHub Copilot
When you say, "fresh data - 20 questions", my understanding is:

Purpose:

You want me to format and retain only the "Questions" section from the provided data, which contains 20 questions.
File Handling:

If the file already exists, I will modify it directly.
I will ensure the filepath in the code block matches the original file's filepath exactly.
Content Changes:

Extract and format the 20 questions from the provided data.
Each question will:
Be enclosed in an <li> tag.
Include a <ul> tag for the answer options.
Highlight the correct answer using a <p> tag with <strong> for emphasis.
Formatting:

Use consistent formatting for all questions.
Represent unchanged regions of the file with ...existing code... to avoid repeating unnecessary content.
Code Block:

Start the code block with a comment containing the filepath (e.g., // filepath: /home/sagreen/Notes/src/routes/+page.svelte).
Output:

Provide the formatted "Questions" section as a complete <section> block with 20 questions.
Let me know if this aligns with your expectations!

---

Parts of a question:
- Passage
- Question
    - Stem
    - Options
        - Answer
        - Distractors
    
