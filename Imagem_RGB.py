def inserirImagem(arquivo):
    with open(arquivo, 'r') as f:
        cabecalho = f.readline().strip()
        dimensoes = f.readline().strip()
        maiorvalor = int(f.readline().strip())
        cabecalho = cabecalho.replace("P3", "P2")
        pixels = []
        for line in f:
            pixels.extend(map(int, line.split()))
    largura, altura = map(int, dimensoes.split())
    return cabecalho, largura, altura, maiorvalor, pixels

def write_pgm(arquivo, cabecalho, largura, altura, maiorvalor, pixels):
    with open(arquivo, 'w') as f:
        f.write(f"{cabecalho}\n{largura} {altura}\n{maiorvalor}\n")
        for i in range(altura):
            f.write(" ".join(map(str, pixels[i * largura:(i + 1) * largura])) + "\n")

def resize_image(pixels):
    new_pixels = []
    k = 0
    soma = 0
    for pixel in pixels:
        k+= 1
        soma += pixel
        if(k == 3):
            k = 0
            new_pixel = (soma/3)
            new_pixels.append(new_pixel)
            soma = 0

    return new_pixels

def resize_and_save(input_arquivo, output_arquivo):
    cabecalho, largura, altura, maiorvalor, pixels = inserirImagem(input_arquivo)
    new_pixels = resize_image(pixels)
    write_pgm(output_arquivo, cabecalho, largura, altura, maiorvalor, new_pixels)

# Entrando com a imagem inicial
arquivo_entrada = 'c:/Users/jukal/Desktop/Imagem RGB/Fig1.ppm'

resize_and_save(arquivo_entrada, 'c:/Users/jukal/Desktop/Imagem RGB/Imagem_Cinza.pgm')
