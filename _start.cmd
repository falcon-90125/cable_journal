# Сборка образа
# docker build . -t cable_j_image:latest

# Сохранить архив образа
# docker save -o C:\Users\sokolov\Yandex_Disk\MyData\cable_j_image.tar cable_j_image 
# C:\Users\sokolov\MyData\cable_j_image.tar - путь сохранения\имя файла архива 
# cable_j_image - имя образа

# Для загрузки образа Docker из tar-архива:
# docker load -i C:\Users\e.titova\cable_j_image.tar

# Сборка контейнера
# docker run --name cable_journal -v C:/Users/e.titova/Documents/cable_journal:/app/cable_journal -d cable_j_image:latest

# Запуск контейнера
docker start cable_journal
