le_arquivo=open("usuario.csv","r", encoding="utf-8").readlines()
usuario= le_arquivo[1].split(",")
nome = usuario[0] 
idade = int(usuario[1])
peso = float(usuario[2])
sexo = usuario[3].upper().strip()
altura = float(usuario[4])
fator = usuario[5].upper().strip() 
print(nome,",",idade,"anos",",", peso,"kg", "," "sexo", sexo,",", "altura", altura,",", "fator:", fator)

            








