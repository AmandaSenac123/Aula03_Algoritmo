preco_unitario = input('valor do ingresso: ') # "20"
preco_unitario = float(preco_unitario) # 20.0

valor_disponivel = float(input('Informe o valor disponível: '))

quantidade = int(valor_disponivel // preco_unitario) # // divisão inteira
troco = valor_disponivel % preco_unitario

print(f"Quantidade de ingressos: {quantidade}")
print(f" Troco de R$ {troco}")