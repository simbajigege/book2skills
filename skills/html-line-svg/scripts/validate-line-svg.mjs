#!/usr/bin/env node

import {readFileSync} from 'node:fs';
import {resolve} from 'node:path';

const inputs = process.argv.slice(2);

if (inputs.length === 0) {
  console.error('Usage: node validate-line-svg.mjs <svg-or-html> [...]');
  process.exit(2);
}

const allowedHexColors = new Set([
  '#ffffff',
  '#0a0a0a',
  '#171717',
  '#737373',
  '#e5e5e5',
  '#ff3700',
  '#fe7e0f',
  '#0348ed',
]);

const forbiddenTags = ['filter', 'linearGradient', 'radialGradient', 'pattern', 'image', 'foreignObject'];
let totalErrors = 0;
let totalWarnings = 0;

function getAttribute(openingTag, name) {
  const match = openingTag.match(new RegExp(`\\s${name}=(?:"([^"]*)"|'([^']*)')`, 'i'));
  return match ? match[1] ?? match[2] : null;
}

for (const input of inputs) {
  const filename = resolve(input);
  let source;

  try {
    source = readFileSync(filename, 'utf8');
  } catch (error) {
    console.error(`[error] ${input}: ${error.message}`);
    totalErrors += 1;
    continue;
  }

  const svgBlocks = [...source.matchAll(/<svg\b[\s\S]*?<\/svg>/gi)].map((match) => match[0]);
  const errors = [];
  const warnings = [];
  const isStandaloneSvg = filename.toLowerCase().endsWith('.svg');
  const documentUsesNonScalingStroke = /vector-effect\s*:\s*non-scaling-stroke|vector-effect=(?:"non-scaling-stroke"|'non-scaling-stroke')/i.test(source);

  if (svgBlocks.length === 0) {
    errors.push('没有找到 <svg> 元素');
  }

  const documentIds = [...source.matchAll(/\sid=(?:"([^"]+)"|'([^']+)')/gi)].map((match) => match[1] ?? match[2]);
  const seenIds = new Set();

  for (const id of documentIds) {
    if (seenIds.has(id)) {
      errors.push(`文档内 ID 重复：${id}`);
    }
    seenIds.add(id);
  }

  svgBlocks.forEach((svg, index) => {
    const label = `SVG ${index + 1}`;
    const openingTag = svg.match(/^<svg\b[^>]*>/i)?.[0] ?? '';
    const viewBox = getAttribute(openingTag, 'viewBox');
    const role = getAttribute(openingTag, 'role');
    const labelledBy = getAttribute(openingTag, 'aria-labelledby');

    if (!viewBox || !/^\s*-?(?:\d+(?:\.\d+)?|\.\d+)\s+-?(?:\d+(?:\.\d+)?|\.\d+)\s+(?:\d+(?:\.\d+)?|\.\d+)\s+(?:\d+(?:\.\d+)?|\.\d+)\s*$/.test(viewBox)) {
      errors.push(`${label} 缺少有效 viewBox`);
    }

    if (role !== 'img') {
      errors.push(`${label} 应设置 role="img"`);
    }

    const titleMatch = svg.match(/<title\b[^>]*\sid=(?:"([^"]+)"|'([^']+)')[^>]*>[\s\S]*?<\/title>/i);
    const descMatch = svg.match(/<desc\b[^>]*\sid=(?:"([^"]+)"|'([^']+)')[^>]*>[\s\S]*?<\/desc>/i);
    const titleId = titleMatch ? titleMatch[1] ?? titleMatch[2] : null;
    const descId = descMatch ? descMatch[1] ?? descMatch[2] : null;

    if (!titleId) errors.push(`${label} 缺少带唯一 ID 的 <title>`);
    if (!descId) errors.push(`${label} 缺少带唯一 ID 的 <desc>`);

    const ariaIds = labelledBy?.trim().split(/\s+/) ?? [];
    if (!labelledBy || !titleId || !descId || !ariaIds.includes(titleId) || !ariaIds.includes(descId)) {
      errors.push(`${label} 的 aria-labelledby 必须同时引用 title 与 desc`);
    }

    for (const tag of forbiddenTags) {
      if (new RegExp(`<${tag}\\b`, 'i').test(svg)) {
        errors.push(`${label} 使用了禁用元素 <${tag}>`);
      }
    }

    if (/\s(?:filter|mask)\s*=/i.test(svg)) {
      errors.push(`${label} 使用了禁用的 filter 或 mask 属性`);
    }

    const references = [...svg.matchAll(/url\(\s*#([^\s)]+)\s*\)/gi)].map((match) => match[1]);
    for (const reference of references) {
      if (!seenIds.has(reference)) {
        errors.push(`${label} 引用了不存在的 ID：${reference}`);
      }
    }

    const hexColors = [...svg.matchAll(/#[0-9a-f]{6}\b/gi)].map((match) => match[0].toLowerCase());
    for (const color of hexColors) {
      if (!allowedHexColors.has(color)) {
        warnings.push(`${label} 使用了 STYLE_DNA 之外的颜色：${color}`);
      }
    }

    if (/^<svg\b[^>]*\s(?:width|height)=/i.test(openingTag)) {
      warnings.push(`${label} 根元素包含固定 width/height；内联场景优先交给 CSS 响应式控制`);
    }

    if (isStandaloneSvg && !documentUsesNonScalingStroke) {
      warnings.push(`${label} 未发现 non-scaling-stroke，缩放后线宽可能失衡`);
    }
  });

  console.log(`${errors.length === 0 ? '[ok]' : '[fail]'} ${input}: ${svgBlocks.length} 个 SVG`);
  for (const error of errors) console.error(`  error: ${error}`);
  for (const warning of warnings) console.warn(`  warning: ${warning}`);

  totalErrors += errors.length;
  totalWarnings += warnings.length;
}

console.log(`检查完成：${totalErrors} 个错误，${totalWarnings} 个警告`);
process.exit(totalErrors === 0 ? 0 : 1);
