import random
import tkinter as tk

root = tk.Tk()
root.title('Chatbot for Fatima Siddiqui!')
root.geometry('800x500')  # Adjust the size as needed
root['bg']='blue'
img= tk.PhotoImage()

botsay = tk.StringVar()

hello = ['hi', 'hey', 'hello', 'hello there', 'heyy', 'is anyone there?', 'are you there?', 'hii']
bye = ['bye', 'see you later', 'bye bye', 'Allah Hafiz', 'okay bye', 'ok bye', 'thanks bye']
howare = ['how are you?', 'how are you', 'how do you do?', 'are you okay?']
name = ['what is your name?', 'what is your name', 'introduce yourself', 'your name?']
menu = ['what is on the menu?', 'i want to order', 'tell me your menu', 'menu please']
hours = ['what is your working hours?', 'what is your timing please', 'your working hours please']
ans = ['okay', 'alright', 'okay thanks', 'fine', 'ok']

print('************************************************************************')

def chat():
    if UserInput.get().lower() in hello:
        bot = ['Hello!', 'Welcome!!', 'Hi dear', 'hey dear!', 'Hi there!']
        botsay.set(random.choice(bot))
    elif UserInput.get().lower() in bye:
        bot = ['Bye! See you again', 'Bye!', 'Allah Hafiz', 'will miss you..please come again :(']
        botsay.set(random.choice(bot))
    elif UserInput.get().lower() in howare:
        bot = ['I am good', 'I am fine, Thank you!', 'Allah ka shukr', 'I am great']
        botsay.set(random.choice(bot))
    elif UserInput.get().lower() in name:
        bot = ['My name is Bot, Created by Fatima Siddiqui :)', 'myself Bot',
               'Hey, My name is Bot.. I am created by Fatima', 'Hey! I am bot']
        botsay.set(random.choice(bot))
    elif UserInput.get().lower() in menu:
        bot = ['We have burgers today', 'we have spicy tikka pizza today in our menu!',
               'We have biryani today!']
        botsay.set(random.choice(bot))
    elif UserInput.get().lower() in hours:
        bot = ['12 pm to 5 pm', 'Hey..its from 12 pm to 5 pm.', 'We are available from 2 pm to 5 pm']
        botsay.set(random.choice(bot))
    elif UserInput.get().lower() in ans:
        bot = ['yes', 'hmm', 'yes dear', 'yup']
        botsay.set(random.choice(bot))
    else:
        bot = ['ahh..what?', 'sorry.. what do you mean']
        botsay.set(random.choice(bot))

head = tk.Label(root, text='Chatbot By Fatima Siddiqui', font=('times new roman', 40))
head.pack(pady=10)

holder = tk.Frame(root)
holder.pack(pady=50)

userText = tk.Label(holder, text='Input-', font=('times new roman', 30))
userText.grid(row=0, column=0, padx=10)

UserInput = tk.Entry(holder, font=('times new roman', 30))
UserInput.grid(row=0, column=1, padx=10)

submitbtn = tk.Button(holder, text='Submit', font=('times new roman', 20), command=chat)
submitbtn.grid(row=0, column=2, padx=10)

botText = tk.Label(root, text='Bot-', font=('times new roman', 30))
botText.pack(pady=10)

botOutput = tk.Entry(root, textvariable=botsay, font=('times new roman', 30))
botOutput.pack(pady=10)

root.mainloop()
