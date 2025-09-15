import pandas as pd

data = pd.read_excel(f'cable_journal/cable_journal.xlsx', header=0)
columns = data.columns
df_out = pd.DataFrame(columns=columns)

for i in range(len(data)):
    stroka = data.loc[i]
    if type(stroka['Позиция']) == float: # Полностью пустые строки имеют первую ячейку с типом float, поэтому их пропускаем
        pass

    elif type(stroka['Позиция']) == str and type(stroka['Начало']) == float: # Строка в первой ячейкой заполнена (имя щита), вторая пустая с типом float, её записываем
        df_i = pd.DataFrame(columns=columns)
        df_i.loc[len(df_out)] = [''] * len(df_i.columns)
        df_i.iloc[0, 0] = stroka['Позиция']

    elif type(stroka['Позиция']) == str and type(stroka['Начало']) == str and type(stroka['Конец']) == str:
        okns = stroka['Обозначение КНС'].replace("\n", "").replace("_x000D_", "")
        okns = okns.split(";") # Разбираем данные по делителю, записываем с список
        gkns = stroka['Габариты КНС'].replace("\n", "").replace("_x000D_", "")
        gkns = gkns.split(";") # Разбираем данные по делителю, записываем с список
        dkns = stroka['Длина в КНС'].replace("\n", "").replace("_x000D_", "")
        dkns = dkns.split(";") # Разбираем данные по делителю, записываем с список
        for i in range(len(dkns)): # Переводим значения 'Длина в КНС' из str во float, с заменой запятой на точку
            dkns[i] = float(dkns[i].replace(',', '.'))

        # Повторяем значения 'Марка' и 'NxS' столько раз сколько значений "Обозначение КНС" в строке, для последующего groupby
        marka = []
        for _ in range(len(okns)):
            marka.append(stroka['Марка'])
        nxs = []
        for _ in range(len(okns)): # Повторяем значения столько раз сколько значений "Обозначение КНС" в строке
            nxs.append(stroka['NxS'])
         # Списки для df
        poziciya = []
        poziciya.append(stroka['Позиция'])
        nachalo = []
        nachalo.append(stroka['Начало'])
        konec = []
        konec.append(stroka['Конец'])
        dlina = []
        dlina.append(stroka['Длина'])
        pust_str = len(okns)-1
        list_pust_str = []
        for _ in range(pust_str): # Добиваем списки с 'Позиция', 'Начало', 'Конец', 'Длина'  до кол-ва значений "Обозначение КНС" в строке
            list_pust_str.append('')
        poziciya.extend(list_pust_str)
        nachalo.extend(list_pust_str)
        konec.extend(list_pust_str)
        dlina.extend(list_pust_str)
        # df с распаршенными данными строки исходного df
        df_i = pd.DataFrame({'Позиция':poziciya, 'Начало':nachalo, 'Конец':konec, 
                                'Обозначение КНС':okns, 'Габариты КНС':gkns, 
                                'Длина в КНС':dkns, 'Марка':marka, 'NxS':nxs, 'Длина':dlina})


    # Добавляем в общий df
    df_out = pd.concat([df_out, df_i])

file_directory_resalts = f'cable_journal/cable_journal_out.xlsx' # Директория сохранения файла

writer_0 = pd.ExcelWriter(file_directory_resalts, engine='xlsxwriter') # + file_name
df_out.to_excel(writer_0, sheet_name='Sheet1', index=False) # Определяем сохранение xlsx методом ExcelWriter
sheet_0 = writer_0.sheets['Sheet1'] # Определяем лист для форматирования

# Закрепляем шапку
sheet_0.freeze_panes(1, 0)

sheet_0.set_column(0, 0, 12) # Позиция
sheet_0.set_column(1, 1, 12) # Начало
sheet_0.set_column(2, 2, 12) # Конец
sheet_0.set_column(3, 3, 40) # Обозначение КНС
sheet_0.set_column(4, 4, 15) # Габариты КНС
sheet_0.set_column(5, 5, 15) # Длина в КНС
sheet_0.set_column(6, 6, 18) # Марка
sheet_0.set_column(7, 7, 7)  # NxS
sheet_0.set_column(8, 8, 10) # Длина
writer_0._save()

# Суммируем 'Длина в КНС' в группировке по 'Марка', 'NxS', 'Габариты КНС', 'Обозначение КНС'
df_out_groupby = df_out.groupby(['Марка', 'NxS', 'Габариты КНС', 'Обозначение КНС'])['Длина в КНС'].sum()
df_out_groupby = df_out_groupby.reset_index()
df_out_groupby = df_out_groupby.drop(0)
df_out_groupby.reset_index(inplace=True)
df_out_groupby = df_out_groupby.drop('index',axis=1)
for i in range(len(df_out_groupby)):
    df_out_groupby['Длина в КНС'][i] = round(df_out_groupby['Длина в КНС'][i], 2)

file_directory_resalts_groupby = f'cable_journal/cable_journal_out_groupby.xlsx' # Директория сохранения файла

writer_1 = pd.ExcelWriter(file_directory_resalts_groupby, engine='xlsxwriter') # + file_name
df_out_groupby.to_excel(writer_1, sheet_name='Sheet1', index=False) # Определяем сохранение xlsx методом ExcelWriter
workbook = writer_1.book #записываем объект 'xlsxwriter' в книгу, для последующих назначений форматов
format1 = workbook.add_format({'num_format': '#,##0.00'}) # Формат для колоноц с ценами
sheet_1 = writer_1.sheets['Sheet1'] # Определяем лист для форматирования
# Закрепляем шапку
sheet_1.freeze_panes(1, 0)

sheet_1.set_column(0, 0, 18) # Марка
sheet_1.set_column(1, 1, 7) # NxS
sheet_1.set_column(2, 2, 15) # Габариты КНС
sheet_1.set_column(3, 3, 40) # Обозначение КНС
sheet_1.set_column(4, 4, 13, format1) # Длина в КНС
writer_1._save()
