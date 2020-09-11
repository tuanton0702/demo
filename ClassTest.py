class SieuNhan:
    def __init__(self,ten,vukhi,mausac):
        self.ten=ten
        self.vukhi=vukhi
        self.mausac=mausac
pass
sieunhando=SieuNhan("GaoRed","Kiem","Do")
sieunhanxanh=SieuNhan("GaoBlue","Sung","Xanh")
print(" {} dang thong dit {}".format(sieunhando.ten,sieunhanxanh.ten))
print("{} la vu khi cua {} ".format(sieunhanxanh.vukhi,sieunhanxanh.ten))
// test master