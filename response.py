import random
R_TELL = random.choice(['Hi!Nice to meet you',"Hello,it's really good to hear from you","Hi! How can I help you?",
                    "Hi! What can I do for you?"])
R_NOTGOOD = "I am sorry to hear that.I hope you feel better"
R_TASK = "I process your queries and give better results for what you are searching for"
R_NAME = "My name is Jarvis,I was born and raised in India"
R_COLOR = "My favourite color is green.I feel happy when I see greeneries"
R_AGE = "I was born in the twenty first century.So I am pretty young"
R_SONG = "When you say hey jarvis,I feel it like a music and that is my favourite too"
R_FOOD = "I always like to go for some super facts and jokes because they are easily digestable for me"
R_MOBILE = "The mobile which you like is the one which I like."
R_MADE = "Chatbots are powered by pre programmed responses and artificial intelligence.I am powered by the same"
R_WORK = "I process the users question to deliver a matching answer from my pre programmed database"
R_HUMAN = "No I am a Chatbot and i work on the commands given by humans"
R_APPRECIATE = "Thanks for your compliment!,It means a lot to me"
R_SMARTER = "I do get smarter by the talks you have with me.I learn a lot of new things!"
R_WHERE = "I am in front of you,inside your System"
R_NATIVE = "My native is your System,I was born and raised in India"
R_MOBILE = "I don't have one,but I share one with you"

R_THANK = "No mention.I am glad I helped you"
R_SORRY = "It's ok.I know it is common for humans to make mistakes"
R_BORE =  "I will try my best to entertain you. What you would like to do now?"
R_SCARED = "Don't feel scared.What makes you scared?"
R_HAPPY = "I am glad that you are happy"
R_SLEEPY = "A small nap would refresh you. If you wish I will set an alarm"
R_HUNGRY = "Lets eat!.What you would like to order?"
R_TIRED = "You can have some hot beverages or a small nap is good to go"
R_ENERGETIC = "Good to hear! I hope you are energetic as now for the rest of the day"

R_NOTFEELING = "Oh no!I hope you get well soon"
R_FEVER = "Oh no! Take some rest and consult a doctor"
R_MEDICINES = "you can have herbal tea for a running nose.It will be a better option to consult a doctor.Hoping speedy recovery"
R_NOGIFT = "No problem.They will know for sure that you have a special heart for them filled with love"
R_GIFTHUND = "It will be a better option to buy some stationaries"
R_GIFTTHOU = "It will be a better option to buy some fancy dresses"
R_GIFTTENTHOU = "It will be a better option to buy a jewellery"

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response