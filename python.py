import requests
import time
import sys
import os
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# Clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

# API Configuration
# Free Api
API_TOKEN = "6817014467:igS6FmL0"
API_URL = "https://leakosintapi.com/"

# KAALVEER Banner
print(Fore.MAGENTA + Style.BRIGHT + """
╔════════════════════════════════════════════════════════╗
║   🔍 LEAKEDD DATA SEARCH TOOL - BY ROLEX OFFICIAL ☠️         ║
╠════════════════════════════════════════════════════════╣
║   📩 Search Leaked Data by:                            ║
║      📱 Phone Number                                   ║
║      📧 Email Address                                  ║
║      🧑 Name                                            ║
║                                                       ║
║   🛡️  Stay Secure | Stay Anonymous | Stay Alert        ║
╚════════════════════════════════════════════════════════╝
""" + Style.RESET_ALL)

# User Input
query = input(Fore.YELLOW + Style.BRIGHT + "📲 Enter number, email or name to search: ")

# Loading Animation
print(Fore.CYAN + Style.BRIGHT + f"\n[⏳] Searching Leak Data for: {query}\n")
animation = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
for i in range(20):
    time.sleep(0.07)
    sys.stdout.write("\r" + Fore.LIGHTGREEN_EX + "🔍 Processing " + animation[i % len(animation)] + " ")
    sys.stdout.flush()
print("\n")

# Request Payload
payload = {
    "token": API_TOKEN,
    "request": query,
    "limit": 100,
    "lang": "en",
    "type": "json"
}

try:
    response = requests.post(API_URL, json=payload)
    response.raise_for_status()
    data = response.json()

    if "Error code" in data:
        print(Fore.RED + f"\n❌ API Error: {data['Error code']}")
    elif "List" in data:
        print(Fore.GREEN + Style.BRIGHT + "\n✅ Data Found! Showing results below:\n")

        for db_name, db_data in data["List"].items():
            print(Fore.CYAN + Style.BRIGHT + f"\n📁 DATABASE: {db_name.upper()}")
            print(Fore.BLUE + f"ℹ️ {db_data.get('InfoLeak', '')}")

            for record in db_data.get("Data", []):
                print(Fore.YELLOW + "\n" + "=" * 50)
                for key, value in record.items():
                    print(Fore.LIGHTGREEN_EX + f"{key:<18}: " + Fore.WHITE + f"{value}")
                print(Fore.YELLOW + "=" * 50)

            # Footer Signature
            print(Fore.MAGENTA + Style.BRIGHT + "\n💀 --- Tool Crafted with 💙 by ROLEX OFFICIAL ---\n")

    else:
        print(Fore.RED + "⚠️ No data found or unknown response format.")

except Exception as e:
    print(Fore.RED + f"\n❗ Error: {e}")
