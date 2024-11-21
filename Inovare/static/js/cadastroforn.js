// Gera o código de barras com base em um valor fixo
function gerarCodigoBarras() {
    JsBarcode("#barcode", "123456789012", {
        format: "CODE128",    // Define o formato do código de barras
        width: 3,             // Largura de cada barra
        height: 50,           // Altura do código de barras
        displayValue: true    // Exibe o valor numérico abaixo do código de barras
    });
}

// Adiciona eventos para manipulação da imagem
function configurarManipulacaoImagem() {
    const imageSelector = document.getElementById('imageSelector');
    const fileInput = document.getElementById('fileInput');

    // Simula o clique no input file invisível quando a imagem é clicada
    imageSelector.addEventListener('click', () => {
        fileInput.click();
    });

    // Atualiza a imagem quando um novo arquivo é selecionado
    fileInput.addEventListener('change', (event) => {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                imageSelector.src = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    });
}

// Inicializa as funções quando o documento estiver completamente carregado
document.addEventListener('DOMContentLoaded', () => {
    gerarCodigoBarras();
    configurarManipulacaoImagem();
});
