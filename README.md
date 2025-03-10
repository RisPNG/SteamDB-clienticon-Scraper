# SteamCDN "clienticon" Tool

A Python-based tool that fetches client icons for all games and applications in your Steam library directly from Steam. Useful for restoring original Steam shortcut icons on your desktop.

My tool DO NOT SCRAPE from SteamDB as that is against SteamDB rules stated [here](https://steamdb.info/faq/#can-i-use-auto-refreshing-plugins-or-automatically-scrape-crawl-steamdb). Instead it fetches the icon directly from Steam's CDN URL, the only contribution that SteamDB had to do with this project is for me to understand the structure of how Steam store their clienticon in their url.

---

## 📌 Requirements

- [SteamCMD](https://developer.valvesoftware.com/wiki/SteamCMD#Downloading_SteamCMD) (must be added to your PATH)
- [Python](https://www.python.org/downloads/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- Python dependencies listed in `requirements.txt`

---

## ⚙️ Installation & Setup

### 1. SteamCMD

- [Download SteamCMD](https://developer.valvesoftware.com/wiki/SteamCMD#Downloading_SteamCMD).
- Add the `SteamCMD` folder path to your system's environment variable (`PATH`).

### 2. Python Dependencies

Install dependencies using `pip`:

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration

### Step 1: Steam Web API Key & Steam64 ID

- Register your Steam Web API Key from:
  [https://steamcommunity.com/dev/apikey](https://steamcommunity.com/dev/apikey)  
  *(Any domain name is acceptable.)*

- Obtain your Steam64 ID from:
  [https://steamid.xyz](https://steamid.xyz)

### Step 2: Populate Owned Games List

- Modify `get_owned_app_ids.py` to include your **Steam Web API Key** and **Steam64 ID**.
- Generate your owned app IDs by running:

```bash
python get_owned_app_ids.py
```

- This will create or overwrite `owned_app_ids.txt`.

---

## 🚀 Fetching Icons from SteamDB

- Copy contents from `owned_app_ids.txt` into `app_ids.txt`.
- Run the main scraper script:

```bash
python main.py
```

*(The download process may take several minutes depending on your library size.)*

---

## 🖼️ Applying the Icons

After downloading is complete:

- Copy all downloaded icons from the scraper's output folder into your Steam icons folder. Default Steam directory:

```
C:\Program Files (x86)\Steam\steam\games
```

- Your desktop shortcuts should now correctly display their original icons.

---

## 🛠️ Troubleshooting

If shortcuts are still missing icons:

- Run the provided registry script `url.reg`.  
  *(May resolve common registry-related icon issues.)*

- Delete your icon cache and restart Explorer:
  1. Press `Win + R` to open the Run dialog.
  2. Paste the following path and press Enter:
     ```
     %localappdata%
     ```
  3. Locate and delete the file `IconCache.db`.
  4. Open Task Manager (`Ctrl + Shift + Esc`), find `explorer.exe` under the Processes tab, select it, and click **Restart**.
