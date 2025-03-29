<script>
  export let className = ""; // Allow dynamic class names for the layout
</script>

<main class={className}>
  <slot /> <!-- Render the child content -->
</main>

<style>
  main.textbook {
    max-width: 1000px; /* Wider layout for textbook pages */
    padding: 2rem; /* Additional padding for textbook layout */
    background-color: #f9f9f9; /* Light background for textbook pages */
    border: 1px solid #ddd; /* Subtle border for textbook layout */
  }

  main.textbook .content-with-side-notes {
    margin-top: 2rem; /* Adjust spacing for textbook layout */
  }

  main.textbook .side-note {
    font-size: 0.85rem; /* Slightly smaller font for textbook side notes */
    background-color: #fff; /* White background for side notes */
    border: 1px solid #ccc; /* Add border to side notes */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Add subtle shadow */
  }

  main.textbook .side-note.right {
    right: -300px; /* Adjust spacing for textbook layout */
  }

  main.textbook .side-note.left {
    left: -300px; /* Adjust spacing for textbook layout */
  }
</style>
