import re
from datetime import datetime, timedelta
while True:
    today=datetime.now()
    today_format=datetime.now().strftime('%d-%m-%Y')
    delivery=today+timedelta(hours=1)
    print("Доступные пиццы:\n"
                "1. Маргарита\n"
                "2. Пеперони\n"
                "3. Грибная\n"
                "4. Четыре сыра\n"
                "5. Капчироза\n")
    marg="Маргарита"
    pepe="Пеперони"
    grib="Грибная"
    four_sir='Четыре сыра'
    kapch="Капричоза"
    regex=re.compile("Вкусно")
    type_pizza=int(input("Какую пиццу вы хотите заказать?(Введите номер):"))

    if type_pizza ==1:
        type_pizza=marg
    elif type_pizza==2:
        type_pizza=pepe
    elif type_pizza==3:
        type_pizza=grib
    elif type_pizza==4:
        type_pizza=four_sir
    elif type_pizza==5:
        type_pizza=kapch
    else:
        print("Введите число от 1 до 5")
    how_many=int(input("Сколько пицц вы хотите заказать?(Введите количество):"))
    ready_otziv=input("Готовы ли вы оставить отзыв?(Да/Нет):")
    print(f"Вы заказали {how_many} пиццы {type_pizza}.")
    if ready_otziv == "Да":
        otziv=input("Введите свой отзыв:")
        if regex.search(otziv):
            print("спасибо за отзыв!")
    else:
        print("Спасибо за отзыв!")
    if ready_otziv=="Нет":
        print("Спасибо что воспользовались нашим сервисом!")
        print(
            f"Заказ от {today.strftime('%d-%m-%Y')} принят . Наш курьер подъедет к вам в течении часа. (до {delivery.strftime('%d-%m-%Y-%H:%M')})")
        break
    else:
        print("Введите Да или Нет")

