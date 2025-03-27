<script>
  export let type = 'info'; // Types: info, warning, error, success
  export let title = '';
</script>

<div class={`admonishment admonishment-${type}`}>
  {#if title}
    <strong>{title}</strong>
  {/if}
  <slot />
</div>

<style>
  .admonishment {
    padding: 1rem;
    border-radius: 5px;
    margin: 1rem 0;
  }
  .admonishment-info {
    background-color: #e7f3fe;
    border: 1px solid #b3d8fd;
    color: #3178c6;
  }
  .admonishment-warning {
    background-color: #fff4e5;
    border: 1px solid #ffd59e;
    color: #b46900;
  }
  .admonishment-error {
    background-color: #fdecea;
    border: 1px solid #f5c6cb;
    color: #a71d2a;
  }
  .admonishment-success {
    background-color: #e6f4ea;
    border: 1px solid #c3e6cb;
    color: #155724;
  }
</style>
