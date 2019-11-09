# **Gilded Rose Kata**
##### Autor: Gustaw Napiórkowski

## **Kroki:**

### Przeniesienie funkcjolnalności zmiany wartości sell_in do osobnej funkcji

Została dodana nowa funkcja odpowiedzialna za zmianę wartości sell_in dla danego przedmiotu o -1 dla wszytkich przedmiotów, poza przedmiotem legendarnym o nazwie "Slfuras"

Funkcja ta wygląda następująco:

```python
    def sell_in_update(self, item):
        if 'Sulfuras' not in item.name:
            item.sell_in -= 1     def sell_in_update(self, item):
        item.sell_in -= 1
```
### Zmiana nazwy update_quality na old_update_quality

Na drodze planowania refactoringu dla tej funkcji została podjęta decyzja o
całkowitym redesignie funkcjie przeprowadzonym w krokach. W tym celu nazwa funkcji
update_quality została zmieniona na old_update_quality. Każdy krok to usunięcie
funkcjonalności dla danego przedmiotu z funkcji old_update_quality i przeniesienie tej funkcjonalności do indywidualnej funkcji dla danego przedmiotu. Nowa funkcja
update_quality ma natomiast za zadanie wywołac funkcję identyfikującą przdmiot i
wywołującą odpowiednią dla niego funkcję oraz wywołać funkcję oniżajacą wartość
sell_in.

Nowa funckja update_quality uzyskała następujący design:

```python
    def update_quality(self):
        for item in self.items:
            self.sell_in_update(item)
            self.quality_update(item)
```
### stworzenie funkcji qualtiy_update identyfikującej przedmioty

Funkcja qualtiy_update została stowrzona tylko w celu identyfikacji przedmiotu po
nazwie i wywołaniu odpowiedniej dla niego funckji. Wygląda ona następująco:

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

### funkcja zmiany quality: Sulfuras

Z funkcji old_update_quality została wyciągnięta i usunięta funkcjonalność dotycząca
przedmiotu "Sulfuras" i przeniesiona do funcji indywidualnej:

```python
    def sulfuras_quality_update(self, item):
        item.quality = 80
```

### funkcja zmiany quality: Backstage passes

Z funkcji old_update_quality została wyciągnięta i usunięta funkcjonalność dotycząca
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

### funkcja zmiany quality: Aged Bride

Z funkcji old_update_quality została wyciągnięta i usunięta funkcjonalność dotycząca
przedmiotu "Aged Bride" i przeniesiona do funcji indywidualnej:

```python
    def bride_qualit_update(self, item):
        if item.sell_in >= 0:
            item.quality += 1
        if item.sell_in < 0:
            item.quality += 2
```

### funkcja zmiany quality: Conjured items

Z funkcji update_quality została wyciągnięta i usunięta funkcjonalność dotycząca
przedmiotu "Conjured items" i przeniesiona do funcji indywidualnej:

```python
    def conjured_quality_update(self, item):
        if item.sell_in >= 0:
            item.quality -= 2
        elif item.sell_in < 0:
            item.quality -= 4
```