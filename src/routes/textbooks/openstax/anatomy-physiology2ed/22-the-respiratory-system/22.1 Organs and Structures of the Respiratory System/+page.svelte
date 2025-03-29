<script>
    export let className = "textbook"; // Set the default class for this page
</script>

<main>

</main>

<style>
    main {
        max-width: 800px;
        margin: 0 auto;
        padding: 0 1rem;
        position: relative;
        font-size: 1.5rem; /* Increased font size for better readability */
        line-height: 1.8; /* Adjusted line height for improved spacing */
    }

    figure img {
        max-width: 100%; /* Ensure the image fits within the page width */
        height: auto; /* Maintain aspect ratio */
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: Arial, sans-serif; /* Set headings to use a sans-serif font */
    }

    ul {
        margin-bottom: 1.5rem; /* Add spacing below the list */
    }

    p {
        margin-bottom: 1.5rem; /* Add spacing below paragraphs */
    }

    .side-note-container {
        position: relative; /* Ensure side notes are positioned relative to the container */
        margin-bottom: 2rem; /* Add spacing between containers */
    }

    .side-note {
        position: absolute; /* Use absolute positioning for side notes */
        top: 0;
        width: 360px; /* Adjusted width to make side notes twice as wide */
        background-color: transparent; /* Match the main page background */
        border: none; /* Remove the border */
        padding: 1rem;
        box-shadow: none; /* Remove the shadow */
        font-size: 0.9rem; /* Set side note text size */
        font-family: Arial, sans-serif; /* Set side note text to use a sans-serif font */
    }

    .side-note.right {
        right: -430px; /* Adjusted for new width */
    }

    .side-note.left {
        left: -430px; /* Adjusted for new width */
    }
</style>