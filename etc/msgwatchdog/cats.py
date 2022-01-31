class check:
    def hunt(message, user = None):
        content = message.content
        keywords = ["You found", "🌱"]
        if any(keyword in content for keyword in keywords):
            if user != None:
                if user.name in content:
                    return True
                else:
                    return False
            return True
        else:
            return False
    def battle (message, user = None):
        content = message.content
        keywords = ["goes into battle!"]
        if any(keyword in content for keyword in keywords):
            if user != None:
                if user.name in content:
                    return True
                else:
                    return False
            return True
        else:
            return False
def check(message, user = None):
    if check.hunt(message, user):
        return "hunt"
    elif check.battle(message, user):
        return "battle"
    else:
        raise Exception("unknown message type")