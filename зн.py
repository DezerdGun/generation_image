from PIL import Image, ImageDraw, ImageFont
import random
import os


# Функция для генерации названия бренда
def generate_brand_name(keywords):
    suffixes = ["Tech", "Corp", "Design", "Studio", "Wave"]
    random_suffix = random.choice(suffixes)
    return f"{keywords.title()} {random_suffix}"


# Функция для генерации случайного цвета
def generate_random_color():
    return tuple(random.randint(0, 255) for _ in range(3))


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
    draw.line((x, y + head_radius + body_height, x - 20, y + head_radius + body_height + leg_length), fill="black",
              width=3)
    draw.line((x, y + head_radius + body_height, x + 20, y + head_radius + body_height + leg_length), fill="black",
              width=3)


# Функция для создания анимации с текстом, объектами и человеком
def create_and_save_brand_image_with_random_animation_and_person(brand_name,
                                                                 output_path="brand_random_animation_with_person.gif",
                                                                 num_frames=30):
    width, height = 800, 500
    frames = []
    font_path = choose_random_font()

    for frame_num in range(num_frames):
        # Создаем градиентный фон
        image = create_gradient_background(width, height)
        draw = ImageDraw.Draw(image)

        try:
            font = ImageFont.truetype(font_path, size=random.randint(40, 70))
        except IOError:
            font = ImageFont.load_default()

        # Рандомизация положения текста
        text_bbox = draw.textbbox((0, 0), brand_name, font=font)
        text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

        # Рандомизация направления движения текста
        direction = random.choice(['left', 'right', 'up', 'down'])

        if direction == 'left':
            text_x = width - text_width - int(frame_num * 5)
            text_y = random.randint(0, height - text_height)
        elif direction == 'right':
            text_x = int(frame_num * 5)
            text_y = random.randint(0, height - text_height)
        elif direction == 'up':
            text_x = random.randint(0, width - text_width)
            text_y = height - text_height - int(frame_num * 5)
        else:  # down
            text_x = random.randint(0, width - text_width)
            text_y = int(frame_num * 5)

        # Рандомизация цвета текста
        text_color = generate_random_color()

        # Рандомизация прозрачности текста
        opacity = random.randint(100, 255)
        text_color_with_opacity = (*text_color, opacity)

        # Рисуем текст на изображении
        draw.text((text_x, text_y), brand_name, font=font, fill=text_color_with_opacity)

        # Рисуем объект на изображении
        object_type = random.choice(['circle', 'rectangle', 'star'])
        object_color = generate_random_color()
        object_size = random.randint(30, 100)
        object_x = random.randint(0, width - object_size)
        object_y = random.randint(0, height - object_size)

        if object_type == 'circle':
            draw.ellipse((object_x, object_y, object_x + object_size, object_y + object_size), fill=object_color)
        elif object_type == 'rectangle':
            draw.rectangle((object_x, object_y, object_x + object_size, object_y + object_size), fill=object_color)
        elif object_type == 'star':
            # Создаем звезду (не идеально, но для примера сойдет)
            points = [
                (object_x + object_size / 2, object_y),
                (object_x + object_size * 0.6, object_y + object_size * 0.4),
                (object_x + object_size, object_y + object_size * 0.4),
                (object_x + object_size * 0.7, object_y + object_size * 0.6),
                (object_x + object_size * 0.8, object_y + object_size),
                (object_x + object_size / 2, object_y + object_size * 0.75),
                (object_x + object_size * 0.2, object_y + object_size),
                (object_x + object_size * 0.3, object_y + object_size * 0.6),
                (object_x, object_y + object_size * 0.4),
                (object_x + object_size * 0.4, object_y + object_size * 0.4)
            ]
            draw.polygon(points, fill=object_color)

        # Рисуем человека
        person_x = random.randint(100, 700)
        person_y = random.randint(200, 400)
        draw_person(draw, person_x, person_y)

        frames.append(image)

    # Сохраняем анимацию как GIF
    frames[0].save(output_path, save_all=True, append_images=frames[1:], duration=100, loop=0)
    print(f"Анимация с объектом и человеком сохранена как {output_path}")


# Пример работы
user_input = input("Введите ключевые слова для бренда: ")
brand_name = generate_brand_name(user_input)
print(f"Сгенерированное название бренда: {brand_name}")
create_and_save_brand_image_with_random_animation_and_person(brand_name)
