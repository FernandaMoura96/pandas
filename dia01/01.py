'''Solicite ao usuario o preço de uma fruta e retorne o preço'''

fruta = input("Qual fruta deseja consultar?") .capitalize() .strip()

frutas = {         "Maça" : "R$6.99",
                   "Banana" : "R$7.99",
                   "Pera" : "R$ 9.99",
                   "Uva" : "R$12.99",
                   "Laranja" : "R$ 3.89",
                   "limão" : "R$ 2.99",
                   "Goiaba" :"R$ 5.49",
                   "Abacaxi" : "R$ 5.00",
                   "Manga" : "R$ 7.99"
                   }

if fruta in frutas :
    print(frutas[fruta])
else:
    print("Entre com uma fruta válida")
