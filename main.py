import pandas as pd
import datetime
import yfinance as yf
from matplotlib import pyplot as plt
import mplcyberpunk
import win32com.client as win32

codigos_de_negociacao = ["MXRF11.SA", "XFIX11.SA"]  

hoje = datetime.datetime.now()
um_ano_atras = hoje - datetime.timedelta(days = 365)

dados_mercado = yf.download(codigos_de_negociacao, um_ano_atras, hoje)

dados_fechamento = dados_mercado['Adj Close']

dados_fechamento.columns = ['MXRF11', 'XFIX11']

dados_fechamento = dados_fechamento.dropna()

dados_anuais = dados_fechamento.resample("Y").last()

dados_mensais = dados_fechamento.resample("M").last()

retorno_anual = dados_anuais.pct_change().dropna()
retorno_mensal = dados_mensais.pct_change().dropna()
retorno_diario = dados_fechamento.pct_change().dropna()

retorno_diario_mxrf = retorno_diario.iloc[-1, 0]
retorno_diario_xfix = retorno_diario.iloc[-1, 1]

retorno_mensal_mxrf = retorno_mensal.iloc[-1, 0]
retorno_mensal_xfix = retorno_mensal.iloc[-1, 1]

retorno_anual_mxrf = retorno_anual.iloc[-1, 0]
retorno_anual_xfix = retorno_anual.iloc[-1, 1]

retorno_diario_mxrf = round((retorno_diario_mxrf * 100), 2)
retorno_diario_xfix = round((retorno_diario_xfix * 100), 2)

retorno_mensal_mxrf = round((retorno_mensal_mxrf * 100), 2)
retorno_mensal_xfix = round((retorno_mensal_xfix * 100), 2) 

retorno_anual_mxrf = round((retorno_anual_mxrf * 100), 2)
retorno_anual_xfix = round((retorno_anual_xfix * 100), 2)

plt.style.use("cyberpunk")

dados_fechamento.plot(y = "XFIX11", use_index = True, legend = False)

plt.title("XFIX11")

#plt.savefig('xfix.png', dpi = 300)

plt.show()

plt.style.use("cyberpunk")

dados_fechamento.plot(y = "MXRF11", use_index = True, legend = False)

plt.title("MXRF11")

#plt.savefig('mxrf.png', dpi = 300)

plt.show()

dados_fechamento['data'] = dados_fechamento.index

plt.style.use("cyberpunk")
x = dados_fechamento["data"]
y1 = dados_fechamento["MXRF11"]
y2 = dados_fechamento["XFIX11"]
#dados_fechamento.plot(x = "data", y = "MXRF11", use_index = True, legend = True)
#dados_fechamento.plot(y = "XFIX11", use_index = True, legend = True)
plt.plot(x, y1, label ='MXRF11')
plt.plot(x, y2, label ='XFIX11')
plt.legend(loc='upper right')

plt.title("MXRF11 VS. IFIX")

#plt.savefig('versus.png', dpi = 300)

plt.show()

outlook = win32.Dispatch("outlook.application")

email = outlook.CreateItem(0)

email.To = 'jaspioncr@gmail.com'
email.Subject = "MXRF11 - RELATÓRIO DIÁRIO"
email.Body = f'''Prezados, segue o relatório diário:

IFIX:

No ano o IFIX está tendo uma rentabilidade de {retorno_anual_xfix}%, 
enquanto no mês a rentabilidade é de {retorno_mensal_xfix}%.

No último dia útil, o fechamento do IFIX foi de {retorno_diario_xfix}%.

Sobre o ETF XFIX11:
O Trend IFIX é o primeiro ETF imobiliário do Brasil, que replica o IFIX, Índices de Fundos de Investimentos Imobiliários, disponível na B3. 
Criado em 2020, o XFIX11 é gerido pela XP Vista Asset Management.
O IFIX é o resultado de uma carteira teórica composta pelas cotas de fundos imobiliários listados no mercado de bolsa e balcão elaborada de acordo com os critérios estabelecidos pela B3.



MXRF11:

No ano o Dólar está tendo uma rentabilidade de {retorno_anual_mxrf}%, 
enquanto no mês a rentabilidade é de {retorno_mensal_mxrf}%.

No último dia útil, o fechamento do Dólar foi de {retorno_diario_mxrf}%.

Sobre o fundo imobiliário MXRF11:
O Maxi Renda Fundo de Investimento Imobiliário investe em ativos financeiros com lastro imobiliário como Certificados de Recebíveis Mobiliários (CRI), 
debêntures, Letras de Crédito Imobiliário (LCI), Letras Hipotecárias (LH) e cotas de fundos de investimento imobiliário.


Atenciosamente,

Caju!

'''

anexo_xfix = r'C:\Users\admin\Desktop\SOFTWARE\MXRF\MXRF\xfix.png'
anexo_mxrf = r'C:\Users\admin\Desktop\SOFTWARE\MXRF\MXRF\mxrf.png'
anexo_versus = r'C:\Users\admin\Desktop\SOFTWARE\MXRF\MXRF\versus.png'

email.Attachments.Add(anexo_xfix)
email.Attachments.Add(anexo_mxrf)
email.Attachments.Add(anexo_versus)

email.Send()