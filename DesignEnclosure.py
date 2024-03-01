#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try: 
        app = adsk.core.Application.get()
        ui = app.userInterface
 
        doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
        design = app.activeProduct
 
        # Get the root component of the active design.
        rootComp = design.rootComponent
        extrudes = rootComp.features.extrudeFeatures
 
        # Create a new sketch on the xy plane.
        sketches = rootComp.sketches
        xZPlane = rootComp.xZConstructionPlane
        sketchX = sketches.add(xZPlane)
 
        yZPlane = rootComp.yZConstructionPlane
        sketchY = sketches.add(yZPlane)        

        xYPlane = rootComp.xYConstructionPlane
        sketchZ = sketches.add(xYPlane)        
 
        # Set var
        Width = 800
        Height = 500
        Depth = 600
        Radius = 0.21
        Profile = 2.0
        Tslot_Thickness = 5
 
        PfPoint = [0.7, 0.2, 0.3, 0.093934, 0.306066, 0.2419725, 0.0519615, 0.03]
 
        mmDepth = adsk.core.ValueInput.createByString(str(Depth-Tslot_Thickness*2)+"mm")
        mmWidth = adsk.core.ValueInput.createByString(str(Width-Profile*2*10)+"mm")
        mmHeight = adsk.core.ValueInput.createByString(str(Height-Profile*2*10)+"mm")
        mmTslot_Thickness = adsk.core.ValueInput.createByString(str(Tslot_Thickness)+"mm")
        mmProfile = adsk.core.ValueInput.createByString(str(Profile*10)+"mm")
        deg0 = adsk.core.ValueInput.createByString("0 deg")
 
        # Draw a circle xZ Plan - Depth.
        circlesX = sketchX.sketchCurves.sketchCircles
        circleX01 = circlesX.addByCenterRadius(adsk.core.Point3D.create(Profile/2, -Profile/2, 0), Radius)
 
        # Draw a circle yZ Plan - Width.
        circlesY = sketchY.sketchCurves.sketchCircles
        circleY02 = circlesY.addByCenterRadius(adsk.core.Point3D.create(-Profile/2, Profile/2, 0), Radius)

        # Draw a circle xY Plan - Width.
        circlesZ = sketchZ.sketchCurves.sketchCircles
        circleZ02 = circlesZ.addByCenterRadius(adsk.core.Point3D.create(Profile/2, Profile/2, 0), Radius)
 
        # Draw a Profile 20x20 XZ Plan - Depth.
        
        linesX = sketchX.sketchCurves.sketchLines
        lineX01 = linesX.addByTwoPoints(adsk.core.Point3D.create(0, 0, 0), adsk.core.Point3D.create(0, -PfPoint[0], 0))
        lineX02 = linesX.addByTwoPoints(lineX01.endSketchPoint, adsk.core.Point3D.create(PfPoint[1], -PfPoint[0], 0))
        lineX03 = linesX.addByTwoPoints(lineX02.endSketchPoint, adsk.core.Point3D.create(PfPoint[1], -PfPoint[0]+PfPoint[2], 0))
        lineX04 = linesX.addByTwoPoints(lineX03.endSketchPoint, adsk.core.Point3D.create(PfPoint[1]+PfPoint[3], -PfPoint[0]+PfPoint[2], 0))
        lineX05 = linesX.addByTwoPoints(lineX04.endSketchPoint, adsk.core.Point3D.create(PfPoint[1]+PfPoint[3]+PfPoint[4], -PfPoint[0]+PfPoint[2]-PfPoint[4], 0))
        lineX06 = linesX.addByTwoPoints(lineX05.endSketchPoint, adsk.core.Point3D.create(PfPoint[1]+PfPoint[3]+PfPoint[4], -PfPoint[0]+PfPoint[2]-PfPoint[4]-PfPoint[5], 0))
        lineX07 = linesX.addByTwoPoints(lineX06.endSketchPoint, adsk.core.Point3D.create(PfPoint[1]+PfPoint[3]+PfPoint[4]+PfPoint[7], -Profile/2, 0))
        lineX08 = linesX.addByTwoPoints(lineX07.endSketchPoint, adsk.core.Point3D.create(PfPoint[1]+PfPoint[3]+PfPoint[4], -Profile/2-PfPoint[6], 0))
        lineX09 = linesX.addByTwoPoints(lineX08.endSketchPoint, adsk.core.Point3D.create(PfPoint[1]+PfPoint[3]+PfPoint[4], -Profile/2-PfPoint[6]-PfPoint[5], 0))
        lineX10 = linesX.addByTwoPoints(lineX09.endSketchPoint, adsk.core.Point3D.create(PfPoint[1]+PfPoint[3], -Profile/2-PfPoint[6]-PfPoint[5]-PfPoint[4], 0))
        lineX11 = linesX.addByTwoPoints(lineX10.endSketchPoint, adsk.core.Point3D.create(PfPoint[1], -Profile/2-PfPoint[6]-PfPoint[5]-PfPoint[4], 0))
        lineX12 = linesX.addByTwoPoints(lineX11.endSketchPoint, adsk.core.Point3D.create(PfPoint[1], -Profile/2-PfPoint[6]-PfPoint[5]-PfPoint[4]+PfPoint[2], 0))
        lineX13 = linesX.addByTwoPoints(lineX12.endSketchPoint, adsk.core.Point3D.create(0, -Profile/2-PfPoint[6]-PfPoint[5]-PfPoint[4]+PfPoint[2], 0))
        lineX14 = linesX.addByTwoPoints(lineX13.endSketchPoint, adsk.core.Point3D.create(0, -Profile, 0))
        lineX15 = linesX.addByTwoPoints(lineX14.endSketchPoint, adsk.core.Point3D.create(PfPoint[0], -Profile, 0))
        lineX16 = linesX.addByTwoPoints(lineX15.endSketchPoint, adsk.core.Point3D.create(PfPoint[0], -Profile+PfPoint[1], 0))
        lineX17 = linesX.addByTwoPoints(lineX16.endSketchPoint, adsk.core.Point3D.create(PfPoint[0]-PfPoint[2], -Profile+PfPoint[1], 0))
        lineX18 = linesX.addByTwoPoints(lineX17.endSketchPoint, adsk.core.Point3D.create(PfPoint[0]-PfPoint[2], -Profile+PfPoint[1]+PfPoint[3], 0))
        lineX19 = linesX.addByTwoPoints(lineX18.endSketchPoint, adsk.core.Point3D.create(PfPoint[0]-PfPoint[2]+PfPoint[4], -Profile+PfPoint[1]+PfPoint[3]+PfPoint[4], 0))
        lineX20 = linesX.addByTwoPoints(lineX19.endSketchPoint, adsk.core.Point3D.create(PfPoint[0]-PfPoint[2]+PfPoint[4]+PfPoint[5], -Profile+PfPoint[1]+PfPoint[3]+PfPoint[4], 0))
        lineX21 = linesX.addByTwoPoints(lineX20.endSketchPoint, adsk.core.Point3D.create(Profile/2, -Profile+PfPoint[1]+PfPoint[3]+PfPoint[4]+PfPoint[7], 0))
        lineX22 = linesX.addByTwoPoints(lineX21.endSketchPoint, adsk.core.Point3D.create(Profile/2+PfPoint[6], -Profile+PfPoint[1]+PfPoint[3]+PfPoint[4], 0))
        lineX23 = linesX.addByTwoPoints(lineX22.endSketchPoint, adsk.core.Point3D.create(Profile/2+PfPoint[6]+PfPoint[5], -Profile+PfPoint[1]+PfPoint[3]+PfPoint[4], 0))        
        lineX24 = linesX.addByTwoPoints(lineX23.endSketchPoint, adsk.core.Point3D.create(Profile/2+PfPoint[6]+PfPoint[5]+PfPoint[4], -Profile+PfPoint[1]+PfPoint[3], 0))
        lineX25 = linesX.addByTwoPoints(lineX24.endSketchPoint, adsk.core.Point3D.create(Profile/2+PfPoint[6]+PfPoint[5]+PfPoint[4], -Profile+PfPoint[1], 0))
        lineX26 = linesX.addByTwoPoints(lineX25.endSketchPoint, adsk.core.Point3D.create(Profile/2+PfPoint[6]+PfPoint[5]+PfPoint[4]-PfPoint[2], -Profile+PfPoint[1], 0))
        lineX27 = linesX.addByTwoPoints(lineX26.endSketchPoint, adsk.core.Point3D.create(Profile/2+PfPoint[6]+PfPoint[5]+PfPoint[4]-PfPoint[2], -Profile, 0))
        lineX28 = linesX.addByTwoPoints(lineX27.endSketchPoint, adsk.core.Point3D.create(Profile, -Profile, 0))
        lineX29 = linesX.addByTwoPoints(lineX28.endSketchPoint, adsk.core.Point3D.create(Profile, -Profile+PfPoint[0], 0))
        lineX30 = linesX.addByTwoPoints(lineX29.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[1], -Profile+PfPoint[0], 0))
        lineX31 = linesX.addByTwoPoints(lineX30.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[1], -Profile+PfPoint[0]-PfPoint[2], 0))
        lineX32 = linesX.addByTwoPoints(lineX31.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[1]-PfPoint[3], -Profile+PfPoint[0]-PfPoint[2], 0))
        lineX33 = linesX.addByTwoPoints(lineX32.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[1]-PfPoint[3]-PfPoint[4], -Profile+PfPoint[0]-PfPoint[2]+PfPoint[4], 0))
        lineX34 = linesX.addByTwoPoints(lineX33.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[1]-PfPoint[3]-PfPoint[4], -Profile/2-PfPoint[6], 0))
        lineX35 = linesX.addByTwoPoints(lineX34.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[1]-PfPoint[3]-PfPoint[4]-PfPoint[7], -Profile/2, 0))
        lineX36 = linesX.addByTwoPoints(lineX35.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[1]-PfPoint[3]-PfPoint[4], -Profile/2+PfPoint[6], 0))
        lineX37 = linesX.addByTwoPoints(lineX36.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[1]-PfPoint[3]-PfPoint[4], -Profile/2+PfPoint[6]+PfPoint[5], 0))
        lineX38 = linesX.addByTwoPoints(lineX37.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[1]-PfPoint[3], -PfPoint[0]+PfPoint[2], 0))
        lineX39 = linesX.addByTwoPoints(lineX38.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[1], -PfPoint[0]+PfPoint[2], 0))
        lineX40 = linesX.addByTwoPoints(lineX39.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[1], -PfPoint[0], 0))
        lineX41 = linesX.addByTwoPoints(lineX40.endSketchPoint, adsk.core.Point3D.create(Profile, -PfPoint[0], 0))
        lineX42 = linesX.addByTwoPoints(lineX41.endSketchPoint, adsk.core.Point3D.create(Profile, 0, 0))
        lineX43 = linesX.addByTwoPoints(lineX42.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[0], 0, 0))
        lineX44 = linesX.addByTwoPoints(lineX43.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[0], -PfPoint[1], 0))
        lineX45 = linesX.addByTwoPoints(lineX44.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[0]+PfPoint[2], -PfPoint[1], 0))
        lineX46 = linesX.addByTwoPoints(lineX45.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[0]+PfPoint[2], -PfPoint[1]-PfPoint[3], 0))
        lineX47 = linesX.addByTwoPoints(lineX46.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[0]+PfPoint[2]-PfPoint[4], -PfPoint[1]-PfPoint[3]-PfPoint[4], 0))
        lineX48 = linesX.addByTwoPoints(lineX47.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[0]+PfPoint[2]-PfPoint[4]-PfPoint[5], -PfPoint[1]-PfPoint[3]-PfPoint[4], 0))
        lineX49 = linesX.addByTwoPoints(lineX48.endSketchPoint, adsk.core.Point3D.create(Profile/2, -PfPoint[1]-PfPoint[3]-PfPoint[4]-PfPoint[7], 0))
        lineX50 = linesX.addByTwoPoints(lineX49.endSketchPoint, adsk.core.Point3D.create(Profile/2-PfPoint[6], -PfPoint[1]-PfPoint[3]-PfPoint[4], 0))
        lineX51 = linesX.addByTwoPoints(lineX50.endSketchPoint, adsk.core.Point3D.create(Profile/2-PfPoint[6]-PfPoint[5], -PfPoint[1]-PfPoint[3]-PfPoint[4], 0))
        lineX52 = linesX.addByTwoPoints(lineX51.endSketchPoint, adsk.core.Point3D.create(Profile/2-PfPoint[6]-PfPoint[5]-PfPoint[4], -PfPoint[1]-PfPoint[3], 0))
        lineX53 = linesX.addByTwoPoints(lineX52.endSketchPoint, adsk.core.Point3D.create(Profile/2-PfPoint[6]-PfPoint[5]-PfPoint[4], -PfPoint[1], 0))
        lineX54 = linesX.addByTwoPoints(lineX53.endSketchPoint, adsk.core.Point3D.create(PfPoint[0], -PfPoint[1], 0))
        lineX55 = linesX.addByTwoPoints(lineX54.endSketchPoint, adsk.core.Point3D.create(PfPoint[0], 0, 0))
        lineX56 = linesX.addByTwoPoints(lineX55.endSketchPoint, adsk.core.Point3D.create(0, 0, 0))
 
 
        # Draw a Profile 20x20 YZ Plan - Width.
        
        linesY = sketchY.sketchCurves.sketchLines
        lineY01 = linesY.addByTwoPoints(adsk.core.Point3D.create(0, 0, 0), adsk.core.Point3D.create(-PfPoint[0], 0, 0))
        lineY02 = linesY.addByTwoPoints(lineY01.endSketchPoint, adsk.core.Point3D.create(-PfPoint[0], PfPoint[1], 0))
        lineY03 = linesY.addByTwoPoints(lineY02.endSketchPoint, adsk.core.Point3D.create(-PfPoint[0]+PfPoint[2], PfPoint[1], 0))
        lineY04 = linesY.addByTwoPoints(lineY03.endSketchPoint, adsk.core.Point3D.create(-PfPoint[0]+PfPoint[2], PfPoint[1]+PfPoint[3], 0))
        lineY05 = linesY.addByTwoPoints(lineY04.endSketchPoint, adsk.core.Point3D.create(-PfPoint[0]+PfPoint[2]-PfPoint[4], PfPoint[1]+PfPoint[3]+PfPoint[4], 0))
        lineY06 = linesY.addByTwoPoints(lineY05.endSketchPoint, adsk.core.Point3D.create(-PfPoint[0]+PfPoint[2]-PfPoint[4]-PfPoint[5], PfPoint[1]+PfPoint[3]+PfPoint[4], 0))
        lineY07 = linesY.addByTwoPoints(lineY06.endSketchPoint, adsk.core.Point3D.create(-Profile/2, PfPoint[1]+PfPoint[3]+PfPoint[4]+PfPoint[7], 0))
        lineY08 = linesY.addByTwoPoints(lineY07.endSketchPoint, adsk.core.Point3D.create(-Profile/2-PfPoint[6], PfPoint[1]+PfPoint[3]+PfPoint[4], 0))
        lineY09 = linesY.addByTwoPoints(lineY08.endSketchPoint, adsk.core.Point3D.create(-Profile/2-PfPoint[6]-PfPoint[5], PfPoint[1]+PfPoint[3]+PfPoint[4], 0))
        lineY10 = linesY.addByTwoPoints(lineY09.endSketchPoint, adsk.core.Point3D.create(-Profile/2-PfPoint[6]-PfPoint[5]-PfPoint[4], PfPoint[1]+PfPoint[3], 0))
        lineY11 = linesY.addByTwoPoints(lineY10.endSketchPoint, adsk.core.Point3D.create(-Profile/2-PfPoint[6]-PfPoint[5]-PfPoint[4], PfPoint[1], 0))
        lineY12 = linesY.addByTwoPoints(lineY11.endSketchPoint, adsk.core.Point3D.create(-Profile/2-PfPoint[6]-PfPoint[5]-PfPoint[4]+PfPoint[2], PfPoint[1], 0))
        lineY13 = linesY.addByTwoPoints(lineY12.endSketchPoint, adsk.core.Point3D.create(-Profile/2-PfPoint[6]-PfPoint[5]-PfPoint[4]+PfPoint[2], 0, 0))
        lineY14 = linesY.addByTwoPoints(lineY13.endSketchPoint, adsk.core.Point3D.create(-Profile, 0, 0))
        lineY15 = linesY.addByTwoPoints(lineY14.endSketchPoint, adsk.core.Point3D.create(-Profile, PfPoint[0],0))
        lineY16 = linesY.addByTwoPoints(lineY15.endSketchPoint, adsk.core.Point3D.create(-Profile+PfPoint[1], PfPoint[0], 0))
        lineY17 = linesY.addByTwoPoints(lineY16.endSketchPoint, adsk.core.Point3D.create(-Profile+PfPoint[1], PfPoint[0]-PfPoint[2], 0))
        lineY18 = linesY.addByTwoPoints(lineY17.endSketchPoint, adsk.core.Point3D.create(-Profile+PfPoint[1]+PfPoint[3], PfPoint[0]-PfPoint[2], 0))
        lineY19 = linesY.addByTwoPoints(lineY18.endSketchPoint, adsk.core.Point3D.create(-Profile+PfPoint[1]+PfPoint[3]+PfPoint[4], PfPoint[0]-PfPoint[2]+PfPoint[4], 0))
        lineY20 = linesY.addByTwoPoints(lineY19.endSketchPoint, adsk.core.Point3D.create(-Profile+PfPoint[1]+PfPoint[3]+PfPoint[4], PfPoint[0]-PfPoint[2]+PfPoint[4]+PfPoint[5], 0))
        lineY21 = linesY.addByTwoPoints(lineY20.endSketchPoint, adsk.core.Point3D.create(-Profile+PfPoint[1]+PfPoint[3]+PfPoint[4]+PfPoint[7], Profile/2, 0))
        lineY22 = linesY.addByTwoPoints(lineY21.endSketchPoint, adsk.core.Point3D.create(-Profile+PfPoint[1]+PfPoint[3]+PfPoint[4], Profile/2+PfPoint[6], 0))
        lineY23 = linesY.addByTwoPoints(lineY22.endSketchPoint, adsk.core.Point3D.create(-Profile+PfPoint[1]+PfPoint[3]+PfPoint[4], Profile/2+PfPoint[6]+PfPoint[5], 0))
        lineY24 = linesY.addByTwoPoints(lineY23.endSketchPoint, adsk.core.Point3D.create(-Profile+PfPoint[1]+PfPoint[3], Profile/2+PfPoint[6]+PfPoint[5]+PfPoint[4], 0))
        lineY25 = linesY.addByTwoPoints(lineY24.endSketchPoint, adsk.core.Point3D.create(-Profile+PfPoint[1], Profile/2+PfPoint[6]+PfPoint[5]+PfPoint[4], 0))
        lineY26 = linesY.addByTwoPoints(lineY25.endSketchPoint, adsk.core.Point3D.create(-Profile+PfPoint[1], Profile-PfPoint[0], 0))
        lineY27 = linesY.addByTwoPoints(lineY26.endSketchPoint, adsk.core.Point3D.create(-Profile, Profile-PfPoint[0], 0))
        lineY28 = linesY.addByTwoPoints(lineY27.endSketchPoint, adsk.core.Point3D.create(-Profile, Profile, 0))
        lineY29 = linesY.addByTwoPoints(lineY28.endSketchPoint, adsk.core.Point3D.create(-Profile+PfPoint[0], Profile, 0))
        lineY30 = linesY.addByTwoPoints(lineY29.endSketchPoint, adsk.core.Point3D.create(-Profile+PfPoint[0], Profile-PfPoint[1], 0))
        lineY31 = linesY.addByTwoPoints(lineY30.endSketchPoint, adsk.core.Point3D.create(-Profile+PfPoint[0]-PfPoint[2], Profile-PfPoint[1], 0))
        lineY32 = linesY.addByTwoPoints(lineY31.endSketchPoint, adsk.core.Point3D.create(-Profile+PfPoint[0]-PfPoint[2], Profile-PfPoint[1]-PfPoint[3], 0))
        lineY33 = linesY.addByTwoPoints(lineY32.endSketchPoint, adsk.core.Point3D.create(-Profile+PfPoint[0]-PfPoint[2]+PfPoint[4], Profile-PfPoint[1]-PfPoint[3]-PfPoint[4], 0))
        lineY34 = linesY.addByTwoPoints(lineY33.endSketchPoint, adsk.core.Point3D.create(-Profile/2-PfPoint[6], Profile-PfPoint[1]-PfPoint[3]-PfPoint[4], 0))
        lineY35 = linesY.addByTwoPoints(lineY34.endSketchPoint, adsk.core.Point3D.create(-Profile/2, Profile-PfPoint[1]-PfPoint[3]-PfPoint[4]-PfPoint[7], 0))
        lineY36 = linesY.addByTwoPoints(lineY35.endSketchPoint, adsk.core.Point3D.create(-Profile/2+PfPoint[6], Profile-PfPoint[1]-PfPoint[3]-PfPoint[4], 0))
        lineY37 = linesY.addByTwoPoints(lineY36.endSketchPoint, adsk.core.Point3D.create(-Profile/2+PfPoint[6]+PfPoint[5], Profile-PfPoint[1]-PfPoint[3]-PfPoint[4], 0))
        lineY38 = linesY.addByTwoPoints(lineY37.endSketchPoint, adsk.core.Point3D.create(-PfPoint[0]+PfPoint[2], Profile-PfPoint[1]-PfPoint[3], 0))
        lineY39 = linesY.addByTwoPoints(lineY38.endSketchPoint, adsk.core.Point3D.create(-PfPoint[0]+PfPoint[2], Profile-PfPoint[1], 0))
        lineY40 = linesY.addByTwoPoints(lineY39.endSketchPoint, adsk.core.Point3D.create(-PfPoint[0], Profile-PfPoint[1], 0))
        lineY41 = linesY.addByTwoPoints(lineY40.endSketchPoint, adsk.core.Point3D.create(-PfPoint[0], Profile, 0))
        lineY42 = linesY.addByTwoPoints(lineY41.endSketchPoint, adsk.core.Point3D.create(0, Profile, 0))
        lineY43 = linesY.addByTwoPoints(lineY42.endSketchPoint, adsk.core.Point3D.create(0, Profile-PfPoint[0], 0))
        lineY44 = linesY.addByTwoPoints(lineY43.endSketchPoint, adsk.core.Point3D.create(-PfPoint[1], Profile-PfPoint[0], 0))
        lineY45 = linesY.addByTwoPoints(lineY44.endSketchPoint, adsk.core.Point3D.create(-PfPoint[1], Profile-PfPoint[0]+PfPoint[2], 0))
        lineY46 = linesY.addByTwoPoints(lineY45.endSketchPoint, adsk.core.Point3D.create(-PfPoint[1]-PfPoint[3], Profile-PfPoint[0]+PfPoint[2], 0))
        lineY47 = linesY.addByTwoPoints(lineY46.endSketchPoint, adsk.core.Point3D.create(-PfPoint[1]-PfPoint[3]-PfPoint[4], Profile-PfPoint[0]+PfPoint[2]-PfPoint[4], 0))
        lineY48 = linesY.addByTwoPoints(lineY47.endSketchPoint, adsk.core.Point3D.create(-PfPoint[1]-PfPoint[3]-PfPoint[4], Profile-PfPoint[0]+PfPoint[2]-PfPoint[4]-PfPoint[5], 0))
        lineY49 = linesY.addByTwoPoints(lineY48.endSketchPoint, adsk.core.Point3D.create(-PfPoint[1]-PfPoint[3]-PfPoint[4]-PfPoint[7], Profile/2, 0))
        lineY50 = linesY.addByTwoPoints(lineY49.endSketchPoint, adsk.core.Point3D.create(-PfPoint[1]-PfPoint[3]-PfPoint[4], Profile/2-PfPoint[6], 0))
        lineY51 = linesY.addByTwoPoints(lineY50.endSketchPoint, adsk.core.Point3D.create(-PfPoint[1]-PfPoint[3]-PfPoint[4], Profile/2-PfPoint[6]-PfPoint[5], 0))
        lineY52 = linesY.addByTwoPoints(lineY51.endSketchPoint, adsk.core.Point3D.create(-PfPoint[1]-PfPoint[3], Profile/2-PfPoint[6]-PfPoint[5]-PfPoint[4], 0))
        lineY53 = linesY.addByTwoPoints(lineY52.endSketchPoint, adsk.core.Point3D.create(-PfPoint[1], Profile/2-PfPoint[6]-PfPoint[5]-PfPoint[4], 0))
        lineY54 = linesY.addByTwoPoints(lineY53.endSketchPoint, adsk.core.Point3D.create(-PfPoint[1], PfPoint[0], 0))
        lineY55 = linesY.addByTwoPoints(lineY54.endSketchPoint, adsk.core.Point3D.create(0, PfPoint[0], 0))
        lineY56 = linesY.addByTwoPoints(lineY55.endSketchPoint, adsk.core.Point3D.create(0, 0, 0))
        
        # Draw a Profile 20x20 XY Plan - Width.

        linesZ = sketchZ.sketchCurves.sketchLines
        lineZ01 = linesZ.addByTwoPoints(adsk.core.Point3D.create(0, 0, 0), adsk.core.Point3D.create(0,PfPoint[0], 0))
        lineZ02 = linesZ.addByTwoPoints(lineZ01.endSketchPoint, adsk.core.Point3D.create(PfPoint[1], PfPoint[0], 0))
        lineZ03 = linesZ.addByTwoPoints(lineZ02.endSketchPoint, adsk.core.Point3D.create(PfPoint[1], PfPoint[0]-PfPoint[2], 0))
        lineZ04 = linesZ.addByTwoPoints(lineZ03.endSketchPoint, adsk.core.Point3D.create(PfPoint[1]+PfPoint[3], PfPoint[0]-PfPoint[2],  0))
        lineZ05 = linesZ.addByTwoPoints(lineZ04.endSketchPoint, adsk.core.Point3D.create(PfPoint[1]+PfPoint[3]+PfPoint[4], PfPoint[0],  0))
        lineZ06 = linesZ.addByTwoPoints(lineZ05.endSketchPoint, adsk.core.Point3D.create(PfPoint[1]+PfPoint[3]+PfPoint[4], Profile/2-PfPoint[6], 0))        
        lineZ07 = linesZ.addByTwoPoints(lineZ06.endSketchPoint, adsk.core.Point3D.create(PfPoint[1]+PfPoint[3]+PfPoint[4]+PfPoint[7], Profile/2, 0))

        lineZ08 = linesZ.addByTwoPoints(lineZ07.endSketchPoint, adsk.core.Point3D.create(PfPoint[1]+PfPoint[3]+PfPoint[4], Profile/2+PfPoint[6], 0))
        lineZ09 = linesZ.addByTwoPoints(lineZ08.endSketchPoint, adsk.core.Point3D.create(PfPoint[1]+PfPoint[3]+PfPoint[4], Profile-PfPoint[0], 0))
        lineZ10 = linesZ.addByTwoPoints(lineZ09.endSketchPoint, adsk.core.Point3D.create(PfPoint[1]+PfPoint[3], Profile-PfPoint[0]+PfPoint[2], 0))
        lineZ11 = linesZ.addByTwoPoints(lineZ10.endSketchPoint, adsk.core.Point3D.create(PfPoint[1], Profile-PfPoint[0]+PfPoint[2], 0))
        lineZ12 = linesZ.addByTwoPoints(lineZ11.endSketchPoint, adsk.core.Point3D.create(PfPoint[1], Profile-PfPoint[0], 0))
        lineZ13 = linesZ.addByTwoPoints(lineZ12.endSketchPoint, adsk.core.Point3D.create(0, Profile-PfPoint[0], 0))
        lineZ14 = linesZ.addByTwoPoints(lineZ13.endSketchPoint, adsk.core.Point3D.create(0, Profile, 0))

        lineZ15 = linesZ.addByTwoPoints(lineZ14.endSketchPoint, adsk.core.Point3D.create(PfPoint[0], Profile, 0))
        lineZ16 = linesZ.addByTwoPoints(lineZ15.endSketchPoint, adsk.core.Point3D.create(PfPoint[0], Profile-PfPoint[1], 0))
        lineZ17 = linesZ.addByTwoPoints(lineZ16.endSketchPoint, adsk.core.Point3D.create(PfPoint[0]-PfPoint[2], Profile-PfPoint[1], 0))
        lineZ18 = linesZ.addByTwoPoints(lineZ17.endSketchPoint, adsk.core.Point3D.create(PfPoint[0]-PfPoint[2], Profile-PfPoint[1]-PfPoint[3], 0))
        lineZ19 = linesZ.addByTwoPoints(lineZ18.endSketchPoint, adsk.core.Point3D.create(PfPoint[0], Profile-PfPoint[1]-PfPoint[3]-PfPoint[4], 0))

        lineZ20 = linesZ.addByTwoPoints(lineZ19.endSketchPoint, adsk.core.Point3D.create(PfPoint[0]+PfPoint[5], Profile-PfPoint[1]-PfPoint[3]-PfPoint[4], 0))
        lineZ21 = linesZ.addByTwoPoints(lineZ20.endSketchPoint, adsk.core.Point3D.create(Profile/2, Profile-PfPoint[1]-PfPoint[3]-PfPoint[4]-PfPoint[7], 0))

        lineZ22 = linesZ.addByTwoPoints(lineZ21.endSketchPoint, adsk.core.Point3D.create(Profile/2+PfPoint[6], Profile-PfPoint[1]-PfPoint[3]-PfPoint[4], 0))
        lineZ23 = linesZ.addByTwoPoints(lineZ22.endSketchPoint, adsk.core.Point3D.create(Profile/2+PfPoint[6]+PfPoint[5], Profile-PfPoint[1]-PfPoint[3]-PfPoint[4], 0))
        lineZ24 = linesZ.addByTwoPoints(lineZ23.endSketchPoint, adsk.core.Point3D.create(Profile/2+PfPoint[6]+PfPoint[5]+PfPoint[4], Profile-PfPoint[1]-PfPoint[3], 0))
        lineZ25 = linesZ.addByTwoPoints(lineZ24.endSketchPoint, adsk.core.Point3D.create(Profile/2+PfPoint[6]+PfPoint[5]+PfPoint[4], Profile-PfPoint[1], 0))
        lineZ26 = linesZ.addByTwoPoints(lineZ25.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[0], Profile-PfPoint[1], 0))
        lineZ27 = linesZ.addByTwoPoints(lineZ26.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[0], Profile, 0))
        lineZ28 = linesZ.addByTwoPoints(lineZ27.endSketchPoint, adsk.core.Point3D.create(Profile, Profile, 0))

        lineZ29 = linesZ.addByTwoPoints(lineZ28.endSketchPoint, adsk.core.Point3D.create(Profile, Profile-PfPoint[0], 0))
        lineZ30 = linesZ.addByTwoPoints(lineZ29.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[1], Profile-PfPoint[0], 0))
        lineZ31 = linesZ.addByTwoPoints(lineZ30.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[1], Profile-PfPoint[0]+PfPoint[2], 0))
        lineZ32 = linesZ.addByTwoPoints(lineZ31.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[1]-PfPoint[3], Profile-PfPoint[0]+PfPoint[2], 0))
        lineZ33 = linesZ.addByTwoPoints(lineZ32.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[1]-PfPoint[3]-PfPoint[4], Profile-PfPoint[0]+PfPoint[2]-PfPoint[4], 0))
        lineZ34 = linesZ.addByTwoPoints(lineZ33.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[1]-PfPoint[3]-PfPoint[4], Profile-PfPoint[0]+PfPoint[2]-PfPoint[4]-PfPoint[5], 0))
        lineZ35 = linesZ.addByTwoPoints(lineZ34.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[1]-PfPoint[3]-PfPoint[4]-PfPoint[7], Profile/2, 0))

        lineZ36 = linesZ.addByTwoPoints(lineZ35.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[1]-PfPoint[3]-PfPoint[4], Profile/2-PfPoint[6], 0))
        lineZ37 = linesZ.addByTwoPoints(lineZ36.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[1]-PfPoint[3]-PfPoint[4], Profile/2-PfPoint[6]-PfPoint[5], 0))
        lineZ38 = linesZ.addByTwoPoints(lineZ37.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[1]-PfPoint[3], PfPoint[0]-PfPoint[2], 0))
        lineZ39 = linesZ.addByTwoPoints(lineZ38.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[1], PfPoint[0]-PfPoint[2], 0))
        lineZ40 = linesZ.addByTwoPoints(lineZ39.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[1], PfPoint[0], 0))
        lineZ41 = linesZ.addByTwoPoints(lineZ40.endSketchPoint, adsk.core.Point3D.create(Profile, PfPoint[0], 0))
        lineZ42 = linesZ.addByTwoPoints(lineZ41.endSketchPoint, adsk.core.Point3D.create(Profile, 0, 0))

        lineZ43 = linesZ.addByTwoPoints(lineZ42.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[0], 0, 0))
        lineZ44 = linesZ.addByTwoPoints(lineZ43.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[0], PfPoint[1], 0))
        lineZ45 = linesZ.addByTwoPoints(lineZ44.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[0]+PfPoint[2], PfPoint[1], 0))
        lineZ46 = linesZ.addByTwoPoints(lineZ45.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[0]+PfPoint[2], PfPoint[1]+PfPoint[3], 0))
        lineZ47 = linesZ.addByTwoPoints(lineZ46.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[0]+PfPoint[2]-PfPoint[4], PfPoint[1]+PfPoint[3]+PfPoint[4], 0))
        lineZ48 = linesZ.addByTwoPoints(lineZ47.endSketchPoint, adsk.core.Point3D.create(Profile-PfPoint[0]+PfPoint[2]-PfPoint[4]-PfPoint[5], PfPoint[1]+PfPoint[3]+PfPoint[4], 0))
        lineZ49 = linesZ.addByTwoPoints(lineZ48.endSketchPoint, adsk.core.Point3D.create(Profile/2, PfPoint[1]+PfPoint[3]+PfPoint[4]+PfPoint[7], 0))

        lineZ50 = linesZ.addByTwoPoints(lineZ49.endSketchPoint, adsk.core.Point3D.create(Profile/2-PfPoint[6], PfPoint[1]+PfPoint[3]+PfPoint[4], 0))
        lineZ51 = linesZ.addByTwoPoints(lineZ50.endSketchPoint, adsk.core.Point3D.create(Profile/2-PfPoint[6]-PfPoint[5], PfPoint[1]+PfPoint[3]+PfPoint[4], 0))
        lineZ52 = linesZ.addByTwoPoints(lineZ51.endSketchPoint, adsk.core.Point3D.create(Profile/2-PfPoint[6]-PfPoint[5]-PfPoint[4], PfPoint[1]+PfPoint[3], 0))
        lineZ53 = linesZ.addByTwoPoints(lineZ52.endSketchPoint, adsk.core.Point3D.create(Profile/2-PfPoint[6]-PfPoint[5]-PfPoint[4], PfPoint[1], 0))
        lineZ54 = linesZ.addByTwoPoints(lineZ53.endSketchPoint, adsk.core.Point3D.create(PfPoint[0], PfPoint[1], 0))
        lineZ55 = linesZ.addByTwoPoints(lineZ54.endSketchPoint, adsk.core.Point3D.create(PfPoint[0], 0, 0))
        lineZ56 = linesZ.addByTwoPoints(lineZ55.endSketchPoint, adsk.core.Point3D.create(0, 0, 0))
 
        # Add a fillet Depth.
        arc = sketchX.sketchCurves.sketchArcs.addFillet(lineX01, lineX01.endSketchPoint.geometry, lineX56, lineX56.endSketchPoint.geometry, .1)
        arc = sketchX.sketchCurves.sketchArcs.addFillet(lineX14, lineX14.endSketchPoint.geometry, lineX15, lineX15.startSketchPoint.geometry, .1)
        arc = sketchX.sketchCurves.sketchArcs.addFillet(lineX28, lineX28.endSketchPoint.geometry, lineX29, lineX29.startSketchPoint.geometry, .1)
        arc = sketchX.sketchCurves.sketchArcs.addFillet(lineX42, lineX42.endSketchPoint.geometry, lineX43, lineX43.startSketchPoint.geometry, .1)
 
        # Add a fillet Width.
        arc = sketchY.sketchCurves.sketchArcs.addFillet(lineY01, lineY01.endSketchPoint.geometry, lineY56, lineY56.endSketchPoint.geometry, .1)
        arc = sketchY.sketchCurves.sketchArcs.addFillet(lineY14, lineY14.endSketchPoint.geometry, lineY15, lineY15.startSketchPoint.geometry, .1)
        arc = sketchY.sketchCurves.sketchArcs.addFillet(lineY28, lineY28.endSketchPoint.geometry, lineY29, lineY29.startSketchPoint.geometry, .1)
        arc = sketchY.sketchCurves.sketchArcs.addFillet(lineY42, lineY42.endSketchPoint.geometry, lineY43, lineY43.startSketchPoint.geometry, .1)

        # Add a fillet Height.
        arc = sketchZ.sketchCurves.sketchArcs.addFillet(lineZ01, lineZ01.endSketchPoint.geometry, lineZ56, lineZ56.endSketchPoint.geometry, .1)
        arc = sketchZ.sketchCurves.sketchArcs.addFillet(lineZ14, lineZ14.endSketchPoint.geometry, lineZ15, lineZ15.startSketchPoint.geometry, .1)
        arc = sketchZ.sketchCurves.sketchArcs.addFillet(lineZ28, lineZ28.endSketchPoint.geometry, lineZ29, lineZ29.startSketchPoint.geometry, .1)
        arc = sketchZ.sketchCurves.sketchArcs.addFillet(lineZ42, lineZ42.endSketchPoint.geometry, lineZ43, lineZ43.startSketchPoint.geometry, .1)
 
 
        # Get the profile defined by the circle.
        profX = sketchX.profiles.item(1)
        profY = sketchY.profiles.item(1)
        profZ = sketchZ.profiles.item(1)
        
        # Create a distance extent definition        
        extrudeInput = extrudes.createInput(profX, adsk.fusion.FeatureOperations.NewComponentFeatureOperation)
        extent_distance = adsk.fusion.DistanceExtentDefinition.create(mmDepth)        
        extrudeInput.setOneSideExtent(extent_distance, adsk.fusion.ExtentDirections.PositiveExtentDirection)
        start_offset = adsk.fusion.OffsetStartDefinition.create(mmTslot_Thickness)
        extrudeInput.startExtent = start_offset
 
        # creating typical extrusions
        extrudeX = extrudes.add(extrudeInput)        
        
        # Create sub occurrence
        occurrences = rootComp.occurrences
        subOccX = occurrences.item(0)            
        
        # Get features from sub component
        subComponentX = subOccX.component                
            
        # Get the associated component.
        
        subComponentX.name = "HFS5-2020-"+ str(Depth-Tslot_Thickness*2)        
 
        # Set body appearance
        
        materialLibs = app.materialLibraries

        # get appearance lib 
        
        appearance = None
        for materialLib in materialLibs:
            appearances = materialLib.appearances

            try:
                appearance = appearances.itemByName("Aluminum - Anodized Glossy (Blue)")
            except:
                pass
        
            if appearance:
                break

        bodyX = extrudeX.bodies[0]
 
        # Create the second joint geometry with sketch point
        startFaceOfExtrude = extrudeX.startFaces.item(0)
        jointGeometryX = adsk.fusion.JointGeometry.createByPoint(subComponentX.originConstructionPoint)
        jointGeometryR = adsk.fusion.JointGeometry.createByPoint(rootComp.originConstructionPoint)
        #ui.messageBox(str(jointGeometryX))
 
        # Create the JointOriginInput
        joints = rootComp.joints
        jointInput = joints.createInput(jointGeometryX,jointGeometryR)
        jointInput.setAsRigidJointMotion()
 
        # Create the JointOrigin
        joints.add(jointInput)                
                 
        # change body appearance         
        bodyX.appearance = appearance;        
 
        # Create input entities for rectangular pattern
        inputEntites = adsk.core.ObjectCollection.create()
        inputEntites.add(subOccX)
        
        # Get x and y axes for rectangular pattern
        xAxis = rootComp.xConstructionAxis
        yAxis = rootComp.yConstructionAxis
        zAxis = rootComp.zConstructionAxis
        
        # Quantity and distance
        quantityOne = adsk.core.ValueInput.createByString('2')
        distanceOne = adsk.core.ValueInput.createByString(str(Width-(Profile*10))+"mm")
        quantityTwo = adsk.core.ValueInput.createByString('2')
        distanceTwo = adsk.core.ValueInput.createByString(str(Height-(Profile*10))+"mm")
        quantityThr = adsk.core.ValueInput.createByString('2')
        distanceThr = adsk.core.ValueInput.createByString(str(Depth-(Profile*10))+"mm")
        
        # Create the input for rectangular pattern xZ Plan
        rectangularPatterns = rootComp.features.rectangularPatternFeatures        
        rectangularPatternInput = rectangularPatterns.createInput(inputEntites, xAxis, quantityOne, distanceOne, adsk.fusion.PatternDistanceType.SpacingPatternDistanceType)
 
        # Set the data for second direction
        rectangularPatternInput.setDirectionTwo(zAxis, quantityTwo, distanceTwo)
        
        # Create the rectangular pattern
        rectangularFeature = rectangularPatterns.add(rectangularPatternInput)        
 
        # Create the input for rectangular pattern yZ Plan
        extrudeInput = extrudes.createInput(profY, adsk.fusion.FeatureOperations.NewComponentFeatureOperation)        
        extent_distance = adsk.fusion.DistanceExtentDefinition.create(mmWidth)        
        extrudeInput.setOneSideExtent(extent_distance, adsk.fusion.ExtentDirections.PositiveExtentDirection)
        start_offset = adsk.fusion.OffsetStartDefinition.create(mmProfile)
        extrudeInput.startExtent = start_offset
 
        # creating typical extrusions
        extrudeY = extrudes.add(extrudeInput)        
        
        subOccY = occurrences.item(4)
        subComponentY = subOccY.component
        subComponentY.name = "HFS5-2020-"+ str(Width-int(Profile)*2*10)
        bodyY = extrudeY.bodies[0]
        bodyY.appearance = appearance;         

        
 
        inputEntites.removeByItem(subOccX)
        inputEntites.add(subOccY)
        rectangularPatterns = rootComp.features.rectangularPatternFeatures        
        rectangularPatternInput = rectangularPatterns.createInput(inputEntites, yAxis, quantityThr, distanceThr, adsk.fusion.PatternDistanceType.SpacingPatternDistanceType)
        rectangularPatternInput.setDirectionTwo(zAxis, quantityTwo, distanceTwo)
        rectangularFeature = rectangularPatterns.add(rectangularPatternInput)

        # Create the input for rectangular pattern xY Plan
        extrudeInput = extrudes.createInput(profZ, adsk.fusion.FeatureOperations.NewComponentFeatureOperation)        
        extent_distance = adsk.fusion.DistanceExtentDefinition.create(mmHeight)        
        extrudeInput.setOneSideExtent(extent_distance, adsk.fusion.ExtentDirections.PositiveExtentDirection)
        start_offset = adsk.fusion.OffsetStartDefinition.create(mmProfile)
        extrudeInput.startExtent = start_offset

        # creating typical extrusions
        extrudeZ = extrudes.add(extrudeInput)      

        subOccZ = occurrences.item(8)
        subComponentZ = subOccZ.component
        subComponentZ.name = "HFS5-2020-"+ str(Height-int(Profile)*2*10)
        bodyZ = extrudeZ.bodies[0]
        bodyZ.appearance = appearance;   
        
        inputEntites.removeByItem(subOccY)
        inputEntites.add(subOccZ)
        rectangularPatterns = rootComp.features.rectangularPatternFeatures        
        rectangularPatternInput = rectangularPatterns.createInput(inputEntites, xAxis, quantityOne, distanceOne, adsk.fusion.PatternDistanceType.SpacingPatternDistanceType)
        rectangularPatternInput.setDirectionTwo(yAxis, quantityThr, distanceThr)
        rectangularFeature = rectangularPatterns.add(rectangularPatternInput)   
        
        app.activeViewport.fit();  
        
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))