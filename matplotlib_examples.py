
#Przytkład 1 Prosty wykres liniowy

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


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


#Przykład 2 Wykres słupkowy z Padnas

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