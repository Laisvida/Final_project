# SPORTO VARŽYBŲ ANALIZĖ

## Detalės

### Sukūrė : Simonas Lekys ir Laisvida Pabrėžienė

Tai UAB Programavimo mokykla (Vilnius Coding school) organizuojamo neformalaus suaugusiųjų švietimo
programos Duomenų analitika ir Python programavimo pagrindai baigiamasis darbas.
Projekto tema : Sporto varžybų analizė ir vizualizacija

Pagrindinis projekto tikslas – išnagrinėti Lietuvos moterų krepšinio lygos A diviziono varžybų duomenis
pagal sezonus, pradedant 2018/2019 ir baigiant 2022/2023 metų sezonu.
Įvertinti krepšininkių ir komandų rezultatus pagal mūsų surinktus duomenis.
Atlikti palyginamąją analizę tarp _skirtingų sezonų, sportininkių ir komandų_.

Šiame projekte išsamiai analizei atlikti bei praktikoje pritaikyti išmoktą teoriją, naudojome Python
programavimo kalbą, CSV failus ir _PostgreSQL duomenų bazę_.

### Taikomosios žinios:
Naudojamos bibliotekos: BeautifulSoup, Pandas, MatplotLib, SeaBorn, Selenium,..........

### postgres .py
_Naudotas duomenų bazės adapteris: psycopg2_
  1.
  2.
  3.

### web_scrap .py 

Duomenų gavimas iš URL ( https://moterulyga.lt/lygos/164-moteru-lkl-a-divizionas/statistika.html)

Baigiamasis_darbas.py
Tai yra pagrindinė projekto byla, kurioje buvo atlikta visa analizė. _Visi vaizdai yra valdomi funkcijomis, kurios
padeda atskirti visus kode esančius grafikus.
_

![Top 5 taiklausios žaidėjos 2018-2023 metais](https://github.com/Laisvida/Final_project/blob/main/Top%205%20pagal%20metim%C5%B3%20pataikymo%20procent%C4%85.PNG)

![Top 5 taiklausios žaidėjos 2018-2023 metais](./main/Top%205%20pagal%20metim%C5%B3%20pataikymo%20procent%C4%85.PNG)

![Top 5 daugiausia laiko žaidžiančios žaidėjos]([./main/Top%205%20daugiausiai%20laiko%20%C5%BEaid%C5%BEian%C4%8Dios%20krep%C5%A1inink%C4%97s.PNG]

![Top 5 daugiausia laiko žaidžiančios žaidėjos](https://github.com/Laisvida/Final_project/blob/main/Top%205%20daugiausiai%20laiko%20%C5%BEaid%C5%BEian%C4%8Dios%20krep%C5%A1inink%C4%97s.PNG))

