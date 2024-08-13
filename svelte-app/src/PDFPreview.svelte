<script>
    import { onMount } from 'svelte';

    let images = [];
    let selectedTemplate;

    async function generatePDF() {
        const response = await fetch('http://localhost:8000/api/generate-pdf/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ images, template_id: selectedTemplate.id })
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

<button on:click={generatePDF}>Generate PDF</button>