import os

def input(message):
    message =  message.lower()
    messageInArray = message.split(" ") 

    if len(messageInArray) == 2:

        file = open("helplib/help.md")
        content = file.read()
        file.close()

        return content

    else:
        helplib = os.listdir("helplib")

        for helpName in helplib:
            if helpName == messageInArray[2] + ".md":
                
                file = open("helplib/" + helpName)
                content = file.read()
                file.close()

                return content
                
        return "Subcommand out of list!"