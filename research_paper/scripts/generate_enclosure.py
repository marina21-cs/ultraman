#!/usr/bin/env python3
"""
Generate Enclosure Design for Ultrasonic Sensor
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle, FancyBboxPatch, Polygon, Circle, Arc, Wedge
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def create_enclosure_2d():
    """Create 2D cross-section and top view of enclosure"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 8))
    
    # =====================================================
    # CROSS-SECTION VIEW (Side view)
    # =====================================================
    ax1 = axes[0]
    ax1.set_xlim(-3, 3)
    ax1.set_ylim(-4, 2)
    ax1.set_aspect('equal')
    ax1.set_title('Enclosure Cross-Section (Side View)', fontsize=12, fontweight='bold')
    ax1.set_xlabel('Width (cm)', fontsize=10)
    ax1.set_ylabel('Height (cm)', fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.axhline(y=0, color='k', linewidth=0.5)
    ax1.axvline(x=0, color='k', linewidth=0.5)
    
    # Main enclosure body (rectangular top)
    body = Rectangle((-2, 0), 4, 1.5, facecolor='#4a4a4a', edgecolor='black', linewidth=2)
    ax1.add_patch(body)
    
    # Cone section
    cone = Polygon([(-2, 0), (2, 0), (0.8, -2.5), (-0.8, -2.5)],
                   facecolor='#4a4a4a', edgecolor='black', linewidth=2)
    ax1.add_patch(cone)
    
    # Sensor opening at bottom
    opening = Rectangle((-0.6, -2.5), 1.2, 0.15, facecolor='black', edgecolor='white', linewidth=1)
    ax1.add_patch(opening)
    
    # PCB inside
    pcb = Rectangle((-1.5, 0.3), 3, 0.15, facecolor='green', edgecolor='darkgreen', linewidth=1)
    ax1.add_patch(pcb)
    ax1.text(0, 0.37, 'PCB', fontsize=7, ha='center', va='center', color='white')
    
    # Ultrasonic transducers
    tx = Circle((-0.5, -0.3), 0.3, facecolor='silver', edgecolor='black', linewidth=1)
    ax1.add_patch(tx)
    ax1.text(-0.5, -0.3, 'TX', fontsize=6, ha='center', va='center')
    
    rx = Circle((0.5, -0.3), 0.3, facecolor='silver', edgecolor='black', linewidth=1)
    ax1.add_patch(rx)
    ax1.text(0.5, -0.3, 'RX', fontsize=6, ha='center', va='center')
    
    # Sound wave representation
    for i in range(4):
        arc = Arc((0, -2.5), 1 + i*0.5, 0.8 + i*0.3, angle=0, theta1=30, theta2=150,
                 linewidth=1, color='blue', linestyle='--', alpha=0.5)
        ax1.add_patch(arc)
    ax1.text(0, -3.5, 'Ultrasonic Waves', fontsize=8, ha='center', color='blue', style='italic')
    
    # O-ring seal
    oring = Rectangle((-2.1, -0.05), 0.15, 0.1, facecolor='red', edgecolor='darkred')
    ax1.add_patch(oring)
    oring2 = Rectangle((1.95, -0.05), 0.15, 0.1, facecolor='red', edgecolor='darkred')
    ax1.add_patch(oring2)
    
    # Cable gland
    gland = FancyBboxPatch((1.8, 0.8), 0.6, 0.5, boxstyle="round,pad=0.02",
                           facecolor='gray', edgecolor='black', linewidth=1)
    ax1.add_patch(gland)
    ax1.text(2.5, 1.05, 'Cable\nGland', fontsize=6, va='center')
    
    # Mounting bracket
    bracket = Polygon([(-2.3, 1.5), (-2.3, 1.8), (-1.5, 1.8), (-1.5, 1.5)],
                     facecolor='gray', edgecolor='black', linewidth=1)
    ax1.add_patch(bracket)
    bracket2 = Polygon([(2.3, 1.5), (2.3, 1.8), (1.5, 1.8), (1.5, 1.5)],
                      facecolor='gray', edgecolor='black', linewidth=1)
    ax1.add_patch(bracket2)
    
    # Mounting holes
    hole1 = Circle((-1.9, 1.65), 0.1, facecolor='white', edgecolor='black')
    ax1.add_patch(hole1)
    hole2 = Circle((1.9, 1.65), 0.1, facecolor='white', edgecolor='black')
    ax1.add_patch(hole2)
    
    # Dimension lines
    # Width
    ax1.annotate('', xy=(-2, 1.95), xytext=(2, 1.95),
                arrowprops=dict(arrowstyle='<->', color='red', lw=1))
    ax1.text(0, 2.1, '8 cm', fontsize=8, ha='center', color='red')
    
    # Height
    ax1.annotate('', xy=(2.4, 1.5), xytext=(2.4, -2.5),
                arrowprops=dict(arrowstyle='<->', color='red', lw=1))
    ax1.text(2.7, -0.5, '8 cm', fontsize=8, ha='center', color='red', rotation=90)
    
    # Legend
    ax1.text(-2.8, -3.5, 'Materials:\n• Body: ABS/PVC (IP68)\n• Seal: Silicone O-ring\n• Gland: PG7 Cable Gland',
             fontsize=7, va='top', bbox=dict(boxstyle='round', facecolor='lightyellow'))
    
    # =====================================================
    # TOP VIEW
    # =====================================================
    ax2 = axes[1]
    ax2.set_xlim(-3, 3)
    ax2.set_ylim(-3, 3)
    ax2.set_aspect('equal')
    ax2.set_title('Enclosure Top View', fontsize=12, fontweight='bold')
    ax2.set_xlabel('Width (cm)', fontsize=10)
    ax2.set_ylabel('Depth (cm)', fontsize=10)
    ax2.grid(True, alpha=0.3)
    
    # Outer body
    outer = Rectangle((-2, -2), 4, 4, facecolor='#4a4a4a', edgecolor='black', linewidth=2)
    ax2.add_patch(outer)
    
    # Mounting tabs
    tab1 = Rectangle((-2.3, 1.5), 0.8, 0.3, facecolor='gray', edgecolor='black', linewidth=1)
    ax2.add_patch(tab1)
    tab2 = Rectangle((1.5, 1.5), 0.8, 0.3, facecolor='gray', edgecolor='black', linewidth=1)
    ax2.add_patch(tab2)
    tab3 = Rectangle((-2.3, -1.8), 0.8, 0.3, facecolor='gray', edgecolor='black', linewidth=1)
    ax2.add_patch(tab3)
    tab4 = Rectangle((1.5, -1.8), 0.8, 0.3, facecolor='gray', edgecolor='black', linewidth=1)
    ax2.add_patch(tab4)
    
    # Mounting holes
    for hx, hy in [(-1.9, 1.65), (1.9, 1.65), (-1.9, -1.65), (1.9, -1.65)]:
        hole = Circle((hx, hy), 0.12, facecolor='white', edgecolor='black', linewidth=1)
        ax2.add_patch(hole)
    
    # Inner cavity
    inner = Rectangle((-1.5, -1.5), 3, 3, facecolor='#606060', edgecolor='gray', linewidth=1, linestyle='--')
    ax2.add_patch(inner)
    ax2.text(0, 0, 'Internal\nCavity', fontsize=8, ha='center', va='center', color='white')
    
    # Cable gland position
    gland_pos = Circle((1.8, 0), 0.25, facecolor='gray', edgecolor='black', linewidth=2)
    ax2.add_patch(gland_pos)
    ax2.text(2.5, 0, 'Cable\nGland', fontsize=6, va='center')
    
    # Lid screws
    for sx, sy in [(-1.3, 1.3), (1.3, 1.3), (-1.3, -1.3), (1.3, -1.3)]:
        screw = Circle((sx, sy), 0.1, facecolor='silver', edgecolor='black', linewidth=1)
        ax2.add_patch(screw)
    
    # Dimensions
    ax2.annotate('', xy=(-2, 2.3), xytext=(2, 2.3),
                arrowprops=dict(arrowstyle='<->', color='red', lw=1))
    ax2.text(0, 2.5, '8 cm', fontsize=8, ha='center', color='red')
    
    ax2.annotate('', xy=(2.5, -2), xytext=(2.5, 2),
                arrowprops=dict(arrowstyle='<->', color='red', lw=1))
    ax2.text(2.7, 0, '8 cm', fontsize=8, ha='center', color='red', rotation=90)
    
    plt.tight_layout()
    plt.savefig('/workspaces/ultraman/research_paper/images/enclosure_2d.png', dpi=300, 
                bbox_inches='tight', facecolor='white')
    plt.savefig('/workspaces/ultraman/research_paper/images/enclosure_2d.pdf', 
                bbox_inches='tight', facecolor='white')
    print("2D enclosure design saved!")

def create_enclosure_3d():
    """Create 3D isometric view of enclosure"""
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Enclosure dimensions (in arbitrary units for visualization)
    width = 4
    depth = 4
    height_top = 1.5
    height_cone = 2.5
    cone_bottom = 1.5
    
    # Top box vertices
    box_vertices = [
        # Bottom face of box
        [-width/2, -depth/2, 0],
        [width/2, -depth/2, 0],
        [width/2, depth/2, 0],
        [-width/2, depth/2, 0],
        # Top face of box
        [-width/2, -depth/2, height_top],
        [width/2, -depth/2, height_top],
        [width/2, depth/2, height_top],
        [-width/2, depth/2, height_top],
    ]
    
    # Box faces
    box_faces = [
        [box_vertices[0], box_vertices[1], box_vertices[5], box_vertices[4]],  # Front
        [box_vertices[1], box_vertices[2], box_vertices[6], box_vertices[5]],  # Right
        [box_vertices[2], box_vertices[3], box_vertices[7], box_vertices[6]],  # Back
        [box_vertices[3], box_vertices[0], box_vertices[4], box_vertices[7]],  # Left
        [box_vertices[4], box_vertices[5], box_vertices[6], box_vertices[7]],  # Top
    ]
    
    # Cone vertices
    cone_vertices_top = [
        [-width/2, -depth/2, 0],
        [width/2, -depth/2, 0],
        [width/2, depth/2, 0],
        [-width/2, depth/2, 0],
    ]
    cone_vertices_bottom = [
        [-cone_bottom/2, -cone_bottom/2, -height_cone],
        [cone_bottom/2, -cone_bottom/2, -height_cone],
        [cone_bottom/2, cone_bottom/2, -height_cone],
        [-cone_bottom/2, cone_bottom/2, -height_cone],
    ]
    
    # Cone faces
    cone_faces = [
        [cone_vertices_top[0], cone_vertices_top[1], cone_vertices_bottom[1], cone_vertices_bottom[0]],  # Front
        [cone_vertices_top[1], cone_vertices_top[2], cone_vertices_bottom[2], cone_vertices_bottom[1]],  # Right
        [cone_vertices_top[2], cone_vertices_top[3], cone_vertices_bottom[3], cone_vertices_bottom[2]],  # Back
        [cone_vertices_top[3], cone_vertices_top[0], cone_vertices_bottom[0], cone_vertices_bottom[3]],  # Left
        [cone_vertices_bottom[0], cone_vertices_bottom[1], cone_vertices_bottom[2], cone_vertices_bottom[3]],  # Bottom
    ]
    
    # Draw box
    box_collection = Poly3DCollection(box_faces, alpha=0.8, facecolor='#4a4a4a', 
                                       edgecolor='black', linewidth=1)
    ax.add_collection3d(box_collection)
    
    # Draw cone
    cone_collection = Poly3DCollection(cone_faces, alpha=0.8, facecolor='#5a5a5a', 
                                        edgecolor='black', linewidth=1)
    ax.add_collection3d(cone_collection)
    
    # Mounting brackets (simplified)
    bracket_size = 0.3
    for bx, by in [(-width/2 - 0.3, depth/2 - 0.5), (width/2, depth/2 - 0.5),
                   (-width/2 - 0.3, -depth/2 + 0.2), (width/2, -depth/2 + 0.2)]:
        bracket_verts = [
            [bx, by, height_top],
            [bx + bracket_size, by, height_top],
            [bx + bracket_size, by + bracket_size, height_top],
            [bx, by + bracket_size, height_top],
            [bx, by, height_top + 0.3],
            [bx + bracket_size, by, height_top + 0.3],
            [bx + bracket_size, by + bracket_size, height_top + 0.3],
            [bx, by + bracket_size, height_top + 0.3],
        ]
    
    # Add sensor opening indicator
    opening_size = 0.8
    opening_verts = [
        [-opening_size/2, -opening_size/2, -height_cone],
        [opening_size/2, -opening_size/2, -height_cone],
        [opening_size/2, opening_size/2, -height_cone],
        [-opening_size/2, opening_size/2, -height_cone],
    ]
    opening_face = Poly3DCollection([[opening_verts[0], opening_verts[1], 
                                      opening_verts[2], opening_verts[3]]], 
                                    alpha=1, facecolor='black', edgecolor='white', linewidth=2)
    ax.add_collection3d(opening_face)
    
    # Sound waves (circles below sensor)
    theta = np.linspace(0, 2*np.pi, 50)
    for r in [0.8, 1.2, 1.6, 2.0]:
        x_wave = r * np.cos(theta)
        y_wave = r * np.sin(theta)
        z_wave = np.full_like(x_wave, -height_cone - 0.5 - r*0.3)
        ax.plot(x_wave, y_wave, z_wave, 'b--', alpha=0.4, linewidth=1)
    
    # Cable gland
    cable_theta = np.linspace(0, 2*np.pi, 20)
    cable_x = 0.2 * np.cos(cable_theta) + width/2 + 0.15
    cable_y = 0.2 * np.sin(cable_theta)
    cable_z = np.full_like(cable_x, height_top/2)
    ax.plot(cable_x, cable_y, cable_z, 'gray', linewidth=3)
    
    # Labels
    ax.text(0, 0, height_top + 0.5, 'Enclosure Body\n(ABS/PVC IP68)', fontsize=9, 
            ha='center', va='bottom')
    ax.text(0, 0, -height_cone - 0.3, 'Sensor Opening', fontsize=8, ha='center', color='blue')
    ax.text(width/2 + 0.5, 0, height_top/2, 'Cable\nGland', fontsize=7)
    
    # Set labels and title
    ax.set_xlabel('Width (cm)')
    ax.set_ylabel('Depth (cm)')
    ax.set_zlabel('Height (cm)')
    ax.set_title('3D Isometric View - Waterproof Sensor Enclosure', fontsize=12, fontweight='bold')
    
    # Set viewing angle
    ax.view_init(elev=25, azim=45)
    
    # Set axis limits
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_zlim(-4, 3)
    
    plt.tight_layout()
    plt.savefig('/workspaces/ultraman/research_paper/images/enclosure_3d.png', dpi=300, 
                bbox_inches='tight', facecolor='white')
    plt.savefig('/workspaces/ultraman/research_paper/images/enclosure_3d.pdf', 
                bbox_inches='tight', facecolor='white')
    print("3D enclosure design saved!")

def create_mounting_diagram():
    """Create pole mounting installation diagram"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 12))
    ax.set_xlim(-3, 7)
    ax.set_ylim(-2, 12)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Installation Diagram - Pole Mounting', fontsize=14, fontweight='bold')
    
    # Ground level
    ground = Rectangle((-3, 0), 10, 0.3, facecolor='#8B4513', edgecolor='black', linewidth=2)
    ax.add_patch(ground)
    ax.text(2, -0.3, 'Ground Level', fontsize=9, ha='center')
    
    # Water surface (flood level)
    water = Rectangle((-3, 0.3), 10, 2, facecolor='#87CEEB', edgecolor='blue', linewidth=1, alpha=0.6)
    ax.add_patch(water)
    ax.text(2, 1.3, 'Flood Water Level', fontsize=9, ha='center', color='darkblue')
    
    # Mounting pole
    pole = Rectangle((0, 0.3), 0.4, 10, facecolor='gray', edgecolor='black', linewidth=2)
    ax.add_patch(pole)
    ax.text(0.7, 5, 'Steel/Concrete\nPole (3-4m)', fontsize=8, va='center')
    
    # Sensor enclosure
    enclosure_body = Rectangle((-0.8, 8), 2, 1.2, facecolor='#4a4a4a', edgecolor='black', linewidth=2)
    ax.add_patch(enclosure_body)
    
    # Cone
    cone = Polygon([(-0.8, 8), (1.2, 8), (0.6, 6.5), (-0.2, 6.5)],
                   facecolor='#4a4a4a', edgecolor='black', linewidth=2)
    ax.add_patch(cone)
    ax.text(0.2, 8.6, 'Sensor', fontsize=8, ha='center', va='center', color='white')
    
    # Mounting bracket
    bracket = Rectangle((-0.2, 9.2), 0.6, 0.3, facecolor='silver', edgecolor='black', linewidth=1)
    ax.add_patch(bracket)
    
    # Cable going up
    ax.plot([1.2, 1.5, 1.5, 0.6, 0.6], [8.5, 8.5, 10.5, 10.5, 11], 'k-', linewidth=2)
    ax.text(1.8, 9.5, 'Power/Data\nCable', fontsize=7)
    
    # Solar panel (on top)
    solar = Polygon([(0, 10.5), (-1, 11.5), (1.5, 11.5), (0.5, 10.5)],
                    facecolor='darkblue', edgecolor='black', linewidth=2)
    ax.add_patch(solar)
    ax.text(0.25, 11.7, 'Solar Panel', fontsize=8, ha='center')
    
    # Sound waves
    for i in range(5):
        arc = Arc((0.2, 6.5), 1 + i*0.6, 0.6 + i*0.3, angle=0, theta1=20, theta2=160,
                 linewidth=1, color='blue', linestyle='--', alpha=0.5)
        ax.add_patch(arc)
    
    # Dimension arrows
    # Pole height
    ax.annotate('', xy=(3, 0.3), xytext=(3, 10.3),
                arrowprops=dict(arrowstyle='<->', color='red', lw=1.5))
    ax.text(3.3, 5, '3-4 m\n(Pole Height)', fontsize=9, va='center', color='red')
    
    # Sensor height
    ax.annotate('', xy=(4.5, 2.3), xytext=(4.5, 6.5),
                arrowprops=dict(arrowstyle='<->', color='green', lw=1.5))
    ax.text(4.8, 4.5, 'Detection\nRange\n(0.2-5m)', fontsize=8, va='center', color='green')
    
    # Water level measurement
    ax.annotate('', xy=(-2, 2.3), xytext=(-2, 6.5),
                arrowprops=dict(arrowstyle='<->', color='blue', lw=1.5))
    ax.text(-2.8, 4.5, 'Measured\nDistance', fontsize=8, va='center', color='blue')
    
    # Labels
    ax.text(5, 8, 'Installation Notes:', fontsize=10, fontweight='bold')
    notes = """• Mount sensor facing downward
• Ensure unobstructed view of water
• Minimum height: 0.5m above max flood
• Secure cable with cable ties
• Use stainless steel brackets
• Apply waterproof sealant at joints"""
    ax.text(5, 7.5, notes, fontsize=8, va='top', 
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('/workspaces/ultraman/research_paper/images/mounting_diagram.png', dpi=300, 
                bbox_inches='tight', facecolor='white')
    plt.savefig('/workspaces/ultraman/research_paper/images/mounting_diagram.pdf', 
                bbox_inches='tight', facecolor='white')
    print("Mounting diagram saved!")

if __name__ == "__main__":
    create_enclosure_2d()
    create_enclosure_3d()
    create_mounting_diagram()
