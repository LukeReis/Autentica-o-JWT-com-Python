import jwt
import PySimpleGUI as sg

token_dic = {} #dicionario para armazenar os tokens dos usuarios cadastrados


def criar_token(login, senha):
    payload = {'username': login, 'role': 'admin'}
    secret_key = senha.encode('utf-8')
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return (token)


sg.theme('Reddit')

layout = [
    [sg.Text('Usuario'), sg.InputText('', key='login')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Text('', key='aviso')],
    [sg.Button('Login'), sg.Button('Salvar Cadastro'), sg.Button('Fechar')]
]

janela = sg.Window('Autenticaçao Usuario', layout)


while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED or eventos == 'Fechar':
        break

    if eventos == 'Salvar Cadastro':
        login_user = valores['login']
        senha_user = valores['senha']
        token_dic[login_user] = criar_token(login_user, senha_user)
        janela['aviso'].Update('Usuario Cadastrado!')

    if eventos == 'Login':
        login_user = valores['login']
        if login_user not in token_dic:
            janela['aviso'].Update('Nenhum usuario cadastrado')
        else:
            try:
                token = token_dic[login_user]
                secret_key = valores['senha'].encode('utf-8')
                payload = jwt.decode(token, secret_key, algorithms=['HS256'])
                janela['aviso'].Update(f'Autenticação bem sucedida. {payload}')
            except jwt.exceptions.ExpiredSignatureError:
                janela['aviso'].Update('Token expirado')
            except jwt.exceptions.InvalidSignatureError:
                janela['aviso'].Update('Assinatura Inválida')
            except jwt.exceptions.InvalidTokenError:
                janela['aviso'].Update('Token inválido')

janela.close()