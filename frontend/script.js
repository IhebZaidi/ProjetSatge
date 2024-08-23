document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const fileInput = document.getElementById('fileInput');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    fetch('/upload_csv/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        alert('Fichier CSV téléchargé avec succès!');
    })
    .catch(error => {
        console.error('Erreur:', error);
        alert('Erreur lors de l\'upload du fichier CSV.');
    });
});

document.getElementById('trainForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const modelSelect = document.getElementById('modelSelect');
    const modelName = modelSelect.value;

    fetch(`/train_model/?model_name=${modelName}`, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        alert('Entraînement terminé avec succès!');
        document.getElementById('plot').src = data.plot_url;

        // Afficher les métriques
        const metrics = data.metrics;
        document.getElementById('metrics').innerHTML = `
            <p><strong>MSE:</strong> ${metrics.MSE.toFixed(2)}</p>
            <p><strong>RMSE:</strong> ${metrics.RMSE.toFixed(2)}</p>
            <p><strong>R²:</strong> ${metrics.R2.toFixed(2)}</p>
            <p><strong>MAE:</strong> ${metrics.MAE.toFixed(2)}</p>
            <p><strong>MAPE:</strong> ${metrics.MAPE.toFixed(2)}</p>
            <p><strong>EVS:</strong> ${metrics.EVS.toFixed(2)}</p>
        `;
    })
    .catch(error => {
        console.error('Erreur:', error);
        alert('Erreur lors de l\'entraînement du modèle.');
    });
});
