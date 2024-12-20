from PIL import Image, ImageDraw, ImageFont
import random
import os

def generate_brand_name(keywords):
    suffixes = ["Tech", "Corp", "Design", "Studio", "Wave"]
    random_suffix = random.choice(suffixes)
    return f"{keywords.title()} {random_suffix}"

def generate_random_color():
    return tuple(random.randint(0, 255) for _ in range(3))

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

def choose_random_font():
    font_dirs = [
        "/usr/share/fonts",
        "/Library/Fonts",
        "C:\\Windows\\Fonts",
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
        return "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def create_and_save_brand_image_with_random_animation(brand_name, output_path="brand_random_animation.gif", num_frames=30):
    width, height = 800, 500
    frames = []
    font_path = choose_random_font()

    for frame_num in range(num_frames):
        image = create_gradient_background(width, height)
        draw = ImageDraw.Draw(image)

        try:
            font = ImageFont.truetype(font_path, size=random.randint(40, 70))  # Рандомный размер шрифта
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

        # Рандомизация прозрачности (используется RGBA, где A — это прозрачность)
        opacity = random.randint(100, 255)  # Прозрачность от 100 до 255
        text_color_with_opacity = (*text_color, opacity)

        draw.text((text_x, text_y), brand_name, font=font, fill=text_color_with_opacity)

        frames.append(image)

    # Сохраняем анимацию как GIF
    frames[0].save(output_path, save_all=True, append_images=frames[1:], duration=100, loop=0)
    print(f"Анимация сохранена как {output_path}")

# Пример работы
user_input = input("Введите ключевые слова для бренда: ")
brand_name = generate_brand_name(user_input)
print(f"Сгенерированное название бренда: {brand_name}")
create_and_save_brand_image_with_random_animation(brand_name)
