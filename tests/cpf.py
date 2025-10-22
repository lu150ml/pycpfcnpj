from pycpfcnpj import cpfcnpj

cpf_list= []
qtd = int(input("Quantos CPFs/CNPJs deseja validar? "))
for i in range(qtd):
    cpf_list.append(input("Digite o CPF/CNPJ: "))

print("\n📋 Resultados da validação:\n")
for cpf in cpf_list:
    valido = cpfcnpj.validate(cpf)
    if valido:
        print(f"{cpf} ✅ Válido")
    else:
        print(f"{cpf} ❌ Inválido")