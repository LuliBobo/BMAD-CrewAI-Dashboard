import json
import re

with open("kartago_sample.html", "r") as f:
    text = f.read()

# look for common injected state variables
matches = re.findall(r'window\.__[A-Z_]+__\s*=\s*({.*?});', text, re.DOTALL)
if matches:
    print(f"Found {len(matches)} injected states.")
    for m in matches:
        print("Length:", len(m))
        if "hotel" in m.lower():
            print("Contains 'hotel'")
else:
    print("No injected state found.")
