from PIL import Image, ImageDraw, ImageFont
import random

def generate_brand_name(keywords):
    # Создаем название бренда, добавляя уникальный суффикс
    suffixes = ["Tech", "Corp", "Design", "Studio", "Wave"]
    random_suffix = random.choice(suffixes)
    return f"{keywords.title()} {random_suffix}"

def generate_random_color():
    # Генерация случайного цвета в формате RGB
    return tuple(random.randint(0, 255) for _ in range(3))

def create_and_save_brand_image(brand_name, output_path="brand_image.png"):
    # Параметры изображения
    width, height = 800, 400
    image = Image.new("RGB", (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Настройки текста
    try:
        font = ImageFont.truetype("arial.ttf", size=60)  # Используем шрифт Arial
    except:
        font = ImageFont.load_default()  # Используем стандартный шрифт, если Arial недоступен

    # Получаем размеры текста с помощью textbbox
    text_bbox = draw.textbbox((0, 0), brand_name, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

    # Рассчитываем позицию текста
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2

    # Генерация случайного цвета для текста
    text_color = generate_random_color()

    # Рисуем текст на изображении
    draw.text((text_x, text_y), brand_name, font=font, fill=text_color)

    # Сохраняем изображение
    image.save(output_path)
    print(f"Изображение сохранено как {output_path}")

# Пример работы
user_input = input("Введите ключевые слова для бренда: ")
brand_name = generate_brand_name(user_input)
print(f"Сгенерированное название бренда: {brand_name}")

# Автоматически создаем и сохраняем изображение
create_and_save_brand_image(brand_name)
