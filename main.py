from nicegui import ui
from deep_translator import GoogleTranslator

# Função que monta o prompt e traduz
def gerar_prompt():
    sujeito = input_sujeito.value
    detalhes = input_detalhes.value
    acao = input_acao.value
    ambiente = input_ambiente.value
    iluminacao = input_iluminacao.value
    imperfeicoes = input_imperfeicoes.value
    camera = input_camera.value

    prompt_pt = f"{sujeito} {detalhes}, {acao}, {ambiente}, {iluminacao}, {imperfeicoes}, {camera}"
    prompt_en = GoogleTranslator(source='auto', target='en').translate(prompt_pt)

    resultado_label.set_text(prompt_en)
    copiar_btn.visible = True

# Copiar texto para área de transferência
def copiar_prompt():
    ui.run_javascript(f"navigator.clipboard.writeText(`{resultado_label.text}`)")
    ui.notify('✅ Prompt copiado!')

ui.markdown("# 🎨 Gerador Interativo de Prompts para ImageFX\nPreencha os campos abaixo **em português** — o prompt será gerado automaticamente em inglês para uso direto no ImageFX.")

with ui.card().classes('bg-white text-black p-6 rounded-2xl shadow-lg max-w-2xl mx-auto'):
    input_sujeito = ui.input(label='👤 Sujeito principal', placeholder='ex: homem com barba grisalha').classes('mb-4')
    input_detalhes = ui.input(label='🎨 Detalhamento visual', placeholder='ex: cabelo cacheado, pele bronzeada').classes('mb-4')
    input_acao = ui.input(label='🎬 Ação ou expressão', placeholder='ex: olhando pela janela segurando um livro').classes('mb-4')
    input_ambiente = ui.input(label='🌄 Ambiente/contexto', placeholder='ex: cabana de madeira sob chuva fina').classes('mb-4')
    input_iluminacao = ui.input(label='💡 Iluminação', placeholder='ex: luz suave e difusa vinda da esquerda').classes('mb-4')
    input_imperfeicoes = ui.input(label='♻️ Imperfeições naturais', placeholder='ex: rugas, sardas, cabelo desalinhado').classes('mb-4')
    input_camera = ui.input(label='📷 Configuração de câmera', placeholder='ex: lente 85mm, f/1.4, Canon R5').classes('mb-4')

    ui.button('✨ GERAR PROMPT', on_click=gerar_prompt, color='orange', icon='wand2').classes('mb-4')

resultado_label = ui.label("Seu prompt aparecerá aqui...").classes('text-lg text-black mb-2')
copiar_btn = ui.button('📋 Copiar Prompt', on_click=copiar_prompt, color='green', icon='copy').classes('mb-4')
copiar_btn.visible = False

with ui.expansion('📚 Exemplos prontos (em português)', icon='sparkles'):
    def carregar_exemplo(prompt_data):
        input_sujeito.value = prompt_data[0]
        input_detalhes.value = prompt_data[1]
        input_acao.value = prompt_data[2]
        input_ambiente.value = prompt_data[3]
        input_iluminacao.value = prompt_data[4]
        input_imperfeicoes.value = prompt_data[5]
        input_camera.value = prompt_data[6]

    exemplos = [
        ("menino pequeno", "cabelos cacheados e sardas", "segurando uma pipa vermelha presa na árvore",
         "campo com neblina ao amanhecer", "luz suave e cinematográfica", "botas sujas, poros visíveis",
         "Canon EOS R5, lente 85mm, f/1.4"),

        ("pescador idoso", "pele marcada pelo sol e barba grisalha", "sentado num barco de madeira",
         "névoa sobre o lago de manhã", "luz dourada do nascer do sol", "mãos rachadas, rugas, roupa gasta",
         "Nikon D850, lente 50mm, f/1.8")
    ]

    for exemplo in exemplos:
        ui.button('Carregar exemplo', on_click=lambda e=exemplo: carregar_exemplo(e)).classes('m-1')

ui.run(title='Gerador de Prompts para ImageFX')
