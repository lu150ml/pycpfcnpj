from pycpfcnpj import cpfcnpj


entrada = input("Cole a lista de CPFs separados por vírgula:\n> ")


cpf_list = [cpf.strip() for cpf in entrada.split(",")]

print("\n📋 Resultados da validação:\n")


for cpf in cpf_list:
    valido = cpfcnpj.validate(cpf)
    status = "✅ Válido" if valido else "❌ Inválido"
    print(f"{cpf} → {status}")