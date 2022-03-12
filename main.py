from models.player import Player
from models.tournoi import Tournoi


def main():
    # monplayer = Player('Natalia', 'FABIANO', '12/11/1982', 'feme', '10')
    monplayer2 = Player('2', 'Maria', 'FABIANO', '22/11/1986', 'feme', '1')
    print(Player.serialize_player(monplayer2))
    Player.save_player(monplayer2)
    montournoi = Tournoi('1', 'torneo de prueba', 'maisons-laffitte', 'hoy', '', '4', 'test', 'corto')
    print(Tournoi.serialize_tournoi(montournoi))
    Tournoi.save_tournoi(montournoi)


if __name__ == '__main__':
    main()
