# B2C6_Backend
Studenten repository voor Backend voor het vak B2C6 DevOps. De backend wordt gemaakt in Python. Elke klas heeft 1 repository voor Backend.

Iets eraan toegevoegd door Nicky. Alweer met Casper naast me.


## install

```bash
pip install -r requirements.txt
```

## run

**dev mode:**
```bash
docker run -e MYSQL_ROOT_PASSWORD=admin -p 3306:3306 mariadb
fastapi dev main.py
```

**prod mode:**
```bash
fastapi run main.py
```

