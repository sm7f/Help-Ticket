import tkinter as tk
import win32clipboard
import os
from datetime import datetime

# Função para copiar o texto selecionado para a área de transferência
def copiar_texto(texto):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(texto)
    win32clipboard.CloseClipboard()

# Função para lidar com a seleção de texto no menu
def selecionar_texto(numero):
    if numero in textos:
        texto_selecionado = textos[numero]
        copiar_texto(texto_selecionado)
        print("Texto copiado para a área de transferência: ", texto_selecionado)
    else:
        print("Opção inválida.")

def registrar_log(informacoes):
    # Nome do arquivo de log (com base no mês e ano atuais)
    data_atual = datetime.now()
    nome_arquivo_log = data_atual.strftime("%Y-%m") + "_log.txt"

    # Caminho completo para o arquivo de log
    caminho_arquivo_log = os.path.join("logs", nome_arquivo_log)

    # Crie o diretório "logs" se ele não existir
    os.makedirs("logs", exist_ok=True)

    # Registrar as informações no arquivo de log
    with open(caminho_arquivo_log, "a") as arquivo_log:
        arquivo_log.write(f"{datetime.now()} - {informacoes}\n")

# Função para registrar o atendimento e copiar informações para a área de transferência
def registrar_atendimento():
    nome_cliente = nome_cliente_entry.get()
    cnpj_empresa = cnpj_empresa_entry.get()
    sistema_empresa = sistema_empresa_entry.get()
    telefone_cliente = telefone_cliente_entry.get()  # Novo campo para o número de telefone
    hora_atendimento = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tipo_atendimento = tipo_atendimento_var.get()

    # Verifica se o tipo de atendimento está nos textos pré-definidos
    if tipo_atendimento in textos:
        # Obtém o texto correspondente ao tipo de atendimento selecionado
        texto_selecionado = textos[tipo_atendimento]

        # Concatena as informações em uma única string
        informacoes_atendimento = f"Nome do Cliente: {nome_cliente}\nCNPJ da Empresa: {cnpj_empresa}\nSistema Empresa: {sistema_empresa}\nTelefone do Cliente: {telefone_cliente}\nHora do Atendimento: {hora_atendimento}\nTipo de Atendimento: {texto_selecionado}"

        # Copiar informações para a área de transferência
        copiar_texto(informacoes_atendimento)

        registrar_log(informacoes_atendimento)
    else:
        tk.messagebox.showerror("Erro", "Tipo de Atendimento inválido.")

# Textos pré-definidos
textos = {
    1:  " Solicitação - | | Descrição do Problema: ",
    2:  "",
    3:  "Comandos Rápidos",
    4:  "netsh advfirewall set allprofiles state off",
    5:  "net user Administrator /active:yes",
    6:  "taskkill /f /im PDV.exe",
    7:  "taskkill /f /im PoliSystemPDV.exe",
    8:  "taskkill /f /im PoliSystemADM.exe",
    9:  "sc stop MSSQLSERVER",
    10: "sc start MSSQLSERVER",
    11: "",
    12: "",
    13: "",
    14: "Respostas Rápidas",
    15: "Para ajudar a resolver sua questão o mais rápido possível, por favor, explique detalhadamente o motivo do seu contato. ",
    16: "Me informe o acesso do teamviewer",
}

# Criação da interface do menu
root = tk.Tk()
root.resizable(width=False, height=False)
root.title("Ticket Help")
root.geometry("400x800")  # Aumenta a largura da janela

label = tk.Label(root, text="Selecione o Motivo")
label.pack(pady=10)

# Criação dos botões do menu
for num, texto in textos.items():
    motivo_resumido = texto.split(":")[0].strip()  # Obtém apenas o motivo resumido

    # Função de callback para o botão
    def callback(numero=num):
        selecionar_texto(numero)

    button = tk.Button(root, text=motivo_resumido, command=callback, width=50, anchor='w')  # Aumenta a largura do botão e alinha o texto à esquerda
    button.pack(pady=2)

# Lista de opções de 1 a 19
opcoes_tipo_atendimento = list(range(1, 20))

# Variável para armazenar o tipo de atendimento selecionado
tipo_atendimento_var = tk.IntVar(root)
tipo_atendimento_var.set(opcoes_tipo_atendimento[0])  # Valor padrão

# Criação do menu suspenso para o tipo de atendimento
tipo_atendimento_option_menu = tk.OptionMenu(root, tipo_atendimento_var, *opcoes_tipo_atendimento)
tipo_atendimento_option_menu.config(width=5)  # Aumenta a largura do menu suspenso
tipo_atendimento_option_menu.pack(pady=5)

# Adicione um rótulo e uma entrada para o Nome do Cliente
nome_cliente_label = tk.Label(root, text="Nome do Cliente:")
nome_cliente_label.pack(pady=2)

nome_cliente_entry = tk.Entry(root, width=50)
nome_cliente_entry.pack(pady=2)

# Adicione um rótulo e uma entrada para o CNPJ da Empresa
cnpj_empresa_label = tk.Label(root, text="CNPJ da Empresa:")
cnpj_empresa_label.pack(pady=2)

cnpj_empresa_entry = tk.Entry(root, width=50)
cnpj_empresa_entry.pack(pady=2)

# Adicione um rótulo e uma entrada para o Sistema Empresa
sistema_empresa_label = tk.Label(root, text="Sistema Empresa:")
sistema_empresa_label.pack(pady=2)

sistema_empresa_entry = tk.Entry(root, width=50)
sistema_empresa_entry.pack(pady=2)

# Adicione um rótulo e uma entrada para o Número de Telefone do Cliente
telefone_cliente_label = tk.Label(root, text="Telefone do Cliente:")
telefone_cliente_label.pack(pady=2)

telefone_cliente_entry = tk.Entry(root, width=50)
telefone_cliente_entry.pack(pady=2)

# Botão para registrar o atendimento
registrar_button = tk.Button(root, text="Registrar Atendimento", command=registrar_atendimento, width=50)
registrar_button.pack(pady=10)

root.mainloop()
