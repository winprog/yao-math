# -*- coding: utf-8 -*-
"""
圆周角定理演示程序
同一个圆弧，对着它的所有圆周角相等
角添加圆心角标注
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib import font_manager
import matplotlib.patches as mpatches

# 设置中文字体 - 使用微软雅黑
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def draw_circumferential_angles():
    """绘制圆周角定理演示图"""
    
    # 创建图形和坐标轴
    fig, ax = plt.subplots(1, 1, figsize=(12, 10))
    
    # 设置坐标轴范围
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    
    # 隐藏坐标轴
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.set_title('圆周角与圆心角定理演示', 
                 fontsize=16, fontweight='bold', pad=20)
    
    # 绘制圆
    circle = plt.Circle((0, 0), 1, fill=False, color='black', linewidth=2)
    ax.add_patch(circle)
    
    # 定义圆弧的端点（A和B）
    theta_A = np.radians(30)   # A点角度
    theta_B = np.radians(150)  # B点角度
    
    A = (np.cos(theta_A), np.sin(theta_A))
    B = (np.cos(theta_B), np.sin(theta_B))
    
    # 在圆上选择三个不同的点作为圆周角的顶点（位于劣弧AB上）
    # 劣弧AB对应的角度范围是150°到30°（经过360°）
    theta_points = [180, 210, 240]  # 三个不同的角度（位于劣弧上）
    points = []
    
    for theta in theta_points:
        theta_rad = np.radians(theta)
        point = (np.cos(theta_rad), np.sin(theta_rad))
        points.append(point)
    
    # 绘制圆弧AB
    arc_angle = theta_B - theta_A
    arc = patches.Arc((0, 0), 2, 2, angle=0, 
                     theta1=np.degrees(theta_A), theta2=np.degrees(theta_B),
                     color='red', linewidth=3)
    ax.add_patch(arc)
    
    # 绘制点A和B
    ax.plot(A[0], A[1], 'ro', markersize=8, label='点A')
    ax.plot(B[0], B[1], 'ro', markersize=8, label='点B')
    ax.text(A[0]+0.05, A[1]+0.05, 'A', fontsize=14, fontweight='bold')
    ax.text(B[0]+0.05, B[1]+0.05, 'B', fontsize=14, fontweight='bold')
    
    # 绘制圆心角（顶点在圆心O）
    O = (0, 0)  # 圆心
    
    # 绘制圆心角的两边（OA和OB）
    ax.plot([O[0], A[0]], [O[1], A[1]], color='purple', linewidth=3)
    ax.plot([O[0], B[0]], [O[1], B[1]], color='purple', linewidth=3)
    
    # 计算圆心角度数
    central_angle = np.degrees(theta_B - theta_A)
    if central_angle < 0:
        central_angle += 360
    
    # 绘制圆心角弧线
    central_arc = patches.Arc(O, 0.4, 0.4, angle=0, 
                             theta1=np.degrees(theta_A), theta2=np.degrees(theta_B),
                             color='purple', linewidth=3)
    ax.add_patch(central_arc)
    
    # 标注圆心角度数
    mid_central_angle = (theta_A + theta_B) / 2
    text_x_central = 0.5 * np.cos(mid_central_angle)
    text_y_central = 0.5 * np.sin(mid_central_angle)
    ax.text(text_x_central, text_y_central, f'{central_angle:.1f}°', fontsize=12, 
            color='purple', fontweight='bold', ha='center', va='center')
    
    # 标注圆心O
    ax.plot(O[0], O[1], 'o', color='purple', markersize=8)
    ax.text(O[0]-0.1, O[1]-0.1, 'O', fontsize=14, fontweight='bold', color='purple')
    
    # 绘制三个圆周角
    colors = ['blue', 'green', 'orange']
    angle_values = []
    
    for i, point in enumerate(points):
        color = colors[i]
        
        # 绘制顶点
        ax.plot(point[0], point[1], 'o', color=color, markersize=8)
        ax.text(point[0]+0.05, point[1]+0.05, f'P{i+1}', fontsize=12, fontweight='bold')
        
        # 绘制角的两边
        ax.plot([point[0], A[0]], [point[1], A[1]], color=color, linewidth=2, linestyle='--')
        ax.plot([point[0], B[0]], [point[1], B[1]], color=color, linewidth=2, linestyle='--')
        
        # 计算并标注角度
        angle = calculate_angle(A, point, B)
        angle_values.append(angle)
        
        # 绘制角度弧线（确保画在角内）
        angle1 = np.arctan2(A[1]-point[1], A[0]-point[0])
        angle2 = np.arctan2(B[1]-point[1], B[0]-point[0])
        
        # 确保角度按逆时针方向排列
        if angle2 < angle1:
            angle1, angle2 = angle2, angle1
        
        # 如果角度差大于180度，交换方向
        if angle2 - angle1 > np.pi:
            angle1, angle2 = angle2, angle1 + 2*np.pi
        
        angle_arc = patches.Arc(point, 0.3, 0.3, angle=0, 
                               theta1=np.degrees(angle1), theta2=np.degrees(angle2),
                               color=color, linewidth=2)
        ax.add_patch(angle_arc)
        
        # 标注角度值
        mid_angle = (np.arctan2(A[1]-point[1], A[0]-point[0]) + 
                    np.arctan2(B[1]-point[1], B[0]-point[0])) / 2
        text_x = point[0] + 0.35 * np.cos(mid_angle)
        text_y = point[1] + 0.35 * np.sin(mid_angle)
        ax.text(text_x, text_y, f'{angle:.1f}°', fontsize=10, 
                color=color, fontweight='bold', ha='center', va='center')
    
    # 添加说明文本
    explanation = (
        '圆周角与圆心角定理：\n'
        '• 同一个圆弧AB所对的圆周角相等\n'
        '• ∠AP1B = ∠AP2B = ∠AP3B\n'
        f'• 所有圆周角都等于 {angle_values[0]:.1f}°\n'
        f'• 圆心角 ∠AOB = {central_angle:.1f}°\n'
        f'• 圆心角 = 2 × 圆周角 ({central_angle:.1f}° = 2 × {angle_values[0]:.1f}°)'
    )
    
    ax.text(-1.4, -1.3, explanation, fontsize=12, 
            bbox=dict(boxstyle="round,pad=0.5", facecolor="lightblue", alpha=0.7))
    
    # 添加图例
    legend_elements = [
        mpatches.Patch(color='red', label='圆弧AB'),
        mpatches.Patch(color='purple', label='圆心角 ∠AOB'),
        mpatches.Patch(color='blue', label='圆周角 ∠AP1B'),
        mpatches.Patch(color='green', label='圆周角 ∠AP2B'),
        mpatches.Patch(color='orange', label='圆周角 ∠AP3B')
    ]
    ax.legend(handles=legend_elements, loc='upper right', fontsize=10)
    
    # 添加数学公式说明
    formula_text1 = r'$\angle AP_1B = \angle AP_2B = \angle AP_3B$'
    formula_text2 = r'$\angle AOB = 2 \times \angle AP_1B$'
    ax.text(0.5, -1.3, formula_text1, fontsize=14, 
            bbox=dict(boxstyle="round,pad=0.5", facecolor="lightyellow", alpha=0.7))
    ax.text(0.5, -1.1, formula_text2, fontsize=14, 
            bbox=dict(boxstyle="round,pad=0.5", facecolor="lightyellow", alpha=0.7))
    
    plt.tight_layout()
    return fig, ax

def calculate_angle(A, P, B):
    """计算三点形成的圆周角（确保角度小于180度）"""
    # 向量PA和PB
    PA = np.array(A) - np.array(P)
    PB = np.array(B) - np.array(P)
    
    # 计算夹角（弧度）
    dot_product = np.dot(PA, PB)
    norm_PA = np.linalg.norm(PA)
    norm_PB = np.linalg.norm(PB)
    
    cos_angle = dot_product / (norm_PA * norm_PB)
    angle_rad = np.arccos(np.clip(cos_angle, -1, 1))
    
    # 转换为角度
    angle_deg = np.degrees(angle_rad)
    
    # 确保圆周角小于180度（取劣弧所对的角）
    if angle_deg > 180:
        angle_deg = 360 - angle_deg
    
    return angle_deg

def main():
    """主函数"""
    print("正在生成圆周角定理演示图...")
    
    # 检查字体是否可用
    available_fonts = [f.name for f in font_manager.fontManager.ttflist]
    print("可用的中文字体:")
    chinese_fonts = [f for f in available_fonts if any(char in f for char in ['YaHei', 'Hei', 'Sim', 'Kai', 'Song'])]
    for font in chinese_fonts[:5]:  # 只显示前5个
        print(f"  - {font}")
    
    # 生成图形
    fig, ax = draw_circumferential_angles()
    
    # 保存图片
    plt.savefig('circumferential_angles.png', dpi=300, bbox_inches='tight')
    print("图片已保存为 'circumferential_angles.png'")
    
    # 显示图形
    plt.show()
    
    print("\n圆周角定理说明：")
    print("• 同一个圆弧所对的所有圆周角都相等")
    print("• 这是圆的基本性质之一")
    print("• 在图中，虽然点P₁、P₂、P₃的位置不同")
    print("  但它们对圆弧AB所张的圆周角都相等")

if __name__ == "__main__":
    main()