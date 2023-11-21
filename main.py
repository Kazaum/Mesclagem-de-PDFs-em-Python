import PyPDF2
import os

#Usuário escolhe o nome que deseja no arquivo final
nome = input("Escolha um nome para o PDF final: ")
final = f"{nome}.pdf"

#Criar a mesclagem dos PDFs atraves do PyPDF2 e selecionar os arquivos que deseja mesclar
mescla = PyPDF2.PdfMerger()
lista_arquivos = os.listdir("arquivos") #lista os arquivos de forma alfabetica
lista_arquivos.sort() #ordena os arquivos
print(lista_arquivos)

#Percorrer os arquivos e encontrar os PDFs para mesclar
for arquivo in lista_arquivos:
    if ".pdf" or ".PDF" in arquivo:
        mescla.append(f"arquivos/{arquivo}") #mescla o arquivo encontrado
        print(f"{arquivo} adicionado à mescla")

#Seleciona o nome que o usuário escolheu ao PDF final
mescla.write(final)
print("Seu arquivo PDF foi criado com sucesso!")