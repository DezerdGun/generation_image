import io
from PIL import Image, ImageDraw, ImageFont
import random
from utils import (generate_random_color, choose_random_font, create_gradient_background)
                   # draw_person,)

def random_text_color():
    return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

def generate_gradient_color(start_color):
    end_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return [(start_color[0] + (end_color[0] - start_color[0]) * i // 100,
             start_color[1] + (end_color[1] - start_color[1]) * i // 100,
             start_color[2] + (end_color[2] - start_color[2]) * i // 100) for i in range(101)]

def draw_text(draw, brand_name, width, height):
    font_path = choose_random_font()  # Выбираем случайный шрифт
    font = ImageFont.truetype(font_path, size=random.randint(40, 70))

    text_bbox = draw.textbbox((0, 0), brand_name, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

    text_x = random.randint(0, width - text_width)
    text_y = random.randint(0, height - text_height)

    # Случайный цвет текста
    text_color = random_text_color()

    # Сложный эффект оформления текста
    effect_type = random.choice(['shadow', 'outline', 'gradient', '3d', 'normal'])

    if effect_type == 'shadow':
        shadow_offset = random.randint(5, 10)
        shadow_color = (text_color[0] // 2, text_color[1] // 2, text_color[2] // 2)
        for i in range(3):  # Многослойная тень
            draw.text((text_x + shadow_offset * i, text_y + shadow_offset * i), brand_name, font=font, fill=shadow_color)

    elif effect_type == 'outline':
        outline_thickness = random.randint(2, 5)
        outline_color = random_text_color()
        for offset in range(-outline_thickness, outline_thickness + 1):
            draw.text((text_x + offset, text_y + offset), brand_name, font=font, fill=outline_color)
        draw.text((text_x, text_y), brand_name, font=font, fill=text_color)  # Основной текст поверх

    elif effect_type == 'gradient':
        gradient = generate_gradient_color(text_color)  # Градиент
        for i, color in enumerate(gradient):
            offset = i * (text_height // 100)
            draw.text((text_x, text_y + offset), brand_name, font=font, fill=color)

    elif effect_type == '3d':
        shadow_offset = random.randint(5, 15)
        shadow_color = (text_color[0] // 3, text_color[1] // 3, text_color[2] // 3)
        for i in range(3):
            draw.text((text_x + shadow_offset * i, text_y + shadow_offset * i), brand_name, font=font, fill=shadow_color)
        draw.text((text_x, text_y), brand_name, font=font, fill=text_color)  # Основной текст

    else:
        draw.text((text_x, text_y), brand_name, font=font, fill=text_color)

# Рисование объекта (круг, прямоугольник или звезда) на изображении
def draw_shadow(draw, object_type, x, y, size, color):
    shadow_offset = random.randint(5, 15)
    shadow_color = (color[0] // 2, color[1] // 2, color[2] // 2)  # Темная версия оригинального цвета
    if object_type == 'circle':
        draw.ellipse((x + shadow_offset, y + shadow_offset, x + size + shadow_offset, y + size + shadow_offset), fill=shadow_color)
    elif object_type == 'rectangle':
        draw.rectangle((x + shadow_offset, y + shadow_offset, x + size + shadow_offset, y + size + shadow_offset), fill=shadow_color)
    elif object_type == 'star':
        points = [(x + size / 2 + shadow_offset, y + shadow_offset),
                  (x + size * 0.6 + shadow_offset, y + size * 0.4 + shadow_offset),
                  (x + size + shadow_offset, y + size * 0.4 + shadow_offset),
                  (x + size * 0.7 + shadow_offset, y + size * 0.6 + shadow_offset),
                  (x + size * 0.8 + shadow_offset, y + size + shadow_offset),
                  (x + size / 2 + shadow_offset, y + size * 0.75 + shadow_offset),
                  (x + size * 0.2 + shadow_offset, y + size + shadow_offset),
                  (x + size * 0.3 + shadow_offset, y + size * 0.6 + shadow_offset),
                  (x + shadow_offset, y + size * 0.4 + shadow_offset),
                  (x + size * 0.4 + shadow_offset, y + size * 0.4 + shadow_offset)]
        draw.polygon(points, fill=shadow_color)

# Функция для рисования случайного объекта с улучшениями
def draw_random_object(draw, width, height):
    object_type = random.choice(['circle', 'rectangle', 'star'])
    object_color = generate_random_color()
    object_size = random.randint(50, 150)
    object_x = random.randint(0, width - object_size)
    object_y = random.randint(0, height - object_size)

    # Рисуем тень
    draw_shadow(draw, object_type, object_x, object_y, object_size, object_color)

    # Рисуем сам объект
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

# Функция для генерации изображения бренда
def create_brand_image(brand_name):
    width, height = 800, 500
    image = create_gradient_background(width, height)
    draw = ImageDraw.Draw(image)

    # Рисуем текст
    draw_text(draw, brand_name, width, height)

    # Рисуем объект
    draw_random_object(draw, width, height)

    # Рисуем человека
    # person_x = random.randint(100, 700)
    # person_y = random.randint(200, 400)
    # draw_person(draw, person_x, person_y)

    # Сохраняем изображение в памяти
    img_io = io.BytesIO()
    image.save(img_io, 'PNG')
    img_io.seek(0)
    return img_io
