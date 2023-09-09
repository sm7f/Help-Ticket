# ticket.help.py

import tkinter as tk
import win32clipboard
import os
import platform
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
    telefone_cliente = telefone_cliente_entry.get()  # Novo campo para o número de telefone
    hora_atendimento = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tipo_atendimento = tipo_atendimento_var.get()

    # Verifica se o tipo de atendimento está nos textos pré-definidos
    if tipo_atendimento in textos:
        # Obtém o texto correspondente ao tipo de atendimento selecionado
        texto_selecionado = textos[tipo_atendimento]

        # Concatena as informações em uma única string
        informacoes_atendimento = f"Nome do Cliente: {nome_cliente}\nCNPJ da Empresa: {cnpj_empresa}\nTelefone do Cliente: {telefone_cliente}\nHora do Atendimento: {hora_atendimento}\nTipo de Atendimento: {texto_selecionado}"

        # Copiar informações para a área de transferência
        copiar_texto(informacoes_atendimento)

        registrar_log(informacoes_atendimento)


    else:
        tk.messagebox.showerror("Erro", "Tipo de Atendimento inválido.")






# Textos pré-definidos
textos = {
    1:  "1 Solicitação - Erro Abertura do Sistema:  O cliente solicitou assistência para investigar as possíveis causas que impedem a abertura do sistema. Foi necessário intervir e fornecer suporte técnico para identificar e resolver as questões relacionadas ao problema mencionado.",
    2:  "2 Solicitação - Vinculação de certificado digital:  O cliente solicitou assistência para vincular o seu certificado digital ao sistema. Foi necessário intervir e fornecer suporte técnico para auxiliar o cliente no processo de vinculação do certificado digital ao sistema.",
    3:  "3 Solicitação - Auxilio NFS-e: O cliente solicitou suporte para a emissão de uma Nota Fiscal de Serviço (NFS-e). Foi necessário intervir e fornecer assistência para auxiliar o cliente no processo de emissão da referida NFS-e. ",
    4:  "4 Solicitação - Auxilio NFC-e: O cliente buscou nossa assistência para obter suporte na emissão de uma Nota Fiscal de Consumidor Eletrônica (NFC-e). Foi necessário intervir e prestar auxílio ao cliente no processo de emissão da referida NFC-e.",
    5:  "5 Solicitação - Auxilio NF-e: O cliente solicitou suporte para a emissão de uma Nota Fiscal Eletrônica (NF-e). Foi necessário intervir e fornecer assistência para auxiliar o cliente no processo de emissão da referida NFe.",
    6:  "6 Solicitação - Auxilio NF-e Devolução: O cliente fez uma solicitação de assistência para emissão de uma nota de devolução. Foi requerida nossa intervenção a fim de fornecer orientação e suporte nesse processo.",
    7:  "7 Solicitação - Auxilio NF-e Remessa: O cliente fez uma solicitação de assistência para emissão de uma nota de Remessa. Foi requerida nossa intervenção a fim de fornecer orientação e suporte nesse processo.",
    8:  "8 Solicitação - Auxilio NF-e Entrada: O cliente fez uma solicitação de assistência para emissão de uma nota de Entrada. Foi requerida nossa intervenção a fim de fornecer orientação e suporte nesse processo.",
    9:  "9 Solicitação - Auxilio NF-e Troca: O cliente fez uma solicitação de assistência para emissão de uma nota de Troca. Foi requerida nossa intervenção a fim de fornecer orientação e suporte nesse processo.",
    10: "10 Solicitação - Erro Extrair XML: O cliente solicitou assistência para investigar as possíveis causas de um erro ocorrido ao extrair um arquivo XML. Foi necessário intervir e fornecer suporte técnico para identificar e resolver as questões relacionadas ao referido erro.",
    11: "11 Solicitação - Auxilio Extrair XML: O cliente solicitou assistência para extrair o arquivo XML referente ao mês em questão. Foi necessário intervir e fornecer suporte técnico para auxiliar o cliente no processo de extração do referido arquivo XML. ",
    12: "12 Solicitação - Auxilio Cancelar Nota: O cliente solicitou assistência para realizar o cancelamento de uma nota fiscal. Foi necessário intervir e fornecer suporte para auxiliar o cliente no processo de cancelamento da referida nota. ",
    13: "13 Solicitação - Auxilio Visualizar Relatório: O cliente solicitou assistência para visualizar o relatório solicitado. Foi necessário intervir e fornecer suporte técnico para auxiliar o cliente no processo de acesso e visualização do referido relatório.",
    14: "14 Solicitação - (Contra-Senha) Sem Pendencia: O cliente solicitou assistência para gerar uma contra-senha e liberar o acesso ao sistema. Foi necessário intervir e fornecer suporte técnico para auxiliar o cliente na geração da contra-senha e garantir o acesso ao referido sistema.",
    15: "15 Solicitação - (Contra-Senha) Block Transfe: Foi identificada uma pendência e o cliente foi transferido para o setor responsável para solução. A pendência está relacionada à geração da contra-senha e acesso ao sistema.",
    16: "16 Solicitação - (Contra-Plantão) Com Pendencia: Devido à solicitação ocorrida no horário de plantão, foi gerada uma contra-senha para liberar o acesso ao sistema. No entanto, a pendência não foi resolvida e o cliente foi orientado a entrar em contato com o setor responsável para solução.",
    17: "17 Solicitação - Erro Impressora de Cupom Fiscal: O cliente solicitou assistência devido a um erro na impressora de cupom fiscal. Foi necessário intervir e fornecer suporte técnico para identificar e resolver as questões relacionadas ao problema da impressora.",
    18: "18 Solicitação - Erro Impressora de Etiquetas: O cliente solicitou assistência devido a um erro na impressora de etiquetas. Foi necessário intervir e fornecer suporte técnico para identificar e resolver as questões relacionadas ao problema da impressora de etiquetas.",
    19: "19 Solicitação - Informações do Sistema: O cliente solicitou informações sobre o sistema. O cliente foi orientado e fornecido com as informações do sistema solicitadas.",
}

