import requests
import seaborn as sns
from bs4 import BeautifulSoup
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image

#pasirenkame 10 statistinių kategorijų, kur nurodome jų pradinius tinklapius, o vietoje konkrečių metų pakeičiame į {}
url_start = "https://moterulyga.lt/lygos/164-moteru-lkl-a-divizionas/statistika.html?fgroup=players&fseason={}&fmonth=0&stage=0&fpos=eff&sort=average&games_type=all"
url_pts = "https://moterulyga.lt/lygos/164-moteru-lkl-a-divizionas/statistika.html?fgroup=players&fseason={}&fmonth=0&stage=0&fpos=pts&sort=average&games_type=all"
url_fg = "https://moterulyga.lt/lygos/164-moteru-lkl-a-divizionas/statistika.html?fgroup=players&fseason={}&fmonth=0&stage=0&fpos=fg&sort=average&games_type=all"
url_ft = "https://moterulyga.lt/lygos/164-moteru-lkl-a-divizionas/statistika.html?fgroup=players&fseason={}&fmonth=0&stage=0&fpos=1pts&sort=average&games_type=all"
url_reb = "https://moterulyga.lt/lygos/164-moteru-lkl-a-divizionas/statistika.html?fgroup=players&fseason={}&fmonth=0&stage=0&fpos=reb&sort=average&games_type=all"
url_ast = "https://moterulyga.lt/lygos/164-moteru-lkl-a-divizionas/statistika.html?fgroup=players&fseason={}&fmonth=0&stage=0&fpos=as&sort=average&games_type=all"
url_bs = "https://moterulyga.lt/lygos/164-moteru-lkl-a-divizionas/statistika.html?fgroup=players&fseason={}&fmonth=0&stage=0&fpos=bs&sort=average&games_type=all"
url_st = "https://moterulyga.lt/lygos/164-moteru-lkl-a-divizionas/statistika.html?fgroup=players&fseason={}&fmonth=0&stage=0&fpos=st&sort=average&games_type=all"
url_to = "https://moterulyga.lt/lygos/164-moteru-lkl-a-divizionas/statistika.html?fgroup=players&fseason={}&fmonth=0&stage=0&fpos=to&sort=average&games_type=all"
url_min = "https://moterulyga.lt/lygos/164-moteru-lkl-a-divizionas/statistika.html?fgroup=players&fseason={}&fmonth=0&stage=0&fpos=min&sort=average&games_type=all"

#pasirenkame analizuojamus sezonus
years = list(range(2018, 2023))
#sukuriame data_list'us kiekvienai analizuojamai kategorijai, kad galėtume vėliau sukurti DataFrame
data_list_eff = []
data_list_pts = []
data_list_fg = []
data_list_ft = []
data_list_reb = []
data_list_ast = []
data_list_bs = []
data_list_st = []
data_list_to = []
data_list_min = []
data_list = []

#sukuriame stulpelių pavadinimus savo busiems DataFrame
column_names = {
    "EFF": ["Metai", "Nr", "Žaidėja", "EFF", "Komanda"],
    "PTS": ["Metai", "Nr", "Žaidėja", "PTS", "Komanda"],
    "FG%": ["Metai", "Nr", "Žaidėja", "FG%", "Komanda"],
    "FT%": ["Metai", "Nr", "Žaidėja", "FT%", "Komanda"],
    "REB": ["Metai", "Nr", "Žaidėja", "REB", "Komanda"],
    "AST": ["Metai", "Nr", "Žaidėja", "AST", "Komanda"],
    "BS": ["Metai", "Nr", "Žaidėja", "BS", "Komanda"],
    "ST": ["Metai", "Nr", "Žaidėja", "ST", "Komanda"],
    "TO": ["Metai", "Nr", "Žaidėja", "TO", "Komanda"],
    "MIN": ["Metai", "Nr", "Žaidėja", "MIN", "Komanda"],
}

