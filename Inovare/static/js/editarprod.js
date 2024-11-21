document.addEventListener('DOMContentLoaded', function() {
    // Seleciona os elementos da imagem, do seletor de arquivo e do código de barras
    const imageSelector = document.getElementById('imageSelector');
    const fileInput = document.getElementById('fileInput');
    const barcodeElement = document.getElementById('barcode');
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

    // Evento para gerar o código de barras ao digitar no campo "Código"
    codigoInput.addEventListener('input', function() {
        const codigo = codigoInput.value; // Obtém o valor digitado
        if (codigo) {
            JsBarcode(barcodeElement, codigo, { format: "CODE128" }); // Gera o código de barras
        } else {
            barcodeElement.innerHTML = ''; // Limpa o código de barras se o campo estiver vazio
        }
    });

    // Evento para resetar o formulário ao clicar no botão "Limpar"
    document.querySelector('input[type="reset"]').addEventListener('click', function() {
        // Após limpar o formulário, restaura a imagem e o código de barras padrão
        imageSelector.src = 'editarFunc.png'; // Define a imagem de volta para o estado original
        barcodeElement.innerHTML = ''; // Limpa o código de barras
    });
});