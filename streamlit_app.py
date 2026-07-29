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

# Lista completa dos 22 passos do tutorial
passos = [
    ("Passo 1: Baixar os documentos gerados", "passo_01"),
    ("Passo 2: Abrir o aplicativo Gov.br", "passo_02"),
    ("Passo 3: Localizar o serviço", "passo_03"),
    ("Passo 4: Selecionar 'Assinar documentos digitalmente'", "passo_04"),
    ("Passo 5: Clicar em 'Escolher arquivo'", "passo_05"),
    ("Passo 6: Selecionar os PDFs recentes", "passo_06"),
    ("Passo 7: Visualizar o documento carregado", "passo_07"),
    ("Passo 8: Arrastar o quadrado para a área de assinatura", "passo_08"),
    ("Passo 9: Confirmar a assinatura", "passo_09"),
    ("Passo 10: Opção de carregar outro documento", "passo_10"),
    ("Passo 11: Iniciar o processo de assinar ambos", "passo_11"),
    ("Passo 12: Autorização via notificação", "passo_12"),
    ("Passo 13: Digitar o código recebido", "passo_13"),
    ("Passo 14: Clicar em Autorizar", "passo_14"),
    ("Passo 15: Concluir etapa de assinatura", "passo_15"),
    ("Passo 16: Baixar arquivos assinados", "passo_16"),
    ("Passo 17: Menu de opções do navegador", "passo_17"),
    ("Passo 18: Abrir no navegador Chrome", "passo_18"),
    ("Passo 19: Retornar às opções", "passo_19"),
    ("Passo 20: Acessar pasta de Transferências", "passo_20"),
    ("Passo 21: Localizar os arquivos assinados", "passo_21"),
    ("Passo 22: Compartilhar os documentos via WhatsApp", "passo_22"),
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
        st.info(f"*(Imagem não encontrada na pasta 'imagens' para este passo)*")
    st.markdown("---")