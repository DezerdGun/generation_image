from PIL import Image, ImageDraw, ImageFont
import random

def generate_brand_name(keywords):
    suffixes = ["Tech", "Corp", "Design", "Studio", "Wave"]
    random_suffix = random.choice(suffixes)
    return f"{keywords.title()} {random_suffix}"

def generate_random_color():
    return tuple(random.randint(0, 255) for _ in range(3))

def create_and_save_brand_image(brand_name, output_path="brand_image.png"):
    width, height = 800, 400
    image = Image.new("RGB", (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)

    try:
        # Используем локальный шрифт, который вы добавили в папку 'fonts'
        font_path = "fonts/DejaVuSans-Bold.ttf"  # Укажите путь к шрифту
        font = ImageFont.truetype(font_path, size=50)
    except IOError:
        font = ImageFont.load_default()

    text_bbox = draw.textbbox((0, 0), brand_name, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2

    text_color = generate_random_color()

    draw.text((text_x, text_y), brand_name, font=font, fill=text_color)

    image.save(output_path)
    print(f"Изображение сохранено как {output_path}")

user_input = input("Введите ключевые слова для бренда: ")
brand_name = generate_brand_name(user_input)
print(f"Сгенерированное название бренда: {brand_name}")
create_and_save_brand_image(brand_name)
