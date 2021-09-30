try:
    from front_blocker import hI,mI,hF,mF,website_list 
except ImportError:
    pass
import time
from datetime import datetime as dt

#ao salvar como .pyw o arquivo rodará no background
#definir todos os caminhos pois não executará mais de dentro da pasta se vc mandar rodar pelo task manager
#não criei uma task para iniciar com o windows....mas pode ser feito, para isso ver o vídeo 125 do módulo 12;



#print(website_list)
hosts_temp="hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"

#website_list=["www.facebook.com","facebook.com","www.globoesporte.globo.com","globo.com","ge.globo","ge.globo.com","web.whatsapp.com","www.linkedin.com","www.cacador.net/","cacador.net","twitter.com","www.twitter.com",]

try:

    while True:
        if dt(dt.now().year,dt.now().month,dt.now().day,hI,mI)  < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,hF,mF):
            print("Working hours...")
            with open(hosts_path,'r+') as file:
                content=file.read()
                #print(content)
                for website in website_list:
                    if website in content:
                        pass
                    else:
                        file.write (redirect + " " + website +'\n')
        else:
            with open(hosts_path,'r+') as file:
                #content vira uma lista com readlines
                content=file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)
                file.truncate()
            print("Fun hours...")
        time.sleep(5)

except NameError: 
    pass
except ImportError:
    pass





