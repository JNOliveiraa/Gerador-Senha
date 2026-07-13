import random 
import string

def gerar_senha(comprimento, usar_especiais): 
      caracteres = string.ascii_letters + string.digits
      if usar_especiais.lower() == "s":
            caracteres += string.punctuation
      return "".join(random.choice(caracteres) for _ in range(comprimento))

print("--- BEM VINDO AO GERADOR DE SENHAS SEGURAS ---")

# o loop 'while True' vai rodar para sempre até encontrar um comando 'break

while True:
      try: 
            tamanho = int( input("\nDigite o tamanho da senha (recomendado entre 8 e 20):"))

            if tamanho < 4: 
                  print("❌ Erro: Escolha um tamanho de pelo menos 4 caracteres")
                  continue
            
            if tamanho > 100:
                  print("❌ Erro: O tamanho máximo permitido é 100 caracteres.")
                  continue

            especiais = input("incluir símbolos especiais (s/n): ")
            nova_senha = gerar_senha(tamanho, especiais)

            print("\n===================================")
            print(f"sua senha gerada é: {nova_senha}")
            print("=====================================")

            break
      
      except ValueError:
            print(
                  "❌ Erro: Por favor, digite apenas números inteiros para o tamanho."
            )

            print("Vamos tentar novamente...")