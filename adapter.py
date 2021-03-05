import argparse
import sys
import datetime
#from serial import Serial


def communicate(dane):
#    port = Serial(args.port, args.baud, timeout=10)
#    port.write(str.encode(dane + '\r\n'))

    encoded_data = str.encode(dane + '\r\n') 
    print("encoded data: ", encoded_data)

    print(">> tx: ", dane)
#    line = port.readline()
    print("<< rx: ", "line")
    #return line

parser = argparse.ArgumentParser()


parser.add_argument('-port', '--port', type=str, choices=['/dev/ttyUSB0', '/dev/ttyUSB1'], default='/dev/ttyUSB0', help='Select USB port')
parser.add_argument('-baud', '--baud', type=str, choices=['115200', '9600'], default='115200', help='Baudrate')

parser.add_argument('-money-get', '--money_get', type=str, choices=["amount"], required=False, help='Get inserted cash')
parser.add_argument('-money-return', '--money_return', type=int, default=-1, help='Return cash amount')
parser.add_argument('-device-rst', '--device_rst', type=str, required=False, choices=['all', 'coins', 'notes'], help='reset device')
parser.add_argument('-device-stat', '--device_stat', type=str, required=False, choices=['get'], help='return device state: ok, fault, off')
parser.add_argument('-device-on', '--device_on', type=str, required=False, choices=['all', 'coins', 'notes'], help='...')
parser.add_argument('-device-off', '--device_off', type=str, required=False, choices=['all', 'coins', 'notes'], help='...')
#parser.add_argument('-coin-enable', nargs = '*', dest = 'coin_enable', help = '...')
parser.add_argument('-coin-enable', '--coin_enable', type=int, default=-1, help='')
parser.add_argument('-coins-get', '--coin-get', type=str, required=False, choices=['tube-type', 'tube-status', 'tube-money'], help='...')
parser.add_argument('-adapter', '--adapter', type=str, required=False, choices=['reboot'], help='...')

parser.add_argument('-device-enable', '--device_enable', type=str, required=False, choices=['all', 'coins', 'notes'], help='...')
parser.add_argument('-device-disable', '--device_disable', type=str, required=False, choices=['all', 'coins', 'notes'], help='...')

# Notes:
parser.add_argument('-device-get', '--device_get', type=str, required=False, choices=['state'], help='...')
parser.add_argument('-notes-get', '--notes_get', type=str, required=False, choices=['map', 'enable', 'recycler-note', 'recycler-amount'], help='...')
#{"notes-set-enable":255}
parser.add_argument('-notes-set-enable', '--notes_set_enable', type=str, required=False, help='...')

#{"notes-set-recycler-note": 3}
parser.add_argument('-notes-set-recycler-note', '--notes_set_recycler_note', type=str, required=False, help='...')

# notes-recycler-to-cashbox
parser.add_argument('-notes-recycler-to-cashbox', '--notes_recycler_to_cashbox', type=str, required=False, choices=['all'], help='...')

# {"cashbox":"reset"}
parser.add_argument('-cashbox', '--cashbox', type=str, required=False, choices=['get', 'reset'], help='...')


args = parser.parse_args()



print ("args: ", args)

# print ("port: ", args.port)
# print ("baudrate: ", args.baud)

if (args.money_get == "amount"):
    communicate('{"money-get":"amount"}')
    exit

if (args.money_return >= 0):
    communicate('{"money-return":' + str(args.money_return) + '}')
    exit

if args.device_rst is not None:
    communicate('{"device-rst":"' + str(args.device_rst) + '"}')
    exit

if args.device_stat is not None:
    communicate('{"device-stat":"' + str(args.device_stat) + '"}')
    exit

if args.device_on is not None:
    communicate('{"device-on":"' + str(args.device_on) + '"}')
    exit

if args.device_off is not None:
    communicate('{"device-off":"' + str(args.device_off) + '"}')
    exit

if (args.coin_enable >= 0):
    communicate('{"coin_enable":' + str(args.coin_enable) + '}')
    exit

if args.coin_get is not None:
    communicate('{"coins-get":"' + str(args.coin_get) + '"}')
    exit

if args.adapter is not None:
    communicate('{"adapter":"' + str(args.adapter) + '"}')
    exit

if args.device_enable is not None:
    communicate('{"device-enable":"' + str(args.device_enable) + '"}')
    exit

if args.device_disable is not None:
    communicate('{"device-disable":"' + str(args.device_disable) + '"}')
    exit


# Notes: 

if args.device_get is not None:
    communicate('{"device-get":"' + str(args.device_get) + '"}')
    exit

if args.notes_get is not None:
    communicate('{"notes-get":"' + str(args.notes_get) + '"}')
    exit

if args.notes_set_enable is not None:
    communicate('{"notes-set-enable":' + args.notes_set_enable + '}')
    exit

if args.notes_set_recycler_note is not None:
    communicate('{"notes-set-recycler-note":' + args.notes_set_recycler_note + '}')
    exit


if args.notes_recycler_to_cashbox is not None:
    communicate('{"notes-recycler-to-cashbox":"' + args.notes_recycler_to_cashbox + '"}')
    exit

if args.cashbox is not None:
    communicate('{"cashbox":"' + args.cashbox + '"}')
    exit