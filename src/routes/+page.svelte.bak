<script>
	import { onMount } from 'svelte';

	let files = [];
	let combinedMarkup = '';
	let errorMessage = '';

	onMount(async () => {
		try {
			 // Dynamically fetch the list of files from the API
			const response = await fetch('/api/list-static-files');
			if (!response.ok) {
				throw new Error(`Failed to fetch file list: ${response.statusText}`);
			}
			files = await response.json();

			 // Debugging: Log the list of files
			console.log('Files:', files);

			// Fetch and combine the content of each file
			const fetchPromises = files.map(async (file) => {
				const res = await fetch(`/${file}`);
				if (!res.ok) {
					throw new Error(`Failed to fetch file: ${file}`);
				}
				const content = await res.text();

				// Debugging: Log the content of each file
				console.log(`Content of ${file}:`, content);

				return `<h2>${file}</h2>\n${content}`;
			});

			const fileContents = await Promise.all(fetchPromises);
			combinedMarkup = fileContents.join('\n');
		} catch (error) {
			errorMessage = error.message;

			// Debugging: Log the error
			console.error('Error:', error);
		}
	});
</script>

<section>
	<h1>Questions</h1>
	{#if errorMessage}
		<p style="color: red;">Error: {errorMessage}</p>
	{:else}
		<div>
			{@html combinedMarkup}
		</div>
	{/if}
</section>
