import time
import etc.security
import etc.msgwatchdog.cats
owoid = None
channel = None
user = None
update = None
messages = []

def prep(self, client, channelid: int, owo=408785106942164992):
    global owoid, channel, user, update, messages
    owoid = owo
    channel = client.get_channel(channelid)
    user = client.user
    update = time.time()
    messages = []

async def check(second):
    """
    call this after you send a message
    """
    called = time.time()
    while True:
        #wait for message
        await client.wait_for('message', check=lambda message: message.author == self.owoid)
        #check if message is sent for us
        #to do this firstly get message type
        try:
            mtype = etc.msgwatchdog.cats.check(message, self.user)
        except Exception as e:
            print(e)
            continue
