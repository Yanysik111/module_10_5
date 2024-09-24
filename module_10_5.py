import multiprocessing
import datetime

#Линейный вызов:0:00:05.477162
#Многопроцессный:0:00:08.691569
def read_info(name):
    all_data = []

    with open(name) as file:
        for line in file:
            if line == '\n':  # Проверяем, является ли строка пустой
                break
            else:
                all_data.append(line)  # Удаляем лишние символы и добавляем строку в список
    return all_data


filenames = [f'./file {number}.txt' for number in range(1, 5)]

start_1 = datetime.datetime.now()
for file in filenames:
    read_info(file)

end_1 = datetime.datetime.now()
print(f'Линейный вызов:{end_1 - start_1}')

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start_2 = datetime.datetime.now()
        pool.map(read_info, filenames)



        end_2 = datetime.datetime.now()
        print(f'Многопроцессный:{end_2 - start_2}')