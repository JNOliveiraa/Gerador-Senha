while True: 
  try: 
    numero =  float(input("digite um numero: "))
    break
  except ValueError: 
    print("Digite um numero valido! Tente novamente.")

print(f"voce digitou o numero {numero}")