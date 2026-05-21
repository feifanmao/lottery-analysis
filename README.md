# 彩票分析系统

大乐透 & 双色球历史数据爬取、走势分析、多维度统计模型，Web 界面可视化展示。

## 功能

- **数据爬取**：自动从官方接口获取大乐透、双色球历史开奖数据
- **走势图**：号码走势折线图，支持最近 50 期数据
- **频率分析**：号码出现频率统计、冷热号排行
- **遗漏分析**：当前遗漏、最大遗漏、平均遗漏
- **号段分布**：前区/红球分段统计
- **奇偶 & 大小比**：比例分布饼图
- **和值分析**：和值范围与区间分布
- **连号分析**：连号出现率、高频连号对
- **重复号分析**：与上期重复号码统计
- **AC 值 & 跨度**：号码离散度与极差分析

## 技术栈

| 层级 | 技术 |
|------|------|
| 后端 | Python + Flask + waitress |
| 数据库 | SQLite |
| 前端 | HTML + CSS + JavaScript + ECharts |
| 打包 | PyInstaller |

## 快速开始

### 方式一：直接运行

```bash
# 安装依赖
pip install -r requirements.txt

# 启动服务
python app.py
```

浏览器访问 http://localhost:5000

### 方式二：使用启动脚本

双击 `start.bat`（前台运行）或 `start-silent.bat`（后台静默运行），自动打开浏览器。

### 方式三：使用 exe（无需 Python 环境）

从 `dist/彩票分析系统/` 目录获取打包好的 exe，双击 `彩票分析系统.exe` 即可运行。

## 项目结构

```
├── app.py                 # Flask 主应用
├── server.py              # 生产级 waitress 服务器
├── launcher.py            # PyInstaller 打包入口
├── config.py              # 配置文件
├── requirements.txt       # Python 依赖
├── start.bat              # 一键启动脚本
├── start-silent.bat       # 静默启动脚本
├── crawler/               # 数据爬虫
│   ├── dlt_crawler.py     # 大乐透爬虫
│   └── ssq_crawler.py     # 双色球爬虫
├── analysis/              # 分析模型
│   ├── frequency.py       # 频率统计
│   ├── missing.py         # 遗漏值分析
│   ├── segment.py         # 号段分布
│   ├── parity.py          # 奇偶/大小比
│   ├── sum_value.py       # 和值分析
│   ├── consecutive.py     # 连号分析
│   ├── repeat.py          # 重复号分析
│   ├── ac_value.py        # AC 值分析
│   └── span.py            # 跨度分析
├── api/                   # REST API
│   ├── draw.py            # 开奖数据接口
│   └── analysis.py        # 分析结果接口
├── models/
│   └── database.py        # SQLite 数据库操作
├── static/                # 前端资源
│   ├── css/style.css
│   └── js/
│       ├── api.js         # API 调用封装
│       ├── app.js         # 页面通用逻辑
│       └── charts.js      # ECharts 图表配置
└── templates/             # 页面模板
    ├── base.html          # 基础布局
    ├── index.html         # 首页
    ├── trend.html         # 走势图
    ├── frequency.html     # 频率分析
    ├── segment.html       # 号段分析
    └── advanced.html      # 高级分析
```

## API 接口

| 接口 | 说明 |
|------|------|
| `GET /api/dlt/draws` | 大乐透开奖记录 |
| `GET /api/dlt/latest` | 大乐透最新开奖 |
| `GET /api/ssq/draws` | 双色球开奖记录 |
| `GET /api/ssq/latest` | 双色球最新开奖 |
| `GET /api/analysis/frequency?lottery=dlt` | 频率分析 |
| `GET /api/analysis/missing?lottery=dlt` | 遗漏分析 |
| `GET /api/analysis/segment?lottery=dlt` | 号段分析 |
| `GET /api/analysis/parity?lottery=dlt` | 奇偶/大小比 |
| `GET /api/analysis/sum?lottery=dlt` | 和值分析 |
| `GET /api/analysis/consecutive?lottery=dlt` | 连号分析 |
| `GET /api/analysis/repeat?lottery=dlt` | 重复号分析 |
| `GET /api/analysis/ac?lottery=dlt` | AC 值分析 |
| `GET /api/analysis/span?lottery=dlt` | 跨度分析 |

> `lottery` 参数：`dlt`（大乐透）或 `ssq`（双色球）

## 数据来源

- 大乐透：体彩官方 webapi.sporttery.cn
- 双色球：中彩网 www.cwl.gov.cn

## 许可证

MIT