#Sukuriame ciklus, kurie sukuria url adresus pagal year listą
for year in years:
    url = url_start.format(year)
    url_pts_year = url_pts.format(year)
    url_fg_year = url_fg.format(year)
    url_ft_year = url_ft.format(year)
    url_reb_year = url_reb.format(year)
    url_ast_year = url_ast.format(year)
    url_bs_year = url_bs.format(year)
    url_st_year = url_st.format(year)
    url_to_year = url_to.format(year)
    url_min_year = url_min.format(year)

#Sukuriame užklausas į nurodytus URL adresus
    response_eff = requests.get(url)
    response_pts = requests.get(url_pts_year)
    response_fg = requests.get(url_fg_year)
    response_ft = requests.get(url_ft_year)
    response_reb = requests.get(url_reb_year)
    response_ast = requests.get(url_ast_year)
    response_bs = requests.get(url_bs_year)
    response_st = requests.get(url_st_year)
    response_to = requests.get(url_to_year)
    response_min = requests.get(url_min_year)

#Su BeautifulSoup pagalba perkeliame internete esantį turinį
    soup_eff = BeautifulSoup(response_eff.text, 'html.parser')
    soup_pts = BeautifulSoup(response_pts.text, 'html.parser')
    soup_fg = BeautifulSoup(response_fg.text, 'html.parser')
    soup_ft = BeautifulSoup(response_ft.text, 'html.parser')
    soup_reb = BeautifulSoup(response_reb.text, 'html.parser')
    soup_ast = BeautifulSoup(response_ast.text, 'html.parser')
    soup_bs = BeautifulSoup(response_bs.text, 'html.parser')
    soup_st = BeautifulSoup(response_st.text, 'html.parser')
    soup_to = BeautifulSoup(response_to.text, 'html.parser')
    soup_min = BeautifulSoup(response_min.text, 'html.parser')

#Ieškome lentelės su clasės pavadinimu list02
    table_eff = soup_eff.find('table', class_='list02')
    table_pts = soup_pts.find('table', class_='list02')
    table_fg = soup_fg.find('table', class_='list02')
    table_ft = soup_ft.find('table', class_='list02')
    table_reb = soup_reb.find('table', class_='list02')
    table_ast = soup_ast.find('table', class_='list02')
    table_bs = soup_bs.find('table', class_='list02')
    table_st = soup_st.find('table', class_='list02')
    table_to = soup_to.find('table', class_='list02')
    table_min = soup_min.find('table', class_='list02')

#Lentelėje ieškome ar yra elementas tbody
    if table_eff and table_pts and table_fg and table_ft and table_reb and table_ast and table_bs and table_st and table_to and table_min:
        body_eff = table_eff.find("tbody")
        body_pts = table_pts.find("tbody")
        body_fg = table_fg.find("tbody")
        body_ft = table_ft.find("tbody")
        body_reb = table_reb.find("tbody")
        body_ast = table_ast.find("tbody")
        body_bs = table_bs.find("tbody")
        body_st = table_st.find("tbody")
        body_to = table_to.find("tbody")
        body_min = table_min.find("tbody")

#Elmente tbody ieškome elementų tr
        if body_eff and body_pts and body_fg and body_ft and body_reb and body_ast and body_bs and body_st and body_to and body_min:
            rows_eff = body_eff.find_all("tr")
            rows_pts = body_pts.find_all("tr")
            rows_fg = body_fg.find_all("tr")
            rows_ft = body_ft.find_all("tr")
            rows_reb = body_reb.find_all("tr")
            rows_ast = body_ast.find_all("tr")
            rows_bs = body_bs.find_all("tr")
            rows_st = body_st.find_all("tr")
            rows_to = body_to.find_all("tr")
            rows_min = body_min.find_all("tr")

#Ieškome stulpelių td
            for row_eff, row_pts, row_fg, row_ft, row_reb, row_ast, row_bs, row_st, row_to, row_min in zip(rows_eff, rows_pts, rows_fg, rows_ft, rows_reb, rows_ast, rows_bs, rows_st, rows_to, rows_min):
                columns_eff = row_eff.select("td")
                columns_pts = row_pts.select("td")
                columns_fg = row_fg.select("td")
                columns_ft = row_ft.select("td")
                columns_reb = row_reb.select("td")
                columns_ast = row_ast.select("td")
                columns_bs = row_bs.select("td")
                columns_st = row_st.select("td")
                columns_to = row_to.select("td")
                columns_min = row_min.select("td")

#Apsirašome sąlygas, kokių reikia galutinių duomenų iš lentelių, t. y. tikriname ar šaltiniuose yra daugiau nei 6
# stulpeliai, pašaliname 3 paskutinius stulpelius, sukuriame data listą, ir perkeliame jį į sąrašą.
                if (len(columns_eff) >= 6
                        and len(columns_pts) >= 6 and len(columns_fg) >= 6 and len(columns_ft) >= 6 and len(
                            columns_reb) >= 6 and len(columns_ast) >= 6 and len (columns_bs) >= 6 and len(
                            columns_st) >= 6 and len(columns_to) >= 6 and len(columns_min) >= 6):
                    if all(col.text.strip() for col in columns_eff[:-3]):
                        data_eff = [year] + [col.text.strip() for col in columns_eff[:-3]]
                        data_list_eff.append(data_eff)

                if(len(columns_pts) >=6
                        and len(columns_eff) >= 6 and len(columns_fg) >= 6 and len(columns_ft) >= 6 and len(
                            columns_reb) >= 6 and len(columns_ast) >= 6 and len(columns_bs) >= 6 and len(
                            columns_st) >= 6 and len(columns_to) >= 6 and len(columns_min) >= 6):
                    if all(col.text.strip() for col in columns_pts[:-3]):
                        data_pts = [year] + [col.text.strip() for col in columns_pts[:-3]]
                        data_list_pts.append(data_pts)

                if (len(columns_fg) >= 6
                        and len(columns_eff) >= 6 and len(columns_pts) >= 6 and len(columns_ft) >= 6 and len(
                            columns_reb) >= 6 and len(columns_ast) >= 6 and len(columns_bs) >= 6 and len(
                            columns_st) >= 6 and len(columns_to) >= 6 and len(columns_min) >= 6):
                    if all(col.text.strip() for col in columns_fg[:-2]):
                        data_fg = [year] + [col.text.strip() for col in columns_fg[:-2]]
                        data_list_fg.append(data_fg)

                if (len(columns_ft) >= 6
                        and len(columns_eff) >= 6 and len(columns_pts) >= 6 and len(columns_fg) >= 6 and len(
                            columns_reb) >= 6 and len(columns_ast) >= 6 and len(columns_bs) >= 6 and len(
                            columns_st) >= 6 and len(columns_to) >= 6 and len(columns_min) >= 6):
                    if all(col.text.strip() for col in columns_ft[:-2]):
                        data_ft = [year] + [col.text.strip() for col in columns_ft[:-2]]
                        data_list_ft.append(data_ft)

                if (len(columns_reb) >= 6
                        and len(columns_eff) >= 6 and len(columns_pts) >= 6 and len(columns_ft) >= 6 and len(
                            columns_ft) >= 6 and len(columns_ast) >= 6 and len(columns_bs) >= 6 and len(
                            columns_st) >= 6 and len(columns_to) >= 6 and len(columns_min) >= 6):
                    if all(col.text.strip() for col in columns_reb[:-3]):
                        data_reb = [year] + [col.text.strip() for col in columns_reb[:-3]]
                        data_list_reb.append(data_reb)

                if (len(columns_ast) >= 6
                        and len(columns_eff) >= 6 and len(columns_pts) >= 6 and len(columns_ft) >= 6 and len(
                            columns_ft) >= 6 and len(columns_reb) >= 6 and len(columns_bs) >= 6 and len(
                            columns_st) >= 6 and len(columns_to) >= 6 and len(columns_min) >= 6):
                    if all(col.text.strip() for col in columns_ast[:-3]):
                        data_ast = [year] + [col.text.strip() for col in columns_ast[:-3]]
                        data_list_ast.append(data_ast)

                if (len(columns_bs) >= 6
                        and len(columns_eff) >= 6 and len(columns_pts) >= 6 and len(columns_ft) >= 6 and len(
                            columns_ft) >= 6 and len(columns_reb) >= 6 and len(columns_ast) >= 6 and len(
                            columns_st) >= 6 and len(columns_to) >= 6 and len(columns_min) >= 6):
                    if all(col.text.strip() for col in columns_bs[:-3]):
                        data_bs = [year] + [col.text.strip() for col in columns_bs[:-3]]
                        data_list_bs.append(data_bs)

                if (len(columns_st) >= 6
                        and len(columns_eff) >= 6 and len(columns_pts) >= 6 and len(columns_ft) >= 6 and len(
                            columns_ft) >= 6 and len(columns_reb) >= 6 and len(columns_ast) >= 6 and len(
                            columns_bs) >= 6 and len(columns_to) >= 6 and len(columns_min) >= 6):
                    if all(col.text.strip() for col in columns_st[:-3]):
                        data_st = [year] + [col.text.strip() for col in columns_st[:-3]]
                        data_list_st.append(data_st)
                if (len(columns_to) >= 6
                        and len(columns_eff) >= 6 and len(columns_pts) >= 6 and len(columns_ft) >= 6 and len(
                            columns_ft) >= 6 and len(columns_reb) >= 6 and len(columns_ast) >= 6 and len(
                            columns_bs) >= 6 and len(columns_st) >= 6 and len(columns_min) >= 6):
                    if all(col.text.strip() for col in columns_to[:-3]):
                        data_to = [year] + [col.text.strip() for col in columns_to[:-3]]
                        data_list_to.append(data_to)

                if (len(columns_min) >= 6
                        and len(columns_eff) >= 6 and len(columns_pts) >= 6 and len(columns_ft) >= 6 and len(
                            columns_ft) >= 6 and len(columns_reb) >= 6 and len(columns_ast) >= 6 and len(
                            columns_bs) >= 6 and len(columns_st) >= 6 and len(columns_to) >= 6):
                    if all(col.text.strip() for col in columns_min[:-3]):
                        data_min = [year] + [col.text.strip() for col in columns_min[:-3]]
                        data_list_min.append(data_min)

# Kiekvienai statistinei kategorijai sukuriame DataFrame
df_eff = pd.DataFrame(data_list_eff, columns=column_names['EFF'])
df_pts = pd.DataFrame(data_list_pts, columns=column_names['PTS'])
df_fg = pd.DataFrame(data_list_fg, columns=column_names['FG%'])
df_ft = pd.DataFrame(data_list_ft, columns=column_names['FT%'])
df_reb = pd.DataFrame(data_list_reb, columns=column_names['REB'])
df_ast = pd.DataFrame(data_list_ast, columns=column_names['AST'])
df_bs = pd.DataFrame(data_list_bs, columns=column_names['BS'])
df_st = pd.DataFrame(data_list_st, columns=column_names['ST'])
df_to = pd.DataFrame(data_list_to, columns=column_names['TO'])
df_min = pd.DataFrame(data_list_min, columns=column_names['MIN'])

# Sujungiame visus DataFrame į vieną failą
result_df = pd.concat(
    [df_eff, df_pts, df_fg, df_ft, df_reb, df_ast, df_bs, df_st, df_to, df_min], axis=1)
# result_df.to_csv('LMKL_statistika.csv', index=False)

# Sukuriame top5 AST žaidėjų grafiką
df_ast['AST'] = pd.to_numeric(df_ast['AST'].str.replace(',', '.'))
df_ast_top5 = df_ast.sort_values(by='AST', ascending=False).head(8)
plt.figure(figsize=(8, 12))
plt.bar(df_ast_top5['Žaidėja'], df_ast_top5['AST'], color='green')
plt.title('Geriausios 5 žaidėjos pagal rezultatyvius perdavimus')
plt.xlabel('Žaidėja')
plt.ylabel('Rezultatyvūs perdavimai')
plt.xticks(rotation=35, ha='right', fontsize=10)
for i, v in enumerate(df_ast_top5['AST']):
    plt.text(i, v, str(round(v, 2)), ha='center', va='bottom', fontsize=12)

# Sukuriame top5 FG% žaidėjų sąrašą
df_fg['FG%'] = pd.to_numeric(df_fg['FG%'].str.replace(',', '.').str.replace('%', ''))
df_fg_top5 = df_fg.sort_values(by='FG%', ascending=False).head(5)
plt.figure(figsize=(8, 12))
plt.bar(df_fg_top5['Žaidėja'], df_fg_top5['FG%'], color='orange')
plt.title('Geriausios 5 žaidėjos pagal metimų iš žaidimo pataikymo procentą (2018/2022)')
plt.xlabel('Žaidėjas')
plt.ylabel('Metimų iš žaidimo procentas')
plt.xticks(rotation=35, ha='right', fontsize=10)
for i, v in enumerate(df_fg_top5['FG%']):
    plt.text(i, v + 1, str(round(v, 2)), ha='center', va='bottom', fontsize=12)

# Sukuriame top5 MIN žaidėjų sąrašą
df_min['MIN'] = pd.to_numeric(df_min['MIN'].str.replace(',', '.'))
df_min_top5 = df_min.sort_values(by='MIN', ascending=False).head(5)
plt.figure(figsize=(8, 12))
plt.bar(df_min_top5['Žaidėja'], df_min_top5['MIN'], color='blue')
plt.title('5 vidutiniškai daugiausiai laiko žaidžiančios krepšininkės (2018/2022)')
plt.xlabel('Žaidėja')
plt.ylabel('Vidutiniškas MIN skaičius per varžybas')
plt.xticks(rotation=35, ha='right', fontsize=10)
for i, v in enumerate(df_min_top5['MIN']):
    plt.text(i, v + 1, str(round(v, 2)), ha='center', va='bottom', fontsize=12)

# Sukuriame koreliacijos matricą pagal pasirinktus rodiklius
result_df['EFF'] = result_df['EFF'].str.replace(',', '.').astype(float)
result_df['PTS'] = result_df['PTS'].str.replace(',', '.').astype(float)
result_df['TO'] = result_df['TO'].str.replace(',', '.').astype(float)
result_df['ST'] = result_df['ST'].str.replace(',', '.').astype(float)
result_df['MIN'] = result_df['MIN'].str.replace(',', '.').astype(float)
result_df['REB'] = result_df['REB'].str.replace(',', '.').astype(float)

corellation_matrix = result_df[['EFF', 'PTS', 'TO', 'ST', 'MIN', 'REB']].corr()

# Sukuriame koreliacijos matricos diagramą
plt.figure(figsize=(10, 8))
sns.heatmap(corellation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Koreliacija tarp EFF, PTS, TO, ST, MIN ir REB statistikos rodiklių')

# Atliekame LMKL logotipo pakeitimus pagal spalvas
image = Image.open('MLKL_logo.jpg')
image_array = np.array(image)


def rgb2grey(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])


def normalize_image(image_array):
    return image_array / 255.0


gray_image_array = rgb2grey(image_array)
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.imshow(image)
plt.title('Originali nuotrauka')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(gray_image_array, cmap=plt.get_cmap('gray'))
plt.title('Pilka')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(normalize_image(gray_image_array))
plt.title('Po normalizacijos')
plt.axis('off')





