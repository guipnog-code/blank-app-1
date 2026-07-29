import os
import streamlit as st

# Configuração da página para focar no tutorial
st.set_page_config(
    page_title="Tutorial de Assinatura Digital",
    page_icon="📖",
    layout="centered"
)

st.title("📖 Tutorial: Como Assinar Digitalmente e Enviar")
st.markdown("<p style='margin-top: -10px; margin-bottom: 15px;'>Siga o passo a passo ilustrado abaixo enquanto realiza o processo:</p>", unsafe_allow_html=True)

# Exibe o player do áudio/vídeo explicativo logo no topo
if os.path.exists("Audio_tutorial.mp4"):
    st.video("Audio_tutorial.mp4")
    st.caption("🎧 *Dica: Você pode reproduzir o guia e pausar ou acelerar a reprodução conforme sua necessidade.*")
else:
    st.info("💡 *(Arquivo de áudio/vídeo do tutorial não encontrado na raiz do projeto)*")

st.markdown("---")

# Lista associando o título do passo ao nome exato do arquivo de imagem correspondente
passos = [
    ("Passo 1: Baixar os documentos gerados", "1000127282"),
    ("Passo 2: Abrir o aplicativo Gov.br", "1000127283"),
    ("Passo 3: Localizar o serviço", "1000127284"),
    ("Passo 4: Selecionar 'Assinar documentos digitalmente'", "1000127285"),
    ("Passo 5: Clicar em 'Escolher arquivo'", "1000127286"),
    ("Passo 6: Selecionar os PDFs recentes", "1000127287"),
    ("Passo 7: Visualizar o documento carregado", "1000127288"),
    ("Passo 8: Arrastar o quadrado para a área de assinatura", "1000127289"),
    ("Passo 9: Confirmar a assinatura", "1000127290"),
    ("Passo 10: Opção de carregar outro documento", "1000127291"),
    ("Passo 11: Iniciar o processo de assinar ambos", "1000127292"),
    ("Passo 12: Autorização via notificação", "1000127293"),
    ("Passo 13: Digitar o código recebido", "1000127294"),
    ("Passo 14: Clicar em Autorizar", "1000127295"),
    ("Passo 15: Concluir etapa de assinatura", "1000127296"),
    ("Passo 16: Baixar arquivos assinados", "1000127297"),
    ("Passo 17: Menu de opções do navegador", "1000127298"),
    ("Passo 18: Abrir no navegador Chrome", "1000127299"),
    ("Passo 19: Retornar às opções", "1000127300"),
    ("Passo 20: Acessar pasta de Transferências", "1000127301"),
    ("Passo 21: Localizar os arquivos assinados", "1000127302"),
    ("Passo 22: Compartilhar os documentos via WhatsApp", "1000127303"),
]

# Exibição iterativa dos passos com as imagens redimensionadas
for titulo, nome_base in passos:
    st.subheader(titulo)
    
    arquivo_encontrado = None
    for ext in [".jpeg", ".jpg", ".JPEG", ".JPG"]:
        caminho_teste = os.path.join("imagens", nome_base + ext)
        if os.path.exists(caminho_teste):
            arquivo_encontrado = caminho_teste
            break
            
    if arquivo_encontrado:
        st.image(arquivo_encontrado, width=400)
    else:
        st.info(f"*(Imagem '{nome_base}' não encontrada na pasta 'imagens')*")
    st.markdown("---")