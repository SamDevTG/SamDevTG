import imageio
import os
from PIL import Image, ImageDraw, ImageFont

# Função para desenhar texto no terminal
def draw_text(draw, text, position, font, color=(255, 255, 255)):
    draw.text(position, text, font=font, fill=color)

# Função para criar uma nova imagem para cada frame do GIF
def create_frame(text_lines, image, font):
    frame = Image.new('RGB', (800, 400), color=(0, 0, 0))
    draw = ImageDraw.Draw(frame)

    y_text = 20
    for line in text_lines:
        draw_text(draw, line, (20, y_text), font)
        y_text += 40

    # Adicionar a imagem do gato com a bandeira trans
    frame.paste(image, (500, 50))

    return frame

# Configuração
frames = []
font = ImageFont.truetype("arial.ttf", 20)
cat_image_path = "Scripts/trans_cat.png"
cat_image = Image.open(cat_image_path).resize((200, 200))
total_frames = 30

# Texto a ser exibido
text = [
    "Welcome to My Terminal!",
    "",
    "Name: Sam",
    "Age: 18 years old",
    "Pronouns: she/her",
    "Company: Winestone",
    "Position: Intern",
]

# Gerar frames para o GIF
for frame_num in range(total_frames):
    frame_text = text[:frame_num // 5]
    frame = create_frame(frame_text, cat_image, font)
    frames.append(frame)

# Salvar GIF
output_path = "output.gif"
imageio.mimsave(output_path, frames, duration=0.1)

print(f"GIF saved to {output_path}")
