from gilded_rose import *
import sys

def update(items, days):
    for day in range(1,days+1):
        GildedRose(items).update_quality()

def testNormalItems():
    items = [Item(name='+5 Dexterity Vest', sell_in = 2, quality = 8)]
    update(items, 2)
    for item in items:
        assert item.quality == 6, 'Normal item, normal rate quality issue'
        assert item.sell_in == 0, 'Normal item, sell_in issue'
    update(items, 2)
    for item in items:
        assert item.quality == 2, 'Normal item, fast rate quality issue'
        assert item.sell_in == -2, 'Normal item, sell_in issue'


def testLegendaryItems():
    items = [Item(name='Sulfuras, Hand of Ragnaros', sell_in = 2, quality = 79)]
    
    update(items, 2)
    for item in items:
        assert item.quality == 80, 'Legendary item, normal rate quality issue'
        assert item.sell_in == 0, 'Legendary item, sell_in issue'
    update(items, 2)
    for item in items:
        assert item.quality == 80, 'Legendary item, fast rate quality issue'
        assert item.sell_in == 0, 'Legendary item, sell_in issue'

def testAgedBride():
    items = [Item(name='Aged Bride', sell_in = 2, quality = 8)]
    
    update(items, 2)
    for item in items:
        assert item.quality == 10, 'Aged Bride item, normal rate quality issue'
        assert item.sell_in == 0, 'Aged Bride item, sell_in issue'
    update(items, 2)
    for item in items:
        assert item.quality == 14, 'Aged Bride item, fast rate quality issue'
        assert item.sell_in == -2, 'Aged Bride item, sell_in issue'

def testBackstagePasses():
    items = [Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in = 12, quality = 8)]
    
    update(items, 2)
    for item in items:
        assert item.quality == 10, 'BackstagePasses item, normal rate quality issue'
        assert item.sell_in == 10, 'BackstagePasses item, sell_in issue'
    update(items, 5)
    for item in items:
        assert item.quality == 20, 'BackstagePasses item, fast rate quality issue'
        assert item.sell_in == 5, 'BackstagePasses item, sell_in issue'
    update(items, 5)
    for item in items:
        assert item.quality == 35, 'BackstagePasses item, fast rate quality issue'
        assert item.sell_in == 0, 'BackstagePasses item, sell_in issue'
    update(items, 5)
    for item in items:
        assert item.quality == 0, 'BackstagePasses item, fast rate quality issue'
        assert item.sell_in == -5, 'BackstagePasses item, sell_in issue'

def testCojuredItems():
    items = [Item(name='Conjured Mana Cake', sell_in = 2, quality = 12)]
    
    update(items, 2)
    for item in items:
        assert item.quality == 8, 'Conjured item, normal rate quality issue'
        assert item.sell_in == 0, 'Conjured item, sell_in issue'
    update(items, 2)
    for item in items:
        assert item.quality == 0, 'Conjured item, fast rate quality issue'
        assert item.sell_in == -2, 'Conjured item, sell_in issue'

testNormalItems()
testLegendaryItems()
testAgedBride()
testBackstagePasses()
testCojuredItems()

print('-'*150, 'PASSSED', sep = '\n')