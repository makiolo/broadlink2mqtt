# -*- coding: utf-8 -*-
import os
import time
import base64
import broadlink
import ConfigParser

def get_broadlink_rm(timeout=3):
    devices = broadlink.discover(timeout=timeout)
    for device in devices:
        if isinstance(device, broadlink.rm):
            break
    else:
        raise Exception("Not broadlink rm Pro device found !!")
    device.auth()
    return device

def execute_command(device, config, machine, command, postsleep=0):
    ir_packet_encoded = config.get(machine, command)
    device.send_data( base64.b64decode(ir_packet_encoded) )
    if postsleep > 0:
        time.sleep(postsleep)

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
    print "-- grabando secuencia"
    sequence = []
    while len(sequence) < 1:
        print "/",
        device.enter_learning()
        time.sleep(5)
        print "\\",
        ir_packet = device.check_data()
        if ir_packet is not None:
            sequence.append( base64.b64encode(ir_packet) )
            print "ok"

    try:
        while True:
            print "-- enviando secuencia"
            for ir_packet_encoded in sequence:
                print "- send {}".format(ir_packet_encoded)
                device.send_data( base64.b64decode(ir_packet_encoded) )
            time.sleep(3)
    except KeyboardInterrupt:
        pass

