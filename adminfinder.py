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
oturum = requests.Session()
oturum.headers.update(
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }
)

try:
    with open("wordlist.txt", "r") as dosya:
        for satir in dosya:
            yol = satir.strip()

            tam_adres = hedef + "/" + yol
            try:
                cevap = oturum.get(tam_adres, timeout=3)

                if cevap.status_code == 200:
                    print(f"[+] 200 OK: {tam_adres}")
            except requests.exceptions.RequestException:
                pass

except FileNotFoundError:
    print("❌ error: 'wordlist.txt' file not found!")
exit()
