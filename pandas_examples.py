#Przykład 1 Wczytywanie i podstawowa analiza danych


import pandas as pd

# Wczytanie danych z pliku CSV
data = pd.read_csv('dane.csv')

# Podstawowe statystyki
print(data.describe())

# Filtrowanie danych
filtered_data = data[data['Wiek'] > 30]
print(filtered_data.head())


# Przykład 2 Grupowanie i agregacja

# Grupowanie danych i obliczanie średniej
grouped = data.groupby('Dział')['Wynagrodzenie'].mean()
print(grouped)

# Tworzenie nowej kolumny
data['Premia'] = data['Wynagrodzenie'] * 0.1