<script>
  export let title = '';
  export let open = false;

  function toggle() {
    open = !open;
  }
</script>

<div class="accordion">
  <div class="accordion-header" on:click={toggle}>
    <strong>{title}</strong>
    <span>{open ? '▼' : '▶'}</span>
  </div>
  {#if open}
    <div class="accordion-content">
      <slot />
    </div>
  {/if}
</div>

<style>
  .accordion {
    border: 1px solid #ccc;
    border-radius: 5px;
    margin: 1rem 0;
  }
  .accordion-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.5rem 1rem;
    background-color: #f9f9f9;
    cursor: pointer;
  }
  .accordion-header:hover {
    background-color: #f1f1f1;
  }
  .accordion-content {
    padding: 1rem;
    border-top: 1px solid #ccc;
  }
</style>
