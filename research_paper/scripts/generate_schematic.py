#!/usr/bin/env python3
"""
Generate Circuit Schematic for Custom Ultrasonic Sensor
Using matplotlib for professional-looking schematic
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle, Circle, FancyBboxPatch, Arc, Polygon
from matplotlib.lines import Line2D
import numpy as np

def draw_resistor(ax, x, y, width=0.8, height=0.2, label='', value='', vertical=False):
    """Draw a resistor symbol"""
    if vertical:
        # Vertical resistor
        points = []
        num_zigs = 6
        for i in range(num_zigs + 1):
            px = x + (0.15 if i % 2 == 1 else -0.15 if i % 2 == 0 and i > 0 else 0)
            py = y + (i / num_zigs) * height
            points.append([px, py])
        points = np.array(points)
        ax.plot(points[:, 0], points[:, 1], 'k-', linewidth=1.5)
        if label:
            ax.text(x + 0.25, y + height/2, f'{label}\n{value}', fontsize=6, va='center')
    else:
        # Horizontal resistor
        points = []
        num_zigs = 6
        for i in range(num_zigs + 1):
            px = x + (i / num_zigs) * width
            py = y + (0.1 if i % 2 == 1 else -0.1 if i % 2 == 0 and i > 0 else 0)
            points.append([px, py])
        points = np.array(points)
        ax.plot(points[:, 0], points[:, 1], 'k-', linewidth=1.5)
        if label:
            ax.text(x + width/2, y + 0.25, f'{label}\n{value}', fontsize=6, ha='center')

def draw_capacitor(ax, x, y, label='', value='', vertical=False):
    """Draw a capacitor symbol"""
    if vertical:
        ax.plot([x-0.15, x+0.15], [y, y], 'k-', linewidth=2)
        ax.plot([x-0.15, x+0.15], [y+0.1, y+0.1], 'k-', linewidth=2)
        if label:
            ax.text(x + 0.25, y + 0.05, f'{label}\n{value}', fontsize=6, va='center')
    else:
        ax.plot([x, x], [y-0.15, y+0.15], 'k-', linewidth=2)
        ax.plot([x+0.1, x+0.1], [y-0.15, y+0.15], 'k-', linewidth=2)
        if label:
            ax.text(x + 0.05, y + 0.3, f'{label}\n{value}', fontsize=6, ha='center')

def draw_transistor_nmos(ax, x, y, label=''):
    """Draw N-channel MOSFET"""
    # Gate
    ax.plot([x-0.3, x], [y, y], 'k-', linewidth=1.5)
    ax.plot([x, x], [y-0.2, y+0.2], 'k-', linewidth=2)
    # Channel
    ax.plot([x+0.1, x+0.1], [y-0.25, y+0.25], 'k-', linewidth=1.5)
    # Source and Drain
    ax.plot([x+0.1, x+0.3], [y-0.2, y-0.2], 'k-', linewidth=1.5)
    ax.plot([x+0.1, x+0.3], [y+0.2, y+0.2], 'k-', linewidth=1.5)
    ax.plot([x+0.3, x+0.3], [y-0.2, y-0.35], 'k-', linewidth=1.5)
    ax.plot([x+0.3, x+0.3], [y+0.2, y+0.35], 'k-', linewidth=1.5)
    # Arrow
    ax.annotate('', xy=(x+0.2, y), xytext=(x+0.1, y),
                arrowprops=dict(arrowstyle='->', color='black', lw=1))
    if label:
        ax.text(x+0.4, y, label, fontsize=6, va='center')

def draw_opamp(ax, x, y, label=''):
    """Draw op-amp triangle"""
    triangle = Polygon([(x, y-0.4), (x, y+0.4), (x+0.6, y)], 
                       fill=False, edgecolor='black', linewidth=1.5)
    ax.add_patch(triangle)
    ax.text(x+0.1, y+0.15, '+', fontsize=8)
    ax.text(x+0.1, y-0.15, '-', fontsize=8)
    if label:
        ax.text(x+0.3, y-0.5, label, fontsize=6, ha='center')

def draw_transducer(ax, x, y, label='TX'):
    """Draw ultrasonic transducer symbol"""
    # Main circle
    circle = Circle((x, y), 0.35, fill=False, edgecolor='black', linewidth=2)
    ax.add_patch(circle)
    # Inner element
    inner = Circle((x, y), 0.2, fill=True, facecolor='lightgray', edgecolor='black', linewidth=1)
    ax.add_patch(inner)
    # Sound waves
    for i in range(3):
        arc = Arc((x + 0.5 + i*0.15, y), 0.2, 0.4, angle=0, theta1=60, theta2=300, 
                 linewidth=1, color='blue')
        ax.add_patch(arc)
    ax.text(x, y, label, fontsize=8, ha='center', va='center', fontweight='bold')

def draw_ic_package(ax, x, y, width, height, label, pins_left, pins_right):
    """Draw IC package with pins"""
    rect = FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.02",
                          facecolor='lightgray', edgecolor='black', linewidth=1.5)
    ax.add_patch(rect)
    ax.text(x + width/2, y + height/2, label, fontsize=8, ha='center', va='center', fontweight='bold')
    
    # Left pins
    pin_spacing = height / (len(pins_left) + 1)
    for i, pin in enumerate(pins_left):
        py = y + height - (i + 1) * pin_spacing
        ax.plot([x-0.2, x], [py, py], 'k-', linewidth=1.5)
        ax.text(x-0.25, py, pin, fontsize=5, ha='right', va='center')
    
    # Right pins
    pin_spacing = height / (len(pins_right) + 1)
    for i, pin in enumerate(pins_right):
        py = y + height - (i + 1) * pin_spacing
        ax.plot([x+width, x+width+0.2], [py, py], 'k-', linewidth=1.5)
        ax.text(x+width+0.25, py, pin, fontsize=5, ha='left', va='center')

def create_schematic():
    fig, ax = plt.subplots(1, 1, figsize=(16, 12))
    ax.set_xlim(-1, 16)
    ax.set_ylim(-1, 12)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Title
    ax.text(7.5, 11.5, 'Custom Ultrasonic Sensor - Complete Circuit Schematic', 
            fontsize=14, fontweight='bold', ha='center')
    ax.text(7.5, 11, 'Designed for ESP32-S3 (3.3V Logic) with 5V Sensor Operation', 
            fontsize=10, ha='center', style='italic')
    
    # =====================================================
    # SECTION 1: ULTRASONIC TRANSDUCERS (Left side)
    # =====================================================
    ax.text(1, 10, 'ULTRASONIC TRANSDUCERS', fontsize=9, fontweight='bold', 
            bbox=dict(boxstyle='round', facecolor='lightblue'))
    
    # TX Transducer
    draw_transducer(ax, 1, 8.5, 'TX')
    ax.text(1, 7.9, '40kHz', fontsize=6, ha='center')
    
    # RX Transducer  
    draw_transducer(ax, 1, 6, 'RX')
    ax.text(1, 5.4, '40kHz', fontsize=6, ha='center')
    
    # =====================================================
    # SECTION 2: TX DRIVER CIRCUIT
    # =====================================================
    ax.text(3.5, 10, 'TX DRIVER (TC4427)', fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='lightyellow'))
    
    # TC4427 Driver IC
    draw_ic_package(ax, 3.5, 7.8, 1.5, 1.4, 'TC4427', 
                   ['IN_A', 'GND', 'IN_B', 'VDD'], 
                   ['OUT_A', 'NC', 'OUT_B', 'NC'])
    
    # Connections from driver to transducer
    ax.plot([1.35, 2.5, 2.5, 3.3], [8.5, 8.5, 9.0, 9.0], 'b-', linewidth=1.5)
    ax.plot([3.3, 3.5], [9.0, 9.0], 'b-', linewidth=1.5)
    ax.plot([5, 5.5, 5.5], [9.0, 9.0, 8.5], 'b-', linewidth=1.5)
    ax.plot([5, 5.5, 5.5], [8.4, 8.4, 8.5], 'b-', linewidth=1.5)
    
    # Coupling capacitors
    draw_capacitor(ax, 2.5, 8.2, 'C1', '100nF')
    
    # =====================================================
    # SECTION 3: RX AMPLIFIER CIRCUIT
    # =====================================================
    ax.text(3.5, 6.8, 'RX AMPLIFIER (LM324)', fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='lightgreen'))
    
    # First stage - preamp
    draw_opamp(ax, 3.5, 5.5, 'U2A')
    
    # Feedback resistor
    ax.plot([3.5, 3.5, 4.5, 4.5], [5.9, 6.3, 6.3, 5.5], 'k-', linewidth=1)
    draw_resistor(ax, 3.7, 6.3, 0.6, 0.15, 'R2', '100kΩ')
    
    # Input from RX transducer
    ax.plot([1.35, 2.5, 2.5, 3.5], [6, 6, 5.65, 5.65], 'g-', linewidth=1.5)
    
    # Coupling cap
    draw_capacitor(ax, 2.5, 5.65, 'C2', '100nF')
    
    # Bias resistor
    draw_resistor(ax, 2.8, 5.2, 0.5, 0.15, 'R1', '10kΩ')
    ax.plot([2.8, 2.8], [5.2, 5.35], 'k-', linewidth=1)
    ax.plot([2.8, 2.8], [5.05, 4.9], 'k-', linewidth=1)
    
    # Second stage - comparator
    draw_opamp(ax, 5, 5.5, 'U2B')
    ax.plot([4.1, 4.5, 4.5, 5], [5.5, 5.5, 5.65, 5.65], 'k-', linewidth=1.5)
    
    # Threshold reference
    draw_resistor(ax, 4.5, 4.8, 0.5, 0.15, 'R3', '10kΩ')
    draw_resistor(ax, 4.5, 4.4, 0.5, 0.15, 'R4', '10kΩ')
    ax.plot([5, 4.75, 4.75], [5.35, 5.35, 4.95], 'k-', linewidth=1)
    
    # =====================================================
    # SECTION 4: LEVEL SHIFTER (BSS138)
    # =====================================================
    ax.text(7, 10, 'LEVEL SHIFTER (5V↔3.3V)', fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='lightcoral'))
    
    # TRIGGER Level Shifter
    ax.text(7, 9.2, 'TRIGGER (3.3V→5V)', fontsize=7, style='italic')
    draw_transistor_nmos(ax, 7.5, 8.5, 'Q1\nBSS138')
    draw_resistor(ax, 7.2, 9, 0.15, 0.4, 'R5', '10kΩ', vertical=True)
    draw_resistor(ax, 8, 9, 0.15, 0.4, 'R6', '10kΩ', vertical=True)
    
    # ECHO Level Shifter
    ax.text(7, 7.2, 'ECHO (5V→3.3V)', fontsize=7, style='italic')
    draw_transistor_nmos(ax, 7.5, 6.5, 'Q2\nBSS138')
    draw_resistor(ax, 7.2, 7, 0.15, 0.4, 'R7', '10kΩ', vertical=True)
    draw_resistor(ax, 8, 7, 0.15, 0.4, 'R8', '10kΩ', vertical=True)
    
    # =====================================================
    # SECTION 5: POWER SUPPLY
    # =====================================================
    ax.text(1, 4, 'POWER SUPPLY', fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='orange'))
    
    # Input from solar/battery
    ax.text(0.5, 3.3, 'VIN\n7-12V', fontsize=7, ha='center', 
            bbox=dict(boxstyle='round', facecolor='yellow'))
    
    # 5V Regulator
    draw_ic_package(ax, 2, 2.5, 1.2, 1, 'LM7805', 
                   ['VIN', 'GND'], ['VOUT'])
    
    # Input capacitor
    draw_capacitor(ax, 1.3, 2.8, 'C3', '100µF', vertical=True)
    
    # Output capacitor
    draw_capacitor(ax, 3.8, 2.8, 'C4', '100µF', vertical=True)
    
    # 3.3V Regulator
    draw_ic_package(ax, 5, 2.5, 1.2, 1, 'AMS1117\n3.3V', 
                   ['VIN', 'GND'], ['VOUT'])
    
    # Output capacitor
    draw_capacitor(ax, 6.8, 2.8, 'C5', '10µF', vertical=True)
    
    # Power rails
    ax.plot([0.8, 2], [3, 3], 'r-', linewidth=2)
    ax.plot([3.2, 5], [3, 3], 'r-', linewidth=2)
    ax.plot([6.2, 7], [3, 3], 'orange', linewidth=2)
    
    ax.text(3.5, 3.3, '5V Rail', fontsize=7, ha='center', color='red', fontweight='bold')
    ax.text(6.5, 3.3, '3.3V Rail', fontsize=7, ha='center', color='orange', fontweight='bold')
    
    # Ground symbols
    for gx in [1.3, 2.6, 3.8, 5.6, 6.8]:
        ax.plot([gx, gx], [2.3, 2.1], 'k-', linewidth=2)
        ax.plot([gx-0.1, gx+0.1], [2.1, 2.1], 'k-', linewidth=2)
        ax.plot([gx-0.07, gx+0.07], [2.0, 2.0], 'k-', linewidth=1.5)
        ax.plot([gx-0.04, gx+0.04], [1.9, 1.9], 'k-', linewidth=1)
    
    # =====================================================
    # SECTION 6: ESP32-S3 CONNECTION HEADER
    # =====================================================
    ax.text(10, 10, 'ESP32-S3 INTERFACE', fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='lightgray'))
    
    # Connection header
    header = FancyBboxPatch((10, 6), 2.5, 3.5, boxstyle="round,pad=0.05",
                            facecolor='white', edgecolor='black', linewidth=2)
    ax.add_patch(header)
    ax.text(11.25, 9.3, 'ESP32-S3', fontsize=10, ha='center', fontweight='bold')
    
    pins = ['3.3V (Power)', 'GND', 'GPIO4 (TRIG)', 'GPIO5 (ECHO)', 'GPIO6 (TEMP)']
    for i, pin in enumerate(pins):
        py = 8.8 - i * 0.5
        ax.plot([9.5, 10], [py, py], 'k-', linewidth=1.5)
        circle = Circle((9.4, py), 0.08, fill=True, facecolor='gold', edgecolor='black')
        ax.add_patch(circle)
        ax.text(10.2, py, pin, fontsize=7, va='center')
    
    # =====================================================
    # SECTION 7: TEMPERATURE SENSOR
    # =====================================================
    ax.text(10, 5.5, 'TEMP SENSOR', fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='cyan'))
    
    draw_ic_package(ax, 10.5, 4, 1, 0.8, 'DS18B20', 
                   ['GND', 'DQ'], ['VDD'])
    
    # Pull-up resistor
    draw_resistor(ax, 11, 5, 0.15, 0.4, 'R9', '4.7kΩ', vertical=True)
    
    # =====================================================
    # CONNECTION LINES
    # =====================================================
    # Level shifter to ESP32
    ax.plot([8.3, 9.5], [8.5, 7.8], 'b-', linewidth=1.5)  # TRIG
    ax.plot([8.3, 9.5], [6.5, 7.3], 'g-', linewidth=1.5)  # ECHO
    
    # RX amp output to level shifter
    ax.plot([5.6, 6.5, 6.5, 7.2], [5.5, 5.5, 6.5, 6.5], 'g-', linewidth=1.5)
    
    # Level shifter to TX driver
    ax.plot([7.2, 6.5, 6.5, 5.5, 5.5, 5], [8.5, 8.5, 8.5, 8.5, 8.5, 8.7], 'b-', linewidth=1.5)
    
    # Power connections
    ax.plot([7, 7, 7.2], [3, 7.4, 7.4], 'orange', linewidth=1.5, linestyle='--')
    ax.plot([3.5, 3.5, 3.5], [3.3, 4.5, 7.8], 'r-', linewidth=1.5, linestyle='--')
    
    # =====================================================
    # NOTES
    # =====================================================
    notes_text = """Design Notes:
• Operating voltage: 5V (sensor), 3.3V (ESP32)
• BSS138 MOSFETs for bidirectional level shifting
• TC4427 provides high-current drive for TX transducer
• LM324 quad op-amp: 2 stages for RX amplification
• DS18B20 for temperature compensation
• All power rails filtered with bypass capacitors"""
    
    ax.text(11, 2.5, notes_text, fontsize=7, va='top',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
    
    # Revision info
    ax.text(14.5, 0.5, 'Rev: 1.0\nDate: 2025', fontsize=6, ha='center')
    
    plt.tight_layout()
    plt.savefig('/workspaces/ultraman/research_paper/images/circuit_schematic.png', dpi=300, 
                bbox_inches='tight', facecolor='white')
    plt.savefig('/workspaces/ultraman/research_paper/images/circuit_schematic.pdf', 
                bbox_inches='tight', facecolor='white')
    print("Circuit schematic saved!")

if __name__ == "__main__":
    create_schematic()
