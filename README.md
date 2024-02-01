# SPORTO VARŽYBŲ ANALIZĖ

## Detalės

### Sukūrė : Simonas Lekys ir Laisvida Pabrėžienė

Tai UAB Programavimo mokykla (Vilnius Coding school) organizuojamo neformalaus suaugusiųjų švietimo
programos Duomenų analitika ir Python programavimo pagrindai baigiamasis darbas.
Projekto tema : Sporto varžybų analizė ir vizualizacija

Pagrindinis projekto tikslas – išnagrinėti Lietuvos moterų krepšinio lygos A diviziono varžybų duomenis
pagal sezonus, pradedant 2018/2019 ir baigiant 2022/2023 metų sezonu.
Įvertinti krepšininkių  rezultatus pagal mūsų surinktus duomenis.
Atlikti palyginamąją analizę, išrinkti TOP 5 visų sezonų žaidėjas.

Šiame projekte išsamiai analizei atlikti bei praktikoje pritaikyti išmoktą teoriją, naudojome Python
programavimo kalbą, CSV failus.

### Taikomosios žinios:
Naudojamos bibliotekos: BeautifulSoup, Pandas, MatplotLib, Seaborn, NumPy, PIL

### web_scrap .py 

Duomenų gavimas iš URL ( https://moterulyga.lt/lygos/164-moteru-lkl-a-divizionas/statistika.html). 
Reikalingų lentelių (informacijos) išgavimas naudojantis Beautiful soup pagal atitinkamas statistines katerorijas.
Naudojantis IF funkcija sukurta data_list'ai kiekvienai kategorijai.
Naudojantis Pandas DataFrame perkelti visi data_listai į bendrą lentelę.

### Baigiamasis_darbas.py

Tai yra pagrindinė projekto byla, kurioje buvo atlikta visa analizė. _Visi vaizdai yra valdomi funkcijomis, kurios
padeda atskirti visus kode esančius grafikus.


Iš surinktų duomenų išrinkome visų sezonų taikliausias žaidėjas ir atvaizdavome grafike

![Top 5 taiklausios žaidėjos 2018-2022 metais](https://github.com/Laisvida/Final_project/blob/main/Top%205%20pagal%20metim%C5%B3%20pataikymo%20procent%C4%85.PNG)


Šiame grafike atvaizdavome 5 visų mūsų nagrinėtų sezonų krepšininkes, kurios žaidžia daugiausiai laiko per varžybas.

![Top 5 daugiausia laiko žaidžiančios žaidėjos](https://github.com/Laisvida/Final_project/blob/main/Top%205%20daugiausiai%20laiko%20%C5%BEaid%C5%BEian%C4%8Dios%20krep%C5%A1inink%C4%97s.PNG)


Varžybų rezultatui didelę įtaką daro rezultatyvūs perdavimai. Grafike vizualizavome 5 geriausias sportininkes pagal rezultatyvius perdavimus 


![Top 5 pagal rezultatyvius perdavimus](https://github.com/Laisvida/Final_project/blob/main/Top_5_pagal_rezultatyvius_perdavimus.png)


Norėjome panaudoti išmoktas žinias, sukūrėme koreliacijos matricą, kuri matuoja koreliacijos koeficientus tarp stulpelių 'EFF', 'PTS', 'TO', 'ST', 'MIN' ir 'REB'.

Pritaikėme seaborn biblioteką koreliacijos matricos vizualizacijai , formatas '.2f' nurodo, kad skaičiai bus rodomi su dviem skaičiais po kablelio.
Galutinis rezultatas parodo koreliacijos koeficientus tarp 'EFF', 'PTS', 'TO', 'ST', 'MIN' ir 'REB' stulpelių. Tai gali padėti identifikuoti, kaip šie statistikos rodikliai yra susiję tarpusavyje.
Matrica vizualiai atspindi, kokio stiprumo yra koreliacija tarp šių skaičiavimo stulpelių.


![Koreliacija tarp pasirinktų statistinių rodiklių](https://github.com/Laisvida/Final_project/blob/main/Koreliacija%20tarp%20pasirinkt%C5%B3%20statistini%C5%B3%20rodikli%C5%B3.PNG)

![Koreliacija tarp pasirinktų statistinių rodiklių](./main/Koreliacija%20tarp%20pasirinkt%C5%B3%20statistini%C5%B3%20rodikli%C5%B3.PNG)





![Logotipas](https://github.com/Laisvida/Final_project/blob/main/Logo.PNG)







