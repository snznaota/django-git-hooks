## Простое приложение для выполнения команды git pull для Django-проекта!

### Установка
  * ``` pip install django-git-hooks ```

### Для использования просто добавьте в файл url.py
  ```
    urlpatterns = ['',
      ...
      url(r'^git/', include('git_hooks.urls')),
      ...
    ]
  ```
### Добавьте в Вашем репозитории Hook - для отправки POST запроса при изменениях в репозитории 
  
  * Перейдите по адресу https://bitbucket.org/*YOUR-LOGIN*/*REPO-NAME*/admin/hooks
  * В поле "Select the hook" выбрать POST
  * В появившемся окне вставить ссылку http://your-domain.com/git/pull/
   
#### Зависимости
  * progressbar2
  * prettytable
  * termcolor

#### Совместимость
  * Python 2.7 точно, остальыне надо тестить
  * Django 1.9
