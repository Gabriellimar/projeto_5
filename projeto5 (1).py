# -*- coding: utf-8 -*-
"""projeto5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wiLz8kFUnNu1txrv1mAuFzgdO_1Cb-zW
"""

import pandas as pd
import numpy as np

df19 = pd.read_csv('/content/Ano2019.csv', delimiter=';')
df19.head()

"""Obter os tipos de despesas realizadas."""

tipo_despesa = (df19["txtDescricao"])
print(tipo_despesa)

"""A soma dos gastos relacionados a legislatura"""

print(df19.groupby(by=['nuLegislatura','vlrLiquido']).sum())

"""A média dos valores gastos em cada despesa"""

print(df19.groupby(by=['vlrLiquido','txtDescricao']).mean())

"""O valor mínimo gasto"""

print(df19.groupby(by=['nuLegislatura','vlrLiquido']).min())

"""# Nova seção"""

df20 = pd.read_csv('/content/Ano2020.csv', delimiter=';')
df20.head()

pd.options.display.float_format = '{:,.2f}'.format



df21 = pd.read_csv('/content/Ano2021.csv', delimiter=';')
df21.head()