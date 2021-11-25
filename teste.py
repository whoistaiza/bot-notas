#função que recebe dois parâmetros soma e devolve o resultado
def soma(n1,n2):
    resultado = n1+n2
    return (resultado)



#main principal que rodará por toda a execução
def main() -> None:
    num1=int(input("digite o primeiro numero pra soma:"))
    num2=int(input("digite o segundo numero pra soma:"))

    #chama a função soma e ja printa o retorno
    print(soma(num1,num2))



#chama o main principal
if __name__ == '__main__':
    main()
