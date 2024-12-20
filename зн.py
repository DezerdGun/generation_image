from PIL import Image, ImageDraw, ImageFont
import random
import os


def generate_brand_name(keywords):
    suffixes = ["Tech", "Corp", "Design", "Studio", "Wave"]
    random_suffix = random.choice(suffixes)
    return f"{keywords.title()} {random_suffix}"


def generate_random_color():
    return tuple(random.randint(0, 255) for _ in range(3))


def choose_random_font():
    # Путь к шрифтам на вашей системе (на Linux может быть по-другому)
    font_dirs = [
        "/usr/share/fonts",  # для Linux
        "/Library/Fonts",  # для macOS
        "C:\\Windows\\Fonts",  # для Windows
    ]

    # Проходим по всем директориям с шрифтами
    fonts = []
    for font_dir in font_dirs:
        if os.path.exists(font_dir):
            for font_file in os.listdir(font_dir):
                if font_file.endswith(".ttf") or font_file.endswith(".otf"):
                    fonts.append(os.path.join(font_dir, font_file))

    # Выбираем случайный шрифт из доступных
    if fonts:
        return random.choice(fonts)
    else:
        return "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Дефолтный шрифт, если ничего не найдено


def create_and_save_brand_image(brand_name, output_path="brand_image.png"):
    width, height = 800, 500
    background_color = generate_random_color()

    # Создаем изображение с цветным фоном
    image = Image.new("RGB", (width, height), color=background_color)
    draw = ImageDraw.Draw(image)

    try:
        # Выбираем случайный шрифт
        font_path = choose_random_font()
        font = ImageFont.truetype(font_path, size=50)
    except IOError:
        font = ImageFont.load_default()

    # Получаем размеры текста
    text_bbox = draw.textbbox((0, 0), brand_name, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2

    text_color = generate_random_color()

    # Рисуем текст
    draw.text((text_x, text_y), brand_name, font=font, fill=text_color)

    # Сохраняем изображение
    image.save(output_path)
    print(f"Изображение сохранено как {output_path}")


# Пример работы
user_input = input("Введите ключевые слова для бренда: ")
brand_name = generate_brand_name(user_input)
print(f"Сгенерированное название бренда: {brand_name}")
create_and_save_brand_image(brand_name)
