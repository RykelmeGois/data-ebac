import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')

plt.figure(figsize=(10, 6))
plt.plot(df['dia'], df['venda'], marker='o', linestyle='-', color='b')


plt.xlabel('Dia')
plt.ylabel('Preço de Venda (R$)')
plt.title('Preço Médio de Venda da Gasolina em São Paulo - Julho 2021')

plt.savefig('gasolina.png')

plt.show()