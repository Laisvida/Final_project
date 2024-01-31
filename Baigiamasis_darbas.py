import requests
from bs4 import BeautifulSoup
import pandas as pd
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

years = list(range(2018, 2023))
data_list = []
column_names = ["Metai", "Nr.", "Zaideja", "EFF", "PTS", "FG%", "FT%", "REB", "AST", "BS", "ST", "TO", "MIN"]

for year in years:
    url = url_start.format(year)
    url_pts_year = url_pts.format(year)
    url_fg_year = url_fg.format(year)
    url_ft_year = url_ft.format(year)
    url_reb_year = url_reb.format(year)
    url_ast_year = url_ast.format(year)
    url_st_year = url_st.format(year)
    url_to_year = url_to.format(year)
    url_min_year = url_min.format(year)

    response_eff = requests.get(url)
    response_pts = requests.get(url_pts_year)
    response_fg = requests.get(url_fg_year)
    response_ft = requests.get(url_ft_year)
    response_reb = requests.get(url_reb_year)
    response_ast = requests.get(url_ast_year)
    response_st = requests.get(url_st_year)
    response_to = requests.get(url_to_year)
    response_min = requests.get(url_min_year)

    soup_eff = BeautifulSoup(response_eff.text, 'html.parser')
    soup_pts = BeautifulSoup(response_pts.text, 'html.parser')
    soup_fg = BeautifulSoup(response_fg.text, 'html.parser')
    soup_ft = BeautifulSoup(response_ft.text, 'html.parser')
    soup_reb = BeautifulSoup(response_reb.text, 'html.parser')
    soup_ast = BeautifulSoup(response_ast.text, 'html.parser')
    soup_st = BeautifulSoup(response_st.text, 'html.parser')
    soup_to = BeautifulSoup(response_to.text, 'html.parser')
    soup_min = BeautifulSoup(response_min.text, 'html.parser')

    table_eff = soup_eff.find('table', class_='list02')
    table_pts = soup_pts.find('table', class_='list02')
    table_fg = soup_fg.find('table', class_='list02')
    table_ft = soup_ft.find('table', class_='list02')
    table_reb = soup_reb.find('table', class_='list02')
    table_ast = soup_ast.find('table', class_='list02')
    table_st = soup_st.find('table', class_='list02')
    table_to = soup_to.find('table', class_='list02')
    table_min = soup_min.find('table', class_='list02')

    if table_eff and table_pts and table_fg and table_ft and table_reb and table_ast and table_st and table_to and table_min:
        body_eff = table_eff.find("tbody")
        body_pts = table_pts.find("tbody")
        body_fg = table_fg.find("tbody")
        body_ft = table_ft.find("tbody")
        body_reb = table_reb.find("tbody")
        body_ast = table_ast.find("tbody")
        body_st = table_st.find("tbody")
        body_to = table_to.find("tbody")
        body_min = table_min.find("tbody")

        if body_eff and body_pts and body_fg and body_ft and body_reb and body_ast and body_st and body_to and body_min:
            rows_eff = body_eff.find_all("tr")
            rows_pts = body_pts.find_all("tr")
            rows_fg = body_fg.find_all("tr")
            rows_ft = body_ft.find_all("tr")
            rows_reb = body_reb.find_all("tr")
            rows_ast = body_ast.find_all("tr")
            rows_st = body_st.find_all("tr")
            rows_to = body_to.find_all("tr")
            rows_min = body_min.find_all("tr")

            for row_eff, row_pts, row_fg, row_ft, row_reb, row_ast, row_st, row_to, row_min in zip(rows_eff, rows_pts[:-1], rows_fg[:-1], rows_ft[:-1], rows_reb[:-1], rows_ast[:-1], rows_st[:-1], rows_to[:-1], rows_min[:-1]):
                columns_eff = row_eff.select("td")
                columns_pts = row_pts.select("td")
                columns_fg = row_fg.select("td")
                columns_ft = row_ft.select("td")
                columns_reb = row_reb.select("td")
                columns_ast = row_ast.select("td")
                columns_st = row_st.select("td")
                columns_to = row_to.select("td")
                columns_min = row_min.select("td")

                if len(columns_eff) >= 6 and len(columns_pts) >= 1 and len(columns_fg) >= 1 and len(columns_ft) >= 1 and len(columns_reb) >= 1 and len(columns_ast) >= 1 and len(columns_st) >= 1 and len(columns_to) >= 1 and len(columns_min) >= 1:
                    if all(col.text.strip() for col in columns_eff[:-3]):
                        data = [year] + [col.text.strip() for col in columns_eff[:-3]]
                        pts = [col.text.strip() for col in columns_pts[2]]
                        fg = [col.text.strip() for col in columns_fg[2]]
                        ft = [col.text.strip() for col in columns_ft[2]]
                        reb = [col.text.strip() for col in columns_reb[2]]
                        ast = [col.text.strip() for col in columns_ast[2]]
                        st = [col.text.strip() for col in columns_st[2]]
                        to = [col.text.strip() for col in columns_to[2]]
                        min = [col.text.strip() for col in columns_min[2]]

                        data_list.append(data + pts + fg + ft + reb + ast + st + to + min)


df = pd.DataFrame(data_list, columns=column_names)
df.to_csv('LMKL_statistika.csv', index=False)
print(df)