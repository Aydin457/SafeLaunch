import os
import json
from datetime import datetime

def save_results(data: dict, tool_name: str):
    """Save scan results in results/ folder as JSON"""
    if not os.path.exists("results"):
        os.makedirs("results")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"results/{tool_name}_{timestamp}.json"

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print(f"[+] Results saved to: {filename}")
