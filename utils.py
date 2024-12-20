import random
import os
from PIL import Image

# Функция для генерации случайного цвета
def generate_random_color():
    return tuple(random.randint(0, 255) for _ in range(3))

# Функция для выбора случайного шрифта
def choose_random_font():
    font_dirs = [
        "/usr/share/fonts",  # для Linux
        "/Library/Fonts",  # для macOS
        "C:\\Windows\\Fonts",  # для Windows
    ]

    fonts = []
    for font_dir in font_dirs:
        if os.path.exists(font_dir):
            for font_file in os.listdir(font_dir):
                if font_file.endswith(".ttf") or font_file.endswith(".otf"):
                    fonts.append(os.path.join(font_dir, font_file))

    if fonts:
        return random.choice(fonts)
    else:
        return "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Дефолтный шрифт, если ничего не найдено

# Функция для создания градиентного фона
def create_gradient_background(width, height):
    start_color = generate_random_color()
    end_color = generate_random_color()

    gradient = Image.new('RGB', (width, height), start_color)
    for y in range(height):
        ratio = y / height
        r = int(start_color[0] * (1 - ratio) + end_color[0] * ratio)
        g = int(start_color[1] * (1 - ratio) + end_color[1] * ratio)
        b = int(start_color[2] * (1 - ratio) + end_color[2] * ratio)
        for x in range(width):
            gradient.putpixel((x, y), (r, g, b))
    return gradient

# Функция для рисования схематичного человека
def draw_person(draw, x, y):
    # Рисуем голову
    head_radius = 30
    draw.ellipse((x - head_radius, y - head_radius, x + head_radius, y + head_radius), outline="black", width=3)

    # Рисуем тело
    body_height = 60
    draw.line((x, y + head_radius, x, y + head_radius + body_height), fill="black", width=3)

    # Рисуем руки
    arm_length = 40
    draw.line((x - arm_length, y + head_radius + 20, x + arm_length, y + head_radius + 20), fill="black", width=3)

    # Рисуем ноги
    leg_length = 50
    draw.line((x, y + head_radius + body_height, x - 20, y + head_radius + body_height + leg_length), fill="black", width=3)
    draw.line((x, y + head_radius + body_height, x + 20, y + head_radius + body_height + leg_length), fill="black", width=3)
