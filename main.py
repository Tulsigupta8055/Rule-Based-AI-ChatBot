# ...RULE BASED PYTHON AI CHATBOT...

print("---Namaste! Welcome to your AI ChatBot---")
print("You can ask me, Basic question, Type <'bye'> to exit from AI ChatBot.")
#chatbot memeory creation[ dictionary of responses ]
responses={
    "hello":"Hi, welcome How can I help you?",
    "how are you":"I am very fine. Thank you",
    "who are you":"I am a Smart AI ChatBot",
    "motivate line":"keep going, every bug of your project makes you a better developer.",
    "i am happy":"Great to hear that",
    "keep motivate me":"No Pain No Gain, One Aim Own Game. "
}
#use of method/function to get response of Ai ChatBot
def getResponseOfBot(userquestion):
    userquestion = userquestion.lower()
    for eachkey in responses:
        if eachkey in userquestion:
            return responses[eachkey]
    return "I am not able to answer that yet, I will learn that very soon."

#Take user input...
while True:
    userinput=input("Please ask your question:")
    reply=getResponseOfBot(userinput)
    print("Bot Response:",reply)

    if "bye" in userinput.lower():
        break





