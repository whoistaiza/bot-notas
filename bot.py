import discord
from discord.ext import commands 

#main principal que rodará por toda a execução
def main() -> None:
    bot = commands.Bot("!")

    @bot.event
    async def on_ready():
        print("Estou pronto!")


    @bot.command(name="oi")
    async def send_hello(ctx):
        name = ctx.author.name
        resposta = "Olá " + name
        await ctx.send(resposta)

    @bot.command(name="notas")
    async def send_notas(ctx):
        name = ctx.author.name
        resposta = "de qual semestre você deseja saber suas notas?"
        await ctx.send(resposta)




    bot.run("OTU0OTAwOTAyOTI4NjA1MTg0.YjZ2xA.m4e03yubtZQ-0hbhDXglQPuJUtA")





#chama o main principal
if __name__ == '__main__':
    main()

#TESTE GITHUB
