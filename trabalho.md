# Trabalho

O trabalho pode ser desenvolvido em dupla. Cada trabalho deve ser único e tratar de um problema diferente ou enunciado diferente. Seguem exemplos de possíveis trabalhos, sendo possível que a dupla apresenta uma proposta diferente.

**Apresentação:** 2/12 (terça-feira)

**Prova Final:** 9/12 (terça-feira)

# 1. Sistema de Controle de Estoque (CSV)

Desenvolva um programa em Python para gerenciar o estoque de uma pequena loja. O sistema deve ler e gravar os dados em um arquivo CSV contendo informações sobre os produtos (código, nome, quantidade e preço unitário).
O programa deve permitir, via console:

- Listar todos os produtos em estoque;
- Adicionar um novo produto;
- Atualizar a quantidade ou o preço de um produto existente;
- Remover um produto;
- Calcular e exibir o valor total do estoque.
- O arquivo deve ser atualizado automaticamente a cada operação.

# 2. Analisador de Notas de Alunos (Excel)

Crie um programa em Python que leia um arquivo Excel (.xlsx) contendo as notas de alunos de uma turma (colunas: nome, nota1, nota2, nota3).
O programa deve:

- Calcular a média de cada aluno;
- Exibir os alunos aprovados e reprovados (média >= 6 para aprovação);
- Permitir salvar um novo arquivo Excel com uma coluna adicional chamada “Situação” (Aprovado/Reprovado).
- O usuário deve escolher o nome do arquivo de saída no console.

# 3. Registro de Viagens e Consumo de Combustível (CSV)

Implemente um sistema em Python que leia um arquivo CSV com registros de viagens (data, distância percorrida, combustível consumido).
O programa deve:

- Exibir estatísticas gerais (total de viagens, distância total, consumo médio);
- Permitir o registro de novas viagens via console, salvando-as no arquivo;
- Gerar um relatório em texto (.txt) com o resumo de desempenho do veículo (média km/l, viagem mais longa, etc.).

# 4. Controle de Despesas Pessoais (Excel)

Desenvolva um programa em Python que leia um arquivo Excel (.xlsx) com lançamentos financeiros (colunas: data, categoria, descrição, valor).
O programa deve:

- Somar os gastos por categoria;
- Exibir o total mensal de despesas;
- Permitir inserir novas despesas via console;
- Exportar um novo arquivo Excel com um resumo de gastos por categoria.
  O objetivo é ajudar o usuário a entender para onde vai o seu dinheiro.

# 5. Catálogo de Filmes (CSV)

Crie um programa em Python que gerencie um catálogo de filmes armazenado em um arquivo CSV (colunas: título, ano, gênero, avaliação).
O programa deve permitir:

- Listar todos os filmes;
- Buscar filmes por gênero ou ano;
- Adicionar novos filmes;
- Calcular a média das avaliações;
- Salvar as alterações no mesmo arquivo CSV.

# 6. Biblioteca

Desenvolva um programa em Python, executado no console, que gerencie os registros de uma pequena biblioteca a partir de um arquivo CSV contendo informações dos livros (título, autor, ano, gênero e disponibilidade).
O programa deve:

- Ler o arquivo CSV e carregar os dados em uma estrutura adequada (lista de dicionários, por exemplo);
- Permitir ao usuário, via menu de opções no console:
- Listar todos os livros;
- Buscar livros por autor, título ou gênero;
- Registrar empréstimos e devoluções (alterando o status de disponibilidade);
- Adicionar novos livros e salvar as alterações no arquivo CSV.
- Garantir que todas as atualizações sejam persistidas no arquivo original.