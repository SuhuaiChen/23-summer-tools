import pandas as pd
import json
import glob

f_names = glob.glob("*.json")

if '中文.json' not in f_names:
    print('缺少中文json文件')

else:
    # put to the front
    f_names.remove('中文.json')
    f_names.append('中文.json')

    df = pd.DataFrame()
    while f_names:
        f_name = f_names.pop()
        f = open(f_name)
        data = json.load(f)

        new_col = []
        for key in data.keys():
            new_col.append(data[key])
            # print(key)

        idx = len(f_name)-5
        col_name = f_name[:idx]
        df[col_name] = new_col

    df.to_csv('translation.csv', encoding='utf-8')
