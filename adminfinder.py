import requests

banner = r"""
   _____       .___      .__       ___________.__            .___             ____   ________ 
  /  _  \    __| _/_____ |__| ____ \_   _____/|__| ____    __| _/___________  \   \ /   /_   |
 /  /_\  \  / __ |/     \|  |/    \ |    __)  |  |/    \  / __ |/ __ \_  __ \  \   Y   / |   |
/    |    \/ /_/ |  Y Y  \  |   |  \|     \   |  |   |  \/ /_/ \  ___/|  | \/   \     /  |   |
\____|__  /\____ |__|_|  /__|___|  /\___  /   |__|___|  /\____ |\___  >__|       \___/   |___|
        \/      \/     \/        \/     \/            \/      \/    \/                        
                                    !Coded by: 4B2A!
"""
print(banner)
hedef = input("Target: ")
print(f"target: {hedef}")

try:
    with open("wordlist.txt", "r") as dosya:
        for satir in dosya:
            yol = satir.strip()

            tam_adres = hedef + "/" + yol
            try:
                cevap = requests.get(tam_adres, timeout=3)

                if cevap.status_code == 200:
                    print(f"[+] 200 OK: {tam_adres}")
            except requests.exceptions.RequestException:
                pass

except FileNotFoundError:
    print("❌ error: 'wordlist.txt' file not found!")
exit()
