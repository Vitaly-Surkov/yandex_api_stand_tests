# Импорт необходимых модулей и данных для запроса
import requests
import configuration
import data

def post_new_user(user_body):
    # Отправка POST-запроса с использованием URL из конфигурации, данных о продуктах и заголовков
    # Возвращается объект ответа, полученный от сервера
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=data.headers)  # Использование заголовков из файла data.py

# Вызов функции с передачей списка ID продуктов из файла data.py
response = post_new_user(data.user_body)

# Вывод HTTP-статус кода ответа и тела ответа в формате JSON
# Это позволяет проверить успешность выполнения запроса и посмотреть результаты поиска наборов
print(response.status_code)
print(response.json())

# Функция для получения данных из таблицы пользователей
def get_users_table():
    # Составление полного URL пути к данным таблицы пользователей
    # путем конкатенации базового URL сервиса и конечной точки таблицы пользователей
    # Возвращает объект ответа от сервера
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

# Выполнение функции и сохранение ответа в переменную response
response = get_users_table()

# Вывод статус-кода ответа сервера в консоль
# Статус-коды HTTP сообщают о результате выполнения запроса
print(response.status_code)