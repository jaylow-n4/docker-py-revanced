with open('src/downloader/sources.py', 'r') as f:
    text = f.read()

text = text.replace('"twitch": f"{APK_MIRROR_BASE_APK_URL}/twitch-interactive-inc/twitch/",', '"twitch": APK_PURE_URL,')
text = text.replace('"twitter": f"{APK_MIRROR_BASE_APK_URL}/x-corp/twitter/",', '"twitter": APK_PURE_URL,')

with open('src/downloader/sources.py', 'w') as f:
    f.write(text)
