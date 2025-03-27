<main>
  <slot />
  <footer>
    <p>Content curated by Scott A. Green. &copy; {new Date().getFullYear()}</p>
    <p>
      <a href="https://openstax.org" target="_blank" rel="noopener noreferrer">
        Visit OpenStax for more resources
      </a>
    </p>
  </footer>
</main>

<style>
  main {
    font-family: Arial, sans-serif;
    margin: 0 auto;
    max-width: 800px;
    padding: 1rem;
    line-height: 1.6;
    color: #444;
  }

  header {
    text-align: center;
    margin-bottom: 2rem;
    border-bottom: 2px solid #ddd;
    padding-bottom: 1rem;
  }

  h1 {
    font-size: 2.5rem;
    color: #222;
  }

  footer {
    text-align: center;
    margin-top: 2rem;
    padding-top: 1rem;
    border-top: 2px solid #ddd;
    font-size: 0.9rem;
    color: #666;
  }

  footer a {
    color: #007acc;
    text-decoration: none;
  }

  footer a:hover {
    text-decoration: underline;
  }

  p {
    margin: 0.5rem 0;
  }
</style>
