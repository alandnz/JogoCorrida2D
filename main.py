from code.DBProxy import DBProxy
from code.Game import Game

# Reseta o banco de dados
'''db_proxy = DBProxy('DBScore')
db_proxy.reset()
db_proxy.close()'''

# Inicia o jogo
game = Game()
game.run()