# Criação da interface do menu
root = tk.Tk()
root.resizable(width=False, height=False)  
root.title("Ticket Help")
root.geometry("300x800")

label = tk.Label(root, text="Selecione o Motivo")
label.pack()

# Criação dos botões do menu
for num, texto in textos.items():
    motivo_resumido = texto.split(":")[0].strip()  # Obtém apenas o motivo resumido

    # Função de callback para o botão
    def callback(numero=num):
        selecionar_texto(numero)

    button = tk.Button(root, text=motivo_resumido, command=callback)
    button.pack()


# Lista de opções de 1 a 19
opcoes_tipo_atendimento = list(range(1, 20))

# Variável para armazenar o tipo de atendimento selecionado
tipo_atendimento_var = tk.IntVar(root)
tipo_atendimento_var.set(opcoes_tipo_atendimento[0])  # Valor padrão

# Criação do menu suspenso para o tipo de atendimento
tipo_atendimento_option_menu = tk.OptionMenu(root, tipo_atendimento_var, *opcoes_tipo_atendimento)
tipo_atendimento_option_menu.pack()

# Adicione um rótulo e uma entrada para o Nome do Cliente
nome_cliente_label = tk.Label(root, text="Nome do Cliente:")
nome_cliente_label.pack()

nome_cliente_entry = tk.Entry(root)
nome_cliente_entry.pack()

# Adicione um rótulo e uma entrada para o CNPJ da Empresa
cnpj_empresa_label = tk.Label(root, text="CNPJ da Empresa:")
cnpj_empresa_label.pack()

cnpj_empresa_entry = tk.Entry(root)
cnpj_empresa_entry.pack()


# Adicione um rótulo e uma entrada para o Número de Telefone do Cliente
telefone_cliente_label = tk.Label(root, text="Telefone do Cliente:")
telefone_cliente_label.pack()

telefone_cliente_entry = tk.Entry(root)
telefone_cliente_entry.pack()

# Botão para registrar o atendimento
registrar_button = tk.Button(root, text="Registrar Atendimento", command=registrar_atendimento)
registrar_button.pack()

root.mainloop()
