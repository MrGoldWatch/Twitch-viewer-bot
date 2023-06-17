import requests
import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from pystyle import Center, Colors, Colorate
import os
import random
import time
import platform

warnings.filterwarnings("ignore", category=DeprecationWarning)


def check_for_updates():
    try:
        r = requests.get("https://raw.githubusercontent.com/Kichi779/Twitch-Viewer-Bot/main/version.txt")
        remote_version = r.content.decode('utf-8').strip()
        local_version = open('version.txt', 'r').read().strip()
        if remote_version != local_version:
            print("A new version is available. Please download the latest version from GitHub.")
            time.sleep(3)
            return False
        return True
    except:
        return True

def print_announcement():
    try:
        r = requests.get("https://raw.githubusercontent.com/Kichi779/Twitch-Viewer-Bot/main/announcement.txt",
                         headers={"Cache-Control": "no-cache"})
        announcement = r.content.decode('utf-8').strip()
        return announcement
    except:
        print("Could not retrieve announcement from GitHub.\n")


def main():
    if not check_for_updates():
        return
    print_announcement()

    os.system(f"title Kichi779 - Twitch Viewer Bot @kichi#0779 ")

    print(Colorate.Vertical(Colors.green_to_cyan, Center.XCenter("""

                      ▄█     █▄        ▄█   ▄█▄  
                      ███    ███       ███ ▄███▀ 
                      ███    ███       ███▐██▀    
                     ▄███▄▄▄▄███▄▄    ▄█████▀     
                     ▀▀███▀▀▀▀███▀    ▀▀█████▄   
                       ███    ███       ███▐██▄   
                       ███    ███       ███ ▀███▄ 
                       ███    █▀        ███   ▀█▀ 

 Improvements can be made to the code. If you're getting an error, visit my discord.
                             Discord discord.gg/AFV9m8UXuT    
                             Github  github.com/kichi779    """)))
    announcement = print_announcement()
    print("")
    print(Colors.red, Center.XCenter("ANNOUNCEMENT"))
    print(Colors.yellow, Center.XCenter(f"{announcement}"))
    print("")
    print("")

    proxy_servers = {
        1: "https://www.blockaway.net",
        2: "https://www.croxyproxy.com",
        3: "https://www.croxyproxy.rocks",
        4: "https://www.croxy.network",
        5: "https://www.croxy.org",
        6: "https://www.youtubeunblocked.live",
        7: "https://www.croxyproxy.net",
    }

    # Selecting proxy server
    print(Colorate.Vertical(Colors.green_to_blue, "Please select a proxy server(1,2,3..). Proxy Server 1 Is Recommended:"))  # Selecting proxy server
    for i in range(1, 7):
        print(Colorate.Vertical(Colors.red_to_blue, f"Proxy Server {i} -> {proxy_servers.get(i)}"))
    proxy_choice = int(input("> "))  # User selects a proxy server by entering a number
    proxy_url = proxy_servers.get(proxy_choice)  # Retrieve the URL of the selected proxy server

    twitch_username = input(Colorate.Vertical(Colors.green_to_blue,
                                              "Enter your channel name (e.g XXX): "))  # User enters their Twitch channel name
    proxy_count = int(
        input(Colorate.Vertical(Colors.cyan_to_blue,
                                "How many proxy sites do you want to open? (Viewer to send)")))  # User specifies the number of proxy sites to open
    os.system("cls")  # Clear the console screen

    print('')
    print('')
    print(Colors.red, Center.XCenter(
        "Viewers Send. Please don't hurry. If the viewers does not arrive, turn it off and on and do the same operations"))


    # chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    driver_path = 'chromedriver.exe'
    if "macOS" in platform.platform():
        driver_path = 'chromedriver'

    chrome_options = webdriver.ChromeOptions()  # Set Chrome options for the webdriver
    chrome_options.add_experimental_option('excludeSwitches',
                                           ['enable-logging'])  # Exclude certain switches from Chrome
    chrome_options.add_argument('--disable-logging')  # Disable logging
    chrome_options.add_argument('--log-level=3')  # Set log level to 3 (only fatal errors)
    chrome_options.add_argument('--disable-extensions')  # Disable Chrome extensions
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode (without a graphical interface)
    chrome_options.add_argument("--mute-audio")  # Mute audio
    chrome_options.add_argument('--disable-dev-shm-usage')  # Disable shared memory usage
    if "macOS" not in platform.platform():
        chrome_options.binary_location = chrome_path  # Set the Chrome binary location
    driver = webdriver.Chrome(executable_path=driver_path,
                              chrome_options=chrome_options)  # Create a new Chrome webdriver

    driver.get(proxy_url)  # Open the selected proxy server in Chrome
    counter = 0  # Counter variable to keep track of the number of drivers created

    for i in range(proxy_count):
        try:
            driver.execute_script(
                "window.open('" + proxy_url + "')")  # Open a new tab in Chrome with the selected proxy server
            driver.switch_to.window(driver.window_handles[-1])  # Switch to the newly opened tab
            driver.get(proxy_url)  # Load the selected proxy server in the new tab

            text_box = driver.find_element(By.ID, 'url')  # Find the URL input box on the proxy server page
            text_box.send_keys(f'www.twitch.tv/{twitch_username}')  # Enter the Twitch channel URL in the input box
            text_box.send_keys(Keys.RETURN)  # Press Enter to submit the URL

            counter += 1  # Increment the counter for each driver created
            print(Colorate.Vertical(Colors.green_to_cyan,
                                    Center.XCenter(f"Viewer {counter}/{proxy_count} spawned for {twitch_username}.")))

            if i != proxy_count:
                rand_int = random.randint(0, 9)
                print(Colorate.Vertical(Colors.purple_to_blue,
                                        Center.XCenter(f"sleeping for {rand_int} seconds")))
                time.sleep(rand_int)  # Sleep for 3 seconds
        except WebDriverException as e:
            print("An error occurred while spawning a virtual viewer (Chrome driver):")
            print(e)
            break  # Exit the loop if an exception occurs

    input(Colorate.Vertical(Colors.red_to_blue,
                            "Viewers have all been sent. You can press enter to withdraw the views and the program will close."))
    driver.quit()  # Close the Chrome webdriver


if __name__ == '__main__':
    main()

# ==========================================
# Copyright 2023 Kichi779

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ==========================================