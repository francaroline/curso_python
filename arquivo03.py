class Dispositivo(object):
    def __init__(self):
        self.android = 1
        self.ios = 2
    
    def detectar_dispositivo(self,tipo_dispositivo): 
        
        if tipo_dispositivo == 1:
            print("android")
        else:
            print("ios")
            
dispositivo = Dispositivo()
dispositivo.detectar_dispositivo (5)
