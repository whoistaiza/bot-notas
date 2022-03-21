from msilib.schema import tables
import discord
from discord.ext import commands 
import requests
import pandas 
from bs4 import BeautifulSoup

#main principal que rodará por toda a execução
def main() -> None:
    # bot = commands.Bot("!")

    # @bot.event
    # async def on_ready():
    #     print("Estou pronto!")


    # @bot.command(name="oi")
    # async def send_hello(ctx):
    #     name = ctx.author.name
    #     resposta = "Olá " + name
    #     await ctx.send(resposta)

    # @bot.command(name="notas")
    # async def send_notas(ctx):
    #     name = ctx.author.name
    #     resposta = "de qual semestre você deseja saber suas notas?"
    #     await ctx.send(resposta)

    requisicao = requests.get("https://portal.santoangelo.uri.br/portal_aluno/(S(zpqe1oibcx3m3155cnocjabe))/login.aspx")
    # print(requisicao.text)
    payload = {'TextBox1': '37632', 'TextBox2': 'hpvida123'}
    login = requests.post("https://portal.santoangelo.uri.br/portal_aluno/(S(33eej345xmdfbw55jj0m4u55))/login.aspx",data=payload)
    if(login.status_code==200):
        print("post deu certo")
        cookie={
            'Cookie':'_ga=GA1.2.1043088173.1634660925; __zlcmid=16dkPuYaneIuoBY; hubspotutk=41c780f80a7d26c44b0456159a7baec0; rdtrk={"id":"42e8377c-6c33-4a11-bf3c-4c9ab9ea2ebb"}; __hstc=10335978.41c780f80a7d26c44b0456159a7baec0.1634660928719.1634660928719.1638140683135.2; _rd_wa_id.4fe9=7b4013a8-e2ab-5053-a95f-7858e00865e0.1634660925.5.1640585217.1639361412.63043a73-5b91-5bb1-9f70-8eca222bc1b1; __trf.src=encoded_eyJmaXJzdF9zZXNzaW9uIjp7InZhbHVlIjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJleHRyYV9wYXJhbXMiOnt9fSwiY3VycmVudF9zZXNzaW9uIjp7InZhbHVlIjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJleHRyYV9wYXJhbXMiOnt9fSwiY3JlYXRlZF9hdCI6MTY0MDU4NTIxNzQ3MH0=; myURISAN.PORTAL_ALUNO=CD_GPES=34099&GUID=9593802F-AA05-459D-AB20-12696C6C7504; cookiesDirective=1; RESTRITO_PA=4AE28CB43FC2A9FE0C61CACD6C2ED9096AF87BD078207785457F3BDD9033C18D664A6BD9334446DD5F91D9745B0273CA009FEE73C4603B7A0A1811EB110F2A93EAE204AFBF9551D61CFA8199D9D55F746364A51D9702F4AF6E715D1AD6BF3C10CB6BE9974C58CB05D50FB44DA80C41A6AFD8EE04'
        }
        menu=requests.get("https://portal.santoangelo.uri.br/portal_aluno/(S(zpqe1oibcx3m3155cnocjabe))/menu.aspx",cookies=cookie)
        if(menu.status_code==200):
            print("get menu deu certo")
            print(menu.text)
            cookie2={
                'Cookie':'_ga=GA1.2.1043088173.1634660925; __zlcmid=16dkPuYaneIuoBY; hubspotutk=41c780f80a7d26c44b0456159a7baec0; rdtrk={"id":"42e8377c-6c33-4a11-bf3c-4c9ab9ea2ebb"}; __hstc=10335978.41c780f80a7d26c44b0456159a7baec0.1634660928719.1634660928719.1638140683135.2; _rd_wa_id.4fe9=7b4013a8-e2ab-5053-a95f-7858e00865e0.1634660925.5.1640585217.1639361412.63043a73-5b91-5bb1-9f70-8eca222bc1b1; __trf.src=encoded_eyJmaXJzdF9zZXNzaW9uIjp7InZhbHVlIjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJleHRyYV9wYXJhbXMiOnt9fSwiY3VycmVudF9zZXNzaW9uIjp7InZhbHVlIjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJleHRyYV9wYXJhbXMiOnt9fSwiY3JlYXRlZF9hdCI6MTY0MDU4NTIxNzQ3MH0=; myURISAN.PORTAL_ALUNO=CD_GPES=34099&GUID=9593802F-AA05-459D-AB20-12696C6C7504; cookiesDirective=1; RESTRITO_PA=4AE28CB43FC2A9FE0C61CACD6C2ED9096AF87BD078207785457F3BDD9033C18D664A6BD9334446DD5F91D9745B0273CA009FEE73C4603B7A0A1811EB110F2A93EAE204AFBF9551D61CFA8199D9D55F746364A51D9702F4AF6E715D1AD6BF3C10CB6BE9974C58CB05D50FB44DA80C41A6AFD8EE04'
            }
            notas = requests.get("https://portal.santoangelo.uri.br/portal_aluno/(S(zpqe1oibcx3m3155cnocjabe))/ensino/shw_discs.aspx?curr=219&ansm=TODOS",cookies=cookie2)
            if(notas.status_code==200):
                print("get notas deu certo")
                print(notas.text)
                soup=BeautifulSoup(notas.text,'html.parser')
                

    # bot.run("OTU0OTAwOTAyOTI4NjA1MTg0.YjZ2xA.m4e03yubtZQ-0hbhDXglQPuJUtA")
#chama o main principal
if __name__ == '__main__':
    main()

#TESTE GITHUB
