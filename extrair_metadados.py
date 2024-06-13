import os
import subprocess

def obter_metadados(caminho_pasta):
    try:
        subprocess.run(["exiftool"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        print("ExifTool não está instalado ou não está no PATH do sistema.")
        return

    if not os.path.isdir(caminho_pasta):
        print(f"O caminho especificado '{caminho_pasta}' não é uma pasta válida.")
        return

    arquivo_saida = os.path.join(caminho_pasta, "metadados.txt")

    arquivos = os.listdir(caminho_pasta)

    with open(arquivo_saida, "w", encoding="utf-8") as f_saida:
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(caminho_pasta, arquivo)
            if os.path.isfile(caminho_arquivo):
              
                resultado = subprocess.run(["exiftool", caminho_arquivo], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                
                f_saida.write(f"Arquivo: {arquivo}\n")
                f_saida.write(resultado.stdout)
                f_saida.write("\n" + "="*40 + "\n\n")

    print(f"Metadados extraídos e salvos em '{arquivo_saida}'")

if __name__ == "__main__":
    caminho_pasta = input("Digite o caminho para a pasta: ")
    obter_metadados(caminho_pasta)


