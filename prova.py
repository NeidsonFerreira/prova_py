questao1 = {
    "valor_questao":10,
    "gabarito":"a",
    "enunciado":"Qual é o resultado da soma 10+20?",
    "opcao1":"30",
    "opcao2":"40",
    "opcao3":"50",
    "opcao4":"60"
}
questao2 = {
    "valor_questao":25,
    "gabarito":"d",
    "enunciado":"toda potência de expoente zero e igual a ...",
    "opcao1":"0",
    "opcao2":"2",
    "opcao3":"4",
    "opcao4":"1"
}
questao3 = {
    "valor_questao":15,
    "gabarito":"c",
    "enunciado":"Qual é a capital do Brasil ?",
    "opcao1":"São Paulo",
    "opcao2":"Rio de Janeiro",
    "opcao3":"Brasília",
    "opcao4":"Minas Gerais"
}
questao4 = {
    "valor_questao":25,
    "gabarito":"b",
    "enunciado":"Qual é o mairo palneta do sistema solar?",
    "opcao1":"Terra",
    "opcao2":"Júpiter",
    "opcao3":"Marte",
    "opcao4":"Plutão"
}
questao5 = {
    "valor_questao":25,
    "gabarito":"a",
    "enunciado":"Qual é a formula química da água ?",
    "opcao1":"H2O",
    "opcao2":"CO2",
    "opcao3":"NaCl",
    "opcao4":"CHO2"
}

prova = []
gabarito = ['a','d','c','a','a']
marcacoes=[]
valor_questao=[10,25,15,25,25]
pontuacao = 0

prova.append(questao1)
prova.append(questao2)
prova.append(questao3)
prova.append(questao4)
prova.append(questao5)

for num,questao in enumerate(prova):
    print(num+1,")",questao["enunciado"])
    print("a)",questao["opcao1"])
    print("b)",questao["opcao2"])
    print("c)",questao["opcao3"])
    print("d)",questao["opcao4"])
    print("\n")
    marcacao= input("Digite a letra da resposta escolhida:")
    marcacoes.append(marcacao)
    if marcacao==questao["gabarito"]: 
      pontuacao+=questao["valor_questao"]

for i in range(0,5):
    if marcacoes[i]==gabarito[i]: print("Questão",i+1,"Certa!")
    else: 
        print("Questão",i+1,"Errada!","Questão Correta:",gabarito[i])  
print("Pontuação Final",pontuacao)