document.addEventListener('DOMContentLoaded', function() {
    // Seleciona o elemento da imagem e o input de arquivo
    const imageSelector = document.getElementById('imageSelector');
    const fileInput = document.getElementById('fileInput');
    const barcode = document.getElementById('barcode');
    const codigoInput = document.querySelector('input[name="codigo"]');

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

    // Evento para gerar o código de barras quando o código do produto for inserido
    codigoInput.addEventListener('input', function() {
        const codigo = codigoInput.value; // Obtém o valor do campo "Código"
        if (codigo) {
            JsBarcode(barcode, codigo, {
                format: "CODE128", // Formato de código de barras
                displayValue: true, // Exibir o valor abaixo do código de barras
                lineColor: "#000", // Cor do código de barras
                width: 2, // Largura das linhas
                height: 100, // Altura do código de barras
            });
        } else {
            barcode.innerHTML = ''; // Limpa o código de barras se o campo estiver vazio
        }

    });
});
