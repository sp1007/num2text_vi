import sys
from num2text_vi import _uintStr2Str

test_numbers = ["123456789", "100", "101", "104", "105", "15", "115", "2000", "30000", "400000", "5000000", "60000000", "700000000", "8000000000", "90000000000", "114552123225", "109820983511231", "1155441144414", "34586709348576112409000001"]

for n in test_numbers:
    t = n + ": " + _uintStr2Str(n, False) + "\n"
    sys.stdout.buffer.write(t.encode('utf8'))