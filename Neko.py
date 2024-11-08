class Oyaneko:
    def __init__(self, breed, color, tail, neko_skill):
        self.breed = breed
        self.color = color
        self.tail = tail
        self.neko_skill = neko_skill

    def hissatu(self):
        print(f'{self.breed}の必殺技{self.neko_skill}!')

class Koneko(Oyaneko):
    def __init__(self, color, tail, name, neko_skill):
        super().__init__("マンチカン", color, tail, neko_skill)
        self.name = name

    # hissatsuメソッドをオーバーライド
    def hissatsu(self):
        print(f'{self.color}色の赤ちゃんマンチカンの必殺技{self.neko_skill}!')

    # 新しいメソッド（飼い主にごあいさつ）の追加
    def say_hello(self):
        print(f'はじめまして。ワタシの名前は{self.name}だにゃ。')


#　ここからが処理
koneko1 = Koneko('オフホワイト', '短い', 'しろねこ', 'ねこじゃらし攻撃')
koneko1.hissatsu()
koneko1.say_hello()