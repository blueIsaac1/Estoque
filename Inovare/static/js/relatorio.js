salvarDadosBtn.addEventListener('click', function () {
    // Coletar dados do formulário
    const codigo = document.getElementById('codigo').value.trim();
    const codigoBarra = document.getElementById('codigoBarra').value.trim();
    const descricao = document.getElementById('descricao').value.trim();
    const custoUnidade = parseFloat(document.getElementById('custoUnidade').value);
    const estoque = parseInt(document.getElementById('estoque').value);
    const quantidade = parseInt(document.getElementById('quantidade').value);
    const preco = parseFloat(document.getElementById('preco').value);

    // Validar campos
    if (!codigo || !codigoBarra || !descricao || isNaN(custoUnidade) || isNaN(estoque) || isNaN(quantidade) || isNaN(preco)) {
        alert('Por favor, preencha todos os campos corretamente.');
        return;
    }

    const total = custoUnidade * quantidade;

    // Criar objeto de dados para enviar via Ajax
    const data = {
        codigo: codigo,
        codigoBarra: codigoBarra,
        descricao: descricao,
        custoUnidade: custoUnidade,
        estoque: estoque,
        quantidade: quantidade,
        preco: preco,
        total: total
    };

    // Enviar dados para o Django via Ajax
    fetch('/salvar-relatorio/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Dados salvos com sucesso!');
            // Atualizar a tabela e o gráfico
            atualizarGrafico();
        } else {
            alert('Erro ao salvar dados.');
        }
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Ocorreu um erro ao salvar os dados.');
    });
});

