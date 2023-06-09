import os
import re
matches = set()
for filename in ['index.qmd', *[f"chapters/{f}" for f in os.listdir('chapters/') if f.endswith('.qmd')]]:
    with open(filename, 'r') as infile:
        for line in infile:
            match = re.search('\([A-Z]+\)', line)
            if match:
                matches.add(match.group(0).strip('(').strip(')'))
print('Acronyms detected','-----------------',
      *sorted(matches), sep='\n')
