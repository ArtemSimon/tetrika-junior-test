import httpx
import pytest
from pytest_httpx import HTTPXMock
from collections import defaultdict
from unittest.mock import patch
from task2.solution import is_russian_letter,get_animals_wikipedia_count



"""TESTS"""


"""TEST 1"""
def test_is_russian_letter():
    assert is_russian_letter('А') == True
    assert is_russian_letter('Ё') == True
    assert is_russian_letter('A') == False  # Английская A
    assert is_russian_letter('1') == False  # Цифра
    assert is_russian_letter('@') == False  # Символ

""" TEST 2 """
# Проверка корректноси работы функции get_animals_wikipedia_count
@pytest.mark.asyncio
async def test_get_animals_count_success(httpx_mock: HTTPXMock):
    mock_response = {
        "query": {
            "categorymembers": [{"title": "Аист"}, {"title": "Барсук"},{"title": "Ёж"}]
        }
    }

    httpx_mock.add_response(
        method="GET",
        url="https://ru.wikipedia.org/w/api.php?action=query&list=categorymembers&cmtitle=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&cmlimit=500&format=json",
        json=mock_response
        )

    result = await get_animals_wikipedia_count()

    assert isinstance(result, defaultdict)
    assert dict(result) == {'А': 1,'Б': 1,"Ё":1}
    
    # Проверяем обработку буквы Ё
    assert 'Ё' in result, "Буква Ё должна обрабатываться корректно"