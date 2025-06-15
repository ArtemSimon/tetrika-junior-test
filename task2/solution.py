import httpx
import asyncio
import aiofiles
from collections import defaultdict 

# вспомогательная функция для определения того,что эта русская буква
def is_russian_letter(letter:str) -> bool:
    return 'А' <= letter <= 'Я' or letter == 'Ё'


""" В данном случае использование defaultdict будет разумнее, чем тот же dict так как 
если ключа не существует то тут автоматически он создается и присваевает значение int(0) """

async def get_animals_wikipedia_count():
    animal_count = defaultdict(int) # используем данную коллекцию для подсчета количества животных каждой буквы
    url = "https://ru.wikipedia.org/w/api.php"
    params = {
        'action': 'query', # действие (делаем запрос)
        'list': 'categorymembers', # запрашивает список страниц определенной категории (указывается в cmtitle)
        'cmtitle': 'Категория:Животные_по_алфавиту', # сама категория 
        'cmlimit': '500', # тут устанавливается лимит на один запрос
        'format': 'json' # указываем формат данных 
    }

    async with httpx.AsyncClient() as client:
        while True:
            responce = await client.get(url,params=params)
            data = responce.json()
            
            # проходим по данныи и считаем количество животных
            for animal in data["query"]['categorymembers']:
                title_animal = animal['title']
                title_first_letter = title_animal[0].upper()
                if is_russian_letter(title_first_letter):
                    animal_count[title_first_letter] += 1

            if 'continue' not in data:
                break
            params.update(data['continue'])

    return animal_count

# для ассинхронной записи в файл
async def save_data_to_file(data, file_path):
    async with aiofiles.open(file_path,'w') as file:
        for letter_upper,count in sorted(data.items()):
            await file.write(f'{letter_upper},{count}\n')

async def main():
    animal_count = await get_animals_wikipedia_count()

    file_path = 'task2/beasts.csv'
    await save_data_to_file(animal_count,file_path)
    print('Данные сохранены в beasts.csv')

asyncio.run(main())