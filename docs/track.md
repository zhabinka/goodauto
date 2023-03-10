## Парсинг

Источник - https://www.blocket.se/annonser/hela_sverige/fordon/bilar?cg=1020

Идея: собрать все ссылки на страницы авто с из каталога и затем парсить по списку.

Начал с простых запросов через _requests_. Ссылки получить не удалось. Данные на страницу подгружаются в самом браузере.

Решение: подключил _selenium_.

В каталоге пагинация с использованием параметров в url:

- https://www.blocket.se/annonser/hela_sverige/fordon/bilar?cg=1020&page=1
- https://www.blocket.se/annonser/hela_sverige/fordon/bilar?cg=1020&page=2
- https://www.blocket.se/annonser/hela_sverige/fordon/bilar?cg=1020&page=3
- и т.д.

Буду использовать простой счётчик в цикле (возможно, стоит использовать переход по ссылке `next` на странице каталога, до конца списка).

На первом шаге открываю каждую страницу и с помощью bs4 паршу ссылки на авто, список по каждой странице сохраняю в отдельный файл.

На втором шаге обрабатываю список ссылок на авто. Сначала получаю исходный код страницы с помощью _selenium_ и сохраняю его в файл. Ссылка на авто заканчивается числом:

- https://www.blocket.se/annons/stockholm/mini_cooper_sd_all4_countryman_automat_pepper_143hk/106543018

Предполагаю, что это уникальный id. Дёргаю его и использую для именования файла с сырцами. Информацию по авто заношу в отдельный список:

```json
{
 'id': 106543018
 'source_path': '/assets/files/autos/106543018.html',
 'url': 'https://www.blocket.se/annons/stockholm/mini_cooper_sd_all4_countryman_automat_pepper_143hk/106543018'
}
```

Запросы по сети с исполоьзованием движка браузера - дорогое удовольствие. Идея в том, разделить получение данных и их обработку. Задачи можно запускать раздельно. К сохранённым файлам можно обратиться в любой момент.

_selenium_ при работе запускает браузер. Настроил запуск в фоновом режиме. Подложил fake user-agent.

Закачал репозиторий на сервер, запустил на нём скрипт. Предварительно настроил окружение:

- настроил ssh для доступа в приватный репозиторий
- установил make
- установил poetry + обновил $PATH (добавил в него .local/bin)
- установил chrome из .deb-пакета
    - wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    - sudo dpkg -i google-chrome-stable_current_amd64.deb
- проапдейтил систему (без этого хром не ставился), сверил версию python
- скачал драйвер для silenium под Ubuntu (понадобился unzip для распаковки архива) - https://chromedriver.chromium.org/downloads


## Задачи

- Настроить логирование _selenium_
- Настроить работу _selenium_ через брокера сообщений Redis или RabbitMQ. Будем обработать большой список (более 100 000 ссылок). Что здесь больше подходит?
- Подключить базу и сохранить в неё информацию.
- Настроить проксирование.
-https://github.com/diprajpatra/selenium-stealth Развернуть окружение для запуска скрипта автоматически (ansible, docker)
- Добавить оболочку silenium-stealth - https://github.com/diprajpatra/selenium-stealth
- Настроить асинхронную работу silenium
