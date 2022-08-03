print("Calculadora simples, digite um número, depois +,-,/,*, depois outro número. Escreva 'done' quando quiser finalizar")
r = input()
r = float(r)
while True:
    opcao = input()
    if opcao == 'done':
        quit()
    elif opcao.isdigit():
        r = float(opcao)
        print(r)
    elif opcao == '+':
        n = input()
        n = float(n)
        r += n
        print(r)
    elif opcao == '-':
        n = input()
        n = float(n)
        r -= n
        print(r)
    elif opcao == '*':
        n = input()
        n = float(n)
        r *= n
        print(r)
    elif opcao == '/':
        n = input()
        n = float(n)
        r /= n
        print(r)