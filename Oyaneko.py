# クラスの定義
class Oyaneko:
    def __init__(self, breed, color, tail, neko_skill):
        self.breed = breed
        self.color = color
        self.tail = tail
        self.neko_skill = neko_skill

    def hissatu(self):
        print(f'{self.breed}の必殺技{self.neko_skill}!')


#neko1 = Oyaneko('マンチカン', '真っ白', '長い', 'ネコパンチ')
#neko2 = Oyaneko('スコティッシュフォールド', '三毛猫', 'ふさふさ', 'ネコキック')