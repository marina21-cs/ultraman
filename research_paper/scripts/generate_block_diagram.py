#!/usr/bin/env python3
"""
Generate Block Diagram for Ultrasonic Sensor System
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

def create_block_diagram():
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Colors
    colors = {
        'sensor': '#3498db',
        'driver': '#e74c3c',
        'mcu': '#2ecc71',
        'power': '#f39c12',
        'interface': '#9b59b6',
        'protection': '#1abc9c'
    }
    
    # Title
    ax.text(7, 9.5, 'Custom Ultrasonic Sensor System Block Diagram', 
            fontsize=16, fontweight='bold', ha='center', va='center')
    
    # === ULTRASONIC TRANSDUCER SECTION ===
    # Transmitter
    tx_box = FancyBboxPatch((0.5, 6.5), 2.5, 1.5, boxstyle="round,pad=0.05",
                            facecolor=colors['sensor'], edgecolor='black', linewidth=2)
    ax.add_patch(tx_box)
    ax.text(1.75, 7.25, 'Ultrasonic\nTransmitter\n(40kHz)', fontsize=9, ha='center', va='center', color='white', fontweight='bold')
    
    # Receiver
    rx_box = FancyBboxPatch((0.5, 4.5), 2.5, 1.5, boxstyle="round,pad=0.05",
                            facecolor=colors['sensor'], edgecolor='black', linewidth=2)
    ax.add_patch(rx_box)
    ax.text(1.75, 5.25, 'Ultrasonic\nReceiver\n(40kHz)', fontsize=9, ha='center', va='center', color='white', fontweight='bold')
    
    # === DRIVER/AMPLIFIER SECTION ===
    # TX Driver
    tx_driver = FancyBboxPatch((4, 6.5), 2.5, 1.5, boxstyle="round,pad=0.05",
                               facecolor=colors['driver'], edgecolor='black', linewidth=2)
    ax.add_patch(tx_driver)
    ax.text(5.25, 7.25, 'TX Driver\nCircuit\n(MAX232/TC4427)', fontsize=8, ha='center', va='center', color='white', fontweight='bold')
    
    # RX Amplifier
    rx_amp = FancyBboxPatch((4, 4.5), 2.5, 1.5, boxstyle="round,pad=0.05",
                            facecolor=colors['driver'], edgecolor='black', linewidth=2)
    ax.add_patch(rx_amp)
    ax.text(5.25, 5.25, 'RX Amplifier\n+ Comparator\n(LM324/LM393)', fontsize=8, ha='center', va='center', color='white', fontweight='bold')
    
    # === LEVEL SHIFTER ===
    level_shift = FancyBboxPatch((7.5, 5.25), 2, 1.5, boxstyle="round,pad=0.05",
                                 facecolor=colors['protection'], edgecolor='black', linewidth=2)
    ax.add_patch(level_shift)
    ax.text(8.5, 6, 'Level Shifter\n3.3V ↔ 5V\n(BSS138)', fontsize=8, ha='center', va='center', color='white', fontweight='bold')
    
    # === MICROCONTROLLER ===
    mcu_box = FancyBboxPatch((10.5, 4.5), 3, 3, boxstyle="round,pad=0.05",
                             facecolor=colors['mcu'], edgecolor='black', linewidth=2)
    ax.add_patch(mcu_box)
    ax.text(12, 6, 'ESP32-S3\nMicrocontroller', fontsize=11, ha='center', va='center', color='white', fontweight='bold')
    ax.text(12, 5.2, '• GPIO Trigger\n• GPIO Echo\n• Timer/Counter\n• ADC (Temp)', fontsize=7, ha='center', va='center', color='white')
    
    # === POWER MANAGEMENT ===
    power_box = FancyBboxPatch((4, 1), 5.5, 2, boxstyle="round,pad=0.05",
                               facecolor=colors['power'], edgecolor='black', linewidth=2)
    ax.add_patch(power_box)
    ax.text(6.75, 2, 'Power Management', fontsize=10, ha='center', va='center', color='white', fontweight='bold')
    ax.text(6.75, 1.4, '5V Regulator (LM7805) → 5V Rail | 3.3V Regulator (AMS1117) → 3.3V Rail', 
            fontsize=7, ha='center', va='center', color='white')
    
    # === TEMPERATURE SENSOR ===
    temp_box = FancyBboxPatch((10.5, 1), 3, 1.5, boxstyle="round,pad=0.05",
                              facecolor=colors['interface'], edgecolor='black', linewidth=2)
    ax.add_patch(temp_box)
    ax.text(12, 1.75, 'Temperature Sensor\n(DS18B20/NTC)', fontsize=8, ha='center', va='center', color='white', fontweight='bold')
    
    # === WATER SURFACE ===
    water = mpatches.Rectangle((0.5, 0.2), 3, 0.5, facecolor='#3498db', alpha=0.5, edgecolor='blue', linewidth=2)
    ax.add_patch(water)
    ax.text(2, 0.45, 'Water Surface', fontsize=8, ha='center', va='center', fontweight='bold')
    
    # === ARROWS ===
    arrow_style = "Simple, tail_width=0.5, head_width=4, head_length=4"
    
    # TX path
    ax.annotate('', xy=(4, 7.25), xytext=(3, 7.25),
                arrowprops=dict(arrowstyle='->', color='black', lw=2))
    ax.annotate('', xy=(0.5, 7.25), xytext=(0, 7.25),
                arrowprops=dict(arrowstyle='->', color='blue', lw=2))
    
    # RX path  
    ax.annotate('', xy=(4, 5.25), xytext=(3, 5.25),
                arrowprops=dict(arrowstyle='<-', color='black', lw=2))
    
    # Sound waves (TX out)
    ax.annotate('', xy=(1.75, 4.5), xytext=(1.75, 0.7),
                arrowprops=dict(arrowstyle='<->', color='blue', lw=1.5, linestyle='--'))
    ax.text(2.3, 2.5, 'Ultrasonic\nWaves', fontsize=7, rotation=90, va='center')
    
    # Driver to Level Shifter
    ax.annotate('', xy=(7.5, 6.7), xytext=(6.5, 7.25),
                arrowprops=dict(arrowstyle='->', color='black', lw=2))
    ax.annotate('', xy=(7.5, 5.5), xytext=(6.5, 5.25),
                arrowprops=dict(arrowstyle='->', color='black', lw=2))
    
    # Level Shifter to MCU
    ax.annotate('', xy=(10.5, 6), xytext=(9.5, 6),
                arrowprops=dict(arrowstyle='<->', color='black', lw=2))
    ax.text(10, 6.3, 'Trigger/Echo', fontsize=7, ha='center')
    
    # Power connections
    ax.annotate('', xy=(5.25, 4.5), xytext=(5.25, 3),
                arrowprops=dict(arrowstyle='->', color='orange', lw=1.5))
    ax.annotate('', xy=(8.5, 5.25), xytext=(8.5, 3),
                arrowprops=dict(arrowstyle='->', color='orange', lw=1.5))
    ax.annotate('', xy=(12, 4.5), xytext=(12, 3),
                arrowprops=dict(arrowstyle='->', color='orange', lw=1.5))
    
    # Temp sensor to MCU
    ax.annotate('', xy=(12, 2.5), xytext=(12, 4.5),
                arrowprops=dict(arrowstyle='->', color='purple', lw=1.5))
    
    # === LABELS ===
    ax.text(3.5, 7.5, 'TRIG', fontsize=7, ha='center', color='red')
    ax.text(3.5, 5.5, 'ECHO', fontsize=7, ha='center', color='green')
    ax.text(10, 5.7, '3.3V', fontsize=7, ha='center', color='green')
    ax.text(7, 6.3, '5V', fontsize=7, ha='center', color='red')
    
    # Voltage labels
    ax.text(4.5, 2.5, '5V', fontsize=8, color='red', fontweight='bold')
    ax.text(8, 4, '3.3V', fontsize=8, color='green', fontweight='bold')
    
    # Legend
    legend_elements = [
        mpatches.Patch(color=colors['sensor'], label='Ultrasonic Transducers'),
        mpatches.Patch(color=colors['driver'], label='Driver/Amplifier Circuits'),
        mpatches.Patch(color=colors['protection'], label='Level Shifting'),
        mpatches.Patch(color=colors['mcu'], label='Microcontroller'),
        mpatches.Patch(color=colors['power'], label='Power Management'),
        mpatches.Patch(color=colors['interface'], label='Temperature Compensation')
    ]
    ax.legend(handles=legend_elements, loc='upper left', fontsize=8)
    
    plt.tight_layout()
    plt.savefig('/workspaces/ultraman/research_paper/images/block_diagram.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.savefig('/workspaces/ultraman/research_paper/images/block_diagram.pdf', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print("Block diagram saved!")

if __name__ == "__main__":
    create_block_diagram()
