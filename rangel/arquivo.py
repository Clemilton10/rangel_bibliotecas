def ler_arquivo(arquivo) -> str:
    try:
        f = open(arquivo, 'r', encoding='utf8')
        t = f.read()
        f.close()
        return t
    except Exception as er:
        print('ler_arquivo:')
        print(er)
        return ''

def salvar_arquivo(arquivo, texto):
    try:
        f = open(arquivo, 'w', encoding='utf8')
        f.writelines(texto)
        f.close()
    except Exception as er:
        print('salvar_arquivo:')
        print(er)