<script>
	export let name;

	async function uploadImage(file) {
		const formData = new FormData();
		formData.append('image', file);

		const response = await fetch('http://localhost:8000/api/images/', {
			method: 'POST',
			body: formData
		});

		return await response.json();
	}

	async function generatePDF(images, templateId) {
		const response = await fetch('http://localhost:8000/api/generate-pdf/', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ images, template_id: templateId })
		});

		const blob = await response.blob();
		const url = window.URL.createObjectURL(blob);
		const a = document.createElement('a');
		a.href = url;
		a.download = 'output.pdf';
		document.body.appendChild(a);
		a.click();
		a.remove();
	}
</script>

<main>
	<h1>Hello {name}!</h1>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>