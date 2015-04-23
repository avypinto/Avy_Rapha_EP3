import matplotlib.pyplot as plt
import numpy as np

N = 7

cal_consumida = (2000, 3500, 3000, 3500, 270, 900,540)

numero_de_barras = np.arange(N)

comprimento = 0.35  # comprimento das barras

fig,ax = plt.subplots()

rects1 = ax.bar(numero_de_barras, cal_consumida,comprimento, color='purple')

cal_necessaria = (Calculo_Necessidade_Cal(fator), Calculo_Necessidade_Cal(fator), Calculo_Necessidade_Cal(fator),Calculo_Necessidade_Cal(fator),Calculo_Necessidade_Cal(fator),Calculo_Necessidade_Cal(fator),Calculo_Necessidade_Cal(fator))

rects2 = ax.bar(numero_de_barras + comprimento,cal_necessaria, comprimento, color='turquoise')


ax.set_xlabel('Dia da semana')
ax.set_ylabel('Quantidade')
ax.set_xticks(numero_de_barras+comprimento)
ax.set_xticklabels( ('domingo','segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado') )

ax.legend( (rects1[0], rects2[0]), ('Calorias Consumidas', 'Calorias Necessarias') )

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')
autolabel(rects1)
autolabel(rects2)
plt.show()




N = 7
proteina_consumida=(180,150,2060,903,90,87,105)
gordura_consumida=(70,30,40,45,54,19,29)
carboidrato_consumido=(130,300,209,340,189,320,2000)

numero_de_barras = np.arange(N)
comprimento = 0.35  # comprimento das barras

fig,ax = plt.subplots()

rects3=ax.bar(numero_de_barras,proteina_consumida, comprimento, color='orange')
rects4=ax.bar(numero_de_barras + comprimento, gordura_consumida,comprimento, color='blue')
rects5=ax.bar(numero_de_barras +comprimento*2, carboidrato_consumido,comprimento/2, color='navy')

ax.set_xlabel('Dia da semana')
ax.set_ylabel('Quantidade')
ax.set_xticks(numero_de_barras+comprimento)
ax.set_xticklabels( ('domingo','segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado') )

ax.legend( (rects3[0], rects4[0], rects5[0]), ('Proteinas Consumidas(g)', 'Carboidratos Consumidos(g)', 'Gorduras Consumida(g)'))


autolabel(rects3)
autolabel(rects4)
autolabel(rects5)
plt.show()

