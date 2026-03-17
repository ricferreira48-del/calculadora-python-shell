print("=== CALCULADORA ===")

n1 = float(input("Numero 1: "))
n2 = float(input("Numero 2: "))

print("1 Soma")
print("2 Subtração")
print("3 Multiplicação")
print("4 Divisão")

op = input("Opção: ")

if op == "1":
    print(n1 + n2)

elif op == "2":
    print(n1 - n2)

elif op == "3":
    print(n1 * n2)

elif op == "4":
    print(n1 / n2)

else:
    print("Erro")
