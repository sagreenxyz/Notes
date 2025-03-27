<script>
  // Flashcards Data
  export let flashCards = [
    {
      id: 1,
      chapter: 1,
      subchapter: 2,
      question: "What are the levels of structural organization in the human body?",
      answer: "Subatomic particles, atoms, molecules, organelles, cells, tissues, organs, organ systems, organism, and biosphere.",
      explanation: "The human body is organized hierarchically, starting from the simplest level (subatomic particles) to the most complex (biosphere).",
      difficulty: 3,
      showAnswer: false
    },
    {
      id: 2,
      chapter: 1,
      subchapter: 2,
      question: "What is the smallest unit of life?",
      answer: "The cell.",
      explanation: "Cells are the basic structural and functional units of life, made up of organelles.",
      difficulty: 2,
      showAnswer: false
    },
    {
      id: 3,
      chapter: 1,
      subchapter: 2,
      question: "What are organelles?",
      answer: "Membrane-enclosed bodies within a cell that perform unique functions.",
      explanation: "Examples of organelles include the nucleus, mitochondria, and endoplasmic reticulum.",
      difficulty: 2,
      showAnswer: false
    },
    {
      id: 4,
      chapter: 1,
      subchapter: 2,
      question: "What are the four types of tissues in the human body?",
      answer: "Epithelial, connective, muscle, and nervous tissues.",
      explanation: "Tissues are groups of cells with a common embryonic origin that share morphological features and perform specific functions.",
      difficulty: 3,
      showAnswer: false
    },
    {
      id: 5,
      chapter: 1,
      subchapter: 2,
      question: "How many organ systems are in the human body?",
      answer: "Eleven.",
      explanation: "The human body has eleven organ systems, including the integumentary, muscular, skeletal, endocrine, nervous, cardiovascular, lymphatic, respiratory, digestive, urinary, and reproductive systems.",
      difficulty: 3,
      showAnswer: false
    },
    {
      id: 6,
      chapter: 1,
      subchapter: 2,
      question: "What are molecules?",
      answer: "Molecules are formed when two or more atoms combine.",
      explanation: "Molecules, such as water and proteins, are the chemical building blocks of all body structures.",
      difficulty: 2,
      showAnswer: false
    },
    {
      id: 7,
      chapter: 1,
      subchapter: 2,
      question: "What is an organ?",
      answer: "An organ is a structure composed of two or more different tissues working together to perform specific functions.",
      explanation: "Examples of organs include the heart, lungs, and stomach.",
      difficulty: 3,
      showAnswer: false
    },
    {
      id: 8,
      chapter: 1,
      subchapter: 2,
      question: "What is the biosphere?",
      answer: "The biosphere includes all organisms on Earth and their environments.",
      explanation: "The biosphere represents the most complex level of structural organization.",
      difficulty: 4,
      showAnswer: false
    },
    {
      id: 9,
      chapter: 1,
      subchapter: 2,
      question: "What are examples of organelles?",
      answer: "Examples include the nucleus, mitochondria, and endoplasmic reticulum.",
      explanation: "Organelles are membrane-enclosed bodies within a cell that perform unique functions.",
      difficulty: 2,
      showAnswer: false
    },
    {
      id: 10,
      chapter: 1,
      subchapter: 2,
      question: "What is the relationship between cells and tissues?",
      answer: "Cells form tissues.",
      explanation: "Tissues are groups of cells with a common origin that perform specific functions.",
      difficulty: 2,
      showAnswer: false
    }
  ];

  // Questions Data
  export let questions = [
    {
      id: 1,
      chapter: 1,
      subchapter: 2,
      type: "multiple-choice",
      question: "What is the smallest unit of an element?",
      options: [
        "Molecule",
        "Atom",
        "Cell",
        "Organ"
      ],
      correctAnswer: 1,
      explanation: "Atoms are the smallest units of an element, composed of subatomic particles such as protons, neutrons, and electrons."
    },
    {
      id: 2,
      chapter: 1,
      subchapter: 2,
      type: "multiple-choice",
      question: "Which level of structural organization is the simplest?",
      options: [
        "Organ",
        "Molecule",
        "Subatomic particles",
        "Tissue"
      ],
      correctAnswer: 2,
      explanation: "Subatomic particles, such as protons, neutrons, and electrons, are the simplest level of structural organization."
    },
    {
      id: 3,
      chapter: 1,
      subchapter: 2,
      type: "multiple-choice",
      question: "Which of the following is NOT one of the four types of tissues?",
      options: [
        "Epithelial",
        "Connective",
        "Muscle",
        "Skeletal"
      ],
      correctAnswer: 3,
      explanation: "The four types of tissues are epithelial, connective, muscle, and nervous tissues. Skeletal is not a tissue type."
    },
    {
      id: 4,
      chapter: 1,
      subchapter: 2,
      type: "multiple-choice",
      question: "What is an example of an organ system?",
      options: [
        "The heart",
        "The digestive system",
        "A neuron",
        "The nucleus"
      ],
      correctAnswer: 1,
      explanation: "The digestive system is an organ system that includes organs such as the stomach and intestines, working together to perform digestion."
    },
    {
      id: 5,
      chapter: 1,
      subchapter: 2,
      type: "multiple-choice",
      question: "What is the relationship between anatomy and physiology?",
      options: [
        "Anatomy studies structure, while physiology studies function.",
        "Anatomy studies function, while physiology studies structure.",
        "Both study the same aspects of the human body.",
        "Neither is related to the human body."
      ],
      correctAnswer: 0,
      explanation: "Anatomy provides the structural framework of the human body, while physiology explains how these structures function."
    },
    {
      id: 6,
      chapter: 1,
      subchapter: 2,
      type: "multiple-choice",
      question: "What is the most complex level of structural organization?",
      options: [
        "Organism",
        "Organ system",
        "Biosphere",
        "Tissue"
      ],
      correctAnswer: 2,
      explanation: "The biosphere includes all organisms on Earth and their environments, making it the most complex level."
    },
    {
      id: 7,
      chapter: 1,
      subchapter: 2,
      type: "multiple-choice",
      question: "Which of the following is an example of an organelle?",
      options: [
        "Heart",
        "Mitochondria",
        "Neuron",
        "Skin"
      ],
      correctAnswer: 1,
      explanation: "Mitochondria are organelles that perform specific functions within a cell."
    },
    {
      id: 8,
      chapter: 1,
      subchapter: 2,
      type: "multiple-choice",
      question: "What is the primary function of tissues?",
      options: [
        "To form organ systems",
        "To perform specific functions",
        "To create molecules",
        "To regulate homeostasis"
      ],
      correctAnswer: 1,
      explanation: "Tissues are groups of cells that share morphological features and perform specific functions."
    },
    {
      id: 9,
      chapter: 1,
      subchapter: 2,
      type: "multiple-choice",
      question: "What is the smallest unit of an organism that can perform all physiological functions?",
      options: [
        "Atom",
        "Molecule",
        "Cell",
        "Organ"
      ],
      correctAnswer: 2,
      explanation: "The cell is the smallest unit of an organism that can independently perform all physiological functions."
    },
    {
      id: 10,
      chapter: 1,
      subchapter: 2,
      type: "multiple-choice",
      question: "Which organ system includes the heart and blood vessels?",
      options: [
        "Respiratory system",
        "Cardiovascular system",
        "Digestive system",
        "Nervous system"
      ],
      correctAnswer: 1,
      explanation: "The cardiovascular system includes the heart and blood vessels, which work together to circulate blood."
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
  <li>The human body is organized hierarchically, starting from the simplest level to the most complex:</li>
  <ul>
    <li><strong>Subatomic particles:</strong> Protons, neutrons, and electrons.</li>
    <li><strong>Atoms:</strong> The smallest unit of an element, such as hydrogen, oxygen, and carbon.</li>
    <li><strong>Molecules:</strong> Formed when two or more atoms combine, such as water and proteins.</li>
    <li><strong>Organelles:</strong> Membrane-enclosed bodies within a cell, such as the nucleus and mitochondria.</li>
    <li><strong>Cells:</strong> The basic structural and functional units of life.</li>
    <li><strong>Tissues:</strong> Groups of cells with a common origin, such as epithelial and connective tissues.</li>
    <li><strong>Organs:</strong> Structures composed of two or more different tissues, such as the heart and lungs.</li>
    <li><strong>Organ systems:</strong> Groups of organs working together, such as the digestive system.</li>
    <li><strong>Organism:</strong> A living being capable of performing all necessary physiological functions.</li>
    <li><strong>Biosphere:</strong> All organisms on Earth and their environments.</li>
  </ul>
  <li>Cells are the basic units of life, made up of organelles that perform specific functions.</li>
  <li>Tissues are groups of cells that share morphological features and perform specific functions.</li>
  <li>The human body has eleven organ systems, each contributing to life-sustaining processes.</li>
  <li>Anatomy provides the structural framework of the human body, while physiology explains how these structures function.</li>
</ul>

<h2>Questions</h2>
<div class="admonishment question">
  <h3>What are the levels of structural organization in the human body?</h3>
  <p>The levels are subatomic particles, atoms, molecules, organelles, cells, tissues, organs, organ systems, organism, and biosphere.</p>
</div>

<div class="admonishment question">
  <h3>What is the smallest unit of life?</h3>
  <p>The cell is the smallest unit of life, made up of organelles.</p>
</div>

<div class="admonishment question">
  <h3>How many organ systems are in the human body?</h3>
  <p>The human body has eleven organ systems, including the digestive and respiratory systems.</p>
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
  Section 1.2 of "OpenStax Anatomy and Physiology 2e" and "Unit 1.pdf" discusses the **structural organization of the human body**, outlining the hierarchical levels from the simplest to the most complex. These levels are:

  *   **Subatomic particles**: Protons, neutrons, and electrons.
  *   **Atoms**: The smallest unit of an element, composed of subatomic particles. Examples include hydrogen, oxygen, carbon, nitrogen, calcium, and iron.
  *   **Molecules**: Formed when two or more atoms combine, such as water, proteins, and sugars. These are the chemical building blocks of all body structures. A pure substance or element contains atoms, which are made up of protons, neutrons, and electrons or subatomic particles. Elements rarely occur alone and combine to form compounds.
  *   **Organelles**: Membrane-enclosed bodies within a cell, each performing a unique function. Examples include the nucleus, mitochondria, and endoplasmic reticulum.
  *   **Cells**: The basic structural and functional units of life, made up of organelles.
  *   **Tissues**: Groups of cells with a common embryonic origin that share morphological features and are arranged in an orderly pattern to achieve specific functions. Examples include epithelial, connective, muscle, and nervous tissues.
  *   **Organs**: Structures composed of two or more different tissues working together to perform specific functions.
  *   **Organ systems**: Groups of organs that work together to perform a unique body function. The human body has eleven distinct organ systems: integumentary, muscular, skeletal, endocrine, nervous, cardiovascular, lymphatic, respiratory, digestive, urinary, and reproductive (male and female). Most organs contribute to more than one system.
  *   **Organism**: A living being that has a cellular structure and can independently perform all physiologic functions necessary for life. In multicellular organisms, all levels work together to maintain the life and health of the organism.
  *   **Biosphere**: All the organisms on Earth and their environments.
  
  The sources emphasize that higher levels of organization are built from lower levels, demonstrating an increasing complexity from chemical to organismal. For instance, cells make up tissues, tissues make up organs, and organs make up organ systems.
  
  Section 1.1, **Overview of Anatomy and Physiology**, introduces the two main disciplines for studying the human body. **Anatomy** is defined as the scientific study of the body's structures. It can be studied through macroscopic or gross anatomy (large structures), microscopic anatomy (structures requiring a microscope), regional anatomy (interrelationships of structures in a specific body region), and systemic anatomy (structures of a discrete body system). Regional and systemic anatomy are approaches to studying anatomy, while macroscopic and microscopic anatomy are specialization areas. All branches of anatomy are similar in that they study the body's structures.
  
  **Physiology** is the scientific study of the chemistry and physics of the body's structures and how they work together to support the functions of life. It focuses on the body's tendency toward **homeostasis**, the state of steady internal conditions maintained by living things.
  
  The relationship between section 1.2 and section 1.1 is fundamental: **anatomy provides the structural framework of the human body, while physiology explains how these structures function.** The levels of structural organization described in section 1.2 are the very components that anatomists study and that physiologists investigate to understand their roles in maintaining life and homeostasis. For example, understanding the anatomy of the muscular system (a systemic approach in anatomy) is crucial for understanding muscle contraction and movement (a topic in physiology). Similarly, the structural organization from cells to organ systems provides the basis for understanding the various functions of human life discussed in section 1.3, such as metabolism and responsiveness. The organization of the body, as described in its structural levels, is essential for its function as a human organism. Therefore, a thorough understanding of the anatomical structures (section 1.2) is necessary to comprehend the physiological processes (section 1.1 and beyond) that occur within these structures.
  
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
