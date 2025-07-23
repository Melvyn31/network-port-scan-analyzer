import sys
import xml.etree.ElementTree as ET

def parse_nmap(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for host in root.findall('host'):
        ip = host.find('address').attrib['addr']
        ports = host.find('ports')
        open_ports = []

        if ports:
            for port in ports.findall('port'):
                if port.find('state').attrib['state'] == 'open':
                    portid = port.attrib['portid']
                    service = port.find('service').attrib.get('name', 'unknown')
                    open_ports.append((portid, service))

        if open_ports:
            print(f"\n[+] Hôte : {ip}")
            for portid, service in open_ports:
                print(f"  - Port ouvert : {portid}/tcp ({service})")
                if service in ['ftp', 'telnet', 'ssh', 'smb']:
                    print("    ⚠️  Service sensible détecté")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Utilisation : python3 analyzer.py scan-result.xml")
        sys.exit(1)

    parse_nmap(sys.argv[1])
