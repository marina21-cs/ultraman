#!/usr/bin/env python3
"""
Generate PCB Layout for Custom Ultrasonic Sensor
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle, Circle, FancyBboxPatch, Polygon, Arc
import numpy as np

def create_pcb_layout():
    fig, axes = plt.subplots(1, 2, figsize=(16, 10))
    
    # =====================================================
    # TOP LAYER (Component Placement)
    # =====================================================
    ax1 = axes[0]
    ax1.set_xlim(-1, 11)
    ax1.set_ylim(-1, 11)
    ax1.set_aspect('equal')
    ax1.set_facecolor('#1a472a')  # Dark green PCB color
    ax1.set_title('PCB Top Layer - Component Placement', fontsize=12, fontweight='bold', pad=10)
    
    # PCB outline
    pcb_outline = Rectangle((0, 0), 10, 10, fill=False, edgecolor='white', linewidth=3)
    ax1.add_patch(pcb_outline)
    
    # Mounting holes
    for mx, my in [(0.5, 0.5), (9.5, 0.5), (0.5, 9.5), (9.5, 9.5)]:
        hole = Circle((mx, my), 0.2, fill=True, facecolor='#1a472a', edgecolor='gold', linewidth=2)
        ax1.add_patch(hole)
        pad = Circle((mx, my), 0.35, fill=False, edgecolor='gold', linewidth=2)
        ax1.add_patch(pad)
    
    # ===== ULTRASONIC TRANSDUCERS =====
    # TX Transducer (top left)
    tx = Circle((2, 8), 0.8, fill=True, facecolor='silver', edgecolor='black', linewidth=2)
    ax1.add_patch(tx)
    tx_inner = Circle((2, 8), 0.5, fill=True, facecolor='gray', edgecolor='black', linewidth=1)
    ax1.add_patch(tx_inner)
    ax1.text(2, 8, 'TX', fontsize=8, ha='center', va='center', fontweight='bold', color='white')
    ax1.text(2, 7, '40kHz', fontsize=6, ha='center')
    
    # RX Transducer
    rx = Circle((4, 8), 0.8, fill=True, facecolor='silver', edgecolor='black', linewidth=2)
    ax1.add_patch(rx)
    rx_inner = Circle((4, 8), 0.5, fill=True, facecolor='gray', edgecolor='black', linewidth=1)
    ax1.add_patch(rx_inner)
    ax1.text(4, 8, 'RX', fontsize=8, ha='center', va='center', fontweight='bold', color='white')
    ax1.text(4, 7, '40kHz', fontsize=6, ha='center')
    
    # ===== TC4427 DRIVER IC =====
    ic1 = FancyBboxPatch((1.2, 5.5), 1.6, 0.8, boxstyle="round,pad=0.02",
                         facecolor='black', edgecolor='white', linewidth=1)
    ax1.add_patch(ic1)
    ax1.text(2, 5.9, 'TC4427', fontsize=7, ha='center', va='center', color='white', fontweight='bold')
    # Pins
    for i in range(4):
        pin_l = Rectangle((1.0, 5.55 + i*0.18), 0.2, 0.12, facecolor='silver', edgecolor='gray')
        pin_r = Rectangle((2.8, 5.55 + i*0.18), 0.2, 0.12, facecolor='silver', edgecolor='gray')
        ax1.add_patch(pin_l)
        ax1.add_patch(pin_r)
    ax1.text(2, 5.2, 'U1', fontsize=6, ha='center', color='yellow')
    
    # ===== LM324 OP-AMP =====
    ic2 = FancyBboxPatch((3.5, 5.3), 2, 1.2, boxstyle="round,pad=0.02",
                         facecolor='black', edgecolor='white', linewidth=1)
    ax1.add_patch(ic2)
    ax1.text(4.5, 5.9, 'LM324', fontsize=7, ha='center', va='center', color='white', fontweight='bold')
    # Pins (DIP-14)
    for i in range(7):
        pin_l = Rectangle((3.3, 5.35 + i*0.15), 0.2, 0.1, facecolor='silver', edgecolor='gray')
        pin_r = Rectangle((5.5, 5.35 + i*0.15), 0.2, 0.1, facecolor='silver', edgecolor='gray')
        ax1.add_patch(pin_l)
        ax1.add_patch(pin_r)
    ax1.text(4.5, 5, 'U2', fontsize=6, ha='center', color='yellow')
    
    # ===== BSS138 MOSFETS (Level Shifters) =====
    # Q1
    q1 = FancyBboxPatch((6.5, 6.5), 0.6, 0.6, boxstyle="round,pad=0.02",
                        facecolor='black', edgecolor='white', linewidth=1)
    ax1.add_patch(q1)
    ax1.text(6.8, 6.8, 'Q1', fontsize=6, ha='center', va='center', color='white')
    for i in range(3):
        pin = Rectangle((6.55 + i*0.18, 6.35), 0.1, 0.15, facecolor='silver')
        ax1.add_patch(pin)
    ax1.text(6.8, 6.2, 'BSS138', fontsize=5, ha='center', color='yellow')
    
    # Q2
    q2 = FancyBboxPatch((6.5, 5.2), 0.6, 0.6, boxstyle="round,pad=0.02",
                        facecolor='black', edgecolor='white', linewidth=1)
    ax1.add_patch(q2)
    ax1.text(6.8, 5.5, 'Q2', fontsize=6, ha='center', va='center', color='white')
    for i in range(3):
        pin = Rectangle((6.55 + i*0.18, 5.05), 0.1, 0.15, facecolor='silver')
        ax1.add_patch(pin)
    ax1.text(6.8, 4.9, 'BSS138', fontsize=5, ha='center', color='yellow')
    
    # ===== VOLTAGE REGULATORS =====
    # LM7805
    vreg1 = FancyBboxPatch((1.5, 2.5), 1.2, 0.8, boxstyle="round,pad=0.02",
                           facecolor='black', edgecolor='white', linewidth=1)
    ax1.add_patch(vreg1)
    ax1.text(2.1, 2.9, 'LM7805', fontsize=6, ha='center', va='center', color='white', fontweight='bold')
    # Heat sink representation
    for i in range(3):
        pin = Rectangle((1.65 + i*0.3, 2.3), 0.15, 0.2, facecolor='silver')
        ax1.add_patch(pin)
    ax1.text(2.1, 2.1, 'U3', fontsize=6, ha='center', color='yellow')
    
    # AMS1117-3.3
    vreg2 = FancyBboxPatch((3.5, 2.5), 1, 0.7, boxstyle="round,pad=0.02",
                           facecolor='black', edgecolor='white', linewidth=1)
    ax1.add_patch(vreg2)
    ax1.text(4, 2.85, 'AMS1117', fontsize=5, ha='center', va='center', color='white')
    ax1.text(4, 2.65, '3.3V', fontsize=5, ha='center', va='center', color='white')
    for i in range(3):
        pin = Rectangle((3.6 + i*0.3, 2.35), 0.12, 0.15, facecolor='silver')
        ax1.add_patch(pin)
    ax1.text(4, 2.1, 'U4', fontsize=6, ha='center', color='yellow')
    
    # ===== CAPACITORS =====
    caps = [
        (0.8, 3.2, 'C1\n100µF'),
        (2.8, 3.2, 'C2\n100µF'),
        (4.8, 3.2, 'C3\n10µF'),
        (1.5, 4.3, 'C4\n100nF'),
        (4, 4.3, 'C5\n100nF'),
    ]
    for cx, cy, label in caps:
        cap = Circle((cx, cy), 0.25, fill=True, facecolor='brown', edgecolor='black', linewidth=1)
        ax1.add_patch(cap)
        ax1.text(cx, cy + 0.4, label, fontsize=5, ha='center')
    
    # ===== RESISTORS (SMD 0805) =====
    resistors = [
        (5.5, 7.2, 'R1\n10k'),
        (5.5, 6.7, 'R2\n100k'),
        (7.5, 7.5, 'R3\n10k'),
        (7.5, 7, 'R4\n10k'),
        (7.5, 6.2, 'R5\n10k'),
        (7.5, 5.7, 'R6\n10k'),
        (6, 4, 'R7\n4.7k'),
    ]
    for rx, ry, label in resistors:
        res = Rectangle((rx-0.2, ry-0.08), 0.4, 0.16, facecolor='beige', edgecolor='black', linewidth=1)
        ax1.add_patch(res)
        ax1.text(rx + 0.35, ry, label, fontsize=4, va='center')
    
    # ===== DS18B20 TEMPERATURE SENSOR =====
    temp = FancyBboxPatch((5.5, 3.5), 0.8, 0.6, boxstyle="round,pad=0.02",
                          facecolor='black', edgecolor='white', linewidth=1)
    ax1.add_patch(temp)
    ax1.text(5.9, 3.8, 'DS18B20', fontsize=5, ha='center', va='center', color='white')
    for i in range(3):
        pin = Rectangle((5.6 + i*0.2, 3.35), 0.1, 0.15, facecolor='silver')
        ax1.add_patch(pin)
    ax1.text(5.9, 3.2, 'U5', fontsize=5, ha='center', color='yellow')
    
    # ===== CONNECTOR HEADER =====
    # ESP32 Interface Header (6-pin)
    header = FancyBboxPatch((8, 5), 1.5, 2, boxstyle="round,pad=0.02",
                            facecolor='black', edgecolor='white', linewidth=2)
    ax1.add_patch(header)
    ax1.text(8.75, 6.8, 'ESP32', fontsize=6, ha='center', color='white', fontweight='bold')
    ax1.text(8.75, 6.5, 'Header', fontsize=6, ha='center', color='white')
    
    pins_labels = ['3.3V', 'GND', 'TRIG', 'ECHO', 'TEMP']
    for i, label in enumerate(pins_labels):
        pin_hole = Circle((8.4, 6.1 - i*0.3), 0.08, fill=True, facecolor='gold', edgecolor='black')
        ax1.add_patch(pin_hole)
        ax1.text(8.55, 6.1 - i*0.3, label, fontsize=5, va='center', color='white')
    
    # Power input connector
    pwr = FancyBboxPatch((8.2, 2.5), 1.2, 0.8, boxstyle="round,pad=0.02",
                         facecolor='green', edgecolor='white', linewidth=2)
    ax1.add_patch(pwr)
    ax1.text(8.8, 2.9, 'PWR IN', fontsize=6, ha='center', va='center', color='white', fontweight='bold')
    ax1.text(8.8, 2.6, '7-12V', fontsize=5, ha='center', color='white')
    
    # ===== SILKSCREEN LABELS =====
    ax1.text(5, 9.5, 'CUSTOM ULTRASONIC SENSOR v1.0', fontsize=8, ha='center', 
             color='white', fontweight='bold')
    ax1.text(5, 0.3, 'Bulacan State University - 2025', fontsize=6, ha='center', color='white')
    
    # Polarity markers
    ax1.text(0.7, 3.5, '+', fontsize=10, ha='center', color='red', fontweight='bold')
    ax1.text(2.7, 3.5, '+', fontsize=10, ha='center', color='red', fontweight='bold')
    
    # =====================================================
    # BOTTOM LAYER (Traces)
    # =====================================================
    ax2 = axes[1]
    ax2.set_xlim(-1, 11)
    ax2.set_ylim(-1, 11)
    ax2.set_aspect('equal')
    ax2.set_facecolor('#1a472a')
    ax2.set_title('PCB Bottom Layer - Copper Traces', fontsize=12, fontweight='bold', pad=10)
    
    # PCB outline
    pcb_outline2 = Rectangle((0, 0), 10, 10, fill=False, edgecolor='white', linewidth=3)
    ax2.add_patch(pcb_outline2)
    
    # Mounting holes
    for mx, my in [(0.5, 0.5), (9.5, 0.5), (0.5, 9.5), (9.5, 9.5)]:
        hole = Circle((mx, my), 0.2, fill=True, facecolor='#1a472a', edgecolor='gold', linewidth=2)
        ax2.add_patch(hole)
    
    # ===== GROUND PLANE =====
    ground_plane = Rectangle((0.3, 0.3), 9.4, 1.5, fill=True, facecolor='#8B4513', 
                             edgecolor='#B87333', linewidth=0, alpha=0.5)
    ax2.add_patch(ground_plane)
    ax2.text(5, 1, 'GROUND PLANE', fontsize=8, ha='center', color='white', fontweight='bold')
    
    # ===== 5V POWER RAIL =====
    # Main 5V trace
    ax2.plot([1.5, 1.5, 7.5], [2.5, 4, 4], color='red', linewidth=4, solid_capstyle='round')
    ax2.plot([1.5, 1.5], [4, 6], color='red', linewidth=4, solid_capstyle='round')
    ax2.text(0.8, 5, '5V', fontsize=7, color='red', fontweight='bold')
    
    # ===== 3.3V POWER RAIL =====
    ax2.plot([4, 4, 8.5], [2.5, 3.5, 3.5], color='orange', linewidth=3, solid_capstyle='round')
    ax2.plot([8.5, 8.5], [3.5, 5.5], color='orange', linewidth=3, solid_capstyle='round')
    ax2.text(4.3, 3.2, '3.3V', fontsize=6, color='orange', fontweight='bold')
    
    # ===== SIGNAL TRACES =====
    # TX signal path (from ESP32 header through level shifter to driver)
    ax2.plot([8.4, 7.5, 7.5, 6.8], [5.8, 5.8, 6.8, 6.8], color='blue', linewidth=2)
    ax2.plot([6.5, 5, 3, 2], [6.8, 6.8, 6.8, 6.3], color='blue', linewidth=2)
    ax2.text(5, 7.1, 'TRIG', fontsize=5, color='cyan')
    
    # RX signal path (from RX amp through level shifter to ESP32)
    ax2.plot([4, 5.5, 6.5], [6, 6, 5.5], color='green', linewidth=2)
    ax2.plot([7.1, 8.4], [5.5, 5.5], color='green', linewidth=2)
    ax2.text(5.5, 6.3, 'ECHO', fontsize=5, color='lime')
    
    # TX transducer connection
    ax2.plot([2, 2], [7.2, 6.3], color='blue', linewidth=2)
    
    # RX transducer connection  
    ax2.plot([4, 4], [7.2, 6.5], color='green', linewidth=2)
    
    # Temperature sensor data line
    ax2.plot([5.9, 5.9, 8.4], [4.1, 4.8, 4.8], color='purple', linewidth=2)
    ax2.text(7, 5, 'TEMP', fontsize=5, color='violet')
    
    # ===== VIAS =====
    vias = [(2, 6.5), (4, 6.5), (1.5, 4), (4, 3.5), (6.8, 6.8), (6.8, 5.5), (5.9, 4.1)]
    for vx, vy in vias:
        via = Circle((vx, vy), 0.1, fill=True, facecolor='gold', edgecolor='black', linewidth=1)
        ax2.add_patch(via)
    
    # ===== COMPONENT OUTLINES (for reference) =====
    # Transducers
    for tx_x in [2, 4]:
        outline = Circle((tx_x, 8), 0.8, fill=False, edgecolor='white', linewidth=1, linestyle='--')
        ax2.add_patch(outline)
    
    # ICs
    for ic_outline in [(1.2, 5.5, 1.6, 0.8), (3.5, 5.3, 2, 1.2), (1.5, 2.5, 1.2, 0.8), (3.5, 2.5, 1, 0.7)]:
        rect = Rectangle((ic_outline[0], ic_outline[1]), ic_outline[2], ic_outline[3],
                         fill=False, edgecolor='white', linewidth=1, linestyle='--')
        ax2.add_patch(rect)
    
    # ===== LEGEND =====
    ax2.text(9.5, 9, 'Legend:', fontsize=7, color='white', fontweight='bold')
    ax2.plot([8.5, 9], [8.5, 8.5], color='red', linewidth=3)
    ax2.text(9.1, 8.5, '5V', fontsize=6, color='white', va='center')
    ax2.plot([8.5, 9], [8.1, 8.1], color='orange', linewidth=3)
    ax2.text(9.1, 8.1, '3.3V', fontsize=6, color='white', va='center')
    ax2.plot([8.5, 9], [7.7, 7.7], color='blue', linewidth=2)
    ax2.text(9.1, 7.7, 'Signal', fontsize=6, color='white', va='center')
    via_legend = Circle((8.75, 7.3), 0.1, fill=True, facecolor='gold')
    ax2.add_patch(via_legend)
    ax2.text(9.1, 7.3, 'Via', fontsize=6, color='white', va='center')
    
    # Dimensions
    ax2.annotate('', xy=(10.3, 0), xytext=(10.3, 10),
                arrowprops=dict(arrowstyle='<->', color='white', lw=1))
    ax2.text(10.5, 5, '50mm', fontsize=7, color='white', rotation=90, va='center')
    
    ax2.annotate('', xy=(0, -0.5), xytext=(10, -0.5),
                arrowprops=dict(arrowstyle='<->', color='white', lw=1))
    ax2.text(5, -0.8, '50mm', fontsize=7, color='white', ha='center')
    
    plt.tight_layout()
    plt.savefig('/workspaces/ultraman/research_paper/images/pcb_layout.png', dpi=300, 
                bbox_inches='tight', facecolor='#2d2d2d')
    plt.savefig('/workspaces/ultraman/research_paper/images/pcb_layout.pdf', 
                bbox_inches='tight', facecolor='#2d2d2d')
    print("PCB layout saved!")

if __name__ == "__main__":
    create_pcb_layout()
