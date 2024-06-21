import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="freegpt3.5docs",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="freegpt3.5docs_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from freegpt3.5docs.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export freegpt3.5docs_KEY=value
export freegpt3.5docs_KEY="@int 42"
export freegpt3.5docs_KEY="@jinja {{ this.db.uri }}"
export freegpt3.5docs_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
freegpt3.5docs_ENV=production freegpt3.5docs run
```

Read more on https://dynaconf.com
"""
