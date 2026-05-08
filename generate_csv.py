"""Gera um CSV de exemplo compativel com o encoder/scaler/kmeans."""
import numpy as np
import pandas as pd

rng = np.random.default_rng(seed=42)

NUMERIC_COLS = [
    'idade', 'numero_de_amigos',
    'basquete', 'futebol_americano', 'futebol', 'softbol', 'voleibol',
    'natacao', 'animacao', 'beisebol', 'tenis', 'esportes',
    'fofo', 'danca', 'banda', 'marcha', 'musica', 'rock',
    'cabelo', 'vestido', 'shopping', 'compras', 'roupas',
    'nossa_marca', 'marca_concorrente', 'bebidas',
]

N = 200

idade = rng.integers(13, 20, size=N)
numero_de_amigos = rng.integers(0, 100, size=N)
keyword_cols = {c: rng.poisson(lam=0.6, size=N) for c in NUMERIC_COLS[2:]}

sexo = rng.choice(['F', 'M', 'NE'], size=N, p=[0.5, 0.45, 0.05])

df = pd.DataFrame({
    'sexo': sexo,
    'idade': idade,
    'numero_de_amigos': numero_de_amigos,
    **keyword_cols,
})

# Reordena: sexo primeiro, depois colunas numericas na ordem esperada
df = df[['sexo'] + NUMERIC_COLS]

out = 'exemplo_interesses.csv'
df.to_csv(out, index=False)
print(f'CSV gerado: {out}  ({len(df)} linhas, {len(df.columns)} colunas)')
print(df.head())
