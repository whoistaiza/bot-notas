#função que recebe dois parâmetros soma e devolve o resultado
def par(n1):
    if n1%2==0:
        print('eh par')
    else:
        print('nao eh par')



#main principal que rodará por toda a execução
def main() -> None:
    num1=float(input("digite o primeiro numero pra saber se eh par:"))
    #chama a função par
    par(num1)



#chama o main principal
if __name__ == '__main__':
    main()
