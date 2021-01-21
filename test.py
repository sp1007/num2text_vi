import sys
import num2text_vi

test_numbers = ["123456789", "100", "101", "104", "105", "15", "115", "2000", "30000", "400000", "5000000", "60000000", "700000000", "8000000000", "90000000000", "114552123225", "980000000234", "109820983511231", "1155441144414", "34586709348576112409000001"]

test_floats = ["145.12", "+79879.34423", "-568.34574568406"]

test_doubles = ["1723687125.1251E-54", "-982352.4347345e34235.12351", "9839234e-2938792336236.2124", "0.34235e-100001"]

for n in test_numbers:
    t = n + ": " + num2text_vi.uintStr2Str(n, False) + "\n"
    sys.stdout.buffer.write(t.encode('utf8'))

for n in test_floats:
    t = n + ": " + num2text_vi.floatStr2Str(n, ".") + "\n"
    sys.stdout.buffer.write(t.encode('utf8'))    

for n in test_doubles:
    t = n + ": " + num2text_vi.doubleStr2Str(n, ".") + "\n"
    sys.stdout.buffer.write(t.encode('utf8'))  