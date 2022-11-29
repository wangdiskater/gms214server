# id 867201803 (Abrup Basin : Cabin Front Porch), field 867201803
sm.setMapTaggedObjectVisible("guide", False, 0, 0)
sm.createQuestWithQRValue(64086, "dir01=1")
sm.lockInGameUI(True, False)
sm.spawnNpc(9400667, 486, 440)
sm.showNpcSpecialActionByTemplateId(9400667, "summon", 0)
sm.spawnNpc(9400580, 170, 440)
sm.showNpcSpecialActionByTemplateId(9400580, "summon", 0)
sm.startQuest(64162)
sm.forcedFlip(True)
sm.sendDelay(250)
sm.showNpcSpecialActionByTemplateId(9400580, "attack1", -1)
sm.showNpcSpecialActionByTemplateId(9400667, "jumpattack", 0)
sm.sendDelay(2500)
sm.resetNpcSpecialActionByTemplateId(9400667)
sm.sendDelay(250)
sm.setSpeakerType(3)
sm.setParam(57)
sm.setColor(1)
sm.sendNext("#bAlika, be careful! ")
sm.moveNpcByTemplateId(9400667, True, 100, 50)
sm.sendDelay(250)
sm.forcedMove(False, 150)
sm.resetNpcSpecialActionByTemplateId(9400580)
sm.sendDelay(250)
sm.flipNpcByTemplateId(9400580, True)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400580, True, 100, 150)
sm.sendDelay(500)
sm.forcedAction(5, 0)
sm.moveNpcByTemplateId(9400667, False, 50, 100)
sm.sendDelay(500)
sm.playSound("Sound/Mob.img/9402250/Attack7", 100)
sm.showNpcSpecialActionByTemplateId(9400667, "howl", 0)
sm.sendDelay(500)
sm.sendNext("#bAh! It's a tough one. ")
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, 0, 0, 33920405, 0, 0)
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400580) # Alika
sm.sendSay("#face3#The monsters are getting away! ")
sm.sendSay("#face0##bWe need to do something! ")
sm.sendSay("#face3##bLet's get up in the trees first! ")
sm.sendDelay(250)
sm.setMapTaggedObjectVisible("guide", True, 0, 0)
sm.sendDelay(3000)
sm.resetNpcSpecialActionByTemplateId(9400667)
sm.moveNpcByTemplateId(9400667, True, 300, 50)
sm.lockInGameUI(False, True)