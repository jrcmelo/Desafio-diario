'''
Crie uma função que filtra uma lista de dicionários de produtos, a lista dos dicionários de produtos, o valor máximo e o valor mínimo.
A função devera retornar uma lista de dicionários dos produtos que estejam dentro desse intervalo de preço
'''

produtos = {
    "Arroz 5kg": 24.90,
    "Feijão 1kg": 7.80,
    "Macarrão 500g": 4.50,
    "Açúcar 1kg": 5.60,
    "Sal 1kg": 2.30,
    "Café 500g": 18.70,
    "Leite 1L": 4.80,
    "Óleo de soja 900ml": 7.20,
    "Manteiga 200g": 12.50,
    "Pão francês 1kg": 13.40,
    "Biscoito recheado 140g": 3.25,
    "Refrigerante 2L": 9.90,
    "Água mineral 1.5L": 2.10,
    "Cerveja lata 350ml": 4.50,
    "Frango inteiro 1kg": 16.90,
    "Carne bovina 1kg": 39.90,
    "Linguiça toscana 1kg": 22.80,
    "Ovos dúzia": 9.30,
    "Queijo mussarela 500g": 24.00,
    "Presunto 500g": 19.80,
    "Maçã 1kg": 7.20,
    "Banana 1kg": 5.80,
    "Laranja 1kg": 4.50,
    "Tomate 1kg": 8.40,
    "Batata 1kg": 5.70,
    "Cebola 1kg": 4.60,
    "Alho 100g": 3.80,
    "Alface unidade": 2.50,
    "Cenoura 1kg": 4.30,
    "Brócolis unidade": 6.20,
    "Sabonete 90g": 2.40,
    "Shampoo 350ml": 14.90,
    "Papel higiênico 4 rolos": 7.50,
    "Detergente 500ml": 2.70,
    "Amaciante 2L": 12.40,
    "Sabão em pó 1kg": 10.30,
    "Creme dental 90g": 5.60,
    "Desodorante aerosol 150ml": 13.20,
    "Barra de chocolate 100g": 6.90,
    "Sorvete 1L": 15.80,
    "Cereal matinal 250g": 9.70,
    "Farinha de trigo 1kg": 4.90,
    "Milho de pipoca 500g": 3.40,
    "Atum em lata 170g": 7.60,
    "Sardinha em lata 125g": 5.10,
    "Molho de tomate 340g": 3.20,
    "Ervilha em lata 200g": 3.60,
    "Azeitona 100g": 4.90,
    "Suco de laranja 1L": 7.80,
    "Vinho tinto 750ml": 34.90,
    "Energético 250ml": 8.50,
    "Pizza congelada 450g": 19.90,
    "Hambúrguer congelado 2 unidades": 12.30
}

def pesquisa (max, min):
    i = 0
    chaves = list(produtos.keys())

    while i < len(chaves):
        if i < max and i > min:
            chave = chaves[i]
            valor = produtos[chave]
            print(f"{chave}, Valor: {valor:.2f}")
        i+=1

    

min = float(input('Valor minimo: '))
max = float(input('Valor maximo: '))

pesquisa(max, min)