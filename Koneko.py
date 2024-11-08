import Oyaneko

class Koneko(Oyaneko.Oyaneko):
    def __init__(self, color, tail, name, neko_skill):
        super().__init__("マンチカン", color, tail, neko_skill)
        self.name = name

    # hissatsuメソッドをオーバーライド
    def hissatsu(self):
        print(f'{self.color}色の赤ちゃんマンチカンの必殺技{self.neko_skill}!')

    # 新しいメソッド（飼い主にごあいさつ）の追加
    def say_hello(self):
        print(f'はじめまして。ワタシの名前は{self.name}だにゃ。')

koneko1 = Koneko('オフホワイト', '短い', 'しろねこ', 'ねこじゃらし攻撃')
koneko1.hissatsu()
koneko1.say_hello()