# Defina uma função para calcular a composição de duas funções
def composicao_de_funcoes(f, g, x):
    return f(g(x))

# Peça ao usuário que insira as expressões para f(x), g(x) e o valor de x
expressao_f = input("Digite a expressão para f(x) (use 'x' como variável): ")
expressao_g = input("Digite a expressão para g(x) (use 'x' como variável): ")
valor_de_x = float(input("Digite o valor de x: "))

# Defina as funções f(x) e g(x) a partir das expressões inseridas pelo usuário
def funcao_f(x):
    return eval(expressao_f)

def funcao_g(x):
    return eval(expressao_g)

# Calcule a composição f(g(x))
resultado = composicao_de_funcoes(funcao_f, funcao_g, valor_de_x)
print(f"O resultado de f(g({valor_de_x})) é: {resultado}")