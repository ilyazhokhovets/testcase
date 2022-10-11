# стандартная питовновская библиотека
import re
#максимальная длина пути
MAX_LENGTH = 255

#различные примеры
d = {'dir1': {'dir_2': ['file1'], 'dir3': ['file2']}, 'dir4': {}}
d1 = {'dir1': {}, 'dir2': ['file1'], 'dir3': {'dir4': ['file2'], 'dir5': {'dir6': {'dir7': {}}}}}
d2 = {'dir1': ['file1', 'file1']}
d3 = {'dir1': ['file1', 'file2', 'file2']}


def biggestPath(X):

    #делаем обход в ширину
    que = []
    depth = 1
    res = {'path': '/', 'depth': 0}
    que.append({'subdirs': X,'depth': depth, 'path': ''})
    while que:
        current_dir = que[0]
        que.pop(0)

        #проверка на то конечная ли директория
        if isinstance(current_dir['subdirs'], dict) and current_dir['subdirs']:

            # Итерируемся по подкаталогам
            # Если название соответсвует критерию и не превышена длина, добавляем в очередь
            for subdir_name in current_dir['subdirs']:
                new_path = f'{current_dir["path"]}/{subdir_name}'
                if re.match(r"[a-zA-Z0-9]*$", subdir_name) and len(new_path) <= MAX_LENGTH:
                    que.append({'subdirs': current_dir['subdirs'][subdir_name],
                                'depth': current_dir['depth']+1,
                                'path': f'{current_dir["path"]}/{subdir_name}'})

        # Проверяет, что в каталоге находятся файлы
        elif isinstance(current_dir['subdirs'], list) and current_dir['depth'] > res['depth']:
            file_list = current_dir['subdirs']
            new_path = f'{current_dir["path"]}/{file_list[0]}'

            # Здесь немного непонятно. В услувии сказано, что путь некорректен, если в папке есть
            # одинаковые файлы. Однако в 3 примере выводится непустой путь.
            # То что в комментарии это, если ориенироваться на условия, то что в коде - если на пример
            if file_list.count(file_list[0]) == 1 and len(new_path) <= MAX_LENGTH:
            #if len(file_list) == len(set(file_list)) and len(new_path) <= MAX_LENGTH:
                res['depth'] = current_dir['depth']
                res['path'] = f'{current_dir["path"]}/{file_list[0]}'

        #Если конец самого длинного пути заканчивается пустой папкой
        elif isinstance(current_dir['subdirs'], dict) and current_dir['depth'] - 1 > res['depth']:
                res['depth'] = current_dir['depth'] - 1
                res['path'] = f'{current_dir["path"]}'

    return res['path']


print(biggestPath(d1))
