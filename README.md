<a href="https://www.youtube.com"><img align="right" src="youtube-icon.png" width="48px" height="48px"></a>

<a href="https://github.com/ZazerConer/YouTube-to-M3U8/actions/workflows/beinsports-haber.yml">
<img src="https://badgen.net/badge/beIN SPORTS HABER/Status/green?icon=github">
</a>

<br>
<hr>

<h1 align="center">YouTube to M3U8</h1>

<h3 align="center"><i>M3U8 Generator For YouTube</i></h3>

- Updated m3u8 links of YouTube live channel, auto-updated every 3 hours.

<br>

## How to get started?

<br>

**1. Create a file.**

**`channel-name.txt`**

```
~~ DO NOT EDIT THE FIRST 2 LINES	
~~ FORMAT: <channel name> | <group name> | <logo> | <tvg-id>


channel-name | | |
Paste here the URL you copied from the live youtube channel.
```

<br>

**2. Generate Python for "_channel-name.txt_".**

**`scripts/channel-name.py`**

```py script
#! /usr/bin/python3

import requests
import os
import sys

windows = False
if 'win' in sys.platform:
    windows = True

def grab(url):
    response = s.get(url, timeout=15).text
    if '.m3u8' not in response:
        response = requests.get(url).text
        if '.m3u8' not in response:
            if windows:
                print('https://raw.githubusercontent.com/user-name/repo-name/main/assets/info.m3u8')
                return
            #os.system(f'wget {url} -O temp.txt')
            os.system(f'curl "{url}" > temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
                print('https://raw.githubusercontent.com/user-name/repo-name/main/assets/info.m3u8')
                return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    streams = s.get(link[start:end]).text.split('#EXT')
    hd = streams[-1].strip()
    st = hd.find('http')
    print(hd[st:].strip())
    #print(f"{link[start : end]}")

print('#EXTM3U')
print('#EXT-X-VERSION:3')
print('#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000')
s = requests.Session()
with open('../channel-name.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
        else:
            grab(line)

if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
```

_Re-edit :_ `https://raw.githubusercontent.com/user-name/repo-name/main/assets/info.m3u8` _and_ `../channel-name.txt`

<br>

**3. Add an error video (This happens if the youtube channel doesn't work at all).**

**`assets/info.m3u8`**

```
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:10
#EXT-X-MEDIA-SEQUENCE:0
#EXTINF:10.000000,
staytuned0.ts
#EXTINF:10.000000,
staytuned1.ts
#EXT-X-ENDLIST
```

**Download this short video and upload it to the "_assets_" folder and place it together with the `info.m3u8` file. For example [here](https://github.com/ZazerConer/YouTube-to-M3U8/tree/main/assets)**

_Click the link :_
- [staytuned0.ts](https://raw.githubusercontent.com/ZazerConer/YouTube-to-M3U8/main/assets/staytuned0.ts)
- [staytuned1.ts](https://raw.githubusercontent.com/ZazerConer/YouTube-to-M3U8/main/assets/staytuned1.ts)

<br>

**4. Create a Shell script file to install "_channel-name.py_" and auto generate a new file "_channel-name.m3u8_".**

**`channel-name.sh`**

```sh script
#!/bin/bash

echo $(dirname $0)

python3 -m pip install requests

cd $(dirname $0)/scripts/

python3 channel-name.py > ../channel-name.m3u8

echo m3u8 grabbed
```

_Re-edit :_ `channel-name.py` _and_ `../channel-name.m3u8`

<br>

**5. Run the workflows on "_Github Actions_".**

**`channel-name.yml`**

--> Go to the **_Actions_** section --> click **_New_** then select **_set up a workflow yourself_** --> the last one create the name **`channel-name.yml`** and copy paste the script file below.

```yml script
# This is a basic workflow to help you get started with Actions

name: channel-name

# Controls when the action will run. 
on:
  schedule:
    - cron: '0 0/3 * * *'
    
  pull_request:
    branches:
      - main
  
  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - uses: actions/checkout@v2

      # Runs a single command using the runners shell
      #- name: Run a one-line script
      #  run: echo testing!

      # Runs a set of commands using the runners shell 
      - name: config
        run: |
          git pull
          git config --global user.email "your.email@gmail.com"
          git config --global user.name "your-name"
      
      
      - name: Main
        run: |
          pwd
          chmod +x channel-name.sh
          ./channel-name.sh
        
      - name: git add
        run: |
          git add -A
          ls -la 
          
      - name: commit & push
        run: |
          git commit -m "Link updated"
          git push
```

_Re-edit :_ `channel-name` in the first part of the second line. `your.email@gmail.com` and `your-name`. Under it `channel-name.sh` and `./channel-name.sh`

<br>

**You Are Done!**

<br>

Now you can wait until the Actions generates itself in **3 hours** on the workflows or you can create your own test. 

**Like this :** --> Go to the **_Actions_** section --> click **_Select workflow_** click on the name of the workflow file you just created. --> Next below you will find the button **_Run workflow_** click that button --> finally click the green button **"Run workflow"**. 

After that you wait in 2-3 seconds and refresh the page, you will see it working manually from yourself. 

<br> 

## Action works 

**_Workflow run results_**

This is a success :
- <img src="https://badgen.net/badge/✅/Success/green?icon=github">

This is a failure :
- <img src="https://badgen.net/badge/❌/Failure/red?icon=github">

<br>
<hr>

#### Credits : [benmoose39](https://github.com/benmoose39/YouTube_to_m3u)

<hr>
<br>

### Another method

<br>

Get YouTube channel live URL using **[Cloudflare Workers](https://github.com/ZazerConer/YouTube-to-M3U8/tree/main/youtube-live-url)**

<br>
