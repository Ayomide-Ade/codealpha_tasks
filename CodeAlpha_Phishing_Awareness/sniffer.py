import socket
import struct
import os


def receiveData(s):
    try:
        data = s.recvfrom(65565)
        return data[0]
    except socket.timeout:
        return b''
    except Exception as e:
        print(f"An error happened: {e}")
        return b''


def getTOS(data):
    precedence = {0: "Routine", 1: "Priority", 2: "Immediate", 3: "Flash", 4: "Flash override", 5: "CRITIC/ECP",
                  6: "Internetwork control", 7: "Network control"}
    delay = {0: "Normal delay", 1: "Low delay"}
    throughput = {0: "Normal throughput", 1: "High throughput"}
    reliability = {0: "Normal reliability", 1: "High reliability"}
    cost = {0: "Normal monetary cost", 1: "Minimize monetary cost"}

    D = (data & 0x10) >> 4
    T = (data & 0x08) >> 3
    R = (data & 0x04) >> 2
    M = (data & 0x02) >> 1
    prec = data >> 5

    tabs = '\n\t\t\t'
    TOS = (precedence.get(prec, "Unknown") + tabs +
           delay.get(D, "Unknown") + tabs +
           throughput.get(T, "Unknown") + tabs +
           reliability.get(R, "Unknown") + tabs +
           cost.get(M, "Unknown"))
    return TOS


def getFlags(data):
    flagR = {0: "0 - Reserved bit", 1: "1 - Reserved bit"}
    flagDF = {0: "0 - Fragment if necessary", 1: "1 - Do not fragment"}
    flagMF = {0: "0 - Last fragment", 1: "1 - More fragments"}

    R = (data & 0x8000) >> 15
    DF = (data & 0x4000) >> 14
    MF = (data & 0x2000) >> 13

    tabs = '\n\t\t\t'
    return flagR.get(R, "Unknown") + tabs + flagDF.get(DF, "Unknown") + tabs + flagMF.get(MF, "Unknown")


def getProtocol(protocolNr):
    protocols = {
        1: "ICMP", 2: "IGMP", 6: "TCP", 17: "UDP", 27: "RDP",
        41: "IPv6", 50: "ESP", 51: "AH", 89: "OSPF"
    }
    return protocols.get(protocolNr, f"Unknown Protocol ({protocolNr})")


def main():
    HOST = socket.gethostbyname(socket.gethostname())

    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    s.bind((HOST, 0))
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    if os.name == 'nt':
        s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    print("Listening for a network packet...")

    try:
        data = receiveData(s)

        if not data or len(data) < 20:
            print("No valid packet captured.")
            return

        unpackedData = struct.unpack('!BBHHHBBH4s4s', data[:20])

        version_IHL = unpackedData[0]
        version = version_IHL >> 4
        IHL = version_IHL & 0xF
        TOS = unpackedData[1]
        totalLength = unpackedData[2]
        ID = unpackedData[3]
        flags_and_offset = unpackedData[4]
        fragmentOffset = flags_and_offset & 0x1FFF
        TTL = unpackedData[5]
        protocolNr = unpackedData[6]
        checksum = unpackedData[7]
        sourceAddress = socket.inet_ntoa(unpackedData[8])
        destinationAddress = socket.inet_ntoa(unpackedData[9])

        print(f"\nAn IP packet with the size {totalLength} bytes was captured.")
        print("\n--- Parsed IP Header Data ---")
        print(f"Version:\t\tIPv{version}")
        print(f"Header Length:\t\t{IHL * 4} bytes")
        print(f"Type of Service:\t{getTOS(TOS)}")
        print(f"Total Length:\t\t{totalLength} bytes")
        print(f"ID:\t\t\t{hex(ID)} ({ID})")
        print(f"Flags:\t\t\t{getFlags(flags_and_offset)}")
        print(f"Fragment offset:\t{fragmentOffset}")
        print(f"TTL:\t\t\t{TTL} hops")
        print(f"Protocol:\t\t{getProtocol(protocolNr)}")
        print(f"Checksum:\t\t{checksum}")
        print(f"Source IP:\t\t{sourceAddress}")
        print(f"Destination IP:\t\t{destinationAddress}")

        payload = data[IHL * 4:]
        print(f"\nPayload Data ({len(payload)} bytes):")
        print(payload[:50])

    except KeyboardInterrupt:
        print("\nCapture manually stopped.")
    finally:
        if os.name == 'nt':
            s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
            print("\nPromiscuous mode disabled. Exiting securely.")


if __name__ == "__main__":
    main()