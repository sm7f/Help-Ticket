import tkinter as tk
import win32clipboard

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

# Textos pré-definidos
textos = {
    1:  "Solicitação - Erro Abertura do Sistema:  O cliente solicitou assistência para investigar as possíveis causas que impedem a abertura do sistema. Foi necessário intervir e fornecer suporte técnico para identificar e resolver as questões relacionadas ao problema mencionado.",
    2:  "Solicitação - Vinculação de certificado digital:  O cliente solicitou assistência para vincular o seu certificado digital ao sistema. Foi necessário intervir e fornecer suporte técnico para auxiliar o cliente no processo de vinculação do certificado digital ao sistema.",
    3:  "Solicitação - Erro Ao abrir o Sistema: O cliente solicitou assistência para investigar as possíveis causas de um erro ocorrido durante a impressão de um cupom fiscal. Foi necessário intervir e fornecer suporte técnico para identificar e resolver as questões relacionadas ao referido erro.",
    4:  "Solicitação - Auxilio NFC-e: O cliente buscou nossa assistência para obter suporte na emissão de uma Nota Fiscal de Consumidor Eletrônica (NFC-e). Foi necessário intervir e prestar auxílio ao cliente no processo de emissão da referida NFC-e.",
    5:  "Solicitação - Auxilio NF-e: O cliente solicitou suporte para a emissão de uma Nota Fiscal Eletrônica (NF-e). Foi necessário intervir e fornecer assistência para auxiliar o cliente no processo de emissão da referida NFe.",
    6:  "Solicitação - Auxilio NF-e Devolução: O cliente fez uma solicitação de assistência para emissão de uma nota de devolução. Foi requerida nossa intervenção a fim de fornecer orientação e suporte nesse processo.",
    7:  "Solicitação - Auxilio NF-e Remessa: O cliente fez uma solicitação de assistência para emissão de uma nota de Remessa. Foi requerida nossa intervenção a fim de fornecer orientação e suporte nesse processo.",
    8:  "Solicitação - Auxilio NF-e Entrada: O cliente fez uma solicitação de assistência para emissão de uma nota de Entrada. Foi requerida nossa intervenção a fim de fornecer orientação e suporte nesse processo.",
    9:  "Solicitação - Auxilio NF-e Troca: O cliente fez uma solicitação de assistência para emissão de uma nota de Troca. Foi requerida nossa intervenção a fim de fornecer orientação e suporte nesse processo.",
    10: "Solicitação - Erro Extrair XML: O cliente solicitou assistência para investigar as possíveis causas de um erro ocorrido ao extrair um arquivo XML. Foi necessário intervir e fornecer suporte técnico para identificar e resolver as questões relacionadas ao referido erro.",
    11: "Solicitação - Auxilio Extrair XML: O cliente solicitou assistência para extrair o arquivo XML referente ao mês em questão. Foi necessário intervir e fornecer suporte técnico para auxiliar o cliente no processo de extração do referido arquivo XML. ",
    12: "Solicitação - Auxilio Cancelar Nota: O cliente solicitou assistência para realizar o cancelamento de uma nota fiscal. Foi necessário intervir e fornecer suporte para auxiliar o cliente no processo de cancelamento da referida nota. ",
    13: "Solicitação - Auxilio Visualizar Relatório: O cliente solicitou assistência para visualizar o relatório solicitado. Foi necessário intervir e fornecer suporte técnico para auxiliar o cliente no processo de acesso e visualização do referido relatório."
}

# Criação da interface do menu
root = tk.Tk()
root.resizable(width=False, height=False)  
root.title("Ticket Help")
root.geometry("300x400")

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

root.mainloop()
