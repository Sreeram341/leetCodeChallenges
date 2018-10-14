"""
Minimum 8 characters.
The alphabets must be between [a-z]
At least one alphabet should be of Upper Case [A-Z]
At least 1 number or digit between [0-9].
At least 1 character from [ _ or @ or $ ].
"""

import re

print(re.findall('(?=[^_@$])(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,16}',"sreeramP_$6"))