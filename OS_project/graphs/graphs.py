import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import time

CSV_FILE = "/app/data/system_monitor.csv"   
MEMORY_PNG_FILE = "/app/data/memory_usage.png" 
CPU_PNG_FILE = "/app/data/cpu_usage.png"
DISK_PNG_FILE = "/app/data/disk_usage.png"
GPU_PNG_FILE = "/app/data/GPU_utilization.png"
rx_PNG_FILE = "/app/data/rx_bytes.png"
tx_PNG_FILE = "/app/data/tx_bytes.png"

while True:
    try:
        df = pd.read_csv(CSV_FILE)
        df['date'] = pd.to_datetime(df['date'])
        dates = df['date']
        graph_pngs = (MEMORY_PNG_FILE,CPU_PNG_FILE,DISK_PNG_FILE,GPU_PNG_FILE,rx_PNG_FILE,tx_PNG_FILE)

        for png in graph_pngs:
            pngname = png[10:len(png)-4]
            print("Generating graph for:", pngname)
            feature = df[pngname]
            plt.figure(figsize=(10,5), facecolor='black')
            ax = plt.gca()
            ax.set_facecolor('black')
            plt.plot(dates, feature, color='lime', linewidth=2)
            plt.title(f"{pngname} Usage Over Time", fontsize=16, color='lime')
            plt.xlabel("Time", fontsize=12, color='lime')
            plt.ylabel(f"{pngname} Usage (%)", fontsize=12, color='lime')
            plt.xticks(color='lime')
            plt.yticks(color='lime')
            plt.gcf().autofmt_xdate()
            plt.gca().xaxis.set_major_formatter(DateFormatter("%H:%M:%S"))
            plt.tight_layout()
            plt.savefig(png, facecolor='black')
            print(f"Graph saved to {png}")
            plt.close()
        time.sleep(2)
    except KeyboardInterrupt:
        print("Stopping graph update.")
        break
    except Exception as e:
        print("Error:", e)
        time.sleep(2)
