class Animal():                                                             
    def __init__(self, weight, mood):                                       #設定Animal的屬性
        self.weight = weight
        self.mood = mood
    def feed(self):                                                         #設定Animal的方法
        pass
    def walk(self):
        pass
    def bath(self):
        pass
    
class Dogs(Animal):
    def __init__(self, weight, mood):                                       #Dogs繼承Animal的屬性
        super().__init__(weight, mood)
    def feed(self):                                                         #Dogs繼承Animal的方法
        super().feed()
        self.weight = self.weight + 0.2
        self.mood = self.mood + 1
    def walk(self):
        super().walk()
        self.weight = self.weight - 0.2
        self.mood = self.mood + 2
    def bath(self):
        super().bath()
        self.mood = self.mood - 2
    def printf(self, n_feed, n_walk, n_bath):                               #設定計算及輸出結果的方法
        for i in range(0,n_feed):
            self.feed()
        for i in range(0,n_walk):
            self.walk()
        for i in range(0,n_bath):
            self.bath()
        print(f"狗狗現在的體重= {round(self.weight,1)}, 心情 {self.mood}") 


class Cats(Animal):
    def __init__(self, weight, mood):                                       #Cats繼承Animal的屬性
        super().__init__(weight, mood)
    def feed(self):                                                         #Cats繼承Animal的方法
        super().feed()
        self.weight = self.weight + 0.1
        self.mood = self.mood + 1
    def walk(self):
        super().walk()
        self.weight = self.weight - 0.1
        self.mood = self.mood - 1
    def bath(self):
        super().bath()
        self.mood = self.mood - 2
    def printf(self, n_feed, n_walk, n_bath):                               #設定計算及輸出結果的方法
        for i in range(0,n_feed):
            self.feed()
        for i in range(0,n_walk):
            self.walk()
        for i in range(0,n_bath):
            self.bath()
        print(f"貓貓現在的體重= {round(self.weight,1)}, 心情 {self.mood}") 

dog = Dogs(4.8, 65) 
dog.printf(18, 10, 4) 

cat = Cats(8.2, 60) 
cat.printf(40, 7, 1) 