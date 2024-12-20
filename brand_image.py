import io
from PIL import Image, ImageDraw, ImageFont
import random
from utils import generate_random_color, choose_random_font, create_gradient_background, draw_person

# Функция для генерации изображения бренда
def create_brand_image(brand_name):
    width, height = 800, 500
    image = create_gradient_background(width, height)
    draw = ImageDraw.Draw(image)

    font_path = choose_random_font()
    font = ImageFont.truetype(font_path, size=random.randint(40, 70))

    # Рандомизация положения текста
    text_bbox = draw.textbbox((0, 0), brand_name, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

    text_x = random.randint(0, width - text_width)
    text_y = random.randint(0, height - text_height)

    # Рандомизация цвета текста
    text_color = generate_random_color()

    # Рисуем текст на изображении
    draw.text((text_x, text_y), brand_name, font=font, fill=text_color)

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

    # Сохраняем изображение в памяти
    img_io = io.BytesIO()
    image.save(img_io, 'PNG')
    img_io.seek(0)
    return img_io
