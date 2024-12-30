def nhap_so_nguyen():
    n=int(input("n="))
    global L
    L=[]
    for i in range(n):
        so_nguyen=int(input(""))
        L.append(so_nguyen)
    return  L

def dem_so_nguyen_duong():
    global so_nguyen_duong
    so_nguyen_duong=0
    for so_nguyen in L:
        if so_nguyen > 0:
          so_nguyen_duong += 1           

def TBC_so_nguyen_duong():
    global sum_so_nguyen_chan
    global so_nguyen_chan
    global TBC_so_nguyen_chan
    sum_so_nguyen_chan = 0
    so_nguyen_chan = 0
    for so_nguyen in L:
        if so_nguyen % 2 == 0:
            sum_so_nguyen_chan += so_nguyen
            so_nguyen_chan += 1
    if so_nguyen_chan == 0:
        TBC_so_nguyen_chan = 0
    else:
        TBC_so_nguyen_chan = sum_so_nguyen_chan / so_nguyen_chan

def InKQ():
    print("SND=", so_nguyen_duong,sep="")
    print("TBC=", TBC_so_nguyen_chan,sep="")

nhap_so_nguyen()
dem_so_nguyen_duong()
TBC_so_nguyen_duong()
InKQ()