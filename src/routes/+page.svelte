<script>
    // You can add any necessary JavaScript here if needed
</script>

<main>
    <h1>Welcome to the Page</h1>
    <p>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    </p>
    <div class="content-with-side-notes">
      <div class="excerpt-with-side-note">
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus imperdiet, nulla et dictum interdum, nisi lorem egestas odio, vitae scelerisque enim ligula venenatis dolor. Maecenas nisl est, ultrices nec congue eget, auctor vitae massa. Fusce luctus vestibulum augue ut aliquet. Nunc sagittis dictum nisi, sed ullamcorper ipsum dignissim ac. In at 
          <span class="side-note-anchor">This is where the first side note goes.</span> libero sed nunc venenatis imperdiet sed ornare turpis.
        </p>
        <aside class="side-note right">
          <p>This is the best thing since sliced bread!</p>
        </aside>
      </div>
      <div class="excerpt-with-side-note">
        <p>
          Another excerpt of text that has a <span class="side-note-anchor">second side note here.</span> This is additional content to demonstrate multiple side notes.
        </p>
        <aside class="side-note right">
          <p>This is another amazing side note!</p>
        </aside>
      </div>
      <div class="excerpt-with-side-note">
        <p>
          This is an excerpt with a <span class="side-note-anchor">side note on the left.</span> It demonstrates how side notes can be positioned on either side of the main text.
        </p>
        <aside class="side-note left">
          <p>This is a side note on the left!</p>
        </aside>
      </div>
      <div>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. At commodi, praesentium et ad, exercitationem voluptatum perferendis illo libero a sed quidem ducimus repellendus delectus, enim velit id blanditiis animi incidunt?
        Lorem ipsum dolor sit amet consectetur, adipisicing elit. Optio soluta aliquam architecto aspernatur repudiandae perspiciatis nesciunt iste dolorum facere earum, aperiam ipsa ullam error. Magni expedita laudantium tempore molestias itaque.
      </div>
      <div>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum sed aperiam omnis, reiciendis nam, illum eveniet itaque nisi repellendus fugit, error dolore delectus officia ex soluta maxime placeat eos a.
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Asperiores fugit eveniet facere, cum repellat reprehenderit delectus dolorem accusantium nobis laboriosam optio quis consequuntur harum illum sed consectetur assumenda. Suscipit, harum?
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Sapiente voluptatibus velit, ad, reprehenderit dignissimos optio dicta animi dolores ab dolorem nisi sequi accusamus. Assumenda cum totam corrupti, explicabo quo deleniti.
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Accusamus earum molestiae nisi iste voluptatum? Architecto praesentium, alias repudiandae, ipsum magnam tenetur ullam laudantium aut odio vero ipsa esse, nisi explicabo?
      </div>
    </div>
</main>

<style>
  main {
    max-width: 800px;
    margin: 0 auto;
    padding: 0 1rem;
    position: relative;
    font-size: 1.125rem; /* Increased font size for better readability */
    line-height: 1.6; /* Adjusted line height for improved spacing */
  }

  .content-with-side-notes {
    position: relative;
  }

  .excerpt-with-side-note {
    display: flex;
    align-items: flex-start;
    position: relative;
    margin-bottom: 2rem; /* Add spacing between excerpts */
  }

  .side-note-anchor {
    position: relative;
  }

  .side-note {
    position: absolute;
    top: 0;
    width: 180px; /* Adjust width as needed */
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    padding: 1rem;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    font-size: 1rem; /* Set side note text size to 1rem */
    font-family: Arial, sans-serif; /* Set side note text to use a sans-serif font */
  }

  .side-note.right {
    right: -250px; /* Adjust as needed for spacing */
  }

  .side-note.left {
    left: -250px; /* Adjust as needed for spacing */
  }
</style>