from nicegui import ui
from deep_translator import GoogleTranslator

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

def copiar_prompt():
    ui.run_javascript(f"navigator.clipboard.writeText(`{resultado_label.text}`)")
    ui.notify('✅ Prompt copiado!')

def preencher_exemplo(data):
    input_sujeito.value = data[0]
    input_detalhes.value = data[1]
    input_acao.value = data[2]
    input_ambiente.value = data[3]
    input_iluminacao.value = data[4]
    input_imperfeicoes.value = data[5]
    input_camera.value = data[6]
    gerar_prompt()

ui.markdown("# 🎨 Gerador Interativo de Prompts para ImageFX\nPreencha os campos abaixo em português — o prompt será traduzido para inglês automaticamente.")

with ui.row().classes('w-full justify-around items-start'):
    
    # COLUNA DA ESQUERDA: RESULTADO + SUGESTÕES
    with ui.column().classes('w-1/2 p-4 items-start'):
        ui.label('🎯 Prompt Gerado (em inglês):').classes('text-lg font-bold text-gray-800')
        resultado_label = ui.label('').classes('bg-gray-100 text-black p-4 rounded-md w-full font-mono shadow-md min-h-[100px]')
        copiar_btn = ui.button('📋 Copiar Prompt', on_click=copiar_prompt, color='green').classes('mt-2')
        copiar_btn.visible = False

        ui.separator().classes('my-4')

        ui.label('💡 Exemplos rápidos (clique para carregar):').classes('font-bold mb-2')
        exemplos = [
            ["garoto pequeno", "cabelos cacheados e sardas", "segurando uma pipa vermelha presa na árvore",
             "campo com neblina ao amanhecer", "luz suave e cinematográfica", "botas sujas, poros visíveis",
             "Canon EOS R5, lente 85mm, f/1.4"],

            ["pescador idoso", "pele marcada pelo sol e barba grisalha", "sentado num barco de madeira",
             "névoa sobre o lago de manhã", "luz dourada do nascer do sol", "mãos rachadas, rugas, roupa gasta",
             "Nikon D850, lente 50mm, f/1.8"],

            ["robô danificado", "olhos azuis brilhantes, armadura enferrujada", "andando entre ruínas futuristas",
             "cidade destruída ao entardecer", "luz dura com sombras profundas", "arranhões, peças quebradas",
             "Sony A7 III, lente 35mm, f/2.0"],
        ]
        for exemplo in exemplos:
            ui.button(exemplo[0].capitalize(), on_click=lambda e=exemplo: preencher_exemplo(e)).classes('m-1')

    # COLUNA DA DIREITA: FORMULÁRIO
    with ui.card().classes('w-1/2 bg-white text-black p-6 rounded-2xl shadow-lg'):
        input_sujeito = ui.input(label='👤 Sujeito principal').classes('mb-3')
        input_detalhes = ui.input(label='🎨 Detalhamento visual').classes('mb-3')
        input_acao = ui.input(label='🎬 Ação ou expressão').classes('mb-3')
        input_ambiente = ui.input(label='🌄 Ambiente/contexto').classes('mb-3')
        input_iluminacao = ui.input(label='💡 Iluminação').classes('mb-3')
        input_imperfeicoes = ui.input(label='♻️ Imperfeições naturais').classes('mb-3')
        input_camera = ui.input(label='📷 Configuração de câmera').classes('mb-3')

        ui.button('✨ GERAR PROMPT', on_click=gerar_prompt, color='orange').classes('mt-4')

ui.run(title='Gerador de Prompts para ImageFX')
