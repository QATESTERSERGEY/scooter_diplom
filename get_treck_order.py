# Клочков Сергей, 9-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import pytest

# Функция для позитивной проверки
def positive_assert(track):
# В переменную order_response сохраняем результат запроса на получение заказа по треку
    order_response = sender_stand_request.get_treck_order(track)
# Проверяется, что код ответа равен 200
    assert order_response.status_code == 200

# Тест 1. Статус заказа
def test_get_order_track_success_response():
    positive_assert(sender_stand_request.track)

