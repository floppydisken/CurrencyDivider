#!/usr/bin/env python3.6
import requests
import os

account_name = "sporring"
# url = "https://pathofexile.com/character-window/get-stash-items?accountName="
url = "https://www.pathofexile.com/character-window/get-stash-items?" 

# example
#accountName=sporring2&league=Delve&tabIndex=1&tabs=1

def create_or_open_with_sessid(force=False):
    sessid_filename = ".sessid"
    sessid_path = os.path.abspath(sessid_filename)
    sessid = "EMPTY"

    exists = os.path.exists(sessid_path)
    
    if exists and not force:
        print(f"Found {sessid_path}")
        with open(".sessid", "r") as file_sessid:
            sessid = file_sessid.readline()
    else:
        print(f"I have to create {sessid_path}")
        with open(".sessid", "w") as file_sessid:
            sessid = input("Can I get the POESESSID? ")
            file_sessid.write(sessid)

    return sessid



def build_stash_url(account, tab_no, league):
    out_url = f"{url}{account}&league={league}&tabIndex={tab_no}&tabs=1"
    return out_url

def get_player_stash(account, tab_no, league, debug=False):
    url = build_stash_url(account_name, stash_tab, league)
    payload = {
            "accountName": account,
            "league": league,
            "tabIndex": tab_no,
            }

    response = requests.get(url, params=payload, cookies={"POESESSID": create_or_open_with_sessid()})
    if (debug):
        print(f"Url: {url}")
        print(f"Response status: {response.status_code}")
        print(f"Reponse as text: {response.text}")
    return response.json()


if "__main__" == __name__:
    account_name = input("Account name? ")
    stash_tab = input("Which stash tab do you want divided? ")
    league = "Delve"

    print(get_player_stash(account_name, stash_tab, league, debug=True))
    
