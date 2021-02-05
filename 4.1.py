import os
choice = 0
listcoffee = [0,0,0,0,0,]
pick = 0
def menu():
    global choice
    print('\tโปรแกรมร้านขายปืน\n','1.แสดงรายการสินค้า\n 2.หยิบสินค้าเข้าตะกร้า\n 3.แสดงรายจำนวนและราคาของสินค้าที่หยิบ\n 4.หยิบสินค้าออกจากตะกร้า\n 5.ปิดโปรแกรม')
    choice = input('กรุณาเลือกทำรายการ : ')
    screen_clear()

def showmenu(): 
    print('\tรายการสินค้าร้านขายปืน')
    print('\t1.ปืนกล 355 บาท\n','\t2.ปืนพก 460 บาท\n','\t3.ปืนไรเฟิ่ล 565 บาท\n','\t4.ปืนบลาซูก้า 755 บาท\n','\t5.ปืนฉีดน้ำ 950 บาท')

def pickmenu():
    global pick
    print('\tรายการสินค้า\n 1.ปืนกล\n 2.ปืนพก\n 3.ปืนไรเฟิ่ล\n 4.ปืนบลาซูก้า\n 5.ปืนฉีดน้ำ')
    pick = int(input('เลือกหยิบสินค้าหมายเลข :'))
    if pick == 1:
        listcoffee[0] += 1
    elif pick == 2:
        listcoffee[1] += 1
    elif pick == 3:
        listcoffee[2] += 1
    elif pick == 4:
        listcoffee[3] += 1
    elif pick == 5:
        listcoffee[4] += 1
    screen_clear()

def showuserpick():
    list_score = ['ปืนกล','ปืนพก','ปืนไรเฟิ่ล','ปืนบลาซูก้า','ปืนฉีดน้ำ']
    list_price = [355,460,565,755,950]
    print('{0:-<13}{1:-<13}{2:-<13}{3}'.format('สินค้า','ราคา','จำนวน','ราคารวม'))
    for i in range(0,5):
        print('{0:-<13}{1:-<13}{2:-<13}{3}'.format(list_score[i],list_price[i],listcoffee[i],listcoffee[i]*list_price[i]))

def deletuserpick():
    print('\t\nรายการสินค้า\n 1.ปืนกล\n 2.ปืนพก\n 3.ปืนไรเฟิ่ล\n 4.ปืนบลาซูก้า\n 5.ปืนฉีดน้ำ')
    depick = int(input('เลือกลำดับสินค้าที่จะหยิบออก หรือพิมพ์ -1 เพื่อออก'))
    if depick == 1:
        listcoffee[0] -= 1
    elif depick == 2:
        listcoffee[1] -= 1
    elif depick == 3:
        listcoffee[2] -= 1
    elif depick == 4:
        listcoffee[3] -= 1
    elif depick == 5:
        listcoffee[4] -= 1

def screen_clear():
    clearscreen = os.system('cls')

while True:
    menu()
    if choice == '1':
        screen_clear()
        showmenu()
    elif choice == '2':
        screen_clear()
        pickmenu()
    elif choice == '3':
        screen_clear()
        showuserpick()
    elif choice == '4':
        deletuserpick()
        screen_clear()
    elif choice == '5':
        c = input('ต้องการใช้โปรแกรมต่อหรือไม่ y/n: ')
        if c.lower() == 'n':
            screen_clear()
        elif c.lower() == 'y':
            screen_clear()
            break