## Port-Scan.
- Mensionei no exemplo a página http://businesscorp.com.br que usei no curso Pentest profissional da Desec Security.
- Esse programa tem a função de descobrir portas abertas em um host.
  
### Exemplo de uso:
- `python3 portscan.py businesscorp.com.br` (Este comando varre todas as 65535 portas)
- `python3 portscan.py businesscorp.com.br -t4` (Este comando varre todas as 65535 portas, com intervalo de 4 segundos entre as requisições)
- `python3 portscan.py businesscorp.com.br -t3 lista-portas.txt` (Este comando varre as portas passadas através de um arquivo .txt em um intervalo de 3 segundos entre as requisições)



### Imagem
![portscan](https://github.com/charlicastelli/port-scan/assets/80997263/7e454226-a936-42d5-ac59-35224378b4ea)
