import geocoder
import time


print("""
████████╗██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝""")
print("""                                𝙲𝚛𝚎𝚊𝚝𝚎𝚍 𝚋𝚢 - 𝚄𝚍𝚊𝚢𝚔𝚞𝚖𝚊𝚛""")

print("Make sure your device is connected with internet...!!")
ip = input('Enter the IP Address here: ')
g = geocoder.ip(ip)
address = g.latlng
print("_______________________PLEASE WAIT_________________________")
time.sleep(5)

print("The Location From Given IP Is: ")
print("Latitude: ",address[0])
print("Longitide: ",address[1])