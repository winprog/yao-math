# yao-math 初中数学教学可视化

本项目用于生成初中数学几何概念的可视化图形，每个脚本绘制一个特定数学概念，输出高清 PNG 图片，供教学使用。

## 项目结构

```
yao-math/
├── README.md                  # 项目说明（本文件）
├── scripts/                   # 绘图脚本目录
│   ├── circumferential_angles.py     # 圆周角与圆心角定理演示
│   ├── parallel_lines_8_angles.py    # 平行线 3 线 8 角图形
│   ├── triangle.py                   # 平行线 + 角平分线 → 等腰三角形
│   └── 3lines.py                     # 三线八角基本图形
├── docs/                      # 文档目录
│   └── query.md               # 教学问答结构化示例
├── output/                    # 生成的图片输出目录（git 忽略）
└── .trae/                     # Trae 技能定义（勿动）
```

## 环境要求

- Python 3.x
- 依赖库：`matplotlib`、`numpy`

安装依赖：

```bash
pip install matplotlib numpy
```

## 使用说明

所有脚本输出到 `output/` 目录。运行任一脚本：

```bash
python scripts/circumferential_angles.py
```

可用脚本一览：

| 脚本 | 演示内容 | 输出图片 |
|------|---------|---------|
| `circumferential_angles.py` | 圆周角定理：同弧所对圆周角相等，且圆心角 = 2 × 圆周角 | `circumferential_angles.png` |
| `parallel_lines_8_angles.py` | 平行线 3 线 8 角：同位角、内错角、同旁内角关系 | `parallel_lines_8_angles_corrected.png` |
| `triangle.py` | 平行线 + 角平分线 → 等腰三角形 | `triangle.png` |
| `3lines.py` | 三线八角基本图形 | `test_q1_basic.png` |

## 字体说明

程序默认使用系统中文字体（优先微软雅黑 Microsoft YaHei），在 Linux 下若缺少该字体，将自动回退到候选中文字体。

## 数学内容说明

- **圆周角定理**：同一个圆弧所对的所有圆周角相等；圆心角等于它所对圆周角的 2 倍。
- **平行线性质**：同位角相等、内错角相等、同旁内角互补。
- **角度关系**：利用平行线性质与角平分线可推导等腰三角形等结论。