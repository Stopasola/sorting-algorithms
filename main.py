import codes

classes = 1
arquivos = 1
algoritmos = 1


vetorArquivo = []
vetorClasses = []
vetor = []
for i in range(0, classes):
    for j in range(0, arquivos):

        nomeArq = str(vetorClasses[i]) + str(vetorArquivo[j]) +'.txt'
        print(nomeArq, end="")
        arqAbre = open(nomeArq, 'r')
        texto = arqAbre.readlines()

        for linha in texto:
            vetor.append(int(linha))

        for k in range(0, algoritmos):
            Resultados = []
            k=5
            if k == 0:
                compara, swap, tempo = Codes.Bubble(vetor)
                Codes.Bubble(vetor)
                Resultados.append(str(compara) + " ")
                Resultados.append(str(swap) + " ")
                Resultados.append(str(tempo) + " ")
                Resultados.append(nomeArq)
                Resultados.append('\n')
                arqSalva = open("Bubbe.txt", 'a')
                arqSalva.writelines(Resultados)
                print(" Executou Buble ", end="")
            if k == 1:
                compara, swap, tempo = Codes.Selection(vetor)
                #Codes.Bubble(vetor)
                '''Resultados.append('Compara ')
                Resultados.append('Swap ')
                Resultados.append('tempo ')'''
                Resultados.append(str(compara) + " ")
                Resultados.append(str(swap) + " ")
                Resultados.append(str(tempo) + " ")
                Resultados.append(nomeArq)
                Resultados.append('\n')
                arqSalva = open("Selection.txt", 'a')
                arqSalva.writelines(Resultados)
                print("Executou Selection ", end="")
            if k == 2:
                compara, swap, tempo = Codes.Insertion(vetor)
                '''Resultados.append('Compara ')
                Resultados.append('Swap ')
                Resultados.append('tempo ')'''
                Resultados.append(str(compara) + " ")
                Resultados.append(str(swap) + " ")
                Resultados.append(str(tempo) + " ")
                Resultados.append(nomeArq)
                Resultados.append('\n')
                arqSalva = open("Insertion.txt", 'a')
                arqSalva.writelines(Resultados)
                print("Executou Insertion ", end="")
            if k == 3:
                compara, swap, tempo = Codes.MergeSort(vetor)
                '''Resultados.append('Compara ')
                Resultados.append('Swap ')
                Resultados.append('tempo ')'''
                Resultados.append(str(compara) + " ")
                Resultados.append(str(swap) + " ")
                Resultados.append(str(tempo) + " ")
                Resultados.append(nomeArq)
                Resultados.append('\n')
                arqSalva = open("MergeSort.txt", 'a')
                arqSalva.writelines(Resultados)
                print("Executou MergeSort ", end="")
            if k == 4:
                compara, swap, tempo = Codes.QuickSort(vetor)
                '''Resultados.append('Compara ')
                Resultados.append('Swap ')
                Resultados.append('tempo ')'''
                Resultados.append(str(compara) + " ")
                Resultados.append(str(swap) + " ")
                Resultados.append(str(tempo) + " ")
                Resultados.append(nomeArq)
                Resultados.append('\n')
                arqSalva = open("QuickSort.txt", 'a')
                arqSalva.writelines(Resultados)
                print("Executou QuickSort ", end="")
            if k == 5:
                compara, swap, tempo = Codes.CountSort(vetor)
                '''Resultados.append('Compara ')
                Resultados.append('Swap ')
                Resultados.append('tempo ')'''
                Resultados.append(str(compara) + " ")
                Resultados.append(str(swap) + " ")
                Resultados.append(str(tempo) + " ")
                Resultados.append(nomeArq)
                Resultados.append('\n')
                arqSalva = open("CountSort.txt", 'a')
                arqSalva.writelines(Resultados)
                print("Executou CountSort ", end="")
            if k == 6:
                compara, swap, tempo = Codes.Bucket_sort(vetor)
                '''Resultados.append('Compara ')
                Resultados.append('Swap ')
                Resultados.append('tempo ')'''
                Resultados.append(str(compara) + " ")
                Resultados.append(str(swap) + " ")
                Resultados.append(str(tempo) + " ")
                Resultados.append(nomeArq)
                Resultados.append('\n')
                arqSalva = open("Bucket_sort.txt", 'a')
                arqSalva.writelines(Resultados)
                print("Executou Bucket_sort ")

            del Resultados
