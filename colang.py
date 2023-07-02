import pandas as pd
import country_to_continent
import requests
from bs4 import BeautifulSoup
import re

mapping = country_to_continent.COUNTRY_ALPHA2_TO_CONTINENT


df = pd.read_csv('country.csv')
# print('number of columns: ', len(df.columns))
num_rows = len(df.index)
# print('number of rows: ', num_rows)


def code_to_continent(country_2_code):
    """Convert country code to continent.
    """
    if country_2_code not in mapping:
        return "Not Applicable"

    return mapping[country_2_code].lower()


def get_lang_num(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="country_b2")
    # print(results.prettify())
    if results is None:
        print('Not Applicable')
        return 'N/A', '0.0 %'
    job_elements = results.find_all("table", class_="std100 hover")
    table = job_elements[0]

    ''' to get all languages use this
    for row in table.findAll("tr"):
        cells = row.findAll("td")
        print(cells)
    '''
    rows = table.findAll("tr")
    # print(len(rows))
    if len(rows) < 2:
        print('Not Applicable')
        return 'N/A', '0.0 %'
    row = rows[1]
    print(row.text)
    lang_num_pair = re.findall('\d*\D+', row.text)
    lang = lang_num_pair[0]
    num = lang_num_pair[1]+lang_num_pair[2]
    print(lang)
    print(num)
    return lang, num


if __name__ == '__main__':

    #print(df.to_string())

    continent_names = []
    main_languages = []
    percentages = []
    for i in range(num_rows):
        country_code = df.iloc[i][0].upper()
        continent_name = code_to_continent(country_code)
        continent_names.append(continent_name)

        if continent_name == 'south america' or continent_name == 'north america':
            continent_name = 'america'
        country_name = df.iloc[i][1].lower()
        country_name = country_name.replace(' ', '-')
        URL = "https://www.worlddata.info/%s/%s/index.php" % (continent_name, country_name)
        print(country_name)
        lang, num = get_lang_num(URL)
        main_languages.append(lang)
        percentages.append(num)

    df['continent'] = continent_names
    df['main_language'] = main_languages
    df['percentage'] = percentages

    print(df.to_string())
    df.to_csv('languages.csv', sep='\t', encoding='utf-8')


    # URL = "https://www.worlddata.info/america/usa/index.php"
    # get_lang_num(URL)







