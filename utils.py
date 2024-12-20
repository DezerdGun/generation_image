import random
import os
from PIL import Image

# Функция для генерации случайного цвета
def generate_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Функция для выбора случайного шрифта
def choose_random_font():
    font_dirs = [
        "/usr/share/fonts",  # для Linux
        "/Library/Fonts",  # для macOS
        "C:\\Windows\\Fonts",  # для Windows
    ]

    fonts = []
    for font_dir in font_dirs:
        if os.path.exists(font_dir) and os.path.isdir(
                font_dir):  # Проверка, существует ли путь и является ли директорией
            for font_file in os.listdir(font_dir):
                font_path = os.path.join(font_dir, font_file)
                # Если это директория, ищем шрифты в ней
                if os.path.isdir(font_path):
                    for subfont_file in os.listdir(font_path):
                        subfont_path = os.path.join(font_path, subfont_file)
                        if subfont_file.endswith(".ttf") or subfont_file.endswith(".otf"):
                            fonts.append(subfont_path)
                elif font_file.endswith(".ttf") or font_file.endswith(".otf"):
                    # Если файл шрифт
                    fonts.append(font_path)

    if fonts:
        random_font = random.choice(fonts)
        if os.path.exists(random_font):
            return random_font
        else:
            print(f"Шрифт не найден: {random_font}")
    else:
        print("Шрифты не найдены в указанных директориях.")

    return "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Дефолтный шрифт


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
# def draw_person(draw, x, y):
#     # Рисуем голову
#     head_radius = 30
#     draw.ellipse((x - head_radius, y - head_radius, x + head_radius, y + head_radius), outline="black", width=3)
#
#     # Рисуем тело
#     body_height = 60
#     draw.line((x, y + head_radius, x, y + head_radius + body_height), fill="black", width=3)
#
#     # Рисуем руки
#     arm_length = 40
#     draw.line((x - arm_length, y + head_radius + 20, x + arm_length, y + head_radius + 20), fill="black", width=3)
#
#     # Рисуем ноги
#     leg_length = 50
#     draw.line((x, y + head_radius + body_height, x - 20, y + head_radius + body_height + leg_length), fill="black", width=3)
#     draw.line((x, y + head_radius + body_height, x + 20, y + head_radius + body_height + leg_length), fill="black", width=3)
