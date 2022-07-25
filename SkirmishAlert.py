import argparse
import ctypes
import socket
import winsound
import scapy
import scapy.layers.inet
import scapy.packet
import scapy.sendrecv

parser = argparse.ArgumentParser()
parser.add_argument("-b", "--beep", action="store_true",
                    help="audio beep when triggered")
parser.add_argument("-mb", "--messagebox", action="store_true",
                    help="messagebox when triggered")
parser.add_argument("-e", "--exit", action="store_true",
                    help="exit when triggered")
args = parser.parse_args()


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def process_packet(packet):
    ip_layer = None
    raw_layer = None

    # check if packet is valid and has data
    if packet.haslayer(scapy.layers.inet.IP):
        ip_layer = packet.getlayer(scapy.layers.inet.IP)
    if packet.haslayer(scapy.packet.Raw):
        raw_layer = packet.getlayer(scapy.packet.Raw)
    if ip_layer is None or raw_layer is None:
        return

    raw_layer = bytes(raw_layer)
    data = raw_layer.hex().upper()

    # check if 'Skirmish' string is in the data
    if "Skirmish".encode('ascii').hex().upper() in data:
        print('Skirmish')
        if args.beep:
            winsound.Beep(440, 250)
            winsound.Beep(880, 250)
            winsound.Beep(440, 250)
            winsound.Beep(880, 250)
        if args.messagebox:
            ctypes.windll.user32.MessageBoxW(None, 'Skirmish', 'Skirmish', 0x00000030)
        if args.exit:
            exit(0)
    return


if __name__ == '__main__':
    sniff = scapy.sendrecv.sniff(filter=f'udp and (len > 100) and (len < 1000) and (dst host {get_ip_address()})',
                                 prn=process_packet,
                                 store=False)
