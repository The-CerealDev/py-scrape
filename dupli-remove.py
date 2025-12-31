# Remove duplicate links from a text file

input_file = 'links_v2.txt'
output_file = 'linksv2 _cleaned.txt'

# Read all lines from the input file
with open(input_file, 'r') as f:
    lines = f.readlines()

# Remove duplicates while preserving order
seen = set()
unique_lines = []

for line in lines:
    # Strip whitespace for comparison but keep original formatting
    stripped = line.strip()
    
    # Skip empty lines and check if we've seen this link before
    if stripped and stripped not in seen:
        seen.add(stripped)
        unique_lines.append(line)

# Write unique lines to the output file
with open(output_file, 'w') as f:
    f.writelines(unique_lines)

print(f"Original file had {len(lines)} lines")
print(f"Cleaned file has {len(unique_lines)} unique lines")
print(f"Removed {len(lines) - len(unique_lines)} duplicates")
print(f"Cleaned file saved as '{output_file}'")