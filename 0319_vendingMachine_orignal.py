
flag = True
balance = 0

drinks = [
    {'name' :'可樂' ,'price': 20},
    {'name' :'雪碧', 'price': 20},
    {'name' :'茶裏王', 'price': 25},
    {'name' :'原萃', 'price': 25},
    {'name' :'純粹喝' ,'price': 30},
    {'name': '水', 'price': 20}
]

# 以上也可以寫成
# drink_name = ['可樂','雪碧','茶裏王']
# drink_price = ['20','20','25']


while flag:
    print('\n===============')
    select = eval(input('1.儲值\n2.購買\n3,查詢餘額\n4.離開\n請選擇:'))


    if select == 1:  # 儲值
        value = eval(input("儲值金額:"))
        while value < 1:
            print('====儲值金額需大於零====')
            value = eval(input('儲值金額:'))
        balance += value
        print(f'儲值後金額為{balance}元')


    elif select == 2: # 購買
        print('請選擇商品')
        # 原 for item in drinks:
        # print(f'{item["name"]}  {["price"]}元')
        # 改成以下寫法(因item無法出現流水號數字)

        for i in range(len(drinks)):
            print(f'{ i +1}. {drinks[i]["name"]}  {drinks[i]["price"]}元')
        # i+1使流水號可以從0-5變成1-6

        while choose< 1 | choose >6:
            choose = eval(input('請選擇編號:'))
            print('請輸入1-6之間的數字')
        else:
            buy_drink = drinks[choose - 1]


        if balance < buy_drink['price']:
            print('====餘額不足====')

        else:
            print(f'已購買{buy_drink["name"]} {buy_drink["price"]}元')
            balance -= buy_drink['price']
            print(f'購買後餘額為{balance}元')


    elif select== 3: # 查詢餘額
        print(f'目前餘額為{balance}元')


    elif select == 4: # 離開
        print('bye')
        flag = 0
        break

    else:  # 重新輸入
        print('====請輸入1-4之間====')
        continue