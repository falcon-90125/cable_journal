# Сборка образа
# docker build . -t cable_m_imade:latest

# Сохранить архив образа
# docker save -o C:\Users\sokolov\MyData\cable_m_imade.tar cable_m_imade, где 
# spec_varton.tar - имя файла архива, 
# spec_varton - имя образа, 
# <C:\Users\sokolov\MyData\> - путь сохранения

# Для разархивирования файла архива docker-образа с расширением tar нужно выполнить следующие шаги:
# 1. Открыть командную строку или терминал.
# 2. Перейти в папку, где сохранен файл архива.
# 3. Выполнить команду для разархивирования файла:
#  tar -xvf cable_m_imade.tar

# Для загрузки образа Docker из tar-архива:
# docker load -i C:\Users\sokolov\MyData\cable_m_imade.tar

# Сборка контейнера
# docker run --name cable_m -v C:/Users/sokolov/MyData/Projects/nom_varton_docker_run_exchange:/app/exchange -d cable_m_imade:latest

docker start cable_m
