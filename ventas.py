from faker import Faker
from googletrans import Translator

def translate_to_english(text):
    translator = Translator()
    translation = translator.translate(text, src='zh-CN', dest='en')
    return translation.text

def chinese_city_name():
    fake = Faker('zh_CN')
    city_name = fake.city_name()
    return city_name

# Ejemplo de uso con traducción
for _ in range(5):
    chinese_name = chinese_city_name()
    english_name = translate_to_english(chinese_name)
    print(f"Nombre en chino: {chinese_name}, Nombre en inglés: {english_name}")
