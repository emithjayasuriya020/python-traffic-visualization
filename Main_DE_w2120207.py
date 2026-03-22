import tkinter as tk

import Sub_ABC_w2120207
from Sub_ABC_w2120207 import *

class HistogramApp:
    def __init__(self, traffic_data, date):
        self.traffic_data = traffic_data
        self.date = date
        self.root = tk.Tk()
        self.canvas = None

    # Referance: https://www.geeksforgeeks.org/python-tkinter-canvas-widget/
    def setup_window(self):
        self.root.title(f"Histogram")
        self.root.geometry("1920x1080")
        self.canvas = tk.Canvas(self.root, width=1920, height=1080, bg="white")
        self.canvas.pack()

    def draw_histogram(self):
        junctions = ["Elm Avenue/Rabbit Road", "Hanley Highway/Westway"]
        hourly_data = {junction: [0] * 24 for junction in junctions}

        for row in self.traffic_data:
            hour = int(row['timeOfDay'].split(':')[0])
            if row['JunctionName'] in hourly_data:
                hourly_data[row['JunctionName']][hour] += 1

        max_count = max(max(hourly_data[junction]) for junction in junctions)
        bar_width = 30
        spacing = 70
        x_start = 100
        y_start = 600

        title = f"Histogram of Vehicle Frequency per Hour ({filex})"
        self.canvas.create_text(450, 50, text=title, font=("Arial", 20, "bold"))

        self.canvas.create_line(x_start, y_start, 1750, y_start, width=2)  # X-axis

        colors = ["palegreen", "salmon"]
        for j, junction in enumerate(junctions):
            for hour, count in enumerate(hourly_data[junction]):
                x0 = x_start + hour * spacing + j * bar_width
                y0 = y_start - (count / max_count * 400) if max_count > 0 else y_start
                x1 = x0 + bar_width
                y1 = y_start
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=colors[j])

                text_x = x0 + bar_width / 2
                text_y = y0 - 10
                self.canvas.create_text(text_x, text_y, text=str(count), anchor="s", font=("Arial", 10))

        self.canvas.create_text(1000, 650, text="Hours 00:00 to 24:00", font=("Arial", 11))

        for hour in range(24):
            x_pos = x_start + hour * spacing + bar_width // 2
            self.canvas.create_text(x_pos + 10, y_start + 20, text=f"{hour:02}", angle=0)

    # Referance: https://www.geeksforgeeks.org/python-tkinter-create-different-shapes-using-canvas-class/
    def add_legend(self):
        self.canvas.create_rectangle(100, 120, 120, 140, fill="palegreen")
        self.canvas.create_text(130, 130, anchor="w", text="Elm Avenue/Rabbit Road")
        self.canvas.create_rectangle(100, 150, 120, 170, fill="salmon")
        self.canvas.create_text(130, 160, anchor="w", text="Hanley Highway/Westway")

    def run(self):
        self.setup_window()
        self.draw_histogram()
        self.add_legend()
        self.root.mainloop()


class MultiCSVProcessor:
    def __init__(self):
        self.current_data = []

    def load_csv_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                csv_reader = csv.DictReader(file)
                self.current_data = list(csv_reader)
        except FileNotFoundError:
            print(f"Error: File {file_path} not found.")

    def clear_previous_data(self):
        self.current_data = []

    def handle_user_interaction(self):
        while True:
            self.load_csv_file(filename)
            # Referance: https://www.w3schools.com/python/python_classes.asp
            if self.current_data:
                histogram = HistogramApp(self.current_data, date_str)
                histogram.run()

            user_input = "N"
            if user_input == 'N'.lower():
                print("Exiting program.")
                break
            elif user_input == 'y'.lower():
                self.clear_previous_data()
            else:
                print("Exiting program.")
                break

    def process_files(self):
        self.handle_user_interaction()


if __name__ == "__main__":
    while True:
        date_str, filex = Sub_ABC_w2120207.validate_date_input()
        filename = f"traffic_data{date_str}.csv"
        outcomes = Sub_ABC_w2120207.process_csv_data(filename)
        if outcomes:
            Sub_ABC_w2120207.display_outcomes(outcomes)
            Sub_ABC_w2120207.save_results_to_file(outcomes, file_name="results.txt")
            processor = MultiCSVProcessor()
            processor.process_files()
        if not Sub_ABC_w2120207.validate_continue_input():
            break
