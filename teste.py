# manipulação de arquivos 

#parte 1: Gravando uma mensagem no arquivo
with open ("meu_arquivo.txt", "w") as pasta: 
    pasta.write("ola! Este texto foi gravado pelo python.\n")
    pasta.write("isso significa que funcionou direitinho!")

print("Arquivo criado com sucesso! Verifique sua pasta.")

#parte 2: Lendo o arquivo que acabamos de criar

with open("meu_arquivo.txt", "r") as pasta:
    texto_salvo = pasta.read()
    print("\n--- OQUE ESTA ESCRITO NO ARQUIVO: ---")
    print(texto_salvo)
