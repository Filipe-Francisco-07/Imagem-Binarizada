def inserirImagem(arquivo):
    with open(arquivo, 'r') as f:
        cabecalho = f.readline().strip()
        dimensoes = f.readline().strip()
        maiorvalor = int(f.readline().strip())
        cabecalho = cabecalho.replace("P2","P1")
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

def resize_image(pixels,limiar):
    new_pixels = []
    for pixel in pixels:
        if(pixel <= limiar):
            new_pixel = 0
            new_pixels.append(new_pixel)
        elif(pixel > limiar):
            new_pixel = 255
            new_pixels.append(new_pixel)
    return new_pixels

def resize_and_save(input_arquivo, output_arquivo):
    cabecalho, largura, altura, maiorvalor, pixels = inserirImagem(input_arquivo)
    limiar = 128
    new_pixels = resize_image(pixels,limiar)
    write_pgm(output_arquivo, cabecalho, largura, altura, maiorvalor, new_pixels)

# Entrando com a imagem inicial
arquivo_entrada = 'Entrada_EscalaCinza.pgm' 

# Criando imagem 20% de brilho
resize_and_save(arquivo_entrada, 'Entrada_EscalaCinza_Binarizada.pgm')
