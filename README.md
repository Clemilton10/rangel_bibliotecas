# Rangel

**Rangel** é um conjunto de bibliotecas em português para facilitar o dia a dia.

### Importação total
~~~python
from rangel import * # Importa todos os módulos<br>
texto = arquivo.ler_arquivo('arquivo_texto.txt') # Chama a função
~~~

### Importação parcial
~~~python
from rangel.arquivo import ler_arquivo # Importa o módulo<br>
texto = ler_arquivo('arquivo.txt') # Chama a função
~~~

### rangel.arquivo
~~~python
texto = ler_arquivo('arquivo.txt') # A função lê um arquivo e devolve o texto<br>
salvar_arquivo('arquivo.txt', texto) # A função salva o texto no arquivo
~~~

### rangel.data_hora
~~~python
ds = dia_semana('sunday') # A função converte um dia da semana em inglês em português<br>
de = data_extenso('01/01/2001') # A função converte uma data para o formato extenso: dia 01 de Janeiro de 2001
~~~

### rangel.db_sqlite
~~~python
db = db_sqlite() # Chama a classe<br>
db.conectar('arquivo_sqlite.db') # Conecta a um arquivo/banco de dados SQLite<br>
lista = db.query('select * from clientes') # Faz a consulta na tabela e retorna uma lista<br>
colunas = db.colunas # Logo que for feita uma consulta, é possível obter uma lista com os nomes das colunas<br>
~~~

### rangel.dicionario
~~~python
dicionario = ordem(dicionario, 'nome') # Ordena um dicionário por uma coluna<br>
ler_json('arquivo.json') # Lê um arquivo json e converte para dicionário<br>
salvar_json('arquivo.json', dicionario) # Salva um dicionário em arquivo json
~~~

### rangel.executar
~~~python
executar('C:/programa.exe parametro1 parametro2 ...') # Executa um programa externo em paralelo (Thead)<br>
outraRota(calcular, parametro1, parametro2, ... ) # Executa uma função em paralelo (Thead)
~~~

### rangel.mysqli
~~~python
m = mysqli() # Chama a classe MSQLi
carregar_configuracoes() # Lê o arquivo de configuração mysqli_configuracoes.json que deve estar na mesma pasta do projeto e conter as seguintes configurações:
{
    "host": "localhost",
    "user": "usuario",
    "passwd": "senha",
    "database": "banco_de_dados"
}

m.conectar() # Conecta ao banco de dados
dicionario = m.squery('select * from clientes') # Faz uma consulta e retorna um dicionário contendo 4 objetos:
-- sql » string
-- colunas » lista
-- linhas » lista
-- sucesso » Boolean

qr = equery("insert into clientes(nome,email) values ('José Ambrósio','joseamb@gmail.com')") # executa uma query e retorna 2 objetos:
-- sql » string
-- sucesso » Boolean

qr = vquery('INSERT INTO usuario (nome, email) VALUES (%s, %s)', ('José Ambrósio','joseamb@gmail.com') ) # executa uma query e retorna 3 objetos:
-- sql » string
-- valores » dicionário
-- sucesso » Boolean

m.fechar_cursor() # fecha o cursor<br>
m.fechar_db() # fecha a conexão
~~~

### rangel.robo
~~~python
### Bibliotecas obrigatórias ###
python -m pip install Pillow<br>
python -m pip install opencv-python<br>

### FUNÇÔES ###
r = robo() # Chama a classe
r.tempo(5) # Aguarda 5 segundos
r.tempo_voz(5) # Aguarda 5 segundos e fala cada segundo
r.falar('texto para falar') # Fala o texto
r.teclar('win', '2') # Aperta e solta uma combinação de teclas
r.pressionar('enter') # Pressiona e solta uma tecla
r.digitar('http://www.google.com.br') # Digita um texto
r.posicao_imagem('imagem.png') # Busca a posição central de uma imagem na tela
r.mover(500, 300) # Move o mouse (x, y)
r.mover_clicar(500, 300) # Move o mouse e clica com botão esquerdo (x, y)
r.clicar(500, 300) # Clica com botão esquerdo
r.clicar_direito(500, 300) # Clica com botão direito
p = r.posicao(5) # Espera e segundos e vai avisando a cada segundo
r.ap_bt_esquerdo() # Aperta e segura o botão esquerdo do mouse
r.st_bt_esquerdo() # Solta o botão esquerdo do mouse
r.ap_bt_direito() # Aperta e segura o botão direito do mouse
r.st_bt_direito() # Solta o botão direito do mouse
r.capturar_click() # Captura a posição do click do botão esquerdo do mouse
p = r.xy # Pega a lista de posições [x, y] armazenda através da função anterior
~~~

### rangel.formatar
~~~python
t = formatar('O rato, roeu a ROUPA do rei de Roma? 123', dicionario) # Formata o texto de acordo com as epecificações passadas no segundo parâmetro (dicionário), ele pode conter as seguintes expecificações:
{
    "tirarLetras": 1,
    "manterAcentos": 1,
    "maiusculo": 1,
    "manterCaracteres": "/*-+ ",
    "minusculo": 1,
    "tirarNumeros": 1
}
# O exemplo abaixo retornaria:
{
    "maiusculo": 1,
    "manterCaracteres": " ",
    "tirarNumeros": 1
}
# Resultado: t = O RATO ROEU A ROUPA DO REI DE ROMA

n = texNum('nove') # Converte um número em extenso para número
# Resultado: n = 9

t = limpar('O rato, roeu a ROUPA do rei de Roma 123') # limpa as seguintes conjuções:
- e
- a
- o
- as
- os
- do
- da
- de
- no
- na
- em
# Resultado: t = RATO, ROEU ROUPA REI ROMA 123

p = comparar('todo mundo tá aqui', 'todo mundo quer ir') # compara palavra por palavra de duas strings
# Resultado: p = 50 (%)
~~~

### rangel.verificar_py
~~~python
v = verificar('arquivo.py') # verifica se um arquivo py está em execução retornando um valor Boolean
~~~

### rangel.medidas
~~~python
m = medidas()
h = m.coordenadas_hipotenusa(x1, y1, x2, y2) # Calcula a hipotenusa de duas coordenadas
h = m.catetos_hipotenusa(cateto_adjacente, cateto_oposto) # Calcula a hipotenusa de dois catetos
a = m.coordenadas_area(x1, y1, x2, y2) # Calcula a área de duas coordenadas
a = m.catetos_area(cateto_adjacente, cateto_oposto) # Calcula a área de dois catetos
a = m.raio_area(raio) # Calcula a área de um raio
c = m.raio_circunferencia(raio) # Calcula a circunferência de um raio
r = m.area_raio(area) # Calcula um raio de uma área
r = m.circunferencia_raio(circunferencia) # Calcula um raio de uma circunferência
~~~