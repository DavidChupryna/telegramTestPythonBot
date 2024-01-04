import os

bot_responses = {
    "hello": ["Привет, путник!", "Здравствуйте!", "Приветствую!", "Добрый день!", "Здорова!", "Хай",
              "Хеллоу(да-да я из Англии)", "Привет, шеф!"],
    "images": [os.path.join(os.getcwd(), "images", "img_1p.jpg"), os.path.join(os.getcwd(), "images", "img_3p.jpg"),
               os.path.join(os.getcwd(), "images", "img_6p.jpg"), os.path.join(os.getcwd(), "images", "img_9p.jpg"),
               os.path.join(os.getcwd(), "images", "img_12p.jpeg")]}

questions = [
    {"question": "1. Может ли Python использоваться для написания игр?", "answer": "Да"},
    {"question": "2. Переменна обьявленная в теле функции является глобальной?", "answer": "Нет"},
    {"question": "3. Функция len() используется для определения длины строки в Python?", "answer": "Да"},
    {"question": "4. Является ли Python безопасным языком программирования?", "answer": "Да"},
    {"question": "5. Python может быть использован для написания драйверов устройств?", "answer": "Нет"},
    {"question": "6. Число может быть ключем в словаре Python?", "answer": "Да"},
    {"question": "7. Ключевое слово Return останавливает выполнение функции?", "answer": "Да"},
    {"question": "8. Список(list) имеет упорядоченый набор элементов?", "answer": "Да"},
    {"question": "9. Является == оператором присвоения?", "answer": "Нет"},
    {"question": "10. Классы в Python принято называть с маленькой буквы?", "answer": "Нет"},
    {"question": "11. Функция str() конвертирует строку в число?", "answer": "Нет"},
    {"question": "12. Нумерация индексов в списке Python начинаются с 1?", "answer": "Нет"},
]

correct_answers = [questions[0]["answer"], questions[1]["answer"], questions[2]["answer"], questions[3]["answer"],
                   questions[4]["answer"], questions[5]["answer"], questions[6]["answer"], questions[7]["answer"],
                   questions[8]["answer"], questions[9]["answer"], questions[10]["answer"], questions[11]["answer"]]

print(correct_answers)
