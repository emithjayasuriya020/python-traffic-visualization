# Traffic Data Analyzer 🚦📊

**A Python-based data analysis and visualization tool that processes raw traffic CSV logs from two major junctions. It calculates key real-world statistics—such as peak hours, speeding violations, and vehicle type distributions—and generates an interactive graphical histogram to visualize daily traffic flow.**

## 📖 About This Project
Welcome to my Traffic Data Analyzer! This repository showcases an old coursework project I developed to demonstrate my foundational skills in Python programming, data processing, and graphical user interface (GUI) design. 

The primary goal of this program is to process and analyze raw daily traffic logs from two busy intersections: **Elm Avenue/Rabbit Road** and **Hanley Highway/Westway**. Using Python, the script reads extensive CSV datasets containing individual vehicle movements and extracts meaningful real-world statistics. It calculates metrics such as total vehicle counts, speeding violations, vehicle type distributions (e.g., trucks, electric vehicles, scooters), and peak traffic hours.

Beyond terminal-based data processing and automated text logging, this project features an interactive visual component built with Python's `tkinter` library. It generates a full-screen histogram that provides a clear visual representation of hourly vehicle frequency across both junctions. It also includes a continuous multi-file processing loop, allowing users to analyze multiple datasets seamlessly without restarting the application.

This coursework serves as a great milestone in my coding journey, highlighting my ability to turn raw tabular data into actionable insights and interactive visual dashboards.

## ✨ Features
* **Robust Input Validation:** Prompts the user for a specific date and validates the day, month, and year formats before execution.
* **In-Depth Data Processing:** Parses raw CSV data to calculate:
  * Total vehicle counts, including breakdowns by type (trucks, electric vehicles, two-wheelers).
  * Specific directional flow (e.g., buses leaving Elm Avenue heading North).
  * The number of vehicles exceeding the junction speed limits.
  * Peak traffic hours and weather-related metrics (e.g., total hours of rain).
* **Automated Reporting:** Outputs formatted statistical results directly to the console and appends them to a persistent `results.txt` file.
* **Graphical Visualization:** Uses Python's `tkinter` library to generate an interactive, full-screen histogram displaying the frequency of vehicles per hour for both junctions.
* **Continuous Execution:** Features a multi-file processing loop, allowing users to load and analyze new CSV datasets without having to restart the application.

## 🛠️ Technologies Used
* **Language:** Python 3
* **Libraries:** `tkinter` (for the GUI), `csv` (for data parsing)

## 📂 Repository Structure
* `Main_DE_w2120207.py`: The main entry point of the program. Handles the Tkinter GUI (HistogramApp) and the continuous multi-file processing logic.
* `Sub_ABC_w2120207.py`: Contains the core functional logic for input validation, CSV data extraction, calculations, and text-based reporting.
* `traffic_data*.csv`: Sample datasets containing raw vehicle logs for specific dates (e.g., `traffic_data15062024.csv`).
* `results.txt`: The output file where the processed statistical reports are continuously saved.
* `Psuedo_Code_DE.pdf`: Step-by-step logical planning for the GUI and multi-file processing.
* `Test_Cases_*.pdf`: Documented test runs showing expected console outputs and GUI screenshots to verify the code's functionality.

## 🚀 How to Run

1. **Prerequisites:** Ensure you have Python 3 installed on your system. (`tkinter` is usually included with standard Python installations).
2. **Clone the repository:**
   ```bash
   git clone [https://github.com/emithjayasuriya020/traffic-data-analyzer.git](https://github.com/yourusername/traffic-data-analyzer.git)
   cd traffic-data-analyzer
3. Ensure data files are present: Make sure your traffic_data*.csv files are located in the same root directory as the Python scripts.
4. Run the main script:
       python Main_DE_w2120207.py
5. Follow the prompts: Enter the day, month, and year (e.g., 15, 06, 2024) of the dataset you wish to analyze when prompted in the terminal.
