#2-7
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
try:
    answer = int(input('請問你右邊要放什麼方塊：'))
    mc.setBlock(x+1,y,z,answer)
except:
    print('只能輸入數字!!!!!!')