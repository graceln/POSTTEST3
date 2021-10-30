print("==== Welcome to my bakery ====")

menu = [['', '', 0], ['baguette', 20000, 1], [
    'garlic bread', 25000, 2], ['bread rolls', 15000, 3]]
order = []

length = len(menu)

grace = 1
while grace < length:
    print(str(grace) + ". " + menu[grace][0] + " : " + str(menu[grace][1]))
    grace += 1

pilih = length
menus = int(input("Masukan nomor menu : "))

while True:
    if menus >= pilih:
        print("||--------------Menu tidak ada--------------||")
        menus = int(input("Masukan nomor menu : "))
    else:
        break

jumlah_pembelian = int(input("Masukkan jumlah pembelian: "))
bayar = jumlah_pembelian * int(menu[menus][1])
order.append([menu[menus][0], menu[menus][1],
             jumlah_pembelian, bayar, int(menu[menus][2])])

orderl = len(order)
listOrder = orderl - 1

print("")
print("Menu" + " | " + "Harga" + " | " + "Jumlah dibeli" + " | " + "Total")
for m in order:
    print(m[0] + " | " + str(m[1]) + " | " + str(m[2]) +
          " | " + str(m[3]))
print("")

while True:
    jawab = input(
        "Apakah ada yang menu yang ingin ditambah atau dikurangi? [tambah/kurang/tidak]: ")
    if jawab == 'tambah':
        print("")
        grace = 1
        while grace < length:
            print(str(grace) + ". " + menu[grace]
                  [0] + " : " + str(menu[grace][1]))
            grace += 1
        menus = int(input("Masukan nomor menu : "))

        while True:
            if menus > pilih:
                print("||--------------Menu tidak ada--------------||")
                menus = int(input("Masukan nomor menu : "))
            else:
                break
        ini = menu[menus][2]

        for lol in order:
            if ini == lol[4]:
                jumlah_tambahan = int(input("Masukkan jumlah tambahan: "))
                lol[2] = int(lol[2]) + jumlah_tambahan
                lol[3] = int(lol[2]) * int(lol[3])
                print("")
                print("Menu" + " | " + "Harga" + " | " +
                      "Jumlah dibeli" + " | " + "Total")
                for m in order:
                    print(m[0] + " | " + str(m[1]) + " | " +
                          str(m[2]) + " | " + str(m[3]))
                print("")
                break
            else:
                jumlah_pembelian = int(input("Masukkan jumlah pembelian: "))
                bayar = jumlah_pembelian * menu[menus][1]

                order.append([menu[menus][0], menu[menus][1],
                             jumlah_pembelian, bayar, menu[menus][2]])

                orderl = len(order)
                listOrder = orderl - 1

                print("")
                print("Menu" + " | " + "Harga" + " | " +
                      "Jumlah dibeli" + " | " + "Total")
                for m in order:
                    print(m[0] + " | " + str(m[1]) + " | " +
                          str(m[2]) + " | " + str(m[3]))
                print("")
                break
        if orderl == 0:
            jumlah_pembelian = int(input("Masukkan jumlah pembelian: "))
            bayar = jumlah_pembelian * menu[menus][1]

            order.append([menu[menus][0], menu[menus][1],
                          jumlah_pembelian, bayar, menu[menus][2]])

            orderl = len(order)
            listOrder = orderl - 1

            print("")
            print("Menu" + " | " + "Harga" + " | " +
                  "Jumlah dibeli" + " | " + "Total")
            for m in order:
                print(m[0] + " | " + str(m[1]) + " | " +
                      str(m[2]) + " | " + str(m[3]))
            print("")
    elif jawab == "kurang":
        grace = 0
        print("Menu" + " | " + "Harga" + " | " +
              "Jumlah dibeli" + " | " + "Total")
        while grace < orderl:
            print(order[grace][0] + " | " + str(order[grace][1]) +
                  " | " + str(order[grace][2]) + " | " + str(order[grace][3]))
            grace += 1
        print("pilih dari 0 - " + str(listOrder))
        menus = int(input("Masukan nomor menu : "))

        while True:
            if menus > listOrder:
                print("||--------------Menu tidak ada--------------||")
                menus = int(input("Masukan nomor menu : "))
            else:
                break
        jumlah_dikurang = int(input("Masukkan jumlah dikurang: "))
        order[menus][2] = int(order[menus][2]) - jumlah_dikurang
        if order[menus][2] <= 0:
            order.pop(menus)
            print("")
            print("Menu" + " | " + "Harga" + " | " +
                  "Jumlah dibeli" + " | " + "Total")
            print("")
            orderl = len(order)
        else:
            order[menus][3] = int(order[menus][2]) * int(order[menus][1])
            print("")
            print("Menu" + " | " + "Harga" + " | " +
                  "Jumlah dibeli" + " | " + "Total")
            for m in order:
                print(m[0] + " | " + str(m[1]) + " | " +
                      str(m[2]) + " | " + str(m[3]))
            print("")
    else:
        orderl = len(order)
        listOrder = orderl - 1

        # table menu dipesan pelanggan
        print("")
        print("Menu" + " | " + "Harga" + " | " +
              "Jumlah dibeli" + " | " + "Total")
        for m in order:
            print(m[0] + " | " + str(m[1]) + " | " +
                  str(m[2]) + " | " + str(m[3]))
        print("")

        total_bayar = 0
        loop = 0
        while loop < orderl:
            total_bayar = total_bayar + order[loop][3]
            loop += 1

        diskon = 0
        # jika membeli diatas harga 50000 akan mendapatkan potongan diskon 10%
        if total_bayar > 50000:
            diskon = total_bayar * (10/100)
        # jika membeli diatas harga 100000 akan mendapatkan potongan diskon 25%
        elif total_bayar > 100000:
            diskon = total_bayar * (25/100)
        else:
            print("tidak ada diskon")

        bayar = total_bayar - diskon

        print("")
        print("Harga sebelum diskon : Rp.{}".format(int(total_bayar)))
        print("Potongan harga yang didapatkan : Rp.{}".format(int(diskon)))
        print("Harga setelah diskon : Rp.{}".format(int(bayar)))
        print("=====")
        print("Total Pembayaran Anda: Rp.{}".format(int(bayar)))
        break
