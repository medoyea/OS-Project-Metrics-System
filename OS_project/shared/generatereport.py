import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import qrcode

df = pd.read_csv("/shared/system_monitor.csv")
styles = getSampleStyleSheet()
story = [Paragraph(df["date"].iloc[-1], styles["Title"]),
         Paragraph(f"Uptime: {df['uptime'].iloc[-1]}", styles["Normal"]),
         Spacer(1, 12)]

for title, col in [("CPU Usage (%)", "cpu_usage"), ("Memory Usage (%)", "memory_usage"), ("Disk Usage (%)", "disk_usage"), ("GPU_utilization (% )", "GPU_utilization"), ("Network RX Usage", "rx_bytes"), ("Network TX Usage", "tx_bytes")]:
    story += [Paragraph(title, styles["Heading2"]),
              Paragraph(f"Max: {df[col].max():.2f}", styles["Normal"]),
              Paragraph(f"Min: {df[col].min():.2f}", styles["Normal"]),
              Paragraph(f"Average: {df[col].mean():.2f}", styles["Normal"]),
              Spacer(1, 12)]

SimpleDocTemplate("/shared/report.pdf").build(story)
qrcode.make("http://192.168.100.16:8000/report").save("/shared/pdf_qr.png")
