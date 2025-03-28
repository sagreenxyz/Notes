<script>
  import { onMount } from 'svelte';
  let challenge13 = null;
  let challenge15 = null;

  onMount(async () => {
    const response = await fetch('/output/challenges.json');
    const data = await response.json();
    challenge13 = data.find(item => item.id === 13);
    challenge15 = data.find(item => item.id === 15);
  });

  function isCorrect(challenge, optionIndex) {
    return challenge.correct_responses.includes(optionIndex);
  }
</script>

<style>
  /* General Typography */
  body {
    font-family: 'Arial', sans-serif; /* Explicitly set to sans-serif */
    line-height: 1.8; /* Increased line height for better readability */
    font-size: 18px; /* Increased font size */
    color: #333;
    background-color: #f9f9f9;
    margin: 0;
    padding: 0;
  }

  /* Page Container */
  .container {
    max-width: 800px;
    margin: 2rem auto;
    padding: 1.5rem; /* Increased padding for better spacing */
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }

  /* Headings */
  h1, h2, h3 {
    font-family: 'Arial', sans-serif; /* Explicitly set to sans-serif */
    color: #2c3e50;
    margin-bottom: 1.5rem; /* Increased margin for better spacing */
  }

  h1 {
    font-size: 3.5rem; /* Increased font size for main heading */
    border-bottom: 2px solid #3498db;
    padding-bottom: 0.5rem;
  }

  h2 {
    font-size: 3rem; /* Increased font size for second-level headings */
    margin-top: 2.5rem;
  }

  h3 {
    font-size: 2.5rem; /* Increased font size for third-level headings */
    margin-top: 2rem;
  }

  h4 {
    font-size: 2rem; /* Increased font size for fourth-level headings */
    margin-top: 1.5rem;
  }

  /* Paragraphs */
  p {
    font-family: 'Arial', sans-serif; /* Explicitly set to sans-serif */
    line-height: 1.8; /* Increased line height */
    font-size: 18px; /* Increased font size */
    margin-bottom: 1.5rem; /* Increased margin for better spacing */
  }

  /* Links */
  a {
    color: #3498db;
    text-decoration: none;
  }

  a:hover {
    text-decoration: underline;
  }

  /* Lists */
  ul {
    margin: 1.5rem 0; /* Increased margin for better spacing */
    padding-left: 1.75rem; /* Adjusted padding for better alignment */
  }

  li {
    font-family: 'Arial', sans-serif; /* Explicitly set to sans-serif */
    margin-bottom: 0.75rem; /* Increased margin for better spacing */
    font-size: 18px; /* Increased font size */
  }

  /* Blockquotes */
  blockquote {
    font-family: 'Arial', sans-serif; /* Explicitly set to sans-serif */
    margin: 1.5rem 0; /* Increased margin for better spacing */
    padding: 1.5rem; /* Increased padding for better readability */
    background: #f1f1f1;
    border-left: 4px solid #3498db;
    font-style: italic;
    color: #555;
    font-size: 18px; /* Increased font size */
  }

  /* Code Blocks */
  pre {
    background: #2c3e50;
    color: #ecf0f1;
    padding: 1.5rem; /* Increased padding for better readability */
    border-radius: 8px;
    overflow-x: auto;
    font-size: 16px; /* Adjusted font size for code blocks */
  }

  code {
    font-family: 'Courier New', monospace;
    background: #ecf0f1;
    padding: 0.3rem 0.5rem; /* Adjusted padding for better readability */
    border-radius: 4px;
    font-size: 16px; /* Adjusted font size for inline code */
  }

  /* Highlighted Sections */
  .highlight {
    background: #fffbcc;
    padding: 0.75rem; /* Increased padding for better readability */
    border-radius: 4px;
    border-left: 4px solid #f39c12;
    font-size: 18px; /* Increased font size */
  }

  /* Responsive Design */
  @media (max-width: 768px) {
    .container {
      padding: 1rem;
    }

    h1 {
      font-size: 2.5rem; /* Adjusted font size for smaller screens */
    }

    h2 {
      font-size: 2rem; /* Adjusted font size for smaller screens */
    }

    h3 {
      font-size: 1.75rem; /* Adjusted font size for smaller screens */
    }
  }
</style>

