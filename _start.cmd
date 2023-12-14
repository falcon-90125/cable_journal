# Сборка образа
# docker build . -t cable_m_image:latest

# Сохранить архив образа
# docker save -o C:\Users\sokolov\MyData\cable_m_image.tar cable_m_image, где 
# cable_m_image.tar - имя файла архива, 
# cable_m_image - имя образа, 
# <C:\Users\sokolov\MyData\> - путь сохранения

# Для разархивирования файла архива docker-образа с расширением tar нужно выполнить следующие шаги:
# 1. Открыть командную строку или терминал.
# 2. Перейти в папку, где сохранен файл архива.
# 3. Выполнить команду для разархивирования файла:
#  tar -xvf cable_m_image.tar

# Для загрузки образа Docker из tar-архива:
# docker load -i C:\Users\sokolov\MyData\cable_m_image.tar

# Сборка контейнера
# docker run --name cable_m -v C:/Users/sokolov/MyData/Projects/cable_m_image:/app/exchange -d cable_m_image:latest

docker start cable_m
