# Настройка Postgresql 

Я бы просто скопировал это, и поменял бы на свои данные
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "mydatabase",
        "USER": "mydatabaseuser",
        "PASSWORD": "mypassword",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
```

тут всё понятно, если вы не сис.админ, то я вам расскажу.
ENGINE: тип используемого движка базы данных
NAME: имя базы данных
USER: имя пользователя базы данных
PASSWORD: пароль пользователя базы данных
HOST: IP, на котором запущена база данных
PORT: порт, на котором работает база данных (default 5432)

