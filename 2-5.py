#2-5
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    x,y,z = mc.player.getTilePos()
    block1 = mc.getBlock(x,y-1,z) #腳下
    block2 = mc.getBlock(x+1,y-1,z) #腳下右邊
    block3 = mc.getBlock(x-1,y-1,z) #腳下左邊
    block4 = mc.getBlock(x,y-1,z+1) #腳下前面
    block5 = mc.getBlock(x,y-1,z-1) #腳下後面
    if block1 == 8  or block1 == 9 or block2 == 8 or block2 == 9\
    or block3 == 8  or block3 == 9 or block4 == 8  or block4 == 9 or\
    block5 == 8  or block5 == 9:
        mc.setBlock(x,y-1,z,79) #腳下
        mc.setBlock(x,y-1,z+1,79) #腳下前面
        mc.setBlock(x,y-1,z-1,79) #腳下後面
        mc.setBlock(x-1,y-1,z,79) #腳下左邊
        mc.setBlock(x+1,y-1,z,79) #腳下右邊
        
    