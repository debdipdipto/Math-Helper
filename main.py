import os
import discord
import math
import requests
from keep_alive import keep_alive
client = discord.Client()
@client.event
async def on_ready():
  print("I am activated!")
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$factorial'):
    msg = message.content
    num = ""
    for i in msg:
      if i >= '0' and i <= '9':
        num += i
    num = int(num)
    reply = "The factorial of " + str(num) + " is " + str(math.factorial(num)) 
    await message.channel.send(reply)
  if message.content.startswith('$solve'):
    exprsn = ""
    for i in range(7, len(message.content)):
      exprsn += message.content[i]
    reply = "|| The answer is" + str(eval(exprsn)) + " ||"
    await message.channel.send(reply)
  msg = message.content
  if msg.startswith('$multiplication table'):
    x = ""
    y = ""
    f = 1
    for i in msg:
      if i == ',':
        f = 0
      if f == 1:
        if i >= '0' and i <= '9' and i != ' ':
          x += i
      else :
        if i <= '9' and i >= '0' and i != ' ':
          y += i
    print(x, y)
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    for i in x:
      if i not in num or len(x) == 0:
        f = 1
    for i in y:
      if i not in num or len(y) == 0:
        f = 1
    print(f)
    if f == 1:
      await message.channel.send("Invalid command.")
      return
    if f == 0:
      x = int(x)
      y = int(y)
      reply = ""
      for i in range(1, y + 1):
        reply += str(x) + ' * ' + str(i) + ' = ' + str(x * i) + '\n'
      await message.channel.send(reply)
  if msg.startswith('$weather'):
    api_key = "d6008c2030c3e1f59a62ac43711d1729"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = ""
    for i in range(9, len(msg)):
      city_name += msg[i]
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    ctx = message.channel
    x = response.json()
    print(x)
    if x['cod'] != '404':
      async with ctx.typing():
        y = x["main"]
        current_temperature = y["temp"]
        current_temperature_celsiuis = str(round(current_temperature - 273.15))
        feels_like_celcius = str(round(y["feels_like"] - 273.15))
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        embed = discord.Embed(title=f"Weather in {city_name}",
                              color=ctx.guild.me.top_role.color,
                              )
        embed.add_field(name="Description", value=f"**{weather_description}**", inline=False)
        embed.add_field(name="Temperature(C)", value=f"**{current_temperature_celsiuis}°C**", inline=True)
        embed.add_field(name="Feels like(C)", value=f"**{feels_like_celcius}°C**", inline=False)
        embed.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
        embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
        embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
        await ctx.send(embed=embed)
    else:
      await ctx.send("City not found.")

my_secret = os.environ['TOKEN']
keep_alive()
client.run(my_secret)


