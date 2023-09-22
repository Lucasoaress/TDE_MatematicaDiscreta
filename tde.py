# Função para calcular a composição de duas funções
def composicao_de_funcoes(f, g, x):
    return f(g(x))

# Insira as expressões para f(x), g(x) e o valor de x

expressaof = input("Digite a expressão para f(x) (use 'x' como variável): ")
expressaog = input("Digite a expressão para g(x) (use 'x' como variável): ")
valor_de_x = float(input("Digite o valor de x: "))

# Defina as funções f(x) e g(x) 

def funcaof(x):
    return eval(expressaof)

def funcaog(x):
    return eval(expressaog)

# Calcula f(g(x))

resultado = composicao_de_funcoes(funcaof, funcaog, valor_de_x)
print(f"O resultado de f(g({valor_de_x})) é: {resultado}")
