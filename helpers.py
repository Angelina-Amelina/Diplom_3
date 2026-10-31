import random



def generate_user_data():
    num = random.randint(100, 999)
    return {
            "email": f"praktikum_user_{num}@yandex.ru",
            "password": f"pass_{num}xyz",
            "name": f"Tester_{num}"
        }