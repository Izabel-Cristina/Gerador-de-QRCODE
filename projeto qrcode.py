#Importando bibliotecas
import qrcode 
from PIL.Image import core as image
import PySimpleGUI as sg
#interface
sg.theme('DarkGrey11')
layout = [
          [sg.Text('Informe o nome do arquivo: ')],
          [sg.InputText(key ='nome_arquivo' )],
          [sg.Text('Informe o link')],
          [sg.InputText(key = 'link_arquivo')],
          [sg.Button('Gerar QRCode')]
          ]
janela = sg.Window("Emissor de QRCode: ",layout)
while True:
  event, values = janela.read()
  if event == sg.WIN_CLOSED:
    break
  try:
    if event == 'Gerar QRCode':
#Entrada de informação dada pelo usuario
      arquivo = values['nome_arquivo']
      link = values['link_arquivo']
      link_qrcode = qrcode.make(link)
#Salvando QRcode em imagem
      link_qrcode.save('{}.png'.format(arquivo))
# Em caso de erro
  except:
    erro = 'Erro'
    janela['link_arquivo'].update(f'{erro}')