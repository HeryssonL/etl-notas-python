import pandas as pd

# EXTRAÇÃO
df = pd.read_csv("alunos.csv")

# TRANSFORMAÇÃO
def verificar_situacao(nota):
    if nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

df["situacao"] = df["nota"].apply(verificar_situacao)

print(df)

# CARREGAMENTO
df.to_csv("resultado.csv", index=False)

print("ETL finalizado com sucesso!")