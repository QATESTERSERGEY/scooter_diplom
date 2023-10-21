# Клочков Сергей, 9-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import pytest
import data
# Функция для позитивной проверки

# Тест 1. Статус заказа
def test_get_order_track_success_response():
    response = sender_stand_request.post_new_orders(data.order_body)
    track = response.json()["track"]
    order_response = sender_stand_request.get_treck_order(track)
    assert order_response.status_code == 200


