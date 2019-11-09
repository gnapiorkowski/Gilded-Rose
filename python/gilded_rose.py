# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def old_update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
                if "Conjured" in item.name and item.quality > 0:
                    item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                            if "Conjured" in item.name and item.quality > 0:
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
    
    def update_quality(self):
        for item in self.items:
            self.sell_in_update(item)
            self.quality_update(item)

    def quality_update(self, item):
        #Special items' behaviour
        if "Aged Bride" in item.name:
            if item.sell_in >= 0:
                item.quality += 1
            if item.sell_in < 0:
                item.quality += 2
        elif "Sulfuras" in item.name:
            item.quality = 80
            return 1
        elif "Backstage passes" in item.name:
            if item.sell_in >= 10:
                item.quality += 1
            elif 10 > item.sell_in >= 5:
                item.quality += 2
            elif 5 > item.sell_in >= 0:
                item.quality += 3
            elif item.sell_in < 0:
                item.quality = 0
        elif "Conjured" in item.name:
            if item.sell_in >= 0:
                item.quality -= 2
            elif item.sell_in < 0:
                item.quality -= 4
        else:
            #Normal items' behaviour
            if item.sell_in >= 0:
                item.quality -= 1
            elif item.sell_in < 0:
                item.quality -= 2
        self.check_if_quality_within_limits(item)

    def sell_in_update(self, item):
        item.sell_in -= 1
    
    def check_if_quality_within_limits(self, item):
        if item.quality > 50: item.quality = 50
        if item.quality < 0: item.quality = 0


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
