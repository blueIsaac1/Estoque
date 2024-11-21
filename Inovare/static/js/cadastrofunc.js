document.addEventListener('DOMContentLoaded', function() {
    // Seleciona o elemento da imagem e o input de arquivo
    const imageSelector = document.getElementById('imageSelector');
    const fileInput = document.getElementById('fileInput');

    // Evento de clique na imagem para abrir o seletor de arquivos
    imageSelector.addEventListener('click', function() {
        fileInput.click(); // Simula o clique no input invisível
    });

    // Evento que é disparado quando o usuário seleciona ou captura uma nova imagem
    fileInput.addEventListener('change', function(event) {
        const file = event.target.files[0]; // Obtém o arquivo selecionado
        if (file) {
            const reader = new FileReader(); // Cria um leitor de arquivos
            reader.onload = function(e) {
                imageSelector.src = e.target.result; // Atualiza a imagem na página
            };
            reader.readAsDataURL(file); // Converte o arquivo em uma URL de dados para exibição
        }
    });
});
