import subprocess
import re
import requests
import os

clienticon_regex = re.compile(r'^\s*"clienticon"\s+"([^"]+)"\s*$', re.MULTILINE)

def get_clienticon(app_id: str) -> str:
    """
    Calls steamcmd to fetch app_info for the given app_id, then
    extracts the 'clienticon' hash from the output. Returns an empty
    string if not found.
    """
    cmd = [
        'steamcmd',
        '+login', 'anonymous',
        '+app_info_print', app_id,
        '+quit'
    ]
    
    # Capture stdout/stderr as bytes, then decode with fallback
    process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = process.stdout.decode('utf-8', errors='replace')

    match = clienticon_regex.search(output)
    return match.group(1) if match else ""

def download_icon(app_id: str, icon_hash: str, out_dir='icons'):
    """
    Download the .ico file from Steam’s CDN and save it using the
    hash as the filename: <icon_hash>.ico
    """
    if not icon_hash:
        return
    url = f"https://cdn.cloudflare.steamstatic.com/steamcommunity/public/images/apps/{app_id}/{icon_hash}.ico"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{icon_hash}.ico")

    try:
        r = requests.get(url, timeout=30)
        if r.status_code == 200:
            with open(out_path, 'wb') as f:
                f.write(r.content)
            print(f"{app_id} -> {out_path}")
        else:
            print(f"Download failed for {app_id} (HTTP {r.status_code})")
    except Exception as e:
        print(f"Error downloading {app_id}: {e}")

def main():
    # Read AppIDs from a text file; one per line. Change to a different file name if using a different list.
    # e.g. app_ids.txt:
    #   4000
    #   2200
    #   292030
    #   etc.
    txt_file = 'app_ids.txt' 
    with open(txt_file, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.read().splitlines()

    # Keep only numeric lines (ignore blanks or invalid lines)
    app_ids = [line for line in lines if line.isdigit()]

    # Fetch & save icons for each AppID
    for app_id in app_ids:
        icon_hash = get_clienticon(app_id)
        if icon_hash:
            download_icon(app_id, icon_hash)
        else:
            print(f"No clienticon found for {app_id}")

if __name__ == "__main__":
    main()