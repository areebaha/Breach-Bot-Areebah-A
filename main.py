#Breach Bot Starter Code
breachYear = 2019

#Greets user
print("Hello! I'm Breach Bot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts year of Breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since the Facebook Data Breach.")

#Introduces Breach
print("Would you like to learn about the Facebook 2019 Breach?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization's response, (c) I would like to hear your reflection")
  topic = input()
  
  if topic.lower() == "a":
    print("Personal information of 533 million users was stolen from Facebook, including phone numbers, full names, locations, and email addresses. The hack was by a malicious actor, who exploited a feature that allowed users to find each other through phone numbers.")
  
  elif topic.lower() == "b":
    print("Facebook fixed the issue in August 2019 but decided not to tell the 533 million users impacted by the data breach. They didn’t recommend anything to the affected users.")
  
  elif topic.lower() == "c":
    break
  
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")


#Introduces my take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#Shares my take
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) in relation to the CIA Triad, (b) my reaction, (c) my advice, (d) none")
  topic = input()
  
  if topic.lower() == "a":
    print("This data breach connects to confidentiality because malicious actors accessed the data of 533 million users in Facebook’s 2019 data breach, and stole phone numbers, names, locations, and email addresses. ")
  
  elif topic.lower() == "b":
    print("We disagree with the organization’s response because Facebook didn’t tell the 533 million affected users that they were involved in a data breach. These affected users had no knowledge that their information was leaked.")
  
  elif topic.lower() == "c":
    print("I would convince victims to take action by saying that personal information can be used to steal a person’s identity and money. My advice would be to change any passwords that are too simple or are reused often.")
    
  elif topic.lower() == "d":
    break  
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")
#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")