from task1.solution import strict

""" Helper functions """
@strict
def sum_number(a:int, b:int) -> int:
    return a+b

@strict
def multiply(a:int,b:int) -> int:
    return a*b

@strict
def divide(a: float, b: float) -> float:
    return a / b

@strict
def func_not_annotation(a,b:int):
    return a,b

# ---------------------------------------------------------------------------------

"""Tests"""


"""Test 1"""
# Проверки str,float 
def test_sum_number():  
    assert sum_number(1,2) == 3

    try:
        sum_number(1.0, 2) # float 
        assert False,"TypeError не вызван "
    except TypeError:
        assert True
    try:
        sum_number('1',3) # str
        assert False,"TypeError не вызван"
    except TypeError:
        assert True


"""Test 2"""
# Проверка строгости типа bool и int 
def test_multiply():
    try:
        multiply(True,5) # bool 
        assert False,"TypeError не вызван"
    except TypeError:
        assert True


"""Test 3"""
# Проверка именнованных аргументов
def test_divide():

    assert divide(a=20.0,b=5.0) == 4.0 # именнованные аргументы

    try:
        divide(a='ab',b=9.0)
        assert False,"TypeError не вызван"
    except TypeError:
        assert True


"""Test 4"""
# Проверка того что не будет ошибки если нет аннотации ля аргумента
def test_func_not_annotation():

    assert func_not_annotation('abc',1) == ('abc',1)