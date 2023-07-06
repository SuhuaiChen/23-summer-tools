# 23-summer-tools

这里有三个简单的小工具～
1. 整合多语言json到同一个csv文件, 每一条内容一一对应 
   - 将所有要整合的多语言的json文件放入这个文件夹
   - 生成的csv的每一列的名称会与各个文件名相同，所以最好提前改好文件名
   - 建议用mac内置的numbers打开生成的`translation.csv`

2. 爬取各国的人口和语言数据，可以进行适当改动爬取其它数据
   - 首先要提供一个csv，它的第一列是想要查找的国家的代码，例子可见country.csv
   - 如果只有国家名，没有国家代码，可以用pycountry转换: ``pycountry.countries.get(name='American Samoa').alpha2``

3. 给反馈自动打标签，并汇总到excel文件 (demo)
   - 需要提供 `input.xlsx`

### Run on terminal

#### Clone the repo

```
git clone https://github.com/SuhuaiChen/23-summer-tools.git
```

##### Install pip
```
python3 -m pip install --user --upgrade pip
python3 -m pip --version
```

##### Install dependencies
```
pip install requirements.txt
```

#### Running the translation helper
```
python3 translation_helper.py
```

#### Running the scrawler
```
python3 colang.py
```

#### Running the tagger
```
python3 feedback_classifify.py
```
