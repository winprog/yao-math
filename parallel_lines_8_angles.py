# -*- coding: utf-8 -*-
"""
平行线3线8角图形示例

这个程序绘制两条平行线被一条截线所截形成的8个角度的几何图形。
在几何学中，这种图形用于展示同位角、内错角、同旁内角等角度关系。
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
from matplotlib.path import Path
import math

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def calculate_angle_arc_points(vertex, line1_dir, line2_dir, radius=0.4, arc_points=20):
    """计算角度弧线的点坐标"""
    # 计算两条线的方向角度
    angle1 = math.atan2(line1_dir[1], line1_dir[0])
    angle2 = math.atan2(line2_dir[1], line2_dir[0])
    
    # 确保角度从较小的开始
    start_angle = min(angle1, angle2)
    end_angle = max(angle1, angle2)
    
    # 如果角度差大于180度，则取另一个方向
    if end_angle - start_angle > math.pi:
        start_angle, end_angle = end_angle, start_angle + 2 * math.pi
    
    # 生成弧线点
    angles = np.linspace(start_angle, end_angle, arc_points)
    points = []
    for angle in angles:
        x = vertex[0] + radius * math.cos(angle)
        y = vertex[1] + radius * math.sin(angle)
        points.append((x, y))
    
    return points

def calculate_angle_bisector(vertex, line1_dir, line2_dir):
    """计算角平分线方向向量"""
    # 计算两条线的方向角度
    angle1 = math.atan2(line1_dir[1], line1_dir[0])
    angle2 = math.atan2(line2_dir[1], line2_dir[0])
    
    # 计算角平分线角度（两个角度的平均值）
    bisector_angle = (angle1 + angle2) / 2
    
    # 返回角平分线方向向量
    return (math.cos(bisector_angle), math.sin(bisector_angle))

def get_angle_label_position(vertex, line1_dir, line2_dir, label_radius=0.6):
    """计算角度标签在角平分线上的位置"""
    bisector_dir = calculate_angle_bisector(vertex, line1_dir, line2_dir)
    
    # 标签位置在角平分线方向上
    label_x = vertex[0] + label_radius * bisector_dir[0]
    label_y = vertex[1] + label_radius * bisector_dir[1]
    
    return label_x, label_y

def draw_parallel_lines_8_angles():
    """绘制平行线3线8角图形"""
    
    # 创建图形
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    ax.set_xlim(-1, 8)
    ax.set_ylim(-1, 6)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # 定义两条平行线的坐标（更合理的布局）
    # 平行线1: y = 4
    line1_start = (0, 4)
    line1_end = (7, 4)
    
    # 平行线2: y = 1
    line2_start = (0, 1)
    line2_end = (7, 1)
    
    # 截线的坐标（更合理的角度）
    transversal_start = (1, 5)
    transversal_end = (6, 0)
    
    # 绘制平行线
    ax.plot([line1_start[0], line1_end[0]], [line1_start[1], line1_end[1]], 
            'b-', linewidth=2, label='平行线1')
    ax.plot([line2_start[0], line2_end[0]], [line2_start[1], line2_end[1]], 
            'b-', linewidth=2, label='平行线2')
    
    # 绘制截线
    ax.plot([transversal_start[0], transversal_end[0]], 
            [transversal_start[1], transversal_end[1]], 
            'r-', linewidth=2, label='截线')
    
    # 计算交点
    # 截线与平行线1的交点
    t = (4 - transversal_start[1]) / (transversal_end[1] - transversal_start[1])
    intersection1_x = transversal_start[0] + t * (transversal_end[0] - transversal_start[0])
    intersection1 = (intersection1_x, 4)
    
    # 截线与平行线2的交点
    t = (1 - transversal_start[1]) / (transversal_end[1] - transversal_start[1])
    intersection2_x = transversal_start[0] + t * (transversal_end[0] - transversal_start[0])
    intersection2 = (intersection2_x, 1)
    
    # 标记交点
    ax.plot(intersection1[0], intersection1[1], 'ko', markersize=8)
    ax.plot(intersection2[0], intersection2[1], 'ko', markersize=8)
    
    # 计算各条线的方向向量
    # 平行线1的方向（向右）
    line1_dir = (1, 0)
    # 平行线2的方向（向右）
    line2_dir = (1, 0)
    # 截线的方向
    transversal_dir = (transversal_end[0] - transversal_start[0], 
                      transversal_end[1] - transversal_start[1])
    transversal_dir = (transversal_dir[0] / np.linalg.norm(transversal_dir), 
                      transversal_dir[1] / np.linalg.norm(transversal_dir))
    
    # 计算各个角度的弧线点并绘制
    angles_info = []
    
    # 交点1处的4个角度
    # ∠1: 截线左上部分与平行线1左侧延长线形成的角
    angle1_points = calculate_angle_arc_points(intersection1, 
                                              (-1, 0),  # 平行线1向左
                                              (-transversal_dir[0], -transversal_dir[1]),  # 截线向左上
                                              radius=0.4)
    label1_x, label1_y = get_angle_label_position(intersection1,
                                                 (-1, 0),  # 平行线1向左
                                                 (-transversal_dir[0], -transversal_dir[1]))  # 截线向左上
    angles_info.append((angle1_points, '∠1', 'red', label1_x, label1_y))
    
    # ∠2: 截线右上部分与平行线1右侧延长线形成的角
    angle2_points = calculate_angle_arc_points(intersection1,
                                              (1, 0),  # 平行线1向右
                                              transversal_dir,  # 截线向右下
                                              radius=0.4)
    label2_x, label2_y = get_angle_label_position(intersection1,
                                                 (1, 0),  # 平行线1向右
                                                 transversal_dir)  # 截线向右下
    angles_info.append((angle2_points, '∠2', 'blue', label2_x, label2_y))
    
    # ∠3: 截线左下部分与平行线1左侧延长线形成的角
    angle3_points = calculate_angle_arc_points(intersection1,
                                              (-1, 0),  # 平行线1向左
                                              transversal_dir,  # 截线向右下
                                              radius=0.4)
    label3_x, label3_y = get_angle_label_position(intersection1,
                                                 (-1, 0),  # 平行线1向左
                                                 transversal_dir)  # 截线向右下
    angles_info.append((angle3_points, '∠3', 'green', label3_x, label3_y))
    
    # ∠4: 截线右下部分与平行线1右侧延长线形成的角
    angle4_points = calculate_angle_arc_points(intersection1,
                                              (1, 0),  # 平行线1向右
                                              (-transversal_dir[0], -transversal_dir[1]),  # 截线向左上
                                              radius=0.4)
    label4_x, label4_y = get_angle_label_position(intersection1,
                                                 (1, 0),  # 平行线1向右
                                                 (-transversal_dir[0], -transversal_dir[1]))  # 截线向左上
    angles_info.append((angle4_points, '∠4', 'orange', label4_x, label4_y))
    
    # 交点2处的4个角度
    # ∠5: 对应∠1的同位角
    angle5_points = calculate_angle_arc_points(intersection2,
                                              (-1, 0),  # 平行线2向左
                                              (-transversal_dir[0], -transversal_dir[1]),  # 截线向左上
                                              radius=0.4)
    label5_x, label5_y = get_angle_label_position(intersection2,
                                                 (-1, 0),  # 平行线2向左
                                                 (-transversal_dir[0], -transversal_dir[1]))  # 截线向左上
    angles_info.append((angle5_points, '∠5', 'red', label5_x, label5_y))
    
    # ∠6: 对应∠2的同位角
    angle6_points = calculate_angle_arc_points(intersection2,
                                              (1, 0),  # 平行线2向右
                                              transversal_dir,  # 截线向右下
                                              radius=0.4)
    label6_x, label6_y = get_angle_label_position(intersection2,
                                                 (1, 0),  # 平行线2向右
                                                 transversal_dir)  # 截线向右下
    angles_info.append((angle6_points, '∠6', 'blue', label6_x, label6_y))
    
    # ∠7: 对应∠3的同位角
    angle7_points = calculate_angle_arc_points(intersection2,
                                              (-1, 0),  # 平行线2向左
                                              transversal_dir,  # 截线向右下
                                              radius=0.4)
    label7_x, label7_y = get_angle_label_position(intersection2,
                                                 (-1, 0),  # 平行线2向左
                                                 transversal_dir)  # 截线向右下
    angles_info.append((angle7_points, '∠7', 'green', label7_x, label7_y))
    
    # ∠8: 对应∠4的同位角
    angle8_points = calculate_angle_arc_points(intersection2,
                                              (1, 0),  # 平行线2向右
                                              (-transversal_dir[0], -transversal_dir[1]),  # 截线向左上
                                              radius=0.4)
    label8_x, label8_y = get_angle_label_position(intersection2,
                                                 (1, 0),  # 平行线2向右
                                                 (-transversal_dir[0], -transversal_dir[1]))  # 截线向左上
    angles_info.append((angle8_points, '∠8', 'orange', label8_x, label8_y))
    
    # 绘制角度弧线和标签
    for points, label, color, label_x, label_y in angles_info:
        if len(points) > 1:
            # 绘制弧线
            x_coords = [p[0] for p in points]
            y_coords = [p[1] for p in points]
            ax.plot(x_coords, y_coords, color=color, linewidth=2)
        
        # 添加角度标签
        ax.text(label_x, label_y, label, fontsize=12, 
               ha='center', va='center', weight='bold', color=color)
    
    # 添加图例说明角度关系
    ax.text(3.5, 5.5, '平行线3线8角关系图', fontsize=16, weight='bold', 
           ha='center', va='center')
    
    # 添加角度关系说明
    explanation = '''角度关系说明：
• 同位角：∠1与∠5，∠2与∠6，∠3与∠7，∠4与∠8（相等）
• 内错角：∠3与∠6，∠4与∠5（相等）
• 同旁内角：∠3与∠5，∠4与∠6（互补，和为180°）
• 同旁外角：∠1与∠7，∠2与∠8（互补，和为180°）'''
    
    ax.text(6, 5.2, explanation, fontsize=10, ha='left', va='top',
           bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    # 添加交点标签
    ax.text(intersection1[0], intersection1[1] + 0.3, 'A', fontsize=12, 
           ha='center', va='bottom', weight='bold')
    ax.text(intersection2[0], intersection2[1] - 0.3, 'B', fontsize=12, 
           ha='center', va='top', weight='bold')
    
    plt.title('平行线3线8角几何图形（修正版）', fontsize=14, pad=20)
    plt.tight_layout()
    
    # 保存图像
    plt.savefig('parallel_lines_8_angles_corrected.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    return fig, ax

def demonstrate_angle_relationships():
    """演示角度关系"""
    print("平行线3线8角的角度关系：")
    print("=" * 50)
    print("1. 同位角（对应位置相等的角）：")
    print("   • ∠1 = ∠5")
    print("   • ∠2 = ∠6") 
    print("   • ∠3 = ∠7")
    print("   • ∠4 = ∠8")
    print()
    print("2. 内错角（内部交错相等的角）：")
    print("   • ∠3 = ∠6")
    print("   • ∠4 = ∠5")
    print()
    print("3. 同旁内角（同一侧内部互补的角）：")
    print("   • ∠3 + ∠5 = 180°")
    print("   • ∠4 + ∠6 = 180°")
    print()
    print("4. 同旁外角（同一侧外部互补的角）：")
    print("   • ∠1 + ∠7 = 180°")
    print("   • ∠2 + ∠8 = 180°")

if __name__ == "__main__":
    # 演示角度关系
    demonstrate_angle_relationships()
    
    # 绘制图形
    print("\n正在生成平行线3线8角图形...")
    fig, ax = draw_parallel_lines_8_angles()
    print("图形已生成并保存为 'parallel_lines_8_angles.png'")
    print("图形展示了平行线被截线所截形成的8个角度及其关系。")