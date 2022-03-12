from models.player import Player


def main():
    # monplayer = Player('Natalia', 'FABIANO', '12/11/1982', 'feme', '10')
    monplayer2 = Player('2', 'Maria', 'FABIANO', '22/11/1986', 'feme', '1')
    print(Player.serialize_player(monplayer2))
    Player.save_player(monplayer2)


if __name__ == '__main__':
    main()
