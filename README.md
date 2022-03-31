# api_yamdb
api_yamdb
# Учебный проект infra_sp2
### Описание
Проект служит для размещения проекта api_yamdb в Doker для разворачивания проекта в любых операционных системах.
Созданы три образа
### Технологии
Doker
### Запуск проекта 
- запуск контейнера 
```docker-compose up -d --build
```  
- запуск миграций
``` 
docker-compose exec web python manage.py migrate
```
- создание суперпользователя
```
docker-compose exec web python manage.py createsuperuser 
```
- собрать статику
```
docker-compose exec web python manage.py collectstatic --no-input 
```

### Авторы
Дмитрий


![example workflow]
( https://github.com/Kolosovdv/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)


http://62.84.115.146/redoc/ 
