# Bilibili 弹幕词频分析系统

本项目基于 pandas、jieba、matplotlib 实现了对 B站视频弹幕的词频统计与可视化展示，包括词云图、饼图、弹幕密度柱状图。

## 项目结构
- `data/`：放置弹幕 XML 文件
- `src/`：核心代码模块
- `output/`：图表结果输出
- `main.py`：项目主入口

## 使用方法

1. 安装依赖
```bash
pip install -r requirements.txt