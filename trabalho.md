# Trabalho

O trabalho pode ser desenvolvido em dupla. Cada trabalho deve ser único e tratar de um problema diferente ou enunciado diferente. Seguem exemplos de possíveis trabalhos, sendo possível que a dupla apresenta uma proposta diferente.

**Apresentação:** 2/12 (terça-feira)

**Prova Final:** 9/12 (terça-feira)

# 1. Sistema de Controle de Estoque (CSV)
**Projeto: https://github.com/pedroacdp10-ai/Trabalho-de-Sistemas-de-controle-de-estoque**

Integrantes: Pedro Arthur e Gabriel Saragioto
Desenvolva um programa em Python para gerenciar o estoque de uma pequena loja. O sistema deve ler e gravar os dados em um arquivo CSV contendo informações sobre os produtos (código, nome, quantidade e preço unitário).
O programa deve permitir, via console:

- Listar todos os produtos em estoque;
- Adicionar um novo produto;
- Atualizar a quantidade ou o preço de um produto existente;
- Remover um produto;
- Calcular e exibir o valor total do estoque.
- O arquivo deve ser atualizado automaticamente a cada operação.

# 2. Analisador de Notas de Alunos (Excel)
**Projeto: https://github.com/oliver1406/lp20252**

Integrantes: Yan e Gabriel
Crie um programa em Python que leia um arquivo Excel (.xlsx) contendo as notas de alunos de uma turma (colunas: nome, nota1, nota2, nota3).
O programa deve:

- Calcular a média de cada aluno;
- Exibir os alunos aprovados e reprovados (média >= 6 para aprovação);
- Permitir salvar um novo arquivo Excel com uma coluna adicional chamada “Situação” (Aprovado/Reprovado).
- O usuário deve escolher o nome do arquivo de saída no console.

# 3. Registro de Viagens e Consumo de Combustível (CSV)
**Projeto: https://github.com/clay132/lp20252**

Clay e Gabriel Almeida (Everton desistiu)
Implemente um sistema em Python que leia um arquivo CSV com registros de viagens (data, distância percorrida, combustível consumido).
O programa deve:

- Exibir estatísticas gerais (total de viagens, distância total, consumo médio);
- Permitir o registro de novas viagens via console, salvando-as no arquivo;
- Gerar um relatório em texto (.txt) com o resumo de desempenho do veículo (média km/l, viagem mais longa, etc.).

# 4. Controle de Despesas Pessoais (Excel)
**Projeto: https://github.com/greici000/controle-de-despesas-pessoais**

Integrantes: Kleber e Greiciele
Desenvolva um programa em Python que leia um arquivo Excel (.xlsx) com lançamentos financeiros (colunas: data, categoria, descrição, valor).
O programa deve:

- Somar os gastos por categoria; NOT OK
- Exibir o total mensal de despesas; OK
- Permitir inserir novas despesas via console; OK
- Exportar um novo arquivo Excel com um resumo de gastos por categoria. NOT OK
  O objetivo é ajudar o usuário a entender para onde vai o seu dinheiro.

# 5. Catálogo de Filmes (CSV)
**Projeto: https://github.com/joaogato1048-creator/webzorde**

Integrantes: João Vitor e Murilo
NAO SOUBE RESPONDER O QUE ERA O UTF-8

Crie um programa em Python que gerencie um catálogo de filmes armazenado em um arquivo CSV (colunas: título, ano, gênero, avaliação).
O programa deve permitir:

- Listar todos os filmes; OK
- Buscar filmes por gênero ou ano; NAO OK
- Adicionar novos filmes; OK
- Calcular a média das avaliações; OK
- Salvar as alterações no mesmo arquivo CSV. OK

# 6. Biblioteca
**Projeto: https://github.com/Matheus1f65/Biblioteca**

Integrantes: Luzineia e Mateus

Desenvolva um programa em Python, executado no console, que gerencie os registros de uma pequena biblioteca a partir de um arquivo CSV contendo informações dos livros (título, autor, ano, gênero e disponibilidade).
O programa deve:

- Ler o arquivo CSV e carregar os dados em uma estrutura adequada (lista de dicionários, por exemplo); OK
- Permitir ao usuário, via menu de opções no console:
- Listar todos os livros; OK
- Buscar livros por autor, título ou gênero; OK
- Registrar empréstimos e devoluções (alterando o status de disponibilidade); OK
- Adicionar novos livros e salvar as alterações no arquivo CSV.OK
- Garantir que todas as atualizações sejam persistidas no arquivo original. OK

# 7. Controle de Chamados de Manutenção/Suporte
**Projeto: https://github.com/Gabriel7074/Trabalho**

Integrante: Gabriel Almeida
Desenvolva em Python, um sistema simples de gerenciamento de chamados de manutenção de equipamentos, fazendo uso de coleções e de operações com arquivos para armazenamento e recuperação dos dados.

O cenário considerado é o de um setor de manutenção que recebe chamados para consertar ou inspecionar diversos equipamentos (computadores, impressoras, etc.). Cada chamado deve conter, no mínimo, um identificador único, o nome do equipamento, uma descrição do problema, a data de abertura, o status (aberto, em andamento, concluído) e, opcionalmente, o técnico responsável e a data de fechamento. Esses dados deverão ser mantidos em memória através de coleções apropriadas (por exemplo, uma lista de dicionários, onde cada dicionário representa um chamado), permitindo consultas e atualizações de forma organizada.

O programa deverá oferecer um menu interativo no terminal, possibilitando ao usuário realizar operações como:
- Cadastrar novo chamado de manutenção; OK
- Listar todos os chamados, com opção de filtrar por status ou por equipamento; Nao tem filtro
- Buscar um chamado específico a partir do seu identificador; OK
- Alterar dados de um chamado, como status, técnico responsável ou descrição do problema; OK
- Encerrar um chamado, registrando a data de fechamento; OK (faltou data de fechamento)
- Excluir chamados (por exemplo, cancelados ou cadastrados por engano). OK

Nao faz persistência dos dados em arquivo.


