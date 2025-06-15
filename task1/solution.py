from functools import wraps
import inspect

def strict(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        
        # Получаем аннотации типов (исключая return)
        annotations_func = func.__annotations__
        params = inspect.signature(func).parameters
        
        
        # Проверяем позиционные аргументы
        for i, (param_name, param) in enumerate(params.items()):
            if param_name not in annotations_func:
                continue
            
            # ожидаемый тип 
            type_param = annotations_func[param_name]

            # определяем значени для позиционного аргумента 
            if i < len(args):
                param_value = args[i]
            
            # если передан по имени
            elif param_name in kwargs:
                param_value = kwargs[param_name]
            else: 
                continue
            
            # Выбрасываем TypeError
            if type(param_value) is not type_param:
                raise TypeError(
                    f'Argument {param_name} must {type_param}, but got {type(param_value)}'
                )
            
            # если считать bool является подклассом int это стандартное поведение в Python
            # if not isinstance(param_value, type_param):
                # raise TypeError(
                #     f'Argument {param_name} must {type_param}, but got {type(param_value)}'
                # )

        return func(*args,**kwargs)
    return wrapper

# @strict
# def sum_two(a: int, b: int) -> int:
#     return a + b

