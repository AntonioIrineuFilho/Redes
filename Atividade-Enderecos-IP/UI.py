from SameNetwork import SameNetwork

class UI:
    def main():
        ip1 = input("Digite o IP 1(xxx.xxx.xxx.xxx): ").split(".")
        ip2 = input("Digite o IP 2(xxx.xxx.xxx.xxx): ").split(".")
        numMask = int(input("Digite a máscara da rede(número 1-32): "))

        print(SameNetwork(ip1, ip2, numMask))

UI.main()
