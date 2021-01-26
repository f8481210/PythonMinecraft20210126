#檔名：2-1
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos() #取得座標
mc.setBlock(x,y,z+1,7) #前
mc.setBlock(x,y,z-1,7) #後
mc.setBlock(x-1,y,z,7) #左
mc.setBlock(x+1,y,z,7) #右
mc.setBlock(x+1,y,z+1,7) #右前
mc.setBlock(x-1,y,z+1,7) #左前
mc.setBlock(x+1,y,z-1,7) #右後
mc.setBlock(x-1,y,z-1,7) #左後

#挑戰題： 開新檔 菱形圖案 2-2