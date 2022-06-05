# Car Dealers API | Python AQA Homework

The following toolset was used:
* Python 3.9
* pipenv
* Flask
* sqlite3

Tables:
* dealer(id, name)
* car(id, modelName, color, dealerId)

There are two endpoints:
* `/dealers`
    * add - `POST` method
    * delete - `DELETE` method
    * list - `GET` method
* `/cars`
    * add - `POST` method
    * delete - `DELETE` method
    * list - `GET` method
    * list with filters by color, model - `GET` method with query parameters, e.g.: `/cars?color=White&model=Slavuta`

Run server:
```bash
$ ./run.sh
```

Database already seeded with fake data. To re-seed db, use `seed_db.py`  
