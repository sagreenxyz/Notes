<script>
  // Flashcards Data
  export let flashCards = [
    // Add flashcards specific to this section
  ];

  // Questions Data
  export let questions = [
    // Add questions specific to this section
  ];

  // Flashcard Functions
  function toggleAnswer(index) {
    flashCards = flashCards.map((card, i) =>
      i === index ? { ...card, showAnswer: !card.showAnswer } : card
    );
  }

  let currentQuestionIndex = 0;
  let selectedAnswer = null;
  let showExplanation = false;
  let formRef;

  function selectAnswer(answerIndex) {
    selectedAnswer = answerIndex;
    showExplanation = true;
  }

  function nextQuestion() {
    if (currentQuestionIndex < questions.length - 1) {
      currentQuestionIndex++;
      selectedAnswer = null;
      showExplanation = false;
      formRef.reset();
    }
  }

  function prevQuestion() {
    if (currentQuestionIndex > 0) {
      currentQuestionIndex--;
      selectedAnswer = null;
      showExplanation = false;
      formRef.reset();
    }
  }

  let currentFlashCardIndex = 0;

  function nextFlashCard() {
    if (currentFlashCardIndex < flashCards.length - 1) {
      currentFlashCardIndex++;
    }
  }

  function prevFlashCard() {
    if (currentFlashCardIndex > 0) {
      currentFlashCardIndex--;
    }
  }

  function toggleCurrentFlashCardAnswer() {
    flashCards = flashCards.map((card, i) =>
      i === currentFlashCardIndex ? { ...card, showAnswer: !card.showAnswer } : card
    );
  }

  let showFlashcards = false;
  let showQuiz = false;

  function toggleSection(section) {
    if (section === "flashcards") {
      showFlashcards = !showFlashcards;
    } else if (section === "quiz") {
      showQuiz = !showQuiz;
    }
  }
</script>

<h1>1.2 Structural Organization of the Human Body</h1>
<p>This section explores the structural organization of the human body, detailing its hierarchical levels.</p>
<a href="https://openstax.org/books/anatomy-and-physiology-2e/pages/1-2-structural-organization-of-the-human-body" target="_blank" rel="noopener noreferrer">
  Read more on OpenStax
</a>

<h1>Key Points</h1>
<ul>
  <!-- Add key points specific to this section -->
</ul>

<h2>Questions</h2>
<div class="admonishment question">
  <!-- Add questions specific to this section -->
</div>

<h2>Interactive Sections</h2>

