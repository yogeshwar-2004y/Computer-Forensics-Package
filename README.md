# Jump List Forensic Investigation Simulator

A Windows-friendly Python desktop demonstration inspired by the research paper **â€œUsing Jump Lists to Identify Fraudulent Documentsâ€** by G. Stevenson Smith, published in *Digital Investigation*, 9 (2013), pp. 193â€“199.

> **Educational simulation only:** This application uses six fictional events. It does **not** parse actual Windows Jump List artifacts, access personal files, send email, or delete documents. The risk labels are illustrative, not forensic conclusions.

## Project objective

Demonstrate how an investigator can organize historical file-activity references into a timeline when examining a potentially fraudulent purchase order. The research paper discusses a hypothetical case involving a downloaded logo, a Word purchase-order template, a completed document stored in an unrelated folder, and later deletion.

## Features

- Tkinter desktop dashboard with a selectable event table
- Six simulated activities involving a logo, template, purchase order, relocation, sending, and deletion
- Evidence-detail viewer with fictional paths and artifact identifiers
- Investigation summary with counts and evidence-chain narrative
- Matplotlib timeline and application-activity bar chart
- CSV export for review in Excel
- Reset button to repeat the demonstration

## Files

```text
JumpList_Forensics/
â”œâ”€â”€ jumplist_forensics_demo.py    # Main Python application
â”œâ”€â”€ requirements_jumplist.txt    # Python package dependency
â””â”€â”€ README.md                    # Setup and demo instructions
```

## Requirements

- Windows 10 or 11
- Python 3.9 or newer (standard installation with Tkinter)
- Visual Studio Code (optional but recommended)
- Matplotlib 3.7 or newer

## Installation on Windows with VS Code

1. Download all three project files into a folder named `JumpList_Forensics`.
2. Open VS Code and choose **File â†’ Open Folder**; select that folder.
3. Open **Terminal â†’ New Terminal**.
4. Confirm Python is available:

   ```powershell
   py --version
   ```

5. Install the dependency:

   ```powershell
   py -m pip install -r requirements_jumplist.txt
   ```

6. Start the desktop application:

   ```powershell
   py jumplist_forensics_demo.py
   ```

If `py` is unavailable but `python` works, replace `py` with `python` in the commands. If Python is missing, install it from https://www.python.org/downloads/windows/ and restart VS Code.

## Live demonstration sequence

1. **1 â€” Simulate Activity:** Populate the table with six fictional events. Click an event to show its timestamp, application, file path, artifact ID, and heuristic risk label.
2. **2 â€” Analyze Evidence:** Display the investigation summary and reconstructed sequence.
3. **3 â€” Show Graphs:** Open a Matplotlib window containing the synthetic activity timeline and the count of events by application. Close the graph window to return to the dashboard.
4. **4 â€” Export CSV:** Save `synthetic_forensic_timeline.csv`, then open it in Excel to show the evidence table.
5. **Reset:** Clear the table and repeat the demo if needed.

### Sample events

| Time | Application | Simulated activity | Risk |
|---|---|---|---|
| 09:00 | Browser | Downloaded organization logo | Low |
| 09:12 | Word | Opened purchase-order template | Medium |
| 09:24 | Word | Created purchase order | High |
| 09:31 | Explorer | Moved purchase order to unrelated folder | High |
| 09:40 | Mail | Sent purchase order to vendor (simulated) | High |
| 09:45 | Explorer | Deleted purchase order (simulated) | High |

The demo references artifact IDs **106** and **207**, corresponding to examples discussed in the paper. Other IDs, times, paths, and events are synthetic; none were extracted from a real computer.

## How this connects to the paper

- **Figure 3:** An artifact related to a downloaded organization logo.
- **Figure 5:** An artifact related to a Microsoft Word purchase-order template.
- **Figure 6:** An artifact identifying the completed document's location in an unrelated desktop folder.

The program visualizes a simplified, synthetic reconstruction of this investigative narrative. It is **not** a reproduction of the JumpLister tool shown in the paper.

## Suggested presentation explanation

> â€œThis Python implementation demonstrates the forensic investigation workflow described in the research paper. I simulate a sequence of suspicious document activities, inspect the associated fictional records, reconstruct their timeline, visualize application activity, and export a report. The goal is to show why historical file references can be useful even after a document is removed. This demonstration does not perform actual Windows Jump List acquisition or parsing.â€

## Troubleshooting

| Issue | Fix |
|---|---|
| `py` not recognized | Install Python or try `python` instead. |
| `No module named matplotlib` | Run `py -m pip install -r requirements_jumplist.txt`. |
| `No module named tkinter` | Install a standard Windows Python build with Tcl/Tk support. |
| Graphs or analysis do not appear | Click **1 â€” Simulate Activity** first. |
| Script not found | Ensure the terminal is open in the project folder. |
| Graph window blocks the dashboard | Close the Matplotlib window to return to the Tkinter interface. |

## Forensic limitations

Real Windows Jump Lists are typically stored in files such as `*.automaticDestinations-ms` and `*.customDestinations-ms`. This demo **does not** read or parse them. A Jump List reference alone cannot establish that an email was sent, a document was deleted, who used the computer, or that fraud occurred. Those conclusions require corroboration from filesystem metadata, email evidence, logs, and other sources. Preserve original evidence and document acquisition methods in a real investigation.

## Reference

Smith, G. Stevenson. â€œUsing jump lists to identify fraudulent documents.â€ *Digital Investigation*, vol. 9, 2013, pp. 193â€“199. DOI: https://doi.org/10.1016/j.diin.2012.11.002