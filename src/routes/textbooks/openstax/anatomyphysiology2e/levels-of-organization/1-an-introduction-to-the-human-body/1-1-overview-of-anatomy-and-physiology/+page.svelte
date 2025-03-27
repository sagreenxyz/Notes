<script>
  // Flashcards Data
  export let flashCards = [
    {
      id: 1,
      chapter: 1,
      subchapter: 1,
      question: "What is anatomy?",
      answer: "The study of the structure of body parts and their relationships to one another.",
      explanation: "Anatomy focuses on the physical structure of the body, including organs, tissues, and systems.",
      difficulty: 2,
      showAnswer: false
    },
    {
      id: 2,
      chapter: 1,
      subchapter: 1,
      question: "What is physiology?",
      answer: "The study of the function of the body’s parts and how they work together.",
      explanation: "Physiology explains how body systems perform their tasks and interact to maintain life.",
      difficulty: 2,
      showAnswer: false
    },
    {
      id: 3,
      chapter: 1,
      subchapter: 1,
      question: "How are anatomy and physiology related?",
      answer: "Structure and function are closely related; anatomy provides the map, and physiology explains the processes.",
      explanation: "Understanding anatomy helps explain the physical basis for physiological functions.",
      difficulty: 3,
      showAnswer: false
    },
    {
      id: 4,
      chapter: 1,
      subchapter: 1,
      question: "What are the two main subdivisions of anatomy?",
      answer: "Gross anatomy and microscopic anatomy.",
      explanation: "Gross anatomy studies large structures visible to the naked eye, while microscopic anatomy focuses on structures requiring magnification.",
      difficulty: 3,
      showAnswer: false
    },
    {
      id: 5,
      chapter: 1,
      subchapter: 1,
      question: "What is homeostasis?",
      answer: "The state of steady internal conditions maintained by living organisms.",
      explanation: "Homeostasis is essential for survival, ensuring that internal conditions remain stable despite external changes.",
      difficulty: 4,
      showAnswer: false
    }
  ];

  // Questions Data
  export let questions = [
    {
      id: 1,
      chapter: 1,
      subchapter: 1,
      type: "multiple-choice",
      question: "What is anatomy?",
      options: [
        "The study of the function of the body’s parts.",
        "The scientific study of the body’s structures.",
        "The study of homeostasis.",
        "The study of body systems."
      ],
      correctAnswer: 1,
      explanation: "Anatomy is the scientific study of the body’s structures, focusing on the form and composition of the body's components."
    },
    {
      id: 2,
      chapter: 1,
      subchapter: 1,
      type: "multiple-choice",
      question: "What are the two main subdivisions of anatomy?",
      options: [
        "Gross anatomy and systemic anatomy.",
        "Microscopic anatomy and regional anatomy.",
        "Gross anatomy and microscopic anatomy.",
        "Cytology and histology."
      ],
      correctAnswer: 2,
      explanation: "Gross anatomy studies larger structures visible without magnification, while microscopic anatomy focuses on structures requiring magnification."
    },
    {
      id: 3,
      chapter: 1,
      subchapter: 1,
      type: "multiple-choice",
      question: "What are the two approaches used by anatomists?",
      options: [
        "Regional anatomy and systemic anatomy.",
        "Gross anatomy and microscopic anatomy.",
        "Cytology and histology.",
        "Physiology and homeostasis."
      ],
      correctAnswer: 0,
      explanation: "Regional anatomy examines structures within a specific body region, while systemic anatomy focuses on body systems, such as the muscular system."
    },
    {
      id: 4,
      chapter: 1,
      subchapter: 1,
      type: "multiple-choice",
      question: "What is physiology?",
      options: [
        "The study of the structure of body parts.",
        "The scientific study of the chemistry and physics of the body’s structures.",
        "The study of homeostasis.",
        "The study of body systems."
      ],
      correctAnswer: 1,
      explanation: "Physiology is the scientific study of the chemistry and physics of the body’s structures and how they work together to support life."
    },
    {
      id: 5,
      chapter: 1,
      subchapter: 1,
      type: "multiple-choice",
      question: "What is homeostasis?",
      options: [
        "The study of body systems.",
        "The state of steady internal conditions maintained by living things.",
        "The study of the function of the body’s parts.",
        "The scientific study of the body’s structures."
      ],
      correctAnswer: 1,
      explanation: "Homeostasis is the state of steady internal conditions maintained by living things, essential for normal functioning and life."
    },
    {
      id: 6,
      chapter: 1,
      subchapter: 1,
      type: "multiple-choice",
      question: "What are examples of parameters regulated by homeostasis?",
      options: [
        "Body temperature, blood pressure, and blood glucose levels.",
        "Body systems and their functions.",
        "The structure of cells and tissues.",
        "The chemistry and physics of the body’s structures."
      ],
      correctAnswer: 0,
      explanation: "Examples of parameters regulated by homeostasis include body temperature, blood pressure, blood glucose levels, water concentration, pH of blood and fluids, and oxygen and carbon dioxide levels."
    }
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
      selectedAnswer = null; // Clear selected answer
      showExplanation = false;
      formRef.reset(); // Reset the form to clear radio buttons
    }
  }

  function prevQuestion() {
    if (currentQuestionIndex > 0) {
      currentQuestionIndex--;
      selectedAnswer = null; // Clear selected answer
      showExplanation = false;
      formRef.reset(); // Reset the form to clear radio buttons
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

  let showFlashcards = false; // Set to false to collapse initially
  let showQuiz = false; // Set to false to collapse initially

  function toggleSection(section) {
    if (section === "flashcards") {
      showFlashcards = !showFlashcards;
    } else if (section === "quiz") {
      showQuiz = !showQuiz;
    }
  }
</script>

<h1>1.1 Overview of Anatomy and Physiology</h1>
<p>This section provides an overview of anatomy and physiology, exploring their definitions and significance.</p>
<a href="https://openstax.org/books/anatomy-and-physiology-2e/pages/1-1-overview-of-anatomy-and-physiology" target="_blank" rel="noopener noreferrer">
  Read more on OpenStax
</a>

<h1>Key Points</h1>
<h2>Anatomy and Its Branches</h2>
<ul>
  <li><strong>Anatomy</strong> is the <strong>scientific study of the body’s structures</strong>, focusing on the <strong>form and composition</strong> of the body's components.</li>
  <li>Historically, anatomy was studied through:
    <ul>
      <li><strong>Injury observation</strong>.</li>
      <li><strong>Cadaver dissection</strong>.</li>
      <li>Modern techniques like <strong>computer-assisted imaging</strong>.</li>
    </ul>
  </li>
  <li>Specializations in anatomy include:
    <ul>
      <li><strong>Gross anatomy</strong> (macroscopic anatomy): Study of <strong>larger structures</strong> visible without magnification.</li>
      <li><strong>Microscopic anatomy</strong>: Study of <strong>structures requiring magnification</strong>, such as cells (<strong>cytology</strong>) and tissues (<strong>histology</strong>).</li>
    </ul>
  </li>
  <li>Anatomists use two approaches:
    <ul>
      <li><strong>Regional anatomy</strong>: Examines structures within a <strong>specific body region</strong>.</li>
      <li><strong>Systemic anatomy</strong>: Focuses on <strong>body systems</strong>, such as the muscular system.</li>
    </ul>
  </li>
  <li>Understanding anatomy is essential for:
    <ul>
      <li>Careers in <strong>health professions</strong>.</li>
      <li>Improving <strong>personal health</strong> and making informed choices.</li>
      <li>Understanding <strong>medical news</strong>, procedures, and devices.</li>
    </ul>
  </li>
  <li>The human body is organized into levels:
    <ul>
      <li><strong>Cells</strong> form <strong>tissues</strong>.</li>
      <li>Tissues form <strong>organs</strong>.</li>
      <li>Organs form <strong>systems</strong>.</li>
    </ul>
  </li>
</ul>

<h2>Physiology</h2>
<ul>
  <li><strong>Physiology</strong> is the <strong>scientific study of the chemistry and physics of the body’s structures</strong> and how they work together to support life.</li>
  <li>Key aspects of physiology:
    <ul>
      <li><strong>Focus on Function:</strong> Explains how body components operate and interact.</li>
      <li><strong>Methods of Study:</strong> Observation, manipulation, and laboratory experiments.</li>
      <li><strong>Specializations:</strong> Includes fields like <strong>neurophysiology</strong>.</li>
      <li><strong>Relationship with Anatomy:</strong> Form (anatomy) often provides insights into function (physiology).</li>
      <li><strong>Homeostasis:</strong> Central to physiology, maintaining steady internal conditions.</li>
      <li><strong>Organ System Functions:</strong> Each system contributes to life-sustaining processes.</li>
    </ul>
  </li>
</ul>

<h2>Homeostasis</h2>
<ul>
  <li><strong>Homeostasis</strong> is the <strong>state of steady internal conditions</strong> maintained by living things.</li>
  <li>Key aspects of homeostasis:
    <ul>
      <li><strong>Steady Internal Conditions:</strong> Includes body temperature, blood pressure, and nutrient levels.</li>
      <li><strong>Normal Range and Set Point:</strong> Physiological values fluctuate within a healthy range.</li>
      <li><strong>Importance:</strong> Essential for normal functioning; deviations can lead to illness or death.</li>
      <li><strong>Maintenance Mechanisms:</strong> Feedback loops regulate internal conditions:
        <ul>
          <li><strong>Negative Feedback:</strong> Reverses deviations to maintain stability (e.g., blood glucose regulation).</li>
          <li><strong>Positive Feedback:</strong> Intensifies changes for specific purposes (e.g., childbirth).</li>
        </ul>
      </li>
      <li><strong>Continuous Process:</strong> Homeostasis is maintained at all times through unconscious processes.</li>
      <li><strong>Examples:</strong> Regulated parameters include:
        <ul>
          <li>Body temperature.</li>
          <li>Blood pressure.</li>
          <li>Blood glucose levels.</li>
          <li>Water concentration.</li>
          <li>pH of blood and fluids.</li>
          <li>Oxygen and carbon dioxide levels.</li>
        </ul>
      </li>
    </ul>
  </li>
</ul>

<h2>Questions</h2>
<div class="admonishment question">
  <h3>What is anatomy?</h3>
  <p>Anatomy is the scientific study of the body’s structures, focusing on the form and composition of the body's components.</p>
</div>

<div class="admonishment question">
  <h3>What is physiology and why is it different from anatomy?</h3>
  <p>Physiology is the scientific study of the chemistry and physics of the body’s structures and how they work together to support life. It differs from anatomy in that it focuses on function rather than form.</p>
</div>

<div class="admonishment question">
  <h3>What is homeostasis?</h3>
  <p>Homeostasis is the state of steady internal conditions maintained by living things, essential for normal functioning and life.</p>
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
</style>