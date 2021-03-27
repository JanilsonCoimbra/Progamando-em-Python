def notas(*n, sit=False):
    """
    \033[33mFunção que recebe notas dos alunos e retorna uma analise e sua situação\033[m
    :param n: notas dos alunos separados por virgula
    :param sit: Valor bool para mostrar se a situação do aluno é boa ou ruim
    :return: retorna um dicionário com informações
    """
    maior = menor = cont = TotSomaNotas = 0
    aluno = dict()
    aluno["total"] = len(n)
    for notas in n:
        if cont == 0:
            menor = notas
        if notas > maior:
            maior = notas
        if menor > notas:
            menor = notas
        TotSomaNotas += notas
        cont += 1
    aluno["MaiorNota"] = maior
    aluno["MenorNota"] = menor
    aluno["media"] = TotSomaNotas / aluno["total"]
    if sit == True:
        if aluno["media"] >= 7:
            aluno["sit"] = 'BOM'
        else:
            aluno["sit"] = 'RUIM'
    print(aluno)


notas(10 ,3 ,10 ,7 ,6 ,8 ,4 ,10, sit=True )
