class Car:
    def __init__(self, brand: str, model: str, year: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year

    def info(self) -> str:
        return f"Car(brand='{self.brand}', model='{self.model}', year={self.year})"


cars = [
    Car('GM', 'Cobalt', 2020),
    Car('GM', 'Nexia', 2012),
    Car('GM', 'Damas', 2017),
    Car('BMW', 'X5', 2019)
]

car = max(cars, key=lambda car: car.year)
print(car.info())
