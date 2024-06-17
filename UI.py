import tkinter as tk
import math

class Nucleobase:
    def __init__(self, canvas, name, letter, color, position, base_type):
        self.canvas = canvas
        self.name = name
        self.letter = letter
        self.color = color
        self.position = position
        self.base_type = base_type

    def create_visual(self):
        if self.base_type == "purine":
            self.draw_purine()
        elif self.base_type == "pyrimidine":
            self.draw_pyrimidine()

    def draw_purine(self):
        points = self.calculate_hexagon_points(self.position[0], self.position[1], 50)
        self.canvas.create_polygon(points, fill=self.color, outline="black")
        self.canvas.create_text(self.position[0], self.position[1], text=self.letter, font=("Arial", 24, "bold"), fill="black")

    def draw_pyrimidine(self):
        size_big = 50
        size_small = 30
        offset = 70

        points_big = self.calculate_hexagon_points(self.position[0], self.position[1], size_big)
        points_small = self.calculate_pentagon_points(self.position[0] + offset, self.position[1], size_small)

        rotated_points = self.rotate_points(points_small, self.position[0] + offset, self.position[1], math.radians(90))

        self.canvas.create_polygon(points_big, fill=self.color, outline="black")
        self.canvas.create_polygon(rotated_points, fill=self.color, outline="black")
        self.canvas.create_text(self.position[0], self.position[1], text=self.letter, font=("Arial", 24, "bold"), fill="black")

    def calculate_hexagon_points(self, x, y, size):
        points = []
        for i in range(6):
            angle_deg = 60 * i - 30
            angle_rad = math.radians(angle_deg)
            point_x = x + size * math.cos(angle_rad)
            point_y = y + size * math.sin(angle_rad)
            points.append(point_x)
            points.append(point_y)
        return points

    def calculate_pentagon_points(self, x, y, size):
        points = []
        for i in range(5):
            angle_deg = 72 * i - 18
            angle_rad = math.radians(angle_deg)
            point_x = x + size * math.cos(angle_rad)
            point_y = y + size * math.sin(angle_rad)
            points.append(point_x)
            points.append(point_y)
        return points

    def rotate_points(self, points, cx, cy, angle_rad):
        rotated_points = []
        for i in range(0, len(points), 2):
            x = points[i]
            y = points[i + 1]
            dx = x - cx
            dy = y - cy
            new_x = cx + dx * math.cos(angle_rad) - dy * math.sin(angle_rad)
            new_y = cy + dx * math.sin(angle_rad) + dy * math.cos(angle_rad)
            rotated_points.extend([new_x, new_y])
        return rotated_points

class Deoxyribose:
    def __init__(self, canvas, position):
        self.canvas = canvas
        self.position = position

    def create_visual(self):
        x, y = self.position
        size = 30
        points = self.calculate_pentagon_points(x, y, size)
        self.canvas.create_polygon(points, fill="green", outline="black")
        self.canvas.create_text(x, y, text="D", font=("Arial", 24, "bold"), fill="black")

    def calculate_pentagon_points(self, x, y, size):
        points = []
        for i in range(5):
            angle_deg = 72 * i - 18
            angle_rad = math.radians(angle_deg)
            point_x = x + size * math.cos(angle_rad)
            point_y = y + size * math.sin(angle_rad)
            points.append(point_x)
            points.append(point_y)
        return points

    def get_vertex_positions(self, x, y, size):
        points = self.calculate_pentagon_points(x, y, size)
        vertex_positions = [(points[i], points[i+1]) for i in range(0, len(points), 2)]
        return vertex_positions

class Phosphate:
    def __init__(self, canvas, position):
        self.canvas = canvas
        self.position = position

    def create_visual(self):
        x, y = self.position
        size = 20
        self.canvas.create_oval(x - size, y - size, x + size, y + size, fill="blue")
        self.canvas.create_text(x, y, text="P", font=("Arial", 24, "bold"), fill="black")

base_map = {
    'A': ("Adenine", "A", "pink", "purine"),
    'T': ("Thymine", "T", "blue", "pyrimidine"),
    'G': ("Guanine", "G", "yellow", "purine"),
    'C': ("Cytosine", "C", "green", "pyrimidine")
}

def DrawStrand(canvas, sequence):
    initial_x = 100
    initial_y = 100
    offset_x = 220
    base_size = 50
    deoxyribose_size = 30

    items = []
    for i, base_char in enumerate(sequence):
        if base_char in base_map:
            name, letter, color, base_type = base_map[base_char]
            base_pos_x = initial_x + i * offset_x
            base = Nucleobase(canvas, name, letter, color, (base_pos_x, initial_y), base_type)

            deoxyribose = Deoxyribose(canvas, (base_pos_x + base_size // 2, initial_y + base_size + 50))
            items.append(base)
            items.append(deoxyribose)

            if i < len(sequence) - 1:
                next_base_pos_x = initial_x + (i + 1) * offset_x
                phosphate_pos_x = (base_pos_x + next_base_pos_x) / 2
                phosphate = Phosphate(canvas, (phosphate_pos_x, initial_y + base_size + 100))
                items.append(phosphate)

                canvas.create_line(deoxyribose.position[0], deoxyribose.position[1], phosphate.position[0], phosphate.position[1], fill="white", width=2)
                
                vertex_positions = deoxyribose.get_vertex_positions(deoxyribose.position[0], deoxyribose.position[1], deoxyribose_size)
                nearest_vertex = min(vertex_positions, key=lambda v: (v[0] - base.position[0])**2 + (v[1] - base.position[1])**2)
                canvas.create_line(base.position[0], base.position[1], nearest_vertex[0], nearest_vertex[1], fill="white", width=2)

                next_deoxyribose_pos = (next_base_pos_x + base_size // 2, initial_y + base_size + 50)
                canvas.create_line(phosphate.position[0], phosphate.position[1], next_deoxyribose_pos[0], next_deoxyribose_pos[1], fill="white", width=2)

            else:
                vertex_positions = deoxyribose.get_vertex_positions(deoxyribose.position[0], deoxyribose.position[1], deoxyribose_size)
                nearest_vertex = min(vertex_positions, key=lambda v: (v[0] - base.position[0])**2 + (v[1] - base.position[1])**2)
                canvas.create_line(base.position[0], base.position[1], nearest_vertex[0], nearest_vertex[1], fill="white", width=2)

    for item in items:
        item.create_visual()

def Test_Gui(canvas):
    initial_x = 100
    initial_y = 100
    offset_x = 220  # Horizontal spacing between base groups
    base_size = 50
    deoxyribose_size = 30

    sequence = ['A', 'T', 'G', 'C','A', 'T', 'G', 'C']
    items = []
    for i, base_char in enumerate(sequence):
        if base_char in base_map:
            name, letter, color, base_type = base_map[base_char]
            base_pos_x = initial_x + i * offset_x
            base = Nucleobase(canvas, name, letter, color, (base_pos_x, initial_y), base_type)

            deoxyribose = Deoxyribose(canvas, (base_pos_x + base_size // 2, initial_y + base_size + 50))
            items.append(base)
            items.append(deoxyribose)

            if i < len(sequence) - 1:  # Add phosphate only if there's a next nucleobase
                next_base_pos_x = initial_x + (i + 1) * offset_x
                phosphate_pos_x = (base_pos_x + next_base_pos_x) / 2
                phosphate = Phosphate(canvas, (phosphate_pos_x, initial_y + base_size + 100))
                items.append(phosphate)

                # Draw line between deoxyribose and phosphate
                canvas.create_line(deoxyribose.position[0], deoxyribose.position[1], phosphate.position[0], phosphate.position[1], fill="white", width=2)
                
                vertex_positions = deoxyribose.get_vertex_positions(deoxyribose.position[0], deoxyribose.position[1], deoxyribose_size)
                nearest_vertex = min(vertex_positions, key=lambda v: (v[0] - base.position[0])**2 + (v[1] - base.position[1])**2)
                canvas.create_line(base.position[0], base.position[1], nearest_vertex[0], nearest_vertex[1], fill="white", width=2)

                next_deoxyribose_pos = (next_base_pos_x + base_size // 2, initial_y + base_size + 50)
                canvas.create_line(phosphate.position[0], phosphate.position[1], next_deoxyribose_pos[0], next_deoxyribose_pos[1], fill="white", width=2)

            else: 
                vertex_positions = deoxyribose.get_vertex_positions(deoxyribose.position[0], deoxyribose.position[1], deoxyribose_size)
                nearest_vertex = min(vertex_positions, key=lambda v: (v[0] - base.position[0])**2 + (v[1] - base.position[1])**2)
                canvas.create_line(base.position[0], base.position[1], nearest_vertex[0], nearest_vertex[1], fill="white", width=2)

    for item in items:
        item.create_visual()