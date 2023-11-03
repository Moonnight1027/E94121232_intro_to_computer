class Animal():
    def __init__(self, weight, mood):               #設定Animal的屬性
        self.weight = weight
        self.mood = mood
    def feed(self):                                 #設定Animal的方法
        pass
    def walk(self):
        pass
    def bath(self):
        pass
    
class Dogs(Animal):
    def __init__(self, weight, mood):               #Dogs繼承Animal的屬性
        super().__init__(weight, mood)
    def feed(self):                                 #Dogs繼承Animal的方法
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
    def printf(self, n_feed, n_walk, n_bath):       #設定計算結果的方法
        for i in range(0,n_feed):
            self.feed()
        for i in range(0,n_walk):
            self.walk()
        for i in range(0,n_bath):
            self.bath()
        print(f"狗狗現在的體重= {round(self.weight,1)}, 心情 {self.mood}") 

class Shiba(Dogs):
    def __init__(self, weight, mood):               #Shiba繼承Dogs的屬性
        super().__init__(weight, mood)
    def feed(self):                                 #Shiba繼承Dogs的方法
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
    def printf(self, n_feed, n_walk, n_bath):       #設定計算結果的方法
        for i in range(0,n_feed):
            self.feed()
        for i in range(0,n_walk):
            self.walk()
        for i in range(0,n_bath):
            self.bath()
        print(f"柴犬現在的體重= {round(self.weight,1)},心情 {self.mood}")
    def mood_constraint(self, constr):              #設定判定並輸出結果的方法
        self.constr = constr
        print("mood最高只能為=" ,self.constr )
        if (self.mood > self.constr):
            print("所以，柴犬現在的心情", self.constr)

shiba = Shiba(5, 70) 
shiba.printf(20, 10, 3) 
shiba.mood_constraint(90) 

shiba = Shiba(5, 70) 
shiba.printf(20, 10, 3) 
shiba.mood_constraint(300)

