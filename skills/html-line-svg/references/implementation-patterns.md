# 实现模式

## 目录

1. 语义分组模板
2. 关系的 SVG 写法
3. HTML 容器与响应式 CSS
4. SVG 样式映射
5. 可访问性写法
6. 几何诊断
7. 常见失误

## 1. 语义分组模板

```html
<div class="semantic-diagram">
  <svg
    class="semantic-diagram__svg"
    viewBox="0 0 600 250"
    role="img"
    aria-labelledby="example-title example-desc"
  >
    <title id="example-title">图的核心判断</title>
    <desc id="example-desc">对象 A 通过一条向右箭头连接对象 B；对象 B 使用虚线表示尚未完成。</desc>
    <defs>
      <marker id="example-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">
        <path d="M 0 0 L 10 5 L 0 10 z"></path>
      </marker>
    </defs>
    <g class="semantic-diagram__object">…</g>
    <g class="semantic-diagram__relation">…</g>
    <g class="semantic-diagram__object semantic-diagram__object--pending">…</g>
  </svg>
</div>
```

按“对象、关系、状态”分组，不按“左上角元素、右下角元素”分组。类名表达语义角色，坐标只负责布局。

## 2. 关系的 SVG 写法

语义属性不是视觉必需项，但能让浏览器测量和人工检查直接对应语义规格。

```html
<!-- 无方向关联：黑线，不使用 marker -->
<g class="semantic-diagram__association" data-relation="association">
  <line x1="180" y1="125" x2="280" y2="125"></line>
</g>

<!-- 包含：外层标签有独立区域，内框完整落在外框内 -->
<g class="semantic-diagram__containment" data-relation="contains">
  <rect class="semantic-diagram__boundary" data-boundary="outer" x="330" y="48" width="210" height="154"></rect>
  <text x="348" y="72">外层状态</text>
  <rect class="semantic-diagram__object" data-boundary="inner" x="365" y="92" width="140" height="76"></rect>
  <text x="435" y="134" text-anchor="middle">内层对象</text>
</g>
```

并列对象可在主体分组上设置相同的 `data-align-group`。它标记需要对齐的主体，不要把标题、说明或角标也放进测量目标。

```html
<g data-align-group="peer-main" data-boundary="group-a">…</g>
<g data-align-group="peer-main" data-boundary="group-b">…</g>
<g data-align-group="peer-main" data-boundary="group-c">…</g>
```

## 3. HTML 容器与响应式 CSS

```css
.semantic-diagram {
  display: flex;
  width: 100%;
  min-width: 0;
  min-height: clamp(10rem, 24vh, 14rem);
  padding: clamp(0.6rem, 1.4vw, 1.1rem);
  align-items: center;
  justify-content: center;
  overflow: hidden;
  border: 1px solid var(--pk-color-hairline, #e5e5e5);
  background: var(--pk-color-canvas, #ffffff);
}

.semantic-diagram__svg {
  display: block;
  width: 100%;
  height: auto;
  max-height: clamp(10rem, 24vh, 14rem);
  overflow: visible;
}

@media (max-width: 640px) {
  .semantic-diagram {
    min-height: 8rem;
    padding: 0.55rem;
  }

  .semantic-diagram__svg {
    max-height: 8.5rem;
  }
}
```

父级 grid 或 flex 子项也设置 `min-width: 0`。若容器隐藏溢出，先确保图形和文字都留在 `viewBox` 安全区内；不要靠 `overflow: visible` 掩盖坐标错误。

## 4. SVG 样式映射

```css
.semantic-diagram__svg text {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

.semantic-diagram__object rect {
  fill: var(--pk-color-canvas, #ffffff);
  stroke: var(--pk-color-ink, #0a0a0a);
  stroke-width: 1.5;
  vector-effect: non-scaling-stroke;
}

.semantic-diagram__object--pending rect {
  stroke-dasharray: 5 4;
}

.semantic-diagram__relation path {
  fill: none;
  stroke: var(--pk-color-link, #0348ed);
  stroke-width: 2;
  stroke-linecap: round;
  vector-effect: non-scaling-stroke;
}

.semantic-diagram__relation marker path {
  fill: var(--pk-color-link, #0348ed);
  stroke: none;
}

.semantic-diagram__association line {
  fill: none;
  stroke: var(--pk-color-ink, #0a0a0a);
  stroke-width: 1.5;
  vector-effect: non-scaling-stroke;
}
```

在 course-design 的 Presentation 中优先直接使用 `--pk-color-*` token。其他项目先读取现有 token，再建立一次映射；不要为单张图创造一组近似颜色。

## 5. 可访问性写法

- `<title>` 回答“这是什么图”。
- `<desc>` 回答“有哪些对象、如何连接、方向是什么、哪些状态特殊”。
- `aria-labelledby` 同时引用 title 与 desc 的 ID。
- 同页多图时给 ID 加页面与语义前缀，例如 `s06-distributed-desc`。
- 图旁正文保留结论，不能把必要信息只藏在 SVG 中。
- 装饰性小折角或分隔线不单独添加 ARIA 标签，避免噪声。

## 6. 几何诊断

结构校验只能发现非法元素、颜色、ID 和可访问性缺失，不能判断“看起来是否对齐”或“是否过于贴近分隔线”。在真实页面中用浏览器测量：

- SVG 内部排布用 `getBBox()` 读取用户坐标；最终缩放结果用 `getBoundingClientRect()` 读取视口坐标。
- 对同一 `data-align-group` 计算主体中心线或指定边缘的最大偏差，与语义规格中的容差比较。
- 对 `data-boundary` 与相邻分隔线计算最近边缘距离；文字、marker 和描边都计入安全区。
- 对 `data-relation="contains"` 检查内框四边都在外框内，并确认外层标签区域不与内框相交。
- 对所有可见 `<text>` 检查其边界是否与非所属框线、关系线或相邻标签相交。

桌面和窄屏分别测量，因为 CSS 缩放、字体替换和分栏堆叠会改变最终视觉结果。数值通过后仍需看截图：光学中心、留白和密度不能完全由碰撞检测代替。

## 7. 常见失误

- 先摆形状再猜含义：回到语义规格，删掉没有对象或关系依据的元素。
- 用箭头表示“只是并列”：改为相同容器、留白或标题对齐。
- 用箭头表示无方向关联或包含：分别改为黑色无 marker 连线或内外嵌套框。
- 卡片标题与图内小标题重复：按可见标签清单只保留信息层级更清楚的一处。
- 三组主体各自凭感觉摆放：选定共同锚点并测量；给分隔线预留安全区。
- 虚线同时表示三种状态：增加状态文字，或拆分为不同图。
- marker ID 重复：使用页面或组件前缀，并对整份 HTML 做唯一性检查。
- 文字转路径：恢复为 `<text>`，保留可读性、可维护性和无障碍信息。
- 固定 `width`、`height` 导致卡片溢出：使用 `viewBox` 与 CSS 宽度。
- 为了“精致”加入阴影、渐变、大面积色块：移除，回到线条、留白和少量语义色。
