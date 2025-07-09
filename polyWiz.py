import maya.cmds as cmds
import time
startTime = time.time()

sel = cmds.ls(sl=True)
tot = cmds.polyEvaluate(v=True, f=False) 
print("vertex count =", tot)

for i in range(tot):
    #cmds.select(sel[0] + '.vtx[' + str(i) + ']')
    vertexID = (sel[0] + '.vtx[' + str(i) + ']')
    rgb = cmds.polyColorPerVertex(vertexID, q=True, rgb=True)
    if (rgb[0] <= 0.5 and rgb[1] <= 0.5 and rgb[2] <= 0.5):
        avg = ((rgb[0]+rgb[1]+rgb[2]) / 3)
        cmds.polyColorPerVertex(vertexID, a=avg)

cmds.setAttr(sel[0] + '.displayColors',  1)
cmds.refresh()

print(time.time() - startTime)