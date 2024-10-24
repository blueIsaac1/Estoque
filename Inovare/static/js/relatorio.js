document.addEventListener('DOMContentLoaded', function () {
    const salvarDadosBtn = document.getElementById('salvar-dados');
    const detalhesEstoque = document.getElementById('detalhes-estoque');
    let grafico = null;

    salvarDadosBtn.addEventListener('click', function () {
        // Coletar dados do formulário
        const codigo = document.getElementById('codigo').value.trim();
        const codigoBarra = document.getElementById('codigo_barra').value.trim();
        const descricao = document.getElementById('descricao').value.trim();
        const custoUnidade = parseFloat(document.getElementById('custo_unidade').value);
        const estoque = parseInt(document.getElementById('estoque').value);
        const quantidade = parseInt(document.getElementById('quantidade').value);
        const preco = parseFloat(document.getElementById('preco').value);

        // Validar campos
        if (!codigo || !codigoBarra || !descricao || isNaN(custoUnidade) || isNaN(estoque) || isNaN(quantidade) || isNaN(preco)) {
            alert('Por favor, preencha todos os campos corretamente.');
            return;
        }

        const total = custoUnidade * quantidade;

        // Adicionar dados à tabela
        const newRow = detalhesEstoque.insertRow();
        newRow.innerHTML = `
            <td>${codigo}</td>
            <td>${codigoBarra}</td>
            <td>${descricao}</td>
            <td>${custoUnidade.toFixed(2)}</td>
            <td>${estoque}</td>
            <td>${quantidade}</td>
            <td>${preco.toFixed(2)}</td>
            <td>${total.toFixed(2)}</td>
        `;

        // Limpar os campos de entrada
        document.getElementById('codigo').value = '';
        document.getElementById('codigo_barra').value = '';
        document.getElementById('descricao').value = '';
        document.getElementById('custo_unidade').value = '';
        document.getElementById('estoque').value = '';
        document.getElementById('quantidade').value = '';
        document.getElementById('preco').value = '';

        // Atualizar o gráfico
        atualizarGrafico();
    });

    function atualizarGrafico() {
        const labels = [];
        const dataValues = [];
        const rows = detalhesEstoque.getElementsByTagName('tr');

        for (let row of rows) {
            const cells = row.getElementsByTagName('td');
            const descricaoItem = cells[2].innerText; // Descrição do Item
            const totalItem = parseFloat(cells[7].innerText); // Total

            labels.push(descricaoItem);
            dataValues.push(totalItem);
        }

        // Verificar se há dados para o gráfico
        if (labels.length === 0 || dataValues.length === 0) {
            alert('Nenhum dado disponível para gerar o gráfico.');
            return;
        }

        // Verificar se já existe um gráfico e destruí-lo antes de criar um novo
        if (grafico) {
            grafico.destroy();
        }

        // Criar ou atualizar o gráfico
        const ctx = document.getElementById('grafico').getContext('2d');
        grafico = new Chart(ctx, {
            type: 'pie',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Total de Itens',
                    data: dataValues,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)',
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)',
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'Distribuição de Itens no Estoque'
                    }
                }
            }
        });
    }
});