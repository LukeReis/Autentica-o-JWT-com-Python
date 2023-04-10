# Autenticacao-JWT-com-Python
Esse é um pequeno exemplo de como implementar um sistema de autenticação com JWT (JSON Web Token) 
utilizando a biblioteca PyJWT em conjunto com a biblioteca gráfica PySimpleGUI.

# Requisitos
Python 3.x

PySimpleGUI

PyJWT

# Como usar
Clone este repositório ou faça o download do arquivo main.py.

Instale as dependências necessárias utilizando o gerenciador de pacotes pip: pip install PySimpleGUI PyJWT.

Execute o arquivo main.py em seu terminal ou IDE de escolha.

# Funcionamento
Ao executar o programa, uma janela será aberta com três opções: "Login", "Salvar Cadastro" e "Fechar".

# Salvar Cadastro
Ao clicar em "Salvar Cadastro", será aberto um formulário para que o usuário informe seu login e senha. 
Esses dados serão armazenados em um dicionário token_dic, juntamente com um token gerado a partir da biblioteca JWT.

# Login
Ao clicar em "Login", será aberto um formulário para que o usuário informe seu login e senha. 
Caso o login não esteja presente no dicionário token_dic, uma mensagem informando que não há usuário cadastrado será exibida. 
Caso o login exista, o programa tentará decodificar o token gerado anteriormente com base na senha informada. 
Caso a decodificação seja bem sucedida, uma mensagem de autenticação bem sucedida será exibida, juntamente com as informações contidas no token. 
Caso ocorra algum erro na decodificação do token, uma mensagem de erro será exibida.
