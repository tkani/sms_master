                       #.............sivan...thunai.................#

#...................................................#
#.....creator:C.Thamrai...kani......................#
#.....IDEA&Contributor:M.jeevanantham...............#
#.....Full_credit_goes_to:visweswaran...............#
#...................................................#
from urllib.parse import urlencode
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import json


# login in to way 2 sms

def login_check(mobile, password):
    try:

        url = "https://smsapi.engineeringtgr.com/login/?Mobile=" + mobile + "&Password=" + password

        req = Request(url)

        response = json.loads(urlopen(req).read())

        if response['msg'] != "Login Sucessfully":
            print(
                "'signup way2sms'='http://site24.way2sms.com/jsp/UserRegistration.jsp'\n And https://smsapi.engineeringtgr.com/ login this website also to get an api key")

        else:

            print("login successfullly")

            vpn_call()
    except Exception as e:
        print(e)


def vpn_call():
    html = urlopen("https://www.vpnbook.com/freevpn")

    o = html.read()

    r = BeautifulSoup(o, 'html.parser')

    list = []

    for i in r.findAll('', {'class': 'disc'}):
        for f in i.find_all('strong'):
            list.append(f.text)

        user = list[7]

        # passwords=input("enter the pass")
        passwords = list[8]

        message_call(user, passwords)
        # chose you want to send vpn message or nornal message or send other number same message or send multiple nummber different message or excit


def message_call(user, passwords):
    k = 'f'
    while len(k) == 1:
        wish = int(
            input("1.vpn book password\t 2.normal message\t 3.send_message multiple_number\t 4.sms_bomb\t 5.exit()"))
        if wish == 1:
            TO = input("enter the sender mobile number")
            # if condition for number checking
            if len(TO) == 10:
                message1 = '''username:''' + user
                message2 = '''password:''' + passwords

                messages = message1 + message2
                message_send_call(TO, messages)
            else:
                print("enter the number 10 digit")
        elif 2 == wish:
            TO = input("enter the sender mobile number")
            # if condition for number checking
            if len(TO) == 10:
                message1 = input("enter the message")
                messages = "{}".format(message1)
                message_send_call(TO, messages)
            else:
                print("enter the number 10 digit")


        elif 3 == wish:
            message1 = input("First enter the message here")
            multi_num = int(input("how many person do you like to send same message"))
            temp = multi_num
            count = 0

            while (multi_num <= temp) & (multi_num != 0):

                print("enter the {}".format((count) + 1) + "\tmobile number")

                TO = input()
                # if condition for number checking



                if len(TO) == 10:

                    count += 1
                    multi_num -= 1
                    messages = "{}".format(message1)
                    message_send_call(TO, str(messages))


                else:
                    print("enter the number 10 digit")

        elif 4 == wish:
            TO = input("enter the sender mobile number")
            if len(TO) == 10:
                message1 = input("first enter the message here")
                bomb = int(input("how many times to send a message"))
                for bombs in range(bomb):
                    print("{}".format(bombs))

                    messages = "{}".format(message1)
                    message_send_call(TO, messages)
            else:
                print("enter the number 10 digit")

        elif 5 == wish:
            break
        else:
            print("enter the number 1 to 5")


def message_send_call(TO, message):
    try:

        api = apikey

        headers = {"Accept-Language": "en-US,en;q=0.5",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                   "Referer": "http://thewebsite.com",
                   "Connection": "keep-alive"}

        values = {
            'Mobile': mobileno,
            'Password': password,
            'Message': message,
            'To': TO,
            'Key': api
        }
        datas = urlencode(values)
        data = datas.encode('ascii')
        urls = "https://smsapi.engineeringtgr.com/send/"
        url = urls + '?' + datas
        req = Request(url, data, headers)
        response = json.loads(urlopen(req).read())

        if response['msg'] != "SMS Send Successfully":

            print("check apikey")

        else:

            print("SMS Send Successfully")




    except Exception as e:
        print(e)


if __name__ == '__main__':

 while 1==1:
    help = (input("Type help(h) or press any key to continue(c)"))

    if ('help' == str(help.lower())) | ('h' == str(help.lower())):
        print("Step NO 1:signup way2sms'='http://site24.way2sms.com/jsp/UserRegistration.jsp'\n Step NO 2:https://smsapi.engineeringtgr.com/ login this website also to get an api key once done this process api comes in your mail\nStep NO 3:note that login mobile number ,login password & apikey in notepad\n#ONE IMPORTANT POINT IS ONLY 100 SMS FREE DAILY# \nIF any problem occurs Don't worry feel free to contact our mail #hackereye001@gmail.com\n")

    else:
        print("enter the way2sms valid login mobile number and login password")
        mobileno = input("enter the login mobile number")
        if len(mobileno) == 10:

            password = input("enter the login password")
            apikey = input("enter the valid apikey ")
            login_check(mobileno, password)
        else:
            print("enter the 10 digit mobile number")

        login_check(mobileno, password)


