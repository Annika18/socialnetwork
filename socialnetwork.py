
allUsers = []
network = True

class Profiles:

   def __init__(self, user):
      self.user = user
      self.userbox = []

   def userbox(self, messages):
      self.messages.append(messages)


   def showUsers(self):
      print(self.user)
      print(self.userbox)

reply = ""

def initialDisp(reply):
    print("Would you like to create user (c), login (l), see user lists (s), or exit (e)?")
    reply = input()
    reply = reply.lower()
    return (reply)

def createUser():
    username = input("Create a username: ")
    #allUsers.append(username)
    x = Profiles(username)
    allUsers.append(x)

    for i in range(len(allUsers)):
        print(allUsers[i].user)


while network==True:
    reply = initialDisp(reply)

    if reply == "c":
        createUser()
        #print(initialDisp)

    elif reply == "l":
        name = input("Username: ")

        for i in range(len(allUsers)):
            if name == allUsers[i].user:
                print("You are logged in")
                print("Enter m to send a message")
                print("Enter v to view inbox")
                print("Enter l to logout")
                sendMessage = input()
                sendMessage = sendMessage.lower()

                if sendMessage == "m":
                    print("Who do you want to send your message to?")
                    recipient = input()
                    for y in range(len(allUsers)):
                        if recipient == allUsers[y].user:
                            myMessage = input("Enter your message here: ")
                            allUsers[y].userbox.append('from: '+allUsers[i].user + "\n" + myMessage + "\n")
                            print("success")

                    

                        else:
                            print("User does not exist")
                if sendMessage == "v":
                    #view messages
                    for item in allUsers[i].userbox:
                        print (item)
                elif sendMessage == "l":
                    #logout
                    break
    elif reply == "s":
        for i in range(len(allUsers)):
            print(allUsers[i].user)
    elif reply == "e":
        network = False

    else:
        print("Command not found.")
