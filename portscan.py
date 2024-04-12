#!/usr/bin/python3
import socket,sys,time,os

################################################################################
# Titulo    : Port scanner                                                     #
# Versão    : 1.2                                                              #
# Data      : 12/04/2024                                                       #
# Tested on : Linux/Windows10                                                  #
# created by: Charli Castelli.                                                 #
# -----------------------------------------------------------------------------#
# Descrição:                                                                   #
#   Esse programa tem a função de descobrir portas abertas em um host.         #
# -----------------------------------------------------------------------------#
# Nota da Versão:                                                              #
# Adicionado opção de tempo entre as requisições.                              #
# Adicionado opção de ler uma wordlist.                                        #
# Exemplo de uso com tempo: python3 portscan businesscorp.com.br -t5           #
# Exemplo de uso com tempo: python3 portscan businesscorp.com.br -t5 list.txt  #
################################################################################

#Constantes cores
RED    = "\033[1;31m"  
RESET  = "\033[0;0m"
BOLD   = "\033[;1m"
BLUE   = "\033[34m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"

#Icones
iconSuccessBlue = BOLD + BLUE + "[+]" + RESET
iconSuccessGreen = GREEN + "[+]" + RESET
iconHelp = BLUE + "[?]" + RESET
iconError = BOLD + RED + "[-]" + RESET
status = BOLD + GREEN + "[ABERTA]" + RESET

#Menssagens
example = f"{iconError} Exemplo de uso da ferramenta --> " + GREEN + f"python3 {sys.argv[0]} businesscorp.com.br\n\n" + RESET
example2 = f"""{iconError} Exemplo de uso da ferramenta: """ + GREEN + f"""
python3 {sys.argv[0]} businesscorp.com.br -t2 
python3 {sys.argv[0]} businesscorp.com.br -t0 wordlist.txt\n\n""" + RESET
close = "\n\n🛑 Execução interrompida pelo usuário!"
stop = f"{iconHelp} Para interromper a execução, pressione Ctrl + C"

#Banner
banner = YELLOW + """
 ____            _   ____                  
|  _ \ ___  _ __| |_/ ___|  ___ __ _ _ __  
| |_) / _ \| '__| __\___ \ / __/ _` | '_ \ 
|  __/ (_) | |  | |_ ___) | (_| (_| | | | |
|_|   \___/|_|   \__|____/ \___\__,_|_| |_|                                                                                       
                                                                                            
""" + RESET

print(banner)


#Verificações
if len(sys.argv) < 2:
     print(f"{example}")
     sys.exit()
elif len(sys.argv) > 4:
     print(f"{example}")
     sys.exit()
#Esta verificação é caso não informe um tempo, o programa seta o tempo como zero.
elif len(sys.argv) > 2 and len(sys.argv) < 5 and sys.argv[2].lower().startswith('-t'): #startswith('-t') Verifica se o 2° argumento começa com -t
     tempo = int(sys.argv[2][2:]) #Pega o número após o '-t'
elif len(sys.argv) > 2 and len(sys.argv) < 4 and not sys.argv[2].lower().startswith('-t'):
     print(f"{example2}")
     sys.exit()
else:
    tempo = 0

try:
    #Se não passar um arquivo.txt com as portas que quer varrer o programa vai varrer todas as 65535
    if len(sys.argv) < 4:
        infoHost = sys.argv[1]
        text = f"{iconSuccessGreen} Iniciando varredura no Host: {infoHost}"
        print(f"{stop}")
        time.sleep(2)
        print(f"{text}\n\n")

        for port in range(1,65535):
            meusocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            meusocket.settimeout(0.5)
            result = meusocket.connect_ex((infoHost,port))
            if (result == 0):
                print(f"{iconSuccessBlue} Porta {port:.<15}{status}")
                socket.close
            else:
                socket.close
            time.sleep(int(tempo))
    
    portsFile = sys.argv[3]
    # Verifique se o arquivo existe e é um arquivo .txt, se for verdadeiro vai varrer as portas que estão no arquivo.txt
    if not os.path.isfile(portsFile) or not portsFile.endswith('.txt'):
        print(f"{iconError} \"{portsFile}\" não é um arquivo válido. Formato aceito é .txt\n\n")
        sys.exit()
    elif not sys.argv[2].lower().startswith('-t'):
        print(f"{iconError} Informe o tempo entre as requisições. Exemplo: -t4\n\n")
        sys.exit()
    else:
        infoHost = sys.argv[1]
        text = f"{iconSuccessGreen} Iniciando varredura no Host: {infoHost}"
        print(f"{stop}")
        time.sleep(2)
        print(f"{text}\n\n")
        with open(portsFile, "r") as arquivo:
            for linha in arquivo:
                port = int(linha.strip())
                meusocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                meusocket.settimeout(0.5)
                result = meusocket.connect_ex((infoHost,port))
                if (result == 0):
                    print(f"{iconSuccessBlue} Porta {port:.<15}{status}")
                    socket.close
                else:
                    socket.close
                time.sleep(int(tempo))

except KeyboardInterrupt:
    print(close) # Se o usuário precionar Ctrl + c vai interromper a execução do script.

print()
print()