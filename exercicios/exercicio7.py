#import datetime 

#def func(year,month,day,aux):
#    x = datetime.datetime(year,month,day)
#    if aux==1:
#        print(x.strftime('%Y')+','+x.strftime('%d')+' of '+x.strftime('%B'))
#    if aux==2:
#        print(x.strftime('%d')+'/'+x.strftime('%m')+'/'+x.strftime('%Y'))
#func(2000,9,8,1)
#func(2000,9,8,2)
#---------

from datetime import datetime

def func(nome,dt,vet):
    dt = dt.split("/")
    date = datetime(int(dt[2]),int(dt[1]),int(dt[0]))
    d = dict()
    vet = vet.split(';')
    d = {"nome": nome, "dataNascimento":date, "telefone":vet } 
    print(d["dataNascimento"])

nome = input("Dígite seu nome: ")
dt = input("Dígite sua Data de aniversario no formato dia/mes/ano: ")
vet = input("Dígite seu número de telefone, sem pontos ou traços. Caso tenha mais de um número, os separe com ;:  ")
teste = func(nome,dt,vet)
#class Pessoa:
#    def __init__(self,nome):
#        self._nome = nome
#    def _get_nome(self):
#        return self._nome
#    def _set_nome(self, nome):
#        self._nome = nome
#    nome = property(_get_nome, _set_nome)

# p = Pessoa('Julio')
# print(p.nome)