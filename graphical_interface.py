import PySimpleGUI as sg

class TelaPython:
    def __init__(self):

        sg.change_look_and_feel('DarkBlue15')

        layout = [
            [sg.Text('Planilha de Pré-Instalação:')],
            [sg.Input(key='planilha')],
            [sg.Checkbox('Enviar credenciais para email específico?', default=False, key='checkbox1')],
            [sg.Input(key='email')],
            [sg.Button('Ok')]
        ]
        window = sg.Window('3CX Extension Creator - By Michatec').layout(layout)
        self.event,self.values = window.read()
    

        
                         
    def Iniciar(self):
        global planilha_pre
        global email_envio
        global checkbox_email
        planilha_pre=self.values['planilha']
        email_envio=self.values['email']
        checkbox_email=self.values['checkbox1']
        

        #print(f'xlsx: {planilha_pre}')
        #print(f'extension: {email_envio}')
        #print(checkbox_email)
        
        
        

tela = TelaPython()
tela.Iniciar()