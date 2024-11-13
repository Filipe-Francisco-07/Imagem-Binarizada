def inserirImagem(arquivo):
    with open(arquivo, 'r') as f:
        cabecalho = f.readline().strip()
        dimensoes = f.readline().strip()
        maiorvalor = int(f.readline().strip())
        pixels = []
        for line in f:
            pixels.extend(map(int, line.split()))
    largura, altura = map(int, dimensoes.split())
    return cabecalho, largura, altura, maiorvalor, pixels

def write_ppm(arquivo, cabecalho, largura, altura, maiorvalor, pixels):
    with open(arquivo, 'w') as f:
        f.write(f"{cabecalho}\n{largura} {altura}\n{maiorvalor}\n")
        for i in range(altura):
            f.write(" ".join(map(str, pixels[i * largura * 3:(i + 1) * largura * 3])) + "\n")

def resize_image_rgb(pixels):
    new_pixels = []
    for i in range(0, len(pixels), 3):
        r, g, b = pixels[i], pixels[i + 1], pixels[i + 2]
        new_pixels.extend([r, g, b])

    return new_pixels

def resize_and_save(input_arquivo, output_arquivo):
    cabecalho, largura, altura, maiorvalor, pixels = inserirImagem(input_arquivo)
    new_pixels = resize_image_rgb(pixels)
    write_ppm(output_arquivo, cabecalho, largura, altura, maiorvalor, new_pixels)

# Entrando com a imagem inicial
arquivo_entrada = 'c:/Users/jukal/Desktop/Imagem RGB/Fig4.ppm'
resize_and_save(arquivo_entrada, 'c:/Users/jukal/Desktop/Imagem RGB/Imagem_RGB_Media.ppm')
