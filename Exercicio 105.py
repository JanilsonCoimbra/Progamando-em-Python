def notas(*n, sit=False):
    """
    \033[33mFunção que recebe notas dos alunos e retorna uma analise e sua situação\033[m
    :param n: notas dos alunos separados por virgula
    :param sit: Valor bool para mostrar se a situação do aluno é boa ou ruim
    :return: retorna um dicionário com informações
    """
    aluno = dict()
    aluno["Total"] = len(n)
    aluno["MaiorNota"] = max(n)
    aluno["MenorNota"] = min(n)
    aluno["media"] = sum(n)/len(n)
    if sit == True:
        if aluno["media"] >= 7:
            aluno["sit"] = 'BOM'
        else:
            aluno["sit"] = 'RUIM'
    print(aluno)


notas(10, 3, 10, 7, sit=True)
