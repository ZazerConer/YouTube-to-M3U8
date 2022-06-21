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
                print('https://raw.githubusercontent.com/ZazerConer/YouTube_to_M3U8/main/assets/info.m3u8')
                return
            #os.system(f'wget {url} -O temp.txt')
            os.system(f'curl "{url}" > temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
                print('https://raw.githubusercontent.com/ZazerConer/YouTube_to_M3U8/main/assets/info.m3u8')
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
print('#EXT-X-STREAM-INF:RESOLUTION=848x477,FRAME-RATE=25.000000,BANDWIDTH=1359872,CODECS="avc1.64001e,mp4a.40.2",NAME="480"')
print('#EXT-X-STREAM-INF:RESOLUTION=320x180,FRAME-RATE=25.000000,BANDWIDTH=475136,CODECS="avc1.42000c,mp4a.40.5",NAME="240"')
print('#EXT-X-STREAM-INF:RESOLUTION=512x288,FRAME-RATE=25.000000,BANDWIDTH=847872,CODECS="avc1.420015,mp4a.40.2",NAME="380"')
print('#EXT-X-STREAM-INF:RESOLUTION=1280x720,FRAME-RATE=25.000000,BANDWIDTH=2179072,CODECS="avc1.64001f,mp4a.40.2",NAME="720"')
print('#EXT-X-STREAM-INF:RESOLUTION=1920x1080,FRAME-RATE=25.000000,BANDWIDTH=6275072,CODECS="avc1.640028,mp4a.40.2",NAME="1080"')
s = requests.Session()
with open('../suketv_info.txt') as f:
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
