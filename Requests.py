import requests

# faz uma requisição GET para o site do Google
response = requests.get('https://www.google.com')

# imprime o código de status da resposta
print(response.status_code)

# imprime o conteúdo da resposta
print(response.content)