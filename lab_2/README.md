## Практическая работа 2

## Розанцева Елизавета бисо-03-20

Диаграмма последовательности
```
"Руководитель подразделения" as boss
actor "Документовед" as doc
group Создание табеля
tabel-> Табель: Создание
activate Табель
tabel-> Табель: Удаление
tabel-> Табель: Редактирование
Табель -> tabel: Результат табеля
deactivate Табель
activate tabel
tabel-> Табель: Отправка на проверку
deactivate tabel
end

tabel-> boss: Запрос на эл.подпись табеля
activate boss
boss-> doc: Передача табеля
boss -> doc: Эл.подпись табеля
deactivate boss

activate doc
doc->Табель:Печать табеля
doc->Табель: Регистрация табеля
deactivate doc
@enduml

```
![image](https://github.com/rozanseva/TMP/assets/128053688/e7b94ff1-67d9-4bfd-b7fc-55004e90be11)


Диаграмма развертывания.

```
@startuml 
left to right direction
database Табель
node "Ответственный за заполнение табеля" as tabel
node "Руководитель подразделения" as boss
node "Документовед" 
node "Редактирование"

tabel - "Редактирование": Используют 
boss- "Редактирование": Используют 
tabel - Табель: Отправка на проверку
Документовед - Табель: Распечатать табель/Зарегестрировать табель

@enduml
```

![image](https://github.com/rozanseva/TMP/assets/128053688/538dc6ca-cb3a-4031-bd5a-363f916be7d9)
