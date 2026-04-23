# Remove duplicate links from a text file or csv
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import *

input_file = SCRAPE_CSV
output_file = "test.csv"


with open(input_file, 'r') as f:
    lines = f.readlines()


seen = set()
unique_lines = []

for line in lines:
    
    stripped = line.strip()
    
    
    if stripped and stripped not in seen:
        seen.add(stripped)
        unique_lines.append(line)


with open(output_file, 'w') as f:
    f.writelines(unique_lines)

print(f"Original file had {len(lines)} lines")
print(f"Cleaned file has {len(unique_lines)} unique lines")
print(f"Removed {len(lines) - len(unique_lines)} duplicates")
print(f"Cleaned file saved as '{output_file}'")