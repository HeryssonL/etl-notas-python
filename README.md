# Projeto ETL com Python

Projeto desenvolvido para praticar o processo ETL (Extração, Transformação e Carregamento) utilizando Python e Pandas.

## Objetivo

Ler um arquivo CSV com notas de alunos, analisar os dados e gerar um novo arquivo com a situação de cada aluno.

---

# Fluxo ETL

## Extração
Leitura do arquivo `alunos.csv`.

## Transformação
Classificação dos alunos de acordo com:
- Aprovado
- Recuperação
- Reprovado
- Reprovado por falta

## Carregamento
Geração do arquivo `resultado.csv` com os dados transformados.

---

# Tecnologias utilizadas

- Python
- Pandas
- CSV

---

# Estrutura do projeto

```bash
etl-notas-python/
│
├── alunos.csv
├── resultado.csv
├── main.py
└── README.md
```

---

# Como executar o projeto

## Instalar dependências

```bash
pip install pandas
```

## Executar o projeto

```bash
python main.py
```

---

# Exemplo de saída

| nome | nota | faltas | situacao |
|---|---|---|---|
| Ana | 8 | 2 | Aprovado |
| Carlos | 5 | 8 | Recuperação |
