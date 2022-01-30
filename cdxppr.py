import requests
from mspam import send_mail as sm
from prev import main
import sys
import os
from time import sleep as sl

def menu():
    while True:
        os.system('CLS') 
        print("""

    ░█████╗░██████╗░██╗░░██╗██████╗░██████╗░██████╗░
    ██╔══██╗██╔══██╗╚██╗██╔╝██╔══██╗██╔══██╗██╔══██╗
    ██║░░╚═╝██║░░██║░╚███╔╝░██████╔╝██████╔╝██████╔╝
    ██║░░██╗██║░░██║░██╔██╗░██╔═══╝░██╔═══╝░██╔══██╗
    ╚█████╔╝██████╔╝██╔╝╚██╗██║░░░░░██║░░░░░██║░░██║
    ░╚════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░╚═╝░░╚═╝
            """)
        print()

        print("1. Send Mail\n2. Ip Info\n3. Phone Number Info")

        who = input("")

        if who == "1":
            sm()
            sl(2)
        elif who == "2":
            ip_info()
        elif who == "3":
            phoneNumber_info()
        else:
            menu()

def phoneNumber_info():
    get_phone = input( '[+] Phone : ' )

    response = requests.get( f'https://htmlweb.ru/geo/api.php?json&telcod={ get_phone }' )
 
    user_country = response.json()[ 'country' ][ 'english' ]
    user_id = response.json()[ 'country' ][ 'id' ]
    user_location = response.json()[ 'country' ][ 'location' ]
    user_city = response.json()[ 'capital' ][ 'english' ]
    user_width = response.json()[ 'capital' ][ 'latitude' ]
    user_lenth = response.json()[ 'capital' ][ 'longitude' ]
    user_post = response.json()[ 'capital' ][ 'post' ]
    user_oper = response.json()[ '0' ][ 'oper' ]
 
    all_info = f'\nCountry : { user_country }\nID : { user_id }\nLocation : { user_location }\nCity : { user_city }\nLatitude : { user_width }\nLongitude : { user_lenth }\nIndex post : { user_post }\nOperator : { user_oper }'
 
    print( all_info )

    input()

def ip_info():
    get_ip = input( '[+] IP : ' )

    response = requests.get( f'http://ipinfo.io/{ get_ip }/json' )
 
    user_ip = response.json()[ 'ip' ]
    user_city = response.json()[ 'city' ]
    user_region = response.json()[ 'region' ]
    user_country = response.json()[ 'country' ]
    user_location = response.json()[ 'loc' ]
    user_org = response.json()[ 'org' ]
    user_timezone = response.json()[ 'timezone' ]
 
    all_info = f'\n<INFO>\nIP : { user_ip }\nCity : { user_city }\nRegion : { user_region }\nCountry : { user_country }\nLocation : { user_location }\nOrganization : { user_org }\nTime zone : { user_timezone }'
 
    print( all_info )

    input()

main()
menu()
