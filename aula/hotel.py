PRECO_SIMPLES = 100.00
PRECO_DUPLO = 150.00
PRECO_LUXO = 250.00

cliente1_nome = str(input('Digite seu nome: '))
cliente1_idade = int(input('Digite sua idade: '))
cliente1_quarto = str(input('Digite seu tipo de quarto: ')) 
cliente1_dias = int(input('Digite a quantidade de dias: '))

cliente2_nome = str(input('Digite seu nome: '))
cliente2_idade = int(input('Digite sua idade: '))
cliente2_quarto = str(input('Digite seu tipo de quarto: ')) 
cliente2_dias = int(input('Digite a quantidade de dias: '))

cliente3_nome = str(input('Digite seu nome: '))
cliente3_idade = int(input('Digite sua idade: '))
cliente3_quarto = str(input('Digite seu tipo de quarto: ')) 
cliente3_dias = int(input('Digite a quantidade de dias: '))

lista_clientes = [cliente1_nome, cliente2_nome, cliente3_nome]

valor_cliente1 = 0.0
diaria_cliente1 = 0.0

if cliente1_quarto == 'SIMPLES':
    diaria_cliente1 = PRECO_SIMPLES
    valor_cliente1 = diaria_cliente1 * cliente1_dias
elif cliente1_quarto == 'DUPLO':
    diaria_cliente1 = PRECO_DUPLO
    valor_cliente1 = diaria_cliente1 * cliente1_dias
elif cliente1_quarto == 'LUXO':
    diaria_cliente1 = PRECO_LUXO
    valor_cliente1 = diaria_cliente1 * cliente1_dias
else:
    print(f"Alerta: Quarto de {cliente1_nome} inválido.")

valor_cliente2 = 0.0
diaria_cliente2 = 0.0

if cliente2_quarto == 'SIMPLES':
    diaria_cliente2 = PRECO_SIMPLES
    valor_cliente2 = diaria_cliente2 * cliente2_dias
elif cliente2_quarto == 'DUPLO':
    diaria_cliente2 = PRECO_DUPLO
    valor_cliente2 = diaria_cliente2 * cliente2_dias
elif cliente2_quarto == 'LUXO':
    diaria_cliente2 = PRECO_LUXO
    valor_cliente2 = diaria_cliente2 * cliente2_dias
else:
    print(f"Alerta: Quarto de {cliente2_nome} inválido.")


valor_cliente3 = 0.0
diaria_cliente3 = 0.0

if cliente3_quarto == 'SIMPLES':
    diaria_cliente3 = PRECO_SIMPLES
    valor_cliente3 = diaria_cliente3 * cliente3_dias
elif cliente3_quarto == 'DUPLO':
    diaria_cliente3 = PRECO_DUPLO
    valor_cliente3 = diaria_cliente3 * cliente3_dias
elif cliente3_quarto == 'LUXO':
    diaria_cliente3 = PRECO_LUXO
    valor_cliente3 = diaria_cliente3 * cliente3_dias
else:
    print(f"Alerta: Quarto de {cliente3_nome} inválido.")


print("\n🏨 **SISTEMA DE RESERVAS DO HOTEL**")
print("-----------------------------------")

print(f"\n✅ Cliente: **{cliente1_nome}**")
print(f"   Quarto: {cliente1_quarto} (R$ {diaria_cliente1:.2f} / dia)")
print(f"   Estadia: {cliente1_dias} dias")
print(f"   Total a Pagar: **R$ {valor_cliente1:.2f}**")

print(f"Cliente: **{cliente2_nome}**")
print(f"   Quarto: {cliente2_quarto} (R$ {diaria_cliente2:.2f} / dia)")
print(f"   Estadia: {cliente2_dias} dias")
print(f"   Total a Pagar: **R$ {valor_cliente2:.2f}**")

print(f" Cliente: {cliente3_nome}")
print(f"   Quarto: {cliente3_quarto} (R$ {diaria_cliente3:.2f} / dia)")
print(f"   Estadia: {cliente3_dias} dias")
print(f"   Total a Pagar: R$ {valor_cliente3:.2f}")

print("-----------------------------------")

valor_total_geral = valor_cliente1 + valor_cliente2 + valor_cliente3
print(f" **TOTAL GERAL DAS RESERVAS**: R$ {valor_total_geral:.2f}")