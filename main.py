puissance = 75
crickit.motor2.run(puissance)
pause(2000)
puissance = -75
crickit.motor2.run(puissance)
pause(2000)
puissance = 0
crickit.motor2.run(puissance)

def on_forever():
    pass
forever(on_forever)
