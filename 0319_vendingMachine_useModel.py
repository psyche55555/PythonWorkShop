# 匯入模組
# import datetime #匯入模組
# import datetime as d #匯入模組並重新命名為d
# import datetime as * #匯入全部的模組，這樣就不用打模組名稱了
# from datetime import date #匯入模組中的某個方法
# from datetime import date as d #匯入模組中的某個方法並重新命名為d

import vending_machine.vending_machine_model as machine

while machine.flag:
    print('\n===============')
    select = eval(input('1.儲值\n2.購買\n3,查詢餘額\n4.離開\n請選擇:'))


    if select == 1:  # 儲值
        machine.deposit()


    elif select == 2: # 購買

        machine.buy()


    elif select==3: # 查詢餘額
        print(f'目前餘額為{machine.balance}元')


    elif select == 4: # 離開
        print('bye')
        flag = 0
        break

    else:  # 重新輸入
        print('====請輸入1-4之間====')
        continue