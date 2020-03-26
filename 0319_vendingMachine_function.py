
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


def deposit():

    """
    儲值
    :return: nothing
    """
    global balance  # 宣告函式中會用到全域變數balance
    value = eval(input('儲值金額:'))
    while value < 1:
        # 若使用者輸入數字小於零,需要重新輸入
        print('====儲值金額需大於零=!==')
        value = eval(input('儲值金額:'))
    balance += value
    print(f'儲值後餘額為 fbalance)元')


def buy():
    """
    購買
    :return: nothing
    """
    global balance, drinks# 宣告函式中會用到全域變數balance, drinks
    # 印出品項
    print( '\n請選擇商品')
    for i in range(0, len(drinks)):
        print(f'({ i +1})\t{drinks [i] ["name"]} \t {drinks [i] ["price"]}元')
    choose = eval(input('請選擇:'))

    while choose < 1 or choose > 6:
        print('====請輸入1-6之間=ニニ=')
        choose = eval(input('請選擇:'))


    buy_drink = drinks [choose - 1]
    while balance < buy_drink['price']:
        print('====餘額不足,需要儲值嗎?====')
        want_deposit = input('y/n? ')
        if want_deposit == 'y':
            deposit()  # 這裡reuse"儲值”函式
        elif want_deposit == 'n':
            break  # 不儲值,跳出迴圈
        else:
            print('====請重新輸入=ニニ=')
    # 儲值後餘額大於商品金額再購買
    if balance >= buy_drink['price']:
        print(f'已購買fbuy_drink["name"] fbuy_drink["price"]元')
        balance -= buy_drink['price']
        print(f'購買後餘額為fbalance元')


while flag:
    print('\n===============')
    select = eval(input('1.儲值\n2.購買\n3,查詢餘額\n4.離開\n請選擇:'))


    if select == 1:  # 儲值
        deposit()


    elif select == 2: # 購買

        buy()


    elif select==3: # 查詢餘額
        print(f'目前餘額為{balance}元')


    elif select == 4: # 離開
        print('bye')
        flag = 0
        break

    else:  # 重新輸入
        print('====請輸入1-4之間====')
        continue