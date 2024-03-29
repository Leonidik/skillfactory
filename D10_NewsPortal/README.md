### D10. Работа с асинхронными задачами через Celery

Состав:
D10.1: Основной вариант в соответствии с ТЗ
D10.2.1: реализована только рассылка уведомлений подписчикам об опубликовании новостей
D10.2.2: реализована только переодическая рассылка перечня новостей, опубликованных,
      за временной интервал в 1 минуту (в течении этого времени можно спокойно создать две-три новости и посмотреть,
      как это все реально работает)
       
Установка:
1. Создаем папку для django проектов, например, django-projects
2. Переносим в нее проект - содержимое папки D10_NewsPortal
3. Создаем в ней вируальное окружение: virtualenv env
4. Активируем виртуальное окружение: source env/bin/activate
5. Устанавливаем необходимые пакеты: pip install -r requirements.txt

Запуск:
1. Пререходим в папку одного из вариантов проекта (D10.1, D10.2.1, D10.2.2)
2. Из этой папки создаем два окна командной строки
3. Для варианта D10.2.1
   - первое окно: python manage.py runserver
   - второе окно: celery -A django_project worker -l INFO
4. Для вариантов D10.1 и D10.2.2
   - первое окно: python manage.py runserver
   - второе окно: celery -A django_project worker -l INFO -B

Стартовая страница:
http://localhost:8000/

Пользователи:
 login   password      email                     groups
admin   admin         admin@example.ru          superuser
ivanov  skillfactory  forestwind@rambler.ru     common, author, owner
petrov  petrov        leontiy.radimoff@mail.ru  common
sidorov sidorov       sidorov@example.ru        common, author
pavlov  propoganda    pavlov@example.ru         common
egorov  tensorflow    egorov@example.ru         common

Пояснения:

1. Django-server содержит три приложения:
   - users: аутентификация и регистрация
   - docs_free: зона свободного доступа для незарегистрированных пользователей
   - docs_work: зона доступа для зарегистрированных пользователей

2. Для незарегистрированных пользователей возможен только просмотр и поиск документов

3. Для зарегистрированных пользователей
   - группы common доступны просмотр и поиск документов, а так же оформление подписки
   - группы authors дополнительно доступны создание и редактирование документов
   - группы owners дополнительно доступно удаление документов

3. Для редактирования документов пользователю предоставляются только те документы, автором которых он является 

4. Для двух пользователей используются реальные почтовые ящики
   (ivanov - pw: Skillfactory2022, petrov - pw: skillfactory), pw's которых после проверки будит изменены
   
5. Почтовая рассылка реализована только для новостей, как и указано в ТЗ.
   Добавление рассылки для статей отличается только первоначальной фильтрацией (новости/статьи)
   и может быть без особого труда реализована по необходимости.





