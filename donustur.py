def c2f(c):
    return c*1.8 + 32

def c2k(c):
    return c+273.15

def f2c(f):
    return (f-32)/1.8

def f2k(f):
    return (f+459.67)*5/9

def  k2c(k):
    return k-273.15

def k2f(k):
    return k*9/5-459.67

def degerAl(secim):
    if secim == 1 or secim == 2:
        sicaklik = "Celcius"
    elif secim == 3 or secim == 4:
        sicaklik = "Fahrenheit"
    elif secim == 5 or secim == 6:
        sicaklik = "Kelvin"

def main():
    print("""
    ********************
    SICAKLIK DÖNÜŞTÜRÜCÜ
    ********************
    Yapabileceğiniz işlemler: 
    1- Celcius -> Fahrenheit dönüşümü
    2- Celcius -> Kelvin dönüşümü
    3- Fahrenheit -> Celcius dönüşümü
    4- Fahrenheit -> Kelvin dönüşümü
    5- Kelvin -> Celcius dönüşümü
    6- Kelvin -> Fahrenheit dönüşümü
    """)
    flag = True
    while(flag):
        secim = input("Lütfen seçiminizi girin (q ile çıkabilirsiniz) :")

        if secim == 'q':
            print("Çıkış yapılıyor...")
            flag = False

        elif secim == '1':
            c = float(input("Celcius değerini girin: "))
            print("{} celcius {} fahrenheit yapmaktadır.".format(c,c2f(c)))

        elif secim == '2':
            flg = True
            while(flg):
                c = float(input("Celcius değerini girin (min -273.15 girebilirsiniz): "))
                if c >= -273.15:
                    flg = False
            print("{} celcius {} kelvin yapmaktadır.".format(c, c2k(c)))

        elif secim == '3':
            f = float(input("Fahrenheit değerini girin: "))
            print("{} fahrenheit {} celcius yapmaktadır.".format(f, f2c(f)))

        elif secim == '4':
            flg = True
            while (flg):
                f = float(input("Fahrenheit değerini girin (min -459.67 girebilirsiniz): "))
                if f >= -459.67:
                    flg = False
            print("{} fahrenheit {} kelvin yapmaktadır.".format(f, f2k(f)))

        elif secim == '5':
            flg = True
            while(flg):
                k = float(input("Kelvin değerini girin (min 0 girebilirsiniz): "))
                if k >=0:
                    flg = False
            print("{} kelvin {} celcius yapmaktadır.".format(k, k2c(k)))

        elif secim == '6':
            flg = True
            while(flg):
                k = float(input("Kelvin değerini girin (min 0 girebilirsiniz): "))
                if k >= 0:
                    flg = False
            print("{} kelvin {} fahrenheit yapmaktadır.".format(k, k2f(k)))

        else:
            print("Hatalı giriş yaptınız! Lütfen yeniden deneyin.")
main()

