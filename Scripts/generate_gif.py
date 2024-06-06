import imageio
from datetime import datetime, time
from PIL import Image, ImageDraw, ImageFont

# Função para imprimir texto de forma animada no terminal
def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)

# Função para gerar o GIF animado
def generate_terminal_gif():
    # Configurações do terminal
    terminal_width = 800
    terminal_height = 500
    font_size = 15
    font_color = (255, 255, 255)  # Cor da fonte (branca)
    background_color = (0, 0, 0)  # Cor de fundo (preta)

    # Lista de quadros do GIF
    frames = []

    # Texto a ser exibido no terminal
    text = """
    Welcome to My Terminal!

    Name: Sam
    Age: 18 years old
    Pronouns: she/her
    Company: Winestone
    Position: Intern

    Press any key to exit...
    """

    # Criação dos quadros do GIF
    for char in text:
        # Criação de uma nova imagem com o tamanho do terminal
        image = Image.new("RGB", (terminal_width, terminal_height), color=background_color)
        draw = ImageDraw.Draw(image)

        # Carrega a fonte
        font = ImageFont.truetype("./fonts/gohufont-uni-14.pil", font_size)

        # Desenha o texto na imagem
        draw.text((15, 15), text, font=font, fill=font_color)

        # Converte a imagem para o formato correto
        frame = image.convert('RGB')

        # Adiciona o quadro à lista de quadros
        frames.append(frame)

    # Salva a lista de quadros como um GIF
    imageio.mimsave('output.gif', frames, duration=0.05)

if __name__ == "__main__":
    generate_terminal_gif()
