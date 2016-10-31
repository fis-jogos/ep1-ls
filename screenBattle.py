from pacBum import *
from FGAme import *
from objects import *
from menuPacBum import*
from colectScreen import *



def battleScreen(pacbum):

    #Gera personagem princial versão FGAme
    pacbum.fgameS

    #Movimenta personagem principal em Y
    @listen('long-press', 'up', dy = pacbum.vel_in_y/2)
    @listen('long-press', 'down', dy=-pacbum.vel_in_y/2)
    def pacbum_move_up(dy):
        pacbum.fgameS.move(0, dy)

    #Movimenta personagem principal em X
    @listen('long-press', 'right', dx = pacbum.vel_in_x/2)
    @listen('long-press', 'left', dx=-pacbum.vel_in_x/2)
    def pacbum_move_up(dx):
        pacbum.fgameS.move(dx, 0)


    run()