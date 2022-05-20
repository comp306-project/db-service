# db-service

## Install docker
https://www.docker.com/products/docker-desktop/

## Install

```
git clone git@github.com:comp306-project/db-service.git
```

## Run
### Docker ile
```
docker-compose up -d --build --force-recreate
```
Usttekini sadece 1 kere runla, run.py veya app klasorunun icindeki dosyalari degistirince suncuyu restartliyo

Containerlar basladiktan sonra docker dekstop uygulamasinda dashboardda cointers kisminda gozukucek, 
flask olanin ustune tiklayinca loglari orda gozukucek
### Dockersiz
#### mysql
files/sql klasorundeki dosyadan world databasini olustur

#### flask
```
python3 -m venv venv #python3.6+
. ./venv/bin/activate
pip install -r requirements.txt

python run.py
```



### Ornek
```
http://localhost:5000/tables
```
