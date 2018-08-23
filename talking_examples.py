def sitAndTalk(speechProxy, postureProxy):
	if postureProxy.getPosture() == "Stand":
		postureProxy.goToPosture("Sit", 1.0)
		speechProxy.say("I am now sitting")
	if postureProxy.getPosture() == "Sit":
		postureProxy.goToPosture("Stand", 1.0)
		speechProxy.say("I am now standing")

def justSit(postureProxy):
	postureProxy.goToPosture("Sit", 1.0)

def justStand(postureProxy):
	postureProxy.goToPosture("Stand", 1.0)