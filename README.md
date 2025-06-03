# Biblioteki Pythona do analizy i wizualizacji danych

Repozytorium prezentuje dwie podstawowe biblioteki Pythona do analizy i wizualizacji danych: Pandas oraz Matplotlib. Zawiera praktyczne przykłady demonstrujące ich główne funkcjonalności.

## 📊 Pandas

**Pandas** to potężna biblioteka do manipulacji i analizy danych. Dostarcza struktury danych takie jak DataFrames, które umożliwiają efektywne czyszczenie, transformację i analizę danych.

### Kluczowe cechy:
- Intuicyjna obsługa danych tabelarycznych
- Bogate funkcje do grupowania, agregacji i łączenia danych
- Integracja z wieloma formatami danych (CSV, Excel, SQL, JSON)
- Rozbudowana dokumentacja z aktywnym wsparciem społeczności

### Przykłady użycia:

#### Podstawowa analiza danych
```python
import pandas as pd

# Wczytanie danych z pliku CSV
dane = pd.read_csv('dane.csv')

# Wyświetlenie podstawowych statystyk
print(dane.describe())

# Filtrowanie danych
przefiltrowane_dane = dane[dane['Wiek'] > 30]
print(przefiltrowane_dane.head())
Agregacja danych
python
# Grupowanie danych i obliczanie średniej
zgrupowane = dane.groupby('Dział')['Wynagrodzenie'].mean()
print(zgrupowane)

# Tworzenie nowej kolumny
dane['Premia'] = dane['Wynagrodzenie'] * 0.1
📈 Matplotlib
Matplotlib to podstawowa biblioteka Pythona do tworzenia wykresów, umożliwiająca tworzenie różnorodnych wizualizacji od prostych wykresów liniowych po złożone diagramy.

Kluczowe cechy:
Duża elastyczność w tworzeniu wykresów

Wiele stylów i opcji konfiguracyjnych

Bezproblemowa integracja z Pandas i NumPy

Możliwość zapisu wykresów w różnych formatach

Przykłady użycia:
Podstawowy wykres liniowy
python
import matplotlib.pyplot as plt
import numpy as np

# Przygotowanie danych
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Generowanie wykresu
plt.figure(figsize=(8, 4))
plt.plot(x, y, label='sin(x)', color='niebieski')
plt.title('Przykładowy wykres funkcji sinus')
plt.xlabel('Oś X')
plt.ylabel('Oś Y')
plt.legend()
plt.grid(True)
plt.show()
Wykres słupkowy z danych Pandas
python
# Przygotowanie danych
dane = pd.DataFrame({
    'Miesiąc': ['Sty', 'Lut', 'Mar', 'Kwi'],
    'Sprzedaż': [120, 145, 160, 210]
})

# Tworzenie wykresu
plt.figure(figsize=(6, 4))
plt.bar(dane['Miesiąc'], dane['Sprzedaż'], color='zielony')
plt.title('Sprzedaż w I kwartale')
plt.xlabel('Miesiąc')
plt.ylabel('Sprzedaż (w tys.)')
plt.show()
🔍 Porównanie
Biblioteka	Najlepsze zastosowanie	Zalety	Ograniczenia
Pandas	Przetwarzanie danych tabelarycznych, czyszczenie danych, analizy	Szybkość, intuicyjność, bogate funkcje	Wymaga dużo pamięci dla dużych zbiorów danych
Matplotlib	Wizualizacja danych, tworzenie wykresów	Elastyczność, wiele typów wykresów	Mniej intuicyjna niż niektóre nowsze biblioteki
Biblioteki doskonale się uzupełniają - Pandas przygotowuje dane, a Matplotlib pomaga je wizualizować. Do bardziej zaawansowanych wizualizacji warto rozważyć bibliotekę Seaborn, która bazuje na Matplotlib i oferuje bardziej atrakcyjne domyślne style.

📚 Linki do dokumentacji
Dokumentacja Pandas

Dokumentacja Matplotlib
