# Problem 1
Vehicle sınıfından miras alan bir Bus sınıfı oluşturun. Bus.seating_capacity()'nin kapasite bağımsız değişkenine varsayılan olarak 50 değerini verin.

```
Output:
> The seating capacity of a bus is 50 passengers
```

# 1.Problemin Çözümünü Buraya Yazınız
class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)
my_bus = Bus("bus", 120)
print(my_bus.seating_capacity())
    
# Problem 2


School_bus'ın aynı zamanda Vehicle sınıfının bir örneği olup olmadığını belirleyiniz.
# 2.Problemin Çözümünü Buraya Yazınız
class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

school_bus = Bus("School Bus", 100)

print(isinstance(school_bus, Vehicle))  
