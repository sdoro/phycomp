def phy = agent('phy')
phy[3].janus = true
phy[1].powerLevel = -1.0
phy[2].powerLevel = -1.0
phy[3].powerLevel = -1.0
phy[4].powerLevel = -1.0
phy.signalPowerLevel = -1.0
node.nodeName = 'tx'
node.address = host(node.nodeName)
phy[1].fmin = 4700
phy[2].fmin = 4700
phy[1].fstep = 80
phy[2].fstep = 80
println "Done!"
