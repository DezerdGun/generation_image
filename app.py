from flask import Flask, render_template, request, Response
from brand_image import create_brand_image

app = Flask(__name__)

# Главная страница
@app.route('/')
def index():
    return render_template('index.html')

# API для генерации изображения бренда
@app.route('/generate_brand_image', methods=['POST'])
def generate_image():
    if request.method == 'POST':  # Проверяем метод
        brand_name = request.form['brand_name']
        image = create_brand_image(brand_name)

        # Отправляем изображение в браузер для отображения
        return Response(image, mimetype='image/png')

    return "Method Not Allowed", 405  # Возвращаем ошибку 405 для недопустимых методов

if __name__ == '__main__':
    app.run(debug=True)
