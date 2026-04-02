# Dokumentacja Silnika Speedway Manager Engine

Niniejszy dokument opisuje logikę matematyczną, atrybuty oraz zależności systemowe symulatora żużlowego.

---

## 🏎️ 1. Model Zawodnika (Rider)

Atrybuty zawodnika są podzielone na trzy kluczowe sekcje. Wpływają one na prawdopodobieństwo sukcesu w różnych fazach biegu.

### A. Atrybuty Techniczne (Silnik Wyścigu)
| Atrybut | Zastosowanie | Logika Matematyczna |
| :--- | :--- | :--- |
| **Refleks** | Start (0m) | Decyduje o czasie opuszczenia maszyny startowej. |
| **Technika Startu** | Dojazd (30m) | Odpowiada za przełożenie mocy na nawierzchnię. |
| **Jazda na Dystansie** | Okrążenia 1-4 | Definiuje utrzymanie prędkości na łukach (Off/Def). |
| **Racecraft** | Wyprzedzanie | Zdolność do znajdowania optymalnych ścieżek. |

### B. Atrybuty Fizyczne (Zasoby)
* **Przygotowanie Kondycyjne:** Wpływa na spadek skilla na 3. i 4. okrążeniu (-10% przy niskiej kondycji).
* **Waga:** Modyfikator startu (1.0 - 1.1). Lżejszy = szybszy start, ale trudniejsze prowadzenie na "kopie".
* **Odporność na urazy:** Parametr ukryty determinujący czas rekonwalescencji po upadku.

### C. Atrybuty Mentalne (Stabilność)
* **Inteligencja Torowa (Setup):** Bonus do statystyk sprzętowych po każdej serii startów.
* **Opanowanie (Presja):** Chroni przed błędami podczas jazdy w kontakcie/szprycy.
* **Waleczność:** Zwiększa szansę na powodzenie agresywnego ataku pod bandą.

---

## 🏗️ 2. Fazy Biegu i Wagi Atrybutów

Algorytm oblicza wynik każdego etapu wyścigu według schematu:
**`Wynik Fazy = (Atrybut Kluczowy * 0.7) + (Atrybut Wspierający * 0.3)`**

| Faza Biegu | Atrybut Kluczowy (0.7) | Atrybut Wspierający (0.3) |
| :--- | :--- | :--- |
| **Start (0m)** | Refleks | Technika Startu |
| **Dojazd (30m)** | Technika Startu | Waga zawodnika |
| **I Łuk** | Opanowanie | Waleczność |
| **Dystans (1-2 okr.)** | Jazda na Dystansie | Racecraft |
| **Dystans (3-4 okr.)** | Kondycja | Racecraft |
| **Atak/Obrona** | Waleczność | Opanowanie |

---

## 🏟️ 3. Model Toru (Track)

Tory klasyfikujemy według dwóch osi: **Geometrii** oraz **Nawierzchni**.

### Oś A: Geometria
* **Technical (Techniczny):** Krótki (260-300m). Bonus do Racecraftu.
* **Classic (Klasyczny):** Średni (320-360m). Zbalansowany.
* **Large (Lotnisko):** Długi (>380m). Bonus do mocy silnika i kondycji.

### Oś B: Nawierzchnia
* **Hard (Beton):** Kluczowy start i krawężnik. Bonus do Refleksu.
* **Deep (Kopa):** Wymagająca fizycznie. Bonus do Kondycji i Jazdy na Dystansie.
* **Slick (Lustro):** Wymaga czucia gazu. Bonus do Opanowania.

---

## 🛠️ 4. Model Tunera i Sprzętu

Silniki nie mają stałej mocy. Ich wydajność zależy od trendów rynkowych.

* **Tuner Trajectory:** Każdy tuner ma przypisaną ścieżkę formy w sezonie: `Stable`, `Ascending`, `Fading`, `Peak`.
* **Narrow Modifiers:** Klasa zawodnika to 80% wyniku, sprzęt i dopasowanie to pozostałe 20%.
* **Lojalność (Bond):** Dłuższa współpraca z jednym tunerem zwiększa bonus do Setupu.

---

## 📈 5. Główny Wzór Obliczeniowy

Każda kalkulacja w silniku opiera się na zasadzie "bezpiecznej klasy":

`Final_Skill = (Base_Skill * 0.8) + (Base_Skill * 0.2 * Track_Modifier * Weather_Penalty)`

* **Base_Skill:** Stała "podłoga" zawodnika (np. 1-100).
* **Track_Modifier:** Wartość wynikająca z dopasowania atrybutów do typu toru.