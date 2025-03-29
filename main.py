from nicegui import ui

def gerar_prompt():
    sujeito = input_sujeito.value
    detalhes = input_detalhes.value
    acao = input_acao.value
    ambiente = input_ambiente.value
    iluminacao = input_iluminacao.value
    imperfeicoes = input_imperfeicoes.value
    camera = input_camera.value

    prompt = f"{sujeito} {detalhes}, {acao}, {ambiente}, {iluminacao}, {imperfeicoes}, {camera}"
    resultado_label.set_text(prompt)
    copiar_btn.visible = True

def copiar_prompt():
    ui.run_javascript(f"navigator.clipboard.writeText(`{resultado_label.text}`)")
    ui.notify('✅ Prompt copiado!')

ui.markdown("# 🎨 Gerador Interativo de Prompts para ImageFX\nPreencha os campos abaixo para criar prompts realistas e cinematográficos.")

with ui.card().classes('bg-gray-900 text-white p-6 rounded-2xl shadow-lg'):
    input_sujeito = ui.input(label='👤 Sujeito principal', placeholder='ex: a young girl').classes('mb-4')
    input_detalhes = ui.input(label='🎨 Detalhamento visual', placeholder='ex: curly hair, freckles, worn jacket').classes('mb-4')
    input_acao = ui.input(label='🎬 Ação ou expressão', placeholder='ex: holding a paper boat near a river').classes('mb-4')
    input_ambiente = ui.input(label='🌄 Ambiente/contexto', placeholder='ex: foggy forest at dawn').classes('mb-4')
    input_iluminacao = ui.input(label='💡 Iluminação', placeholder='ex: cinematic soft lighting').classes('mb-4')
    input_imperfeicoes = ui.input(label='♻️ Imperfeições naturais', placeholder='ex: muddy boots, skin pores').classes('mb-4')
    input_camera = ui.input(label='📷 Configuração de câmera', placeholder='ex: shot on Canon EOS R5, 85mm lens, f/1.4').classes('mb-4')

    ui.button('✨ Gerar Prompt', on_click=gerar_prompt, color='orange', icon='wand2').classes('mb-4')

resultado_label = ui.label("Seu prompt aparecerá aqui...").classes('text-lg text-orange-400 mb-2')
copiar_btn = ui.button('📋 Copiar Prompt', on_click=copiar_prompt, color='green', icon='copy').classes('mb-4')
copiar_btn.visible = False

with ui.expansion('📚 Exemplos prontos', icon='sparkles'):
    def carregar_exemplo(prompt_data):
        input_sujeito.value = prompt_data[0]
        input_detalhes.value = prompt_data[1]
        input_acao.value = prompt_data[2]
        input_ambiente.value = prompt_data[3]
        input_iluminacao.value = prompt_data[4]
        input_imperfeicoes.value = prompt_data[5]
        input_camera.value = prompt_data[6]

    exemplos = [
        ("a young boy", "with messy curly hair and freckles", "holding a red kite tangled in a tree branch",
         "standing in a foggy field at sunrise", "soft cinematic lighting", "muddy boots, visible skin pores",
         "shot on Canon EOS R5, 85mm lens, f/1.4"),

        ("an elderly fisherman", "with weathered skin and gray beard", "sitting on a wooden boat",
         "early morning mist on the lake", "golden hour lighting", "cracked hands, wrinkles, worn clothing",
         "shot on Nikon D850, 50mm lens, f/1.8")
    ]

    for exemplo in exemplos:
        ui.button('Carregar exemplo', on_click=lambda e=exemplo: carregar_exemplo(e)).classes('m-1')

ui.run(title='Gerador de Prompts para ImageFX')
