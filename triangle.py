import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

# 设置中文字体 - 固定使用微软雅黑
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建图形
fig, ax = plt.subplots(1, 1, figsize=(10, 8))
ax.set_xlim(-4, 8)
ax.set_ylim(-1, 6)
ax.set_aspect('equal')
ax.axis('off')

# 定义关键点坐标
# AB 水平线在 y=4，从 x=0 到 x=5
# CD 水平线在 y=1，从 x=0 到 x=6
# B 点位于 (0, 4)，A 点位于 (-1, 4) 作为 AB 延长线
# C 点位于 (0, 1)，D 点位于 (6, 1)
# E 点为角平分线与 CD 的交点，位于 (4, 1) 附近，但需要计算使得 BE 平分角 ABC

# 设定 B 点坐标
B = (2, 4)
C = (0, 1)
# 确定 A 点，使 AB 水平向左
A = (0, 4)
# 确定 D 点，使 CD 水平向右
D = (6, 1)

# 计算 E 点：BE 平分角 ABC，需要满足角 ABE = 角 EBC
# 正确的角平分线计算方法：使用角平分线定理
import math
import numpy as np

# 计算向量 BA 和 BC
BA = np.array([A[0]-B[0], A[1]-B[1]])
BC = np.array([C[0]-B[0], C[1]-B[1]])

# 单位化向量
BA_unit = BA / np.linalg.norm(BA)
BC_unit = BC / np.linalg.norm(BC)

# 角平分线方向向量 = BA单位向量 + BC单位向量
BE_dir = BA_unit + BC_unit

# 角平分线方程：从B点出发，沿BE_dir方向
# 我们需要找到与CD线的交点E
# CD线方程：y = 1 (水平线)

# 参数方程：x = B[0] + t * BE_dir[0], y = B[1] + t * BE_dir[1]
# 当 y = 1 时，求 t
t = (1 - B[1]) / BE_dir[1]

# 计算交点E的坐标
E_x = B[0] + t * BE_dir[0]
E_y = 1  # 在CD线上

E = (E_x, E_y)

# 验证角平分线：计算∠ABE和∠EBC是否相等
# 计算向量夹角
def angle_between_vectors(v1, v2):
    """计算两个向量之间的夹角（弧度）"""
    dot_product = np.dot(v1, v2)
    norms = np.linalg.norm(v1) * np.linalg.norm(v2)
    return np.arccos(np.clip(dot_product / norms, -1.0, 1.0))

# 验证角平分
BE = np.array([E[0]-B[0], E[1]-B[1]])
angle_ABE = angle_between_vectors(-BA, BE)  # 注意：BA方向是从B到A，需要取反
angle_EBC = angle_between_vectors(BE, BC)

print(f"∠ABE = {np.degrees(angle_ABE):.2f}°")
print(f"∠EBC = {np.degrees(angle_EBC):.2f}°")
print(f"角度差 = {abs(np.degrees(angle_ABE - angle_EBC)):.4f}°")

# 重新计算
BC_length = math.sqrt((B[0]-C[0])**2 + (B[1]-C[1])**2)
CE_length = E[0] - C[0]

# 绘制平行线
# AB 水平线
ax.plot([A[0], B[0]], [A[1], B[1]], 'k-', linewidth=2)
# CD 水平线
ax.plot([C[0], D[0]], [C[1], D[1]], 'k-', linewidth=2)
# 延长线虚线表示平行
ax.plot([B[0], B[0]+1], [B[1], B[1]], 'k--', alpha=0.5, linewidth=1)
ax.plot([D[0], D[0]+1], [D[1], D[1]], 'k--', alpha=0.5, linewidth=1)

# 绘制角平分线 BE
ax.plot([B[0], E[0]], [B[1], E[1]], 'r-', linewidth=2.5, label='角平分线 BE')

# 绘制三角形 BCE
triangle = plt.Polygon([B, C, E], fill=None, edgecolor='blue', linewidth=2, linestyle='--')
ax.add_patch(triangle)

# 标注点 - 设置颜色分组
ax.plot(A[0], A[1], 'ro', markersize=8)  # 红色标记A点
ax.text(A[0]-0.2, A[1], 'A', fontsize=14, va='center', ha='right', color='red')

ax.plot(B[0], B[1], 'bo', markersize=8)  # 蓝色标记B点
ax.text(B[0]-0.2, B[1]+0.1, 'B', fontsize=14, va='bottom', ha='right', color='blue')

ax.plot(C[0], C[1], 'go', markersize=8)  # 绿色标记C点
ax.text(C[0]-0.2, C[1]-0.1, 'C', fontsize=14, va='top', ha='right', color='green')

ax.plot(D[0], D[1], 'mo', markersize=8)  # 洋红色标记D点
ax.text(D[0]+0.2, D[1]-0.1, 'D', fontsize=14, va='top', ha='left', color='magenta')

ax.plot(E[0], E[1], 'co', markersize=8)  # 青色标记E点
ax.text(E[0]+0.2, E[1]-0.1, 'E', fontsize=14, va='top', ha='left', color='cyan')

# 标注平行线符号（箭头）
# 在 AB 和 CD 左侧添加双箭头表示平行
ax.annotate('', xy=(A[0]+0.3, A[1]), xytext=(A[0]+0.8, A[1]),
            arrowprops=dict(arrowstyle='->', lw=1, color='gray'))
ax.annotate('', xy=(C[0]+0.3, C[1]), xytext=(C[0]+0.8, C[1]),
            arrowprops=dict(arrowstyle='->', lw=1, color='gray'))
ax.text(A[0]+0.55, A[1]+0.15, '∥', fontsize=12, ha='center', color='gray')

# 标注角度
# 为了标注角，需要绘制圆弧
def draw_angle(ax, center, p1, p2, radius=0.5, color='green', label=None, label_offset=0.2):
    """绘制角度弧线并标注"""
    import numpy as np
    # 计算向量
    v1 = (p1[0]-center[0], p1[1]-center[1])
    v2 = (p2[0]-center[0], p2[1]-center[1])
    # 计算角度
    angle1 = np.arctan2(v1[1], v1[0])
    angle2 = np.arctan2(v2[1], v2[0])
    # 确保从 angle1 到 angle2 是逆时针
    theta = np.linspace(angle1, angle2, 50)
    # 绘制弧线
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    ax.plot(x, y, color=color, linewidth=1.5)
    # 标注角度文字
    mid_angle = (angle1 + angle2) / 2
    label_x = center[0] + (radius + label_offset) * np.cos(mid_angle)
    label_y = center[1] + (radius + label_offset) * np.sin(mid_angle)
    if label:
        ax.text(label_x, label_y, label, fontsize=10, color=color, ha='center', va='center')

# 在 B 点标注角 ABE 和角 EBC
# 需要计算方向向量
import numpy as np

# 角 ABE：BA 方向 和 BE 方向
BA = (A[0]-B[0], A[1]-B[1])
BE_vec = (E[0]-B[0], E[1]-B[1])
BC_vec = (C[0]-B[0], C[1]-B[1])

# 计算各方向角度
angle_BA = np.arctan2(BA[1], BA[0])
angle_BE = np.arctan2(BE_vec[1], BE_vec[0])
angle_BC = np.arctan2(BC_vec[1], BC_vec[0])

# 绘制角 ABE (从 BA 到 BE)
# 需要确保绘制小弧
def draw_angle_at_point(ax, center, dir1, dir2, radius=0.4, color='green', label=None):
    """通过方向向量绘制角"""
    angle1 = np.arctan2(dir1[1], dir1[0])
    angle2 = np.arctan2(dir2[1], dir2[0])
    # 确保逆时针
    if angle2 < angle1:
        angle2 += 2*np.pi
    if angle2 - angle1 > np.pi:
        angle1, angle2 = angle2, angle1 + 2*np.pi
    theta = np.linspace(angle1, angle2, 30)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    ax.plot(x, y, color=color, linewidth=1.5)
    if label:
        mid = (angle1 + angle2) / 2
        lx = center[0] + (radius + 0.2) * np.cos(mid)
        ly = center[1] + (radius + 0.2) * np.sin(mid)
        ax.text(lx, ly, label, fontsize=9, color=color, ha='center', va='center')

# 角 ABE
draw_angle_at_point(ax, B, BA, BE_vec, radius=0.5, color='orange', label='∠1')
# 角 EBC
draw_angle_at_point(ax, B, BE_vec, BC_vec, radius=0.5, color='orange', label='∠2')

# 在 E 点标注内错角
# 角 BEC 和角 EBC 相等
# 绘制角 BEC
EB = (B[0]-E[0], B[1]-E[1])
EC = (C[0]-E[0], C[1]-E[1])
draw_angle_at_point(ax, E, EB, EC, radius=0.5, color='purple', label='∠3')
# 也可以标注角 CED 等，但不需要

# 标注等腰三角形的相等边
# 在 BC 和 CE 边上添加双斜线表示相等
def add_equal_mark(ax, p1, p2, offset=0.1):
    """在边的中点附近添加双斜线标记"""
    mid = ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)
    # 计算边的垂直方向
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    length = np.sqrt(dx**2 + dy**2)
    if length == 0:
        return
    # 单位方向向量
    ux, uy = dx/length, dy/length
    # 垂直向量
    nx, ny = -uy, ux
    # 绘制双斜线
    for i in [-1, 1]:
        x1 = mid[0] + nx * offset * i
        y1 = mid[1] + ny * offset * i
        x2 = mid[0] + ux * 0.15 + nx * offset * i
        y2 = mid[1] + uy * 0.15 + ny * offset * i
        ax.plot([x1, x2], [y1, y2], 'k-', linewidth=1.5)

# 在 BC 和 CE 上添加相等标记
add_equal_mark(ax, B, C, offset=0.12)
add_equal_mark(ax, C, E, offset=0.12)

# 添加标题和说明
ax.text(3, 5.5, '平行线 + 角平分线 → 等腰三角形', fontsize=16, ha='center', fontweight='bold')
ax.text(3, 5.0, '已知: AB ∥ CD, BE 平分 ∠ABC', fontsize=12, ha='center', color='gray')
ax.text(3, 4.6, '结论: △BCE 是等腰三角形 (BC = CE)', fontsize=12, ha='center', color='blue')

# 添加角度关系说明
ax.text(5.5, 4.2, '∠1 = ∠2 (角平分线)', fontsize=10, color='orange')
ax.text(5.5, 3.8, '∠2 = ∠3 (内错角，AB∥CD)', fontsize=10, color='orange')
ax.text(5.5, 3.4, '∴ ∠1 = ∠3', fontsize=10, fontweight='bold')
ax.text(5.5, 3.0, '∴ BC = CE (等角对等边)', fontsize=10, fontweight='bold', color='blue')

plt.tight_layout()
plt.show()