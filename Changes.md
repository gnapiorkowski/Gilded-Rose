# **Gilded Rose Kata**

##### Autor: Gustaw Napiórkowski

## **Kroki główne:**

### Przeniesienie funkcjolnalności zmiany wartości sell_in do osobnej funkcji

Została dodana nowa funkcja odpowiedzialna za zmianę wartości sell_in dla danego przedmiotu o -1 dla wszytkich przedmiotów, poza przedmiotem legendarnym o nazwie "Slfuras"

Funkcja ta wygląda następująco:

```python
    def sell_in_update(self, item):
        if 'Sulfuras' not in item.name:
            item.sell_in -= 1     def sell_in_update(self, item):
        item.sell_in -= 1
```

### Restrukturyzacja funkcji update_quality

Na drodze planowania refaktoryzacji dla tej funkcji została podjęta decyzja o
przekształceniu jej w funkcję wyższego rzędu wywołującą dwie inne - sell_in_update() oraz
quality_update, gdzie ta druga jest odpowiednikiem starej funkcji update_update quality.

Pętla iterująca przedmioty została także wyciągnięta do tej funkcji ze starej wersji update_quality w celu zwiększenia przejrzystości.

Nowa funckja update_qualityusała następujący design:

```python
    def update_quality(self):
        for item in self.items:
            self.sell_in_update(item)
            self.quality_update(item)
```

### Funkcja quality_update() - następca starej update_quality()

Funkcja qualtiy_update została stowrzona jako dokładna kopia pierwotnej funkcji
update_quality jednak w trakcie pracy postanowiono pozostawić w niej tylko funkcjonalność
identyfikacji przedmiotu po nazwie i wywołaniu odpowiedniej dla niego funckji, która to
przejmie konkretną aktualizację wartości *quality*.

Wygląda ona następująco:

```python
def quality_update(self, item):
        #Special items' behaviour
        if "Aged Bride" in item.name:
            self.bride_qualit_update(item)
        elif "Sulfuras" in item.name:
            self.sulfuras_quality_update(item)
            return 1
        elif "Backstage passes" in item.name:
            self.backstage_quality_update(item)
        elif "Conjured" in item.name:
            self.conjured_quality_update(item)
        else:
        #Normal items' behaviour
            self.normal_quality_update(item)
```

## **Funkcje indywidualne dla przedmiotów**

W związku z potencjalną potrzebą dodawania przedmiotów w przyszłości do programu postanowiono każdy przedmiot z funkcji quality_update wydzielić do osobnej funkcji, dzięki czemu zachowujemy klarowność mając nadal odwołanie się do aktualizacji każdego z nich w jednym miejscu, ale także przenosząc część kodu w inne miejsce - mamy wyższą przejrzystość.

### Funkcja zmiany quality: Sulfuras

Z funkcji pierwonej update_quality została wyciągnięta i usunięta funkcjonalność dotycząca
przedmiotu "Sulfuras" i przeniesiona do funcji indywidualnej:

```python
    def sulfuras_quality_update(self, item):
        item.quality = 80
```

### Funkcja zmiany quality: Backstage passes

Z funkcji pierwonej update_quality została wyciągnięta i usunięta funkcjonalność dotycząca
przedmiotu "Backstage passes" i przeniesiona do funcji indywidualnej:

```python
    def backstage_quality_update(self, item):
        if item.sell_in >= 10:
            item.quality += 1
        elif 10 > item.sell_in >= 5:
            item.quality += 2
        elif 5 > item.sell_in >= 0:
            item.quality += 3
        elif item.sell_in < 0:
            item.quality = 0
```

### Funkcja zmiany quality: Aged Bride

Z funkcji pierwonej update_quality została wyciągnięta i usunięta funkcjonalność dotycząca
przedmiotu "Aged Bride" i przeniesiona do funcji indywidualnej:

```python
    def bride_qualit_update(self, item):
        if item.sell_in >= 0:
            item.quality += 1
        if item.sell_in < 0:
            item.quality += 2
```

### Funkcja zmiany quality: Conjured items

Z funkcji pierwotnej update_quality została wyciągnięta i usunięta funkcjonalność dotycząca
przedmiotu "Conjured items" i przeniesiona do funcji indywidualnej:

```python
    def conjured_quality_update(self, item):
        self.normal_quality_update(item)
        self.normal_quality_update(item)
```

### Funkcja zmiany quality: normal items

Z funkcji pierwotnej update_quality została wyciągnięta i usunięta
funkcjonalność dotycząca przedmiotów normalnych i przeniesiona do funcji indywidualnej:

```python
    def normal_quality_update(self, item):
        if item.sell_in >= 0:
            item.quality -= 1
        elif item.sell_in < 0:
            item.quality -= 2
```