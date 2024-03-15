import cloudscraper, threading, os

class data:
    count = 0

def view(url):
    try:
        scraper = cloudscraper.create_scraper()
        r = scraper.post(url)
        if r.status_code == 200:
            data.count += 1
            print(f"View Sended [{data.count}]") 
    except:
        pass

def main():
    os.system("cls||clear")
    url = input("Url: ")
    amount = input("Amount: ")
    for i in range(int(amount)):
        threading.Thread(target=view, args=(url, )).start()

main()