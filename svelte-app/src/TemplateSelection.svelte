<script>
    import { onMount } from 'svelte';

    let templates = [];
    let selectedTemplate;

    onMount(async () => {
        const response = await fetch('http://localhost:8000/api/templates/');
        templates = await response.json();
    });

    function selectTemplate(template) {
        selectedTemplate = template;
    }
</script>

<ul>
    {#each templates as template}
        <li on:click={() => selectTemplate(template)}>{template.name}</li>
    {/each}
</ul>