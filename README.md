1. Pandas
Opis
Pandas to potężna biblioteka do manipulacji i analizy danych. Oferuje struktury danych takie jak DataFrame, które umożliwiają efektywne czyszczenie, transformowanie i analizowanie danych.

Zalety:
Intuicyjna obsługa danych tabelarycznych

Bogate funkcje do grupowania, agregacji i łączenia danych

Integracja z wieloma formatami danych (CSV, Excel, SQL, JSON)

Dobrze udokumentowana z aktywną społecznością

Przykłady użycia:
Przykład 1: Wczytywanie i podstawowa analiza danych
python
import pandas as pd

# Wczytanie danych z pliku CSV
data = pd.read_csv('dane.csv')

# Podstawowe statystyki
print(data.describe())

# Filtrowanie danych
filtered_data = data[data['Wiek'] > 30]
print(filtered_data.head())
Przykład 2: Grupowanie i agregacja
python
# Grupowanie danych i obliczanie średniej
grouped = data.groupby('Dział')['Wynagrodzenie'].mean()
print(grouped)

# Tworzenie nowej kolumny
data['Premia'] = data['Wynagrodzenie'] * 0.1
2. Matplotlib
Opis
Matplotlib to podstawowa biblioteka do tworzenia wykresów w Pythonie. Pozwala na generowanie różnorodnych wizualizacji od prostych wykresów liniowych do złożonych diagramów.

Zalety:
Duża elastyczność w tworzeniu wykresów

Wiele stylów i opcji konfiguracyjnych

Integracja z Pandas i numpy

Możliwość zapisu wykresów w różnych formatach

Przykłady użycia:
Przykład 1: Prosty wykres liniowy
python
import matplotlib.pyplot as plt
import numpy as np

# Dane do wykresu
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Tworzenie wykresu
plt.figure(figsize=(8, 4))
plt.plot(x, y, label='sin(x)', color='blue')
plt.title('Przykładowy wykres funkcji sinus')
plt.xlabel('Oś X')
plt.ylabel('Oś Y')
plt.legend()
plt.grid(True)
plt.show()
Przykład 2: Wykres słupkowy z danych Pandas
python
# Przygotowanie danych
data = pd.DataFrame({
    'Miesiąc': ['Sty', 'Lut', 'Mar', 'Kwi'],
    'Sprzedaż': [120, 145, 160, 210]
})

# Tworzenie wykresu
plt.figure(figsize=(6, 4))
plt.bar(data['Miesiąc'], data['Sprzedaż'], color='green')
plt.title('Sprzedaż w I kwartale')
plt.xlabel('Miesiąc')
plt.ylabel('Sprzedaż (w tys.)')
plt.show()
Porównanie i wnioski
Biblioteka	Najlepsze zastosowania	Zalety	Ograniczenia
Pandas	Przetwarzanie danych tabelarycznych, czyszczenie danych, analizy	Szybkość, intuicyjność, bogate funkcje	Wymaga pamięci dla dużych zbiorów danych
Matplotlib	Tworzenie wykresów, wizualizacja danych	Elastyczność, wiele typów wykresów	Mniej intuicyjna niż niektóre nowsze biblioteki
Obie biblioteki doskonale się uzupełniają - Pandas przygotowuje dane, a Matplotlib pomaga je wizualizować. Dla bardziej zaawansowanych wizualizacji warto rozważyć bibliotekę Seaborn, która jest zbudowana na Matplotlib i oferuje bardziej atrakcyjne domyślne style.

Linki do dokumentacji
Pandas: https://pandas.pydata.org/docs/

Matplotlib: https://matplotlib.org/stable/contents.html

