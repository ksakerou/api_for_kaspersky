Это мое тестовое задание на стажировку в Kaspersky
Итак, для того, чтобы запустить приложение, необходимо
1) Клонировать репозиторий
git clone https://github.com/ksakerou/api_for_kaspersky.git
2) Собрать docker-образ
docker build . -t myimage
3) Запустить docker-контейнер
docker run -d --name mycontainer -p 80:80 myimage