<div class="accordion">
  <div class="accordion-item">
    <button class="accordion-header" on:click={() => toggleSection("flashcards")}>
      Flashcards {showFlashcards ? "▼" : "▶"}
    </button>
    {#if showFlashcards}
      <div class="accordion-content">
        <div class="flashcard-container">
          {#if flashCards.length > 0}
            <div class="flashcard">
              <p><strong>Question:</strong> {flashCards[currentFlashCardIndex].question}</p>
              <button on:click={toggleCurrentFlashCardAnswer}>
                {flashCards[currentFlashCardIndex].showAnswer ? 'Hide Answer' : 'Show Answer'}
              </button>
              {#if flashCards[currentFlashCardIndex].showAnswer}
                <p><strong>Answer:</strong> {flashCards[currentFlashCardIndex].answer}</p>
                <p><strong>Explanation:</strong> {flashCards[currentFlashCardIndex].explanation}</p>
              {/if}
            </div>
            <div class="flashcard-navigation">
              <button on:click={prevFlashCard} disabled={currentFlashCardIndex === 0}>
                Previous
              </button>
              <span>Flashcard {currentFlashCardIndex + 1} of {flashCards.length}</span>
              <button on:click={nextFlashCard} disabled={currentFlashCardIndex === flashCards.length - 1}>
                Next
              </button>
            </div>
          {:else}
            <p>No flashcards available.</p>
          {/if}
        </div>
      </div>
    {/if}
  </div>

  <div class="accordion-item">
    <button class="accordion-header" on:click={() => toggleSection("quiz")}>
      Quiz Yourself {showQuiz ? "▼" : "▶"}
    </button>
    {#if showQuiz}
      <div class="accordion-content">
        <div class="quiz-container">
          {#if questions.length > 0}
            <div class="flashcard">
              <p><strong>Question:</strong> {questions[currentQuestionIndex].question}</p>
              <form bind:this={formRef}>
                {#each questions[currentQuestionIndex].options as option, index}
                  <div
                    class="option"
                    class:selected={selectedAnswer === index}
                    class:correct={showExplanation && index === questions[currentQuestionIndex].correctAnswer}
                    class:incorrect={showExplanation && selectedAnswer === index && index !== questions[currentQuestionIndex].correctAnswer}
                  >
                    <input
                      type="radio"
                      id={`option-${index}`}
                      name="question-options"
                      value={index}
                      on:change={() => selectAnswer(index)}
                      disabled={showExplanation}
                    />
                    <label for={`option-${index}`}>{option}</label>
                  </div>
                {/each}
              </form>
              {#if showExplanation}
                <div class="explanation">
                  <p>
                    <strong>
                      {selectedAnswer === questions[currentQuestionIndex].correctAnswer
                        ? "Correct!"
                        : "Incorrect."}
                    </strong>
                  </p>
                  <p><strong>Explanation:</strong> {questions[currentQuestionIndex].explanation}</p>
                </div>
              {/if}
            </div>
            <div class="flashcard-navigation">
              <button on:click={prevQuestion} disabled={currentQuestionIndex === 0}>
                Previous
              </button>
              <span>Question {currentQuestionIndex + 1} of {questions.length}</span>
              <button on:click={nextQuestion} disabled={currentQuestionIndex === questions.length - 1}>
                Next
              </button>
            </div>
          {:else}
            <p>No questions available.</p>
          {/if}
        </div>
      </div>
    {/if}
  </div>
</div>

<h2 class="raw-notes-heading">Raw Notes</h2>
<div class="raw-notes">
  <!-- Content will be pasted here -->
</div>

<style>
  .flashcard-container {
    margin-top: 2rem;
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
  .flashcard {
    border: 1px solid #ccc;
    padding: 1rem;
    border-radius: 8px;
    background-color: #f9f9f9;
  }
  .flashcard button {
    margin-top: 0.5rem;
    padding: 0.5rem 1rem;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  .flashcard button:hover {
    background-color: #0056b3;
  }
  .flashcard-navigation {
    margin-top: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .flashcard-navigation button {
    padding: 0.5rem 1rem;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  .flashcard-navigation button:disabled {
    background-color: #ccc;
    cursor: not-allowed;
  }
  .flashcard-navigation span {
    font-weight: bold;
  }
  .quiz-container {
    margin-top: 2rem;
  }
  .quiz-container .flashcard {
    border: 1px solid #ccc;
    padding: 1rem;
    border-radius: 8px;
    background-color: #f9f9f9;
  }
  .quiz-container .flashcard ul {
    list-style: none;
    padding: 0;
  }
  .quiz-container .flashcard li {
    margin-bottom: 0.5rem;
  }
  .quiz-container .flashcard button {
    padding: 0.5rem 1rem;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  .quiz-container .flashcard button:hover {
    background-color: #0056b3;
  }
  .quiz-container .flashcard button.selected {
    background-color: #28a745;
  }
  .quiz-container .flashcard button:disabled {
    background-color: #ccc;
    cursor: not-allowed;
  }
  .quiz-container .flashcard .explanation {
    margin-top: 1rem;
    padding: 1rem;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #e9ecef;
  }
  .quiz-container .flashcard-navigation {
    margin-top: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center.
  }
  .quiz-container .flashcard-navigation button {
    padding: 0.5rem 1rem;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer.
  }
  .quiz-container .flashcard-navigation button:disabled {
    background-color: #ccc;
    cursor: not-allowed.
  }
  .quiz-container .flashcard-navigation span {
    font-weight: bold.
  }
  .accordion {
    margin-top: 2rem.
  }
  .accordion-item {
    margin-bottom: 1rem.
  }
  .accordion-header {
    width: 100%;
    text-align: left;
    padding: 0.5rem 1rem;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1rem.
  }
  .accordion-header:hover {
    background-color: #0056b3.
  }
  .accordion-content {
    margin-top: 0.5rem;
    padding: 1rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    background-color: #f9f9f9.
  }
  .quiz-container .option {
    margin-bottom: 0.5rem;
    display: flex;
    align-items: center;
  }
  .quiz-container .option input[type="radio"] {
    margin-right: 0.5rem;
  }
  .quiz-container .option label {
    cursor: pointer;
  }
  .quiz-container .option.correct label {
    color: #28a745; /* Green for correct */
    font-weight: bold;
  }
  .quiz-container .option.incorrect label {
    color: #dc3545; /* Red for incorrect */
    font-weight: bold;
  }
  .raw-notes-heading {
    display: none; /* Hide the raw notes heading */
  }
  .raw-notes {
    margin-top: 2rem;
    display: none; /* Hide the raw notes section */
  }
</style>
