# 34658 (Fourth Fighting Tactic, Cadena 4th job adv)
sm.setPlayerAsSpeaker()
if chr.getJob() == 6411:
    sm.sendNext("Well, those skills the Chief taught me are perfect now.")
    sm.sendSay("Guess it's time to start getting creative and come up with some new skills.")
    sm.sendSay("This is good... and this would help here... it's coming together nicely.")
    # add stats
    sm.setJob(6412)
    sm.addAP(5)
    sm.addSP(5)
    sm.addMaxHP(350)
    sm.addMaxMP(200)
    sm.sendNext("Yes! The first skill unique to me is done! Chief is gonna be blown away.")
    sm.sendSayOkay("Let's test this bad boy out. Time to open the skill window (K) and take a look.")
    sm.completeQuestNoCheck(parentID)