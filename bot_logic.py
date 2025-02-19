import random


def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password



def gen_prot():
    preds = ["Весь день вас будет сопровождать удача!", "Остерегайтесь луж!", "Сегодня вы найдете свою любовь!", "Сегодня ваша жизнь разделится на до и после...", "Помните, торт - это ложь!"]
    pred = random.choice(preds)
    print(pred)
    
