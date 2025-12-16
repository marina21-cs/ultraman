#!/usr/bin/env python3
"""
Generate Flowcharts for Ultrasonic Sensor Algorithm
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle, FancyBboxPatch, Polygon, Ellipse, Circle
import numpy as np

def draw_start_end(ax, x, y, text, width=2, height=0.6):
    """Draw start/end terminal (rounded rectangle)"""
    ellipse = Ellipse((x, y), width, height, facecolor='#90EE90', edgecolor='black', linewidth=2)
    ax.add_patch(ellipse)
    ax.text(x, y, text, ha='center', va='center', fontsize=9, fontweight='bold')

def draw_process(ax, x, y, text, width=2.5, height=0.8):
    """Draw process box (rectangle)"""
    rect = FancyBboxPatch((x - width/2, y - height/2), width, height, 
                          boxstyle="round,pad=0.03", facecolor='#ADD8E6', 
                          edgecolor='black', linewidth=2)
    ax.add_patch(rect)
    ax.text(x, y, text, ha='center', va='center', fontsize=8, wrap=True)

def draw_decision(ax, x, y, text, size=0.8):
    """Draw decision diamond"""
    diamond = Polygon([(x, y + size), (x + size*1.2, y), (x, y - size), (x - size*1.2, y)],
                     facecolor='#FFD700', edgecolor='black', linewidth=2)
    ax.add_patch(diamond)
    ax.text(x, y, text, ha='center', va='center', fontsize=7, wrap=True)

def draw_io(ax, x, y, text, width=2.2, height=0.7):
    """Draw I/O parallelogram"""
    skew = 0.3
    parallelogram = Polygon([(x - width/2 + skew, y + height/2),
                            (x + width/2 + skew, y + height/2),
                            (x + width/2 - skew, y - height/2),
                            (x - width/2 - skew, y - height/2)],
                           facecolor='#DDA0DD', edgecolor='black', linewidth=2)
    ax.add_patch(parallelogram)
    ax.text(x, y, text, ha='center', va='center', fontsize=8)

def draw_arrow(ax, x1, y1, x2, y2, label=''):
    """Draw arrow between shapes"""
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    if label:
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        ax.text(mid_x + 0.15, mid_y, label, fontsize=7, color='red')

def create_main_flowchart():
    """Main measurement flowchart"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 14))
    ax.set_xlim(-2, 8)
    ax.set_ylim(-1, 15)
    ax.set_aspect('equal')
    ax.axis('off')
    
    ax.text(3, 14.5, 'Main Measurement Algorithm Flowchart', 
            fontsize=14, fontweight='bold', ha='center')
    
    # Start
    draw_start_end(ax, 3, 13.5, 'START')
    
    # Initialize
    draw_process(ax, 3, 12.3, 'Initialize ESP32\nConfigure GPIO pins\nSet timer/counter')
    draw_arrow(ax, 3, 13.2, 3, 12.7)
    
    # Read temperature
    draw_io(ax, 3, 11.2, 'Read Temperature\nfrom DS18B20')
    draw_arrow(ax, 3, 11.9, 3, 11.55)
    
    # Calculate speed of sound
    draw_process(ax, 3, 10.1, 'Calculate Speed of Sound\nv = 331.4 + 0.6×T (m/s)')
    draw_arrow(ax, 3, 10.85, 3, 10.5)
    
    # Initialize sample array
    draw_process(ax, 3, 9, 'Initialize sample array\nSet sample_count = 0\nSet N = 15 samples')
    draw_arrow(ax, 3, 9.7, 3, 9.4)
    
    # Loop start - Decision
    draw_decision(ax, 3, 7.8, 'sample_count\n< N?')
    draw_arrow(ax, 3, 8.6, 3, 8.6)
    
    # Trigger pulse
    draw_process(ax, 3, 6.5, 'Send TRIGGER pulse\n(10µs HIGH)')
    draw_arrow(ax, 3, 7, 3, 6.9, 'YES')
    
    # Wait for echo
    draw_io(ax, 3, 5.4, 'Wait for ECHO pin\nto go HIGH')
    draw_arrow(ax, 3, 6.1, 3, 5.75)
    
    # Start timer
    draw_process(ax, 3, 4.3, 'Start Timer\nRecord start_time')
    draw_arrow(ax, 3, 5.05, 3, 4.7)
    
    # Wait echo low
    draw_io(ax, 3, 3.2, 'Wait for ECHO pin\nto go LOW')
    draw_arrow(ax, 3, 3.9, 3, 3.55)
    
    # Stop timer
    draw_process(ax, 3, 2.1, 'Stop Timer\nRecord end_time\nCalculate duration')
    draw_arrow(ax, 3, 2.85, 3, 2.5)
    
    # Calculate distance
    draw_process(ax, 3, 1, 'distance = (duration × v) / 2\nStore in sample array\nsample_count++')
    draw_arrow(ax, 3, 1.7, 3, 1.4)
    
    # Loop back
    ax.plot([3, 5.5, 5.5, 3.8], [0.6, 0.6, 7.8, 7.8], 'k-', linewidth=1.5)
    ax.annotate('', xy=(3.96, 7.8), xytext=(5.5, 7.8),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    
    # Exit loop - process samples
    draw_process(ax, -0.5, 6.5, 'Sort sample array\nRemove outliers\n(outside 2σ)')
    draw_arrow(ax, 1.8, 7.8, 0.5, 7.8, 'NO')
    ax.plot([0.5, -0.5, -0.5], [7.8, 7.8, 6.9], 'k-', linewidth=1.5)
    
    # Calculate median
    draw_process(ax, -0.5, 5.3, 'Calculate median\nof valid samples')
    draw_arrow(ax, -0.5, 6.1, -0.5, 5.7)
    
    # Convert to water level
    draw_process(ax, -0.5, 4.1, 'water_level = \nsensor_height - distance')
    draw_arrow(ax, -0.5, 4.9, -0.5, 4.5)
    
    # Output
    draw_io(ax, -0.5, 3, 'Store water_level\nSend via LoRa\n(when scheduled)')
    draw_arrow(ax, -0.5, 3.7, -0.5, 3.35)
    
    # Decision - critical level?
    draw_decision(ax, -0.5, 1.8, 'Critical\nlevel?')
    draw_arrow(ax, -0.5, 2.65, -0.5, 2.6)
    
    # Adjust interval
    draw_process(ax, 1.5, 1.8, 'Set short\ninterval (30s)')
    draw_arrow(ax, 0.7, 1.8, 0.7, 1.8, 'YES')
    
    draw_process(ax, -2.5, 1.8, 'Set normal\ninterval (5min)')
    draw_arrow(ax, -1.7, 1.8, -1.7, 1.8, 'NO')
    
    # Delay
    draw_process(ax, -0.5, 0.5, 'Wait for\nnext interval')
    ax.plot([1.5, 1.5, -0.5], [1.4, 0.5, 0.5], 'k-', linewidth=1.5)
    ax.plot([-2.5, -2.5, -0.5], [1.4, 0.5, 0.5], 'k-', linewidth=1.5)
    ax.annotate('', xy=(-0.5, 0.9), xytext=(-0.5, 0.5),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    
    # Loop back to read temp
    ax.plot([-0.5, -1.8, -1.8, 3], [0.1, 0.1, 11.2, 11.2], 'k-', linewidth=1.5)
    ax.annotate('', xy=(1.8, 11.2), xytext=(-1.8, 11.2),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    
    plt.tight_layout()
    plt.savefig('/workspaces/ultraman/research_paper/images/flowchart_main.png', dpi=300, 
                bbox_inches='tight', facecolor='white')
    plt.savefig('/workspaces/ultraman/research_paper/images/flowchart_main.pdf', 
                bbox_inches='tight', facecolor='white')
    print("Main flowchart saved!")

def create_adaptive_flowchart():
    """Adaptive sampling flowchart"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 12))
    ax.set_xlim(-2, 8)
    ax.set_ylim(-1, 13)
    ax.set_aspect('equal')
    ax.axis('off')
    
    ax.text(3, 12.5, 'Adaptive Sampling Rate Algorithm', 
            fontsize=14, fontweight='bold', ha='center')
    
    # Start
    draw_start_end(ax, 3, 11.5, 'START')
    
    # Get current water level
    draw_io(ax, 3, 10.3, 'Get current\nwater_level')
    draw_arrow(ax, 3, 11.2, 3, 10.65)
    
    # Get previous level
    draw_io(ax, 3, 9.2, 'Get previous\nwater_level')
    draw_arrow(ax, 3, 9.95, 3, 9.55)
    
    # Calculate rate of change
    draw_process(ax, 3, 8.1, 'rate_of_change = \n(current - previous) / time')
    draw_arrow(ax, 3, 8.85, 3, 8.5)
    
    # Check critical threshold
    draw_decision(ax, 3, 6.8, 'water_level >\nCRITICAL?')
    draw_arrow(ax, 3, 7.7, 3, 7.6)
    
    # Critical action
    draw_process(ax, 6, 6.8, 'interval = 10s\nPRIORITY = HIGH\nTrigger Alert')
    draw_arrow(ax, 4.2, 6.8, 4.8, 6.8, 'YES')
    
    # Check warning threshold
    draw_decision(ax, 3, 5.3, 'water_level >\nWARNING?')
    draw_arrow(ax, 3, 6, 3, 6.1, 'NO')
    
    # Warning action
    draw_process(ax, 6, 5.3, 'interval = 30s\nPRIORITY = MEDIUM')
    draw_arrow(ax, 4.2, 5.3, 4.8, 5.3, 'YES')
    
    # Check rising fast
    draw_decision(ax, 3, 3.8, 'rate_of_change\n> FAST?')
    draw_arrow(ax, 3, 4.5, 3, 4.6, 'NO')
    
    # Rising fast action
    draw_process(ax, 6, 3.8, 'interval = 60s\nPRIORITY = MEDIUM')
    draw_arrow(ax, 4.2, 3.8, 4.8, 3.8, 'YES')
    
    # Normal mode
    draw_process(ax, 3, 2.5, 'interval = 300s (5 min)\nPRIORITY = LOW')
    draw_arrow(ax, 3, 3, 3, 2.9, 'NO')
    
    # Converge paths
    ax.plot([6, 6, 3], [7.6, 1.8, 1.8], 'k-', linewidth=1.5)
    ax.plot([6, 6], [6.0, 5.7], 'k-', linewidth=1.5)
    ax.plot([6, 6], [4.9, 4.2], 'k-', linewidth=1.5)
    
    # Set timer
    draw_process(ax, 3, 1.3, 'Configure timer\nfor next reading')
    draw_arrow(ax, 3, 2.1, 3, 1.7)
    
    # Return
    draw_start_end(ax, 3, 0.3, 'RETURN interval')
    draw_arrow(ax, 3, 0.9, 3, 0.6)
    
    # Legend box
    legend_box = FancyBboxPatch((-1.5, 0), 2.2, 2.5, boxstyle="round,pad=0.05",
                                facecolor='lightyellow', edgecolor='black', linewidth=1)
    ax.add_patch(legend_box)
    ax.text(-0.4, 2.3, 'Threshold Values:', fontsize=8, fontweight='bold')
    ax.text(-0.4, 2.0, 'CRITICAL: 80% capacity', fontsize=7)
    ax.text(-0.4, 1.7, 'WARNING: 50% capacity', fontsize=7)
    ax.text(-0.4, 1.4, 'FAST: >5cm/min rise', fontsize=7)
    ax.text(-0.4, 1.1, 'Sensor Height: 3-4m', fontsize=7)
    ax.text(-0.4, 0.8, 'Max Range: 5m', fontsize=7)
    ax.text(-0.4, 0.5, 'Resolution: ±1cm', fontsize=7)
    ax.text(-0.4, 0.2, 'Accuracy: ±1cm', fontsize=7)
    
    plt.tight_layout()
    plt.savefig('/workspaces/ultraman/research_paper/images/flowchart_adaptive.png', dpi=300, 
                bbox_inches='tight', facecolor='white')
    plt.savefig('/workspaces/ultraman/research_paper/images/flowchart_adaptive.pdf', 
                bbox_inches='tight', facecolor='white')
    print("Adaptive sampling flowchart saved!")

def create_outlier_flowchart():
    """Outlier rejection flowchart"""
    fig, ax = plt.subplots(1, 1, figsize=(8, 10))
    ax.set_xlim(-1, 7)
    ax.set_ylim(-1, 11)
    ax.set_aspect('equal')
    ax.axis('off')
    
    ax.text(3, 10.5, 'Outlier Rejection Algorithm', 
            fontsize=14, fontweight='bold', ha='center')
    
    # Start
    draw_start_end(ax, 3, 9.5, 'START')
    
    # Input samples
    draw_io(ax, 3, 8.4, 'Input: samples[N]')
    draw_arrow(ax, 3, 9.2, 3, 8.75)
    
    # Calculate mean
    draw_process(ax, 3, 7.3, 'Calculate mean (μ)\nof all samples')
    draw_arrow(ax, 3, 8.05, 3, 7.7)
    
    # Calculate std dev
    draw_process(ax, 3, 6.2, 'Calculate standard\ndeviation (σ)')
    draw_arrow(ax, 3, 6.9, 3, 6.6)
    
    # Initialize
    draw_process(ax, 3, 5.1, 'valid_samples = []\ni = 0')
    draw_arrow(ax, 3, 5.8, 3, 5.5)
    
    # Loop
    draw_decision(ax, 3, 3.9, 'i < N?')
    draw_arrow(ax, 3, 4.7, 3, 4.7)
    
    # Check if within bounds
    draw_decision(ax, 3, 2.5, '|samples[i] - μ|\n< 2σ?')
    draw_arrow(ax, 3, 3.1, 3, 3.3, 'YES')
    
    # Add to valid
    draw_process(ax, 5.5, 2.5, 'Add to\nvalid_samples')
    draw_arrow(ax, 4.2, 2.5, 4.5, 2.5, 'YES')
    
    # Increment
    draw_process(ax, 3, 1.2, 'i = i + 1')
    draw_arrow(ax, 3, 1.7, 3, 1.6, 'NO')
    ax.plot([5.5, 5.5, 3], [2.1, 1.2, 1.2], 'k-', linewidth=1.5)
    
    # Loop back
    ax.plot([3, 5.8, 5.8, 4.2], [0.8, 0.8, 3.9, 3.9], 'k-', linewidth=1.5)
    
    # Exit loop
    draw_process(ax, 0.5, 2.5, 'Calculate median\nof valid_samples')
    draw_arrow(ax, 1.8, 3.9, 0.7, 3.9, 'NO')
    ax.plot([0.5, 0.5], [3.9, 2.9], 'k-', linewidth=1.5)
    
    # Return
    draw_start_end(ax, 0.5, 1.5, 'RETURN median')
    draw_arrow(ax, 0.5, 2.1, 0.5, 1.8)
    
    plt.tight_layout()
    plt.savefig('/workspaces/ultraman/research_paper/images/flowchart_outlier.png', dpi=300, 
                bbox_inches='tight', facecolor='white')
    plt.savefig('/workspaces/ultraman/research_paper/images/flowchart_outlier.pdf', 
                bbox_inches='tight', facecolor='white')
    print("Outlier rejection flowchart saved!")

if __name__ == "__main__":
    create_main_flowchart()
    create_adaptive_flowchart()
    create_outlier_flowchart()
