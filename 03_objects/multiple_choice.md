```py
area = 25
perimeter = 20
has_fringe = False

area_cost = area * 5
if has_fringe:
    perimeter_cost = perimeter * 1.5
else:
    perimeter_cost = 0

cost = area_cost + total_cost
print(cost)
```



```py
def cost(area, perimeter, has_fringe):
    area_cost = area * 5
    if has_fringe:
        perimeter_cost = perimeter * 1.5
    else:
        perimeter_cost = 0
    return area_cost + perimeter_cost

print(cost(25, 20, False))
```


```py
class Rug():
    def __init__(self, area, perimeter, has_fringe):
        self.area = area
        self.perimeter = perimeter
        self.has_fringe = has_fringe
    
    def cost(self):
        area_cost = self.area * 5
        if has_fringe:
            perimeter_cost = perimeter * 1.5
        else:
            perimeter_cost = 0
        return area_cost + perimeter_cost

rug = Rug(25, 20, False)
print(rug.cost())
```
