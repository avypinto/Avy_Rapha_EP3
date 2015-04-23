

def Calculo_TMB(peso,altura,idade):                         
     
    if sexo == "M": 
        TMB= 88.36+(13.4*peso)+(4.8*altura*100)-(5.7*idade)
    elif sexo == "F":
        TMB= 447.6+(9.2*peso)+(3.1*altura)-(4.3*idade) 
    return TMB
print("A sua Taxa Metabolica Basal e:", Calculo_TMB(peso,altura,idade))
 
    
def Calculo_Necessidade_Cal(fator):  
    
    if fator == "MÍNIMO":
        Calculo_Necessidade_Cal = Calculo_TMB(peso,altura,idade)*1.2
    elif fator == "BAIXO":
       Calculo_Necessidade_Cal  = Calculo_TMB(peso,altura,idade)*1.375
    elif fator == "MÉDIO":    
        Calculo_Necessidade_Cal  = Calculo_TMB(peso,altura,idade)*1.55
    elif fator == "ALTO":    
        Calculo_Necessidade_Cal  = Calculo_TMB(peso,altura,idade)*1.725
    elif fator == "MUITO ALTO":    
        Calculo_Necessidade_Cal  = Calculo_TMB(peso,altura,idade)*1.9        
    return Calculo_Necessidade_Cal 
print("A sua necessidade calorica diaria e:", Calculo_Necessidade_Cal(fator))


def Calculo_Imc(peso,altura):
    Imc=(1.3*peso) /altura**2.5
    return Imc
print("O seu Indice de Massa Corporal e:", Calculo_Imc(peso,altura))

def Tipagem_Imc(peso,altura):
    if Calculo_Imc(peso,altura)<16:
        print("A partir do Imc, o seu nivel e: Magreza Grave")
    elif 16<= Calculo_Imc(peso,altura)<17:
        print("A partir do Imc, o seu nivel e: Magreza Moderada")
    elif 17<=Calculo_Imc(peso,altura)<18.5:
        print("A partir do Imc, o seu nivel e: Magreza Leve ")
    elif 18.5<=Calculo_Imc(peso,altura)<25:
        print("A partir do Imc, o seu nivel e: Saudavel")
    elif 25<=Calculo_Imc(peso,altura)<30:
        print("A partir do Imc, o seu nivel e: Sobrepeso")
    elif 30<=Calculo_Imc(peso,altura)<35:
        print("A partir do Imc, o seu nivel e: Obesidade grau 1")
    elif 35<=Calculo_Imc(peso,altura)<40:
        print("A partir do Imc, o seu nivel e: Obesidade Grau 2")
    else:
        print("A partir do Imc, o seu nivel e: Obesidade Grau 3")
print(Tipagem_Imc(peso,altura))
        
        


            








