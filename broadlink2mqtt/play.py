import os
import time
import ConfigParser
from broadlink2mqtt.record import get_broadlink_rm
from broadlink2mqtt.record import execute_command

here = os.path.abspath(os.path.dirname(__file__))

def put_on_humificator(device, config):
    # precondition: humificador esta apagado
    execute_command(device, config, 'humificador', 'on', 1)
    execute_command(device, config, 'humificador', 'timing', 0.120)
    for _ in range(16):
        execute_command(device, config, 'humificador', 'light', 0.120)
    # postcondicion: humificador queda encendido por 2 horas

def put_off_humificator(device, config):
    # precondition: humificador esta encendido
    execute_command(device, config, 'humificador', 'on', 1)
    # postcondicion: humificador queda encendido

if __name__ == '__main__':
    device = get_broadlink_rm()
    config = ConfigParser.ConfigParser()
    config.read(['buttons.txt', here])
    put_on_humificator(device, config)
    time.sleep(10)
    put_off_humificator(device, config)
    for _ in range(16):
        execute_command(device, config, 'enchufe', '3on', 1)
        execute_command(device, config, 'enchufe', '3off', 1)
    # execute_command(device, config, 'movistar', 'guia', 0.5)

    # execute_command(device, config, 'movistar', 'b0', 2)
    # execute_command(device, config, 'movistar', 'b1', 2)
    # execute_command(device, config, 'movistar', 'b2', 2)
    # execute_command(device, config, 'movistar', 'b3', 2)
    # execute_command(device, config, 'movistar', 'b4', 2)
    # execute_command(device, config, 'movistar', 'b5', 2)
    # execute_command(device, config, 'movistar', 'b6', 2)
    # execute_command(device, config, 'movistar', 'b7', 2)
    # execute_command(device, config, 'movistar', 'b8', 2)
    # execute_command(device, config, 'movistar', 'b9', 2)
    # time.sleep(3)

    # execute_command(device, config, 'movistar', 'b3', 0.7)
    # execute_command(device, config, 'movistar', 'b0', 0.7)
    # # execute_command(device, config, 'movistar', 'back', 0.5)
    #
    # time.sleep(3)

    # execute_command(device, config, 'movistar', 'guia', 0.5)
    # execute_command(device, config, 'movistar', 'b6', 0.7)
    # execute_command(device, config, 'movistar', 'b0', 0.7)
    # execute_command(device, config, 'movistar', 'back', 0.5)

