    #-*- coding:utf-8 -*-
import random
#@author P51C0
print("""
##########################################################################################
#                                                                                        #
#                                        P51C0                                           #
#                                                                                        #
#                                  Dictionary Gen V1                                     #
#                                                                                        #
# contact: contact.p51c0@gmail.com                                                       #
##########################################################################################
""")
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
num = '1234567890'
signos = '?-,.=!"·$%&/)('
total = upper + num + lower + signos
     
def get_passwd(len_passw=(16)):
        passwd = ''
        for i in range(len_passw):
            text = random.choice(total)
            passwd = passwd+text
        return passwd
     
passwd = get_passwd()

print(f'The password are: {passwd}')
