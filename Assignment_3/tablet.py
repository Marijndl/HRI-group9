import nao_nocv_2_1 as nao
IP="192.168.0.116"
nao.InitProxy(IP)
tabletProxy = nao.ConnectProxy("ALTabletService",IP,9559)


tabletProxy.showImage('naam.jpg')
nao.sleep(10)
tabletProxy.hideImage()
