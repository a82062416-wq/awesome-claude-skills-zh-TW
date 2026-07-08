---
name: remotion-video
description: 用 Remotion（React + TypeScript）程式化製作影片。當使用者要求「做影片」「產生動畫影片」「做開場動畫」「資料動畫」「把數據做成影片」「MP4」「影片模板」時使用此技能。Claude 寫 React 組件描述每一幀，Remotion 渲染成 MP4。
---

# Remotion 程式化影片製作

## 核心概念

Remotion 把影片當成 React 應用：每一幀（frame）都是一次 React 渲染。
你用 `useCurrentFrame()` 取得目前幀數，用數學函數把幀數轉成動畫。

## 專案建立

```bash
npx create-video@latest my-video --blank
cd my-video && npm install
```

## 四個必會 API

### 1. useCurrentFrame — 動畫的心臟
```tsx
import { useCurrentFrame, useVideoConfig } from 'remotion';

const MyComp = () => {
  const frame = useCurrentFrame();        // 目前第幾幀
  const { fps, durationInFrames, width, height } = useVideoConfig();
  return <div>第 {frame} 幀</div>;
};
```

### 2. interpolate — 數值映射（淡入淡出、位移）
```tsx
import { interpolate } from 'remotion';

// 第 0~30 幀之間，透明度從 0 到 1（淡入）
const opacity = interpolate(frame, [0, 30], [0, 1], {
  extrapolateRight: 'clamp',  // 超過 30 幀後固定在 1
});

// 位移：從左邊滑入
const translateX = interpolate(frame, [0, 20], [-200, 0], { extrapolateRight: 'clamp' });
```

### 3. spring — 彈簧物理動畫（自然的彈跳感）
```tsx
import { spring } from 'remotion';

const scale = spring({
  frame,
  fps,
  config: { damping: 12, stiffness: 100 },  // damping 越小越彈
});
```

### 4. Sequence + Composition — 時間軸編排
```tsx
import { Sequence, Composition } from 'remotion';

// Sequence：讓子元素在指定時間出現（類似剪輯軌道）
<Sequence from={0} durationInFrames={60}>
  <TitleScene />
</Sequence>
<Sequence from={60} durationInFrames={90}>
  <DataScene />
</Sequence>

// Composition：註冊影片（在 Root.tsx）
<Composition
  id="MyVideo"
  component={MyVideo}
  durationInFrames={300}   // 300 幀 ÷ 30fps = 10 秒
  fps={30}
  width={1920}
  height={1080}
/>
```

## 常用元素

```tsx
import { AbsoluteFill, Img, Audio, Video, staticFile } from 'remotion';

<AbsoluteFill style={{ backgroundColor: '#0f172a' }}>  {/* 滿版容器 */}
  <Img src={staticFile('logo.png')} />
  <Audio src={staticFile('bgm.mp3')} volume={0.5} />
  <Video src={staticFile('clip.mp4')} startFrom={30} />
</AbsoluteFill>
```

## 渲染輸出

```bash
# 預覽（開發模式，瀏覽器即時看）
npx remotion studio

# 渲染成 MP4
npx remotion render MyVideo out/video.mp4

# 指定品質與並發
npx remotion render MyVideo out/video.mp4 --crf 18 --concurrency 4

# 只渲染一幀（做封面圖）
npx remotion still MyVideo out/thumbnail.png --frame=45
```

## 實戰模式

1. **先問清楚**：影片長度、尺寸（16:9 / 9:16 直式 / 1:1）、風格、要放什麼內容
2. **拆場景**：每個場景一個組件，用 `<Sequence>` 串接
3. **動畫節奏**：進場用 spring（彈性）、轉場用 interpolate（線性/緩動）、每個元素錯開 3~5 幀更有層次
4. **中文字體**：`fontFamily: '"Noto Sans TC", sans-serif'`，記得先載入字體
5. **渲染前檢查**：`durationInFrames` 加總是否等於 Composition 總長

## 與 FFmpeg 搭配（見 ffmpeg-video-skill）

Remotion 產出 MP4 後，用 FFmpeg 做壓縮、轉 GIF、加字幕、平台規格轉換。
