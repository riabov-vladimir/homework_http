# Домашнее задание к лекции 3.2 «Работа с библиотекой requests, http-запросы»

Исходный код для выполнения домашней работы вы найдете в папке [3.2.http.requests](https://github.com/netology-code/py-homework-basic-files/tree/master/3.2.http.requests).

## Задача №1
Необходимо расширить функцию переводчика так, чтобы она принимала следующие параметры:

* Путь к файлу с текстом;
* Путь к файлу с результатом;
* Язык с которого перевести;
* Язык на который перевести (по-умолчанию русский).

У вас есть 3 файла (`DE.txt`, `ES.txt`, `FR.txt`) с новостями на 3 языках: французском, испанском, немецком. Функция должна взять каждый файл с текстом, перевести его на русский и сохранить результат в новом файле.

Для переводов можно пользоваться [API Yandex.Переводчик](https://tech.yandex.ru/translate/).

## \*Задача №2
Научиться работать с api [Яндекс.Диска](https://yandex.ru/dev/disk/rest/)
Написать программу, которая загружает переведенные файлы на Яндекс.Диск. 
[Документация по загрузке файлов](https://yandex.ru/dev/disk/api/reference/upload-docpage/)
Токен можно получить на [Полигоне](https://yandex.ru/dev/disk/poligon/) кликнув по кнопке "Получить OAuth-токен"

---
