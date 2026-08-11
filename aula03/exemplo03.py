preco = float(input('Preço do produto: '))
quantidade = int(input('Quantidade comprada: '))

#processamento
total = preco * quantidade

desconto = total * 0.1 # desconto de 10%

valor_pagar = total - desconto
print(30*"=")
print(f'Valor total: R$ {total:.2f}')
print(f'Valor a pagar: R$ {valor_pagar:.2f}')
print(f'Desconto de R$ {desconto:.2f}')