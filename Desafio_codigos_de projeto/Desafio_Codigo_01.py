def formatar_mensagem(mensagem):

    # Remove espaços extras no início e fim
    mensagem = mensagem.strip()

    # Se estiver vazia após o strip, imprime vazio
    if not mensagem:
        print("")
    else:
        # Converte para minúsculas e remove múltiplos espaços entre palavras
        palavras = mensagem.lower().split()
        mensagem_processada = " ".join(palavras)

    return mensagem_processada


# TODO: Processar o texto para garantir:
#   - letras minúsculas
#   - apenas um espaço separando as palavras (não podem haver múltiplos espaços)
# Dica: separe a string em palavras e depois una novamente, garantindo um espaço entre elas

# Retorne o texto já formatado conforme as regras
# return mensagem_formatada

# Lê a mensagem enviada ao robô via input padrão
entrada = input()  # Tipo de dado esperado: str

# Chama a função formatar_mensagem (você irá implementar a lógica)
saida = formatar_mensagem(entrada)

# Exibe a mensagem padronizada
print(saida)