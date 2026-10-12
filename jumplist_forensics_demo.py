"""Educational synthetic Jump List investigation, inspired by Smith (2013).
No actual Windows Jump List files are parsed or altered.
"""
import csv
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from datetime import datetime, timedelta

EVENTS = [
    ("09:00", "Browser", "Downloaded organization logo", "C:/Users/Larry/Pictures/Car/headerSELogo.png", "Logo image", "106", "Low"),
    ("09:12", "Word", "Opened purchase order template", "C:/Users/Larry/AppData/Roaming/Microsoft/Templates/PurchaseOrder.dotx", "Template", "207", "Medium"),
    ("09:24", "Word", "Created purchase order", "C:/Users/Larry/Documents/PO-123.docx", "Document", "301", "High"),
    ("09:31", "Explorer", "Moved purchase order into unrelated folder", "C:/Users/Larry/Desktop/Forensic Course/PO-123.docx", "Document", "302", "High"),
    ("09:40", "Mail", "Sent purchase order to vendor (simulated)", "C:/Users/Larry/Desktop/Forensic Course/PO-123.docx", "Document", "—", "High"),
    ("09:45", "Explorer", "Deleted purchase order (simulated)", "C:/Users/Larry/Desktop/Forensic Course/PO-123.docx", "Document", "—", "High"),
]
# Artifact IDs 301 and 302, times, and paths are synthetic demonstration values.
# 106 and 207 are references to the paper's illustrated entries, not recovered evidence.

class App:
    def __init__(self, root):
        self.root = root
        root.title("Jump List Forensic Investigation — Research Demo")
        root.geometry("1120x760")
        root.minsize(820, 620)
        self.records = []
        self.selected = None
        self.status = tk.StringVar(value="Ready. Click 1 — Simulate Activity.")
        self.build()

    def build(self):
        top = ttk.Frame(self.root, padding=12)
        top.pack(fill="x")
        ttk.Label(top, text="JUMP LIST FORENSIC INVESTIGATION", font=("Arial", 19, "bold")).pack(anchor="w")
        ttk.Label(top, text="Research-inspired synthetic simulation | No actual Windows artifacts are read", foreground="#555").pack(anchor="w")
        buttons = ttk.Frame(self.root, padding=(12, 2))
        buttons.pack(fill="x")
        for name, action in [("1 — Simulate Activity", self.simulate), ("2 — Analyze Evidence", self.analyze),
                             ("3 — Show Graphs", self.graphs), ("4 — Export CSV", self.export), ("Reset", self.reset)]:
            ttk.Button(buttons, text=name, command=action).pack(side="left", padx=(0, 8), pady=5)
        columns = ("time", "application", "activity", "artifact", "risk")
        frame = ttk.LabelFrame(self.root, text="Forensic activity timeline (synthetic)", padding=8)
        frame.pack(fill="both", expand=True, padx=12, pady=7)
        self.tree = ttk.Treeview(frame, columns=columns, show="headings", height=11)
        for c, label, width in [("time", "Time", 95), ("application", "Application", 110),
                                ("activity", "Activity", 530), ("artifact", "Artifact #", 95), ("risk", "Risk", 85)]:
            self.tree.heading(c, text=label)
            self.tree.column(c, width=width, minwidth=60, stretch=(c == "activity"))
        scroll = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        self.tree.bind("<<TreeviewSelect>>", self.show_detail)
        details = ttk.LabelFrame(self.root, text="Artifact details / investigation findings", padding=10)
        details.pack(fill="both", expand=True, padx=12, pady=7)
        self.detail = tk.Text(details, height=9, wrap="word", font=("Consolas", 10))
        self.detail.pack(fill="both", expand=True)
        self.detail.insert("end", "Simulate activity to populate the timeline.\n")
        self.detail.configure(state="disabled")
        ttk.Label(self.root, textvariable=self.status, padding=(12, 6), relief="sunken", anchor="w").pack(fill="x")

    def set_detail(self, text):
        self.detail.configure(state="normal")
        self.detail.delete("1.0", "end")
        self.detail.insert("end", text)
        self.detail.configure(state="disabled")

    def simulate(self):
        self.records = [dict(time=t, application=a, activity=act, path=p, file_type=ft, artifact=art, risk=r)
                        for t, a, act, p, ft, art, r in EVENTS]
        self.tree.delete(*self.tree.get_children())
        for i, e in enumerate(self.records):
            self.tree.insert("", "end", iid=str(i), values=(e["time"], e["application"], e["activity"], e["artifact"], e["risk"]))
        self.set_detail("Six fictional activities generated.\n\nSelect a timeline entry to inspect its path and artifact ID.\nThen click 'Analyze Evidence' to reconstruct the sequence.")
        self.status.set("Simulation generated: 6 synthetic events. No real files created or deleted.")

    def show_detail(self, _event=None):
        ids = self.tree.selection()
        if not ids or not self.records:
            return
        e = self.records[int(ids[0])]
        self.set_detail("TIME: " + e["time"] + "\nAPPLICATION: " + e["application"] +
                        "\nACTIVITY: " + e["activity"] + "\nPATH: " + e["path"] +
                        "\nFILE TYPE: " + e["file_type"] + "\nARTIFACT ID: " + e["artifact"] +
                        "\nHEURISTIC RISK: " + e["risk"] + "\n\nAll records are fictional teaching examples.")

    def analyze(self):
        if not self.records:
            messagebox.showinfo("First step", "Click 'Simulate Activity' first.")
            return
        deleted = [e for e in self.records if "Deleted" in e["activity"]]
        related = [e for e in self.records if "purchase order" in e["activity"].lower()]
        findings = (
            "INVESTIGATION SUMMARY — SIMULATED DATA\n"
            "--------------------------------------\n"
            f"Total timeline events: {len(self.records)}\n"
            f"Purchase-order-related events: {len(related)}\n"
            f"Deletion events: {len(deleted)}\n"
            "Evidence chain: logo -> template -> document -> moved -> sent -> deleted\n\n"
            "FINDING: The simulated record still contains historical references to\n"
            "the purchase order after the fictional deletion event.\n\n"
            "IMPORTANT: A Jump List by itself does not prove that an email was sent,\n"
            "a file was deleted, who operated the machine, or that fraud occurred.\n"
            "Those claims require corroborating evidence (mail, filesystem, logs).\n"
            "This demonstration does not parse real .automaticDestinations-ms files."
        )
        self.set_detail(findings)
        self.status.set("Analysis complete: synthetic sequence reconstructed.")

    def graphs(self):
        if not self.records:
            messagebox.showinfo("First step", "Click 'Simulate Activity' first.")
            return
        try:
            import matplotlib.pyplot as plt
            from collections import Counter
        except ImportError:
            messagebox.showerror("Missing dependency", "Install matplotlib with: pip install matplotlib")
            return
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 8), constrained_layout=True)
        times = [datetime.strptime(e["time"], "%H:%M") for e in self.records]
        x = [(t - times[0]).total_seconds() / 60 for t in times]
        ax1.scatter(x, [1] * len(x), s=105, zorder=3)
        ax1.plot(x, [1] * len(x), linewidth=1, alpha=.5)
        for i, (xx, e) in enumerate(zip(x, self.records)):
            label = e["activity"].replace(" (simulated)", "")
            ax1.annotate(f"{e['time']}  {label}", (xx, 1), xytext=(0, 15 if i % 2 == 0 else -25),
                         textcoords="offset points", ha="center", fontsize=8, rotation=12)
        ax1.set_xlim(-12, max(x) + 12)
        ax1.set_ylim(.65, 1.35)
        ax1.set_yticks([])
        ax1.set_xlabel("Minutes since first activity")
        ax1.set_title("Synthetic evidence timeline")
        ax1.grid(axis="x", alpha=.25)
        counts = Counter(e["application"] for e in self.records)
        ax2.bar(list(counts), list(counts.values()))
        ax2.set_ylabel("Number of simulated events")
        ax2.set_title("Events by application")
        ax2.set_ylim(0, max(counts.values()) + 1)
        fig.suptitle("Jump List Forensic Investigation — Educational Simulation", fontsize=14)
        plt.show()
        self.status.set("Graph window opened.")

    def export(self):
        if not self.records:
            messagebox.showinfo("First step", "Click 'Simulate Activity' first.")
            return
        path = filedialog.asksaveasfilename(defaultextension=".csv", initialfile="synthetic_forensic_timeline.csv",
                                            filetypes=[("CSV files", "*.csv")])
        if not path:
            return
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(self.records[0]))
            writer.writeheader()
            writer.writerows(self.records)
        self.status.set("Synthetic report exported to " + path)
        messagebox.showinfo("Export complete", "CSV report saved successfully.")

    def reset(self):
        self.records = []
        self.tree.delete(*self.tree.get_children())
        self.set_detail("Reset complete. Click 'Simulate Activity' to begin.")
        self.status.set("Ready.")

if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
