import discord
import os
import colorama
from colorama import Fore, Style
import requests
import time
from colorama import Fore



def Cls():
  os.system('cls')
Cls()
b = Style.BRIGHT
message = input("PROVIDE A TEXT FOR YRUS MASS DM")
Cls()


token = input("PASTE TOKEN HERE: ")

Cls()

b = Style.BRIGHT 
print(f"""
{b+Fore.GREEN}


╦ ╦╦═╗╦ ╦╔═╗  ╔╦╗╔═╗╔═╗╔═╗  ╔╦╗╔╦╗
╚╦╝╠╦╝║ ║╚═╗  ║║║╠═╣╚═╗╚═╗   ║║║║║
 ╩ ╩╚═╚═╝╚═╝  ╩ ╩╩ ╩╚═╝╚═╝  ═╩╝╩ ╩
 

{b+Fore.BLUE} > {Fore.RESET}YRUS MASS DM
{b+Fore.BLUE} > {Fore.RESET}Creator: $yrusDaOnly
""")

Yrus = discord.Client()


@Yrus.event
async def on_connect():
  for user in Yrus.user.friends:
    try:
      Yrus = discord.Embed(color= discord.Color(0x9400D3))
      Yrus.set_author(name="https://discord.gg/TApSCZX7xv")
      Yrus.add_field(name=DISCORD.GG/YRUS",value=message)
      Yrus.set_image(url="https://cdn.discordapp.com/attachments/850710404752605204/856586976753090570/image0.gif")   
      time.sleep(.1)
      await user.send(embed=Yrus)
      time.sleep(.1)
      print(f"Successfully messaged: {user.name}")
     except:
        print(f"Revoked message from: {user.name}")
        print(f"Direct message sent to all users")
                     
                     
Yrus.run(token, bot=False)                     