<div class="container">
  <h1>1. Chapter 1 - An Introduction to the Human Body</h1>

  <ul>
    <li>
      <strong>1.1 Overview of Anatomy and Physiology</strong>
      <p>
        <a href="https://openstax.org/books/anatomy-and-physiology-2e/pages/1-1-overview-of-anatomy-and-physiology" target="_blank" rel="noopener noreferrer">
          Link to Textbook Section
        </a>
      </p>
    </li>

    <li>
      <strong>1.2 Key Themes and Important Ideas</strong>
      <ul>
        <li>
          <strong>1.2.1 Definition and Scope of Anatomy</strong>
          <ul>
            <li>
              <strong>Definition:</strong> Human anatomy is defined as "the scientific study of the body’s structures."
            </li>
            <li>
              <strong>Historical Perspective:</strong>
              <blockquote>
                Human anatomy was first studied by observing the exterior of the body and observing the wounds of soldiers and other injuries. Later, physicians were allowed to dissect bodies of the dead to augment their knowledge.
              </blockquote>
            </li>
            <li>
              <strong>Modern Techniques:</strong> Contemporary anatomy utilizes various imaging techniques to visualize internal structures in living individuals.
            </li>
            <li>
              <strong>Specializations within Anatomy:</strong>
              <ul>
                <li>
                  <strong>Gross Anatomy (Macroscopic Anatomy):</strong> Focuses on the study of larger structures visible without magnification.
                </li>
                <li>
                  <strong>Microscopic Anatomy:</strong> Studies structures visible only with the aid of magnification, including:
                  <ul>
                    <li><strong>Cytology:</strong> The study of individual cells.</li>
                    <li><strong>Histology:</strong> The study of tissues.</li>
                  </ul>
                </li>
              </ul>
            </li>
            <li>
              <strong>Approaches to Anatomical Study:</strong>
              <ul>
                <li>
                  <strong>Regional Anatomy:</strong> Examines the interrelationships of all structures within a specific body region (e.g., abdomen).
                </li>
                <li>
                  <strong>Systemic Anatomy:</strong> Focuses on the structures that comprise a discrete body system (e.g., the muscular system).
                </li>
              </ul>
            </li>
          </ul>
        </li>

        <li>
          <strong>1.2.2 Definition and Scope of Physiology</strong>
          <ul>
            <li>
              <strong>Definition:</strong> Human physiology is "the scientific study of the chemistry and physics of the structures of the body and the ways in which they work together to support the functions of life."
            </li>
            <li>
              <strong>Focus on Homeostasis:</strong>
              <blockquote>
                A central theme in physiology is homeostasis, defined as "the state of steady internal conditions maintained by living things."
              </blockquote>
            </li>
            <li>
              <strong>Methodology:</strong> Physiology involves observation, manipulation, measurement, and carefully designed laboratory experiments to understand the functions of different structures and chemical compounds.
            </li>
            <li>
              <strong>Specializations within Physiology:</strong>
              <blockquote>
                For example, neurophysiology is the study of the brain, spinal cord, and nerves and how these work together to perform functions as complex and diverse as vision, movement, and thinking.
              </blockquote>
            </li>
          </ul>
        </li>

        <li>
          <strong>1.2.3 The Fundamental Relationship Between Anatomy and Physiology</strong>
          <ul>
            <li>
              <strong>Interdependence:</strong> The source strongly emphasizes the inseparable link between structure (anatomy) and function (physiology).
            </li>
            <li>
              <strong>Illustrative Example:</strong>
              <blockquote>
                The text uses the example of the eyelid's structure (thin flap, nerves, and muscles) enabling its function (clearing dust and allowing vision).
              </blockquote>
            </li>
            <li>
              <strong>Importance for Learning:</strong>
              <blockquote>
                Your study of anatomy and physiology will make more sense if you continually relate the form of the structures you are studying to their function.
              </blockquote>
            </li>
            <li>
              <strong>Further Example:</strong>
              <blockquote>
                Imagine trying to appreciate the unique arrangement of the bones of the human hand if you had no conception of the function of the hand.
              </blockquote>
            </li>
          </ul>
        </li>
      </ul>
    </li>
  </ul>

  {#if challenge13}
    <div class="challenge">
      <p><strong>Challenge:</strong> {challenge13.challenge}</p>
      <ul>
        {#each challenge13.options as option, index}
          <li>
            <button on:click={() => alert(isCorrect(challenge13, index) ? 'Correct!' : 'Try again!')}>
              {option}
            </button>
          </li>
        {/each}
      </ul>
      <p><strong>Explanation:</strong> {challenge13.explanation}</p>
    </div>
  {/if}

  {#if challenge15}
    <div class="challenge">
      <p><strong>Challenge:</strong> {challenge15.challenge}</p>
      <ul>
        {#each challenge15.options as option, index}
          <li>
            <button on:click={() => alert(isCorrect(challenge15, index) ? 'Correct!' : 'Try again!')}>
              {option}
            </button>
          </li>
        {/each}
      </ul>
      <p><strong>Explanation:</strong> {challenge15.explanation}</p>
    </div>
  {/if}
</div>




