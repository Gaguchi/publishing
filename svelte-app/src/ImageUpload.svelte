<script>
    let selectedFile;

    async function uploadImage() {
        const formData = new FormData();
        formData.append('image', selectedFile);

        const response = await fetch('http://localhost:8000/api/images/', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();
        console.log(result);
    }
</script>

<input type="file" bind:this={selectedFile} />
<button on:click={uploadImage}>Upload Image</button>