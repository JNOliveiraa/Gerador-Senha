import random 
import string 
import streamlit as st


def gerar_senha(comprimento, usar_especiais): 
   caracteres = string.ascii_letters + string.digits
   if usar_especiais: 
      caracteres += string.punctuation 
   return "".join(random.choice(caracteres) for _ in range (comprimento))


# --- CONFIGURAÇÂO DA INTERFACE VISUAL ---
st.set_page_config(page_title="Gerador de senhas", page_icon="🔐")

st.title("🔐 Gerador de Senhas Seguras")
st.write("Crie senhas fortes de forma simples e rápida direto no seu navegador.")

# Controle de arrastar para o tamanho 
tamanho = st.slider (
   "Escolha o tamanho da senha: ", min_value=4, max_value=100, value=12
)

# caixa de seleção para símbolos
especiais = st.checkbox (
   "Incluir símbolos especiais?", help="Ex: !, @, #"
)

st.divider()

# Botão para gerar
if st.button("Gerar Nova Senha", type = "primary"):
   nova_senha = gerar_senha(tamanho, especiais)

   st.success("Sua senha foi gerada com sucesso!")
   st.code(nova_senha, language="txt") # caixa de texto pronta para copiar

   # Salva no histórico Local automaticamente
   with open("senhas_web.txt", "a", encoding= "utf-8") as arquivo:
      arquivo.write(f"senha gerada: {nova_senha}\n")
   
   st.caption (
      "💾 Esta senha também foi guardada no seu arquivo 'senhas_web.txt' "
   )