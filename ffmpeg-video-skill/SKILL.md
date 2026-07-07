---
name: ffmpeg-video
description: 用 FFmpeg 做影片後製處理。當使用者要求「壓縮影片」「轉檔」「剪影片」「影片轉 GIF」「抽音軌」「加字幕」「合併影片」「調整解析度」「做成 IG/YouTube/抖音規格」時使用此技能。零成本 CLI 工具，符合 CLI 優先原則。
---

# FFmpeg 影片後製技能

## 檢查安裝

```bash
ffmpeg -version || (apt-get install -y ffmpeg 2>/dev/null || brew install ffmpeg)
```

## 最常用的 10 個模式

### 1. 壓縮影片（CRF 品質壓縮，最常用）
```bash
# CRF 18=近無損、23=預設、28=小檔案。+2 約減半檔案大小
ffmpeg -i input.mp4 -c:v libx264 -crf 23 -preset medium -c:a aac -b:a 128k output.mp4
```

### 2. 剪片段（不重新編碼，秒完成）
```bash
# 從 00:01:30 開始剪 45 秒
ffmpeg -ss 00:01:30 -i input.mp4 -t 45 -c copy clip.mp4
```

### 3. 影片轉 GIF（高品質兩段式）
```bash
ffmpeg -i input.mp4 -vf "fps=12,scale=480:-1:flags=lanczos,palettegen" palette.png
ffmpeg -i input.mp4 -i palette.png -filter_complex "fps=12,scale=480:-1:flags=lanczos[x];[x][1:v]paletteuse" output.gif
```

### 4. GIF 轉 MP4（網頁友善，檔案小 10 倍）
```bash
ffmpeg -i input.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" output.mp4
```

### 5. 調整解析度 / 直式轉換
```bash
# 縮到 1080p（寬度自動等比）
ffmpeg -i input.mp4 -vf "scale=-2:1080" output.mp4

# 16:9 轉 9:16 直式（置中裁切）
ffmpeg -i input.mp4 -vf "crop=ih*9/16:ih" vertical.mp4
```

### 6. 抽出音軌 / 去掉聲音
```bash
ffmpeg -i input.mp4 -vn -c:a libmp3lame -q:a 2 audio.mp3   # 抽音軌
ffmpeg -i input.mp4 -an -c:v copy muted.mp4                 # 去聲音
```

### 7. 合併多支影片
```bash
printf "file 'a.mp4'\nfile 'b.mp4'\nfile 'c.mp4'\n" > list.txt
ffmpeg -f concat -safe 0 -i list.txt -c copy merged.mp4
```

### 8. 加字幕
```bash
# 燒錄硬字幕（永久嵌入畫面）
ffmpeg -i input.mp4 -vf "subtitles=subs.srt:force_style='FontName=Noto Sans TC,FontSize=24'" output.mp4
```

### 9. 平台規格預設
```bash
# YouTube 1080p
ffmpeg -i in.mp4 -c:v libx264 -crf 21 -preset slow -c:a aac -b:a 192k -movflags faststart yt.mp4

# Instagram Reels / 抖音（9:16、60 秒內）
ffmpeg -i in.mp4 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2" -c:v libx264 -crf 23 -t 60 reels.mp4

# LINE / 通訊軟體傳送（壓小）
ffmpeg -i in.mp4 -vf "scale=-2:720" -c:v libx264 -crf 28 -preset fast line.mp4
```

### 10. 批次處理
```bash
for f in *.mov; do ffmpeg -i "$f" -c:v libx264 -crf 23 "${f%.mov}.mp4"; done
```

## 除錯要訣

- 看影片資訊：`ffprobe -v quiet -print_format json -show_format -show_streams input.mp4`
- 尺寸報錯（not divisible by 2）：加 `-vf "scale=trunc(iw/2)*2:trunc(ih/2)*2"`
- 網頁播放要加 `-movflags faststart -pix_fmt yuv420p`
- `-c copy` 不重編碼最快，但剪切點可能不準（只能切在關鍵幀）；要精準就去掉 `-c copy` 重編碼
