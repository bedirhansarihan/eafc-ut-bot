import pprint
import time

from bs4 import BeautifulSoup
from selenium import webdriver
import undetected_chromedriver as uc

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def search_player(player_name):
    # Selenium WebDriver'ı başlat
    opts = uc.ChromeOptions()

    driver = uc.Chrome(options=opts)  # Initialize the driver instance
    # Futbin web sitesine git
    url = f"https://www.futbin.com/players?page=1&search={player_name}"
    driver.get(url)

    # Sayfa kaynağını BeautifulSoup ile analiz et
    soup = BeautifulSoup(driver.page_source, "html.parser")

    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')))
    login_button.click()

    tables = soup.find_all("table", id="repTb")
    player_info = None
    # Tüm bulunan tabloları döngüye al
    for table in tables:
        # Tüm tbody etiketlerini bul
        tbodies = table.find_all("tbody")

        for _ in tbodies:

            player_info = parse_player_info(soup)
    driver.quit()
    return player_info


def parse_player_info(soup):
    # BeautifulSoup kullanarak HTML içeriğini analiz et

    # 'tr' etiketlerini bul
    player_trs = soup.find_all("tr", class_=["player_tr_1", "player_tr_2"])

    # Oyuncu bilgilerini saklamak için bir liste oluştur
    player_info_list = []

    # Her 'tr' etiketi için işlem yap
    for tr in player_trs:
        # 'tr' etiketinin içindeki 'td' etiketlerini bul
        tds = tr.find_all("td")

        # Gerekli bilgileri çıkar ve bir sözlüğe ekle
        player_info = {
            "player_id": tr["data-url"].split("/")[-2],
            "name": tds[1].find("a").text.strip(),
            "rating": tds[2].text.strip(),
            "price": tds[5].text.strip().split("\n")[0],  # \n karakterinden önceki kısmı al
            "promo": tds[4].text.strip().split("\n")[0]  # \n karakterinden önceki kısmı al
        }

        # Oyuncu bilgileri listesine ekle
        player_info_list.append(player_info)

    # Oyuncu bilgilerini döndür
    return player_info_list


if __name__ == "__main__":
    player_name = input("Enter player name: ")
    player_info = get_player_info(player_name)
