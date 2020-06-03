from example import translate_it


# передаём один аргумент -- перевод с любого языка на русский (проверка автоопределения исходного языка)
print(translate_it('habló'))
# передаём два аргумента -- перевод с любого языка на русский (указание исходного языка вручную)
print(translate_it('habló', 'es'))
# передаём текст и пару "исходный язык - язык перевода"
print(translate_it('habló', 'es', 'en'))
# переводим файл с испанским текстом
translate_it(None, 'es', 'ru', 'ES.txt', 'ES_translated.txt')
# переводим файл с немецким текстом
translate_it(None, 'de', 'ru', 'DE.txt', 'DE_translated.txt')
# переводим файл с французским текстом
translate_it(None, 'fr', 'ru', 'FR.txt', 'FR_translated.txt')