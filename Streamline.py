import requests
import pyperclip
from bs4 import BeautifulSoup
import webbrowser
import subprocess

title_art = r"""
 ________   _________   ________   _______    ________   _____ ______    ___        ___   ________    _______      
|\   ____\ |\___   ___\|\   __  \ |\  ___ \  |\   __  \ |\   _ \  _   \ |\  \      |\  \ |\   ___  \ |\  ___ \     
\ \  \___|_\|___ \  \_|\ \  \|\  \\ \   __/| \ \  \|\  \\ \  \\\__\ \  \\ \  \     \ \  \\ \  \\ \  \\ \   __/|    
 \ \_____  \    \ \  \  \ \   _  _\\ \  \_|/__\ \   __  \\ \  \\|__| \  \\ \  \     \ \  \\ \  \\ \  \\ \  \_|/__  
  \|____|\  \    \ \  \  \ \  \\  \|\ \  \_|\ \\ \  \ \  \\ \  \    \ \  \\ \  \____ \ \  \\ \  \\ \  \\ \  \_|\ \ 
    ____\_\  \    \ \__\  \ \__\\ _\ \ \_______\\ \__\ \__\\ \__\    \ \__\\ \_______\\ \__\\ \__\\ \__\\ \_______\
   |\_________\    \|__|   \|__|\|__| \|_______| \|__|\|__| \|__|     \|__| \|_______| \|__| \|__| \|__| \|_______|
   \|_________|                                                                                                    
                                                                                                                   
"""
print(title_art+'\n')

def download_and_stream(search_name, stream=False):
    # Construct the search URL
    search_url = f"https://thepiratebay10.org/search/{search_name}/1/99/0"

    # Send a GET request to the search URL
    response = requests.get(search_url)

    # Parse the HTML content of the search page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the search results
    search_results = soup.select('div#main-content')

    if search_results:
        for result in search_results:
            magnet_link = result.select_one('a[href^=magnet]')

            if magnet_link:
                magnet_link = magnet_link['href']
            if stream:
                cmd = ['peerflix', magnet_link, '--vlc', '--fullscreen']
                subprocess.call(cmd, shell=True)
                print("Torrent downloaded and streamed successfully.")
            else: 
                # Download the torrent
                webbrowser.open(magnet_link)
                print("Torrent software opened, Download finished.")
                break
        else:
            print("No magnet link found in the search results.")
    else:
        print("No search results found.")

# Ask the user to input a name
search_name = input("Enter a name to search for: ")

# Ask the user if they want to stream the torrent
stream = input("Do you want to stream the torrent? (yes/no): ")

# Download and stream the torrent
download_and_stream(search_name, stream.lower() == 'yes')