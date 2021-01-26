import sys
import num2text_vi

test_numbers = ["123456789", "100", "101", "104", "105", "15", "115", "2000", "30000", "400000", "5000000", "60000000", "700000000", "8000000000", "90000000000", "114552123225", "980000000234", "109820983511231", "1155441144414", "34586709348576112409000001", '1000000000000', '1000000000001', '10000000000000000000001', "145.12", "+79879.34423", "-568.34574568406", "1723687125.1251E-54", "-982352.4347345e34235.12351", "9839234e-2938792336236.2124", "0.34235e-100001", "100.000001", "3.000001", "0000002345", "0000000000"]

for n in test_numbers:
    t = n + ": " + num2text_vi.doubleStr2Str(n, ".") + "\n"
    sys.stdout.buffer.write(t.encode('utf8'))  

test_str = 'tại thời điểm 122:14:15,123, 12/12/2020, chúng tôi đã tới 06:30, 07H44 05/01 22:14:15'
test_Str2 = "Test so: 123.235.564,12e543.643,76m/s, 0,1d, 1vnd, 123.123,12lm, 234.234,12km, 345.345.3456,12345678m, 113kg, 114g, 1511,12k, 123b, 2kb, 5mb, 6gb, 124tb, -19°c, +90°k, 545dm, 23cm, -534mm, 502mg, 250va, 1200W, 120km/h, 10m/s, 33,22kg/m3, 77,99m3/s, 45°80′323″, 60kΩ, 21ºC, 18°, 19°, Gió Đông Nam đến Đông cấp 2-3, 14 – 19 độ, 25-26/1, Dự báo thời tiết đêm nay và ngày mai (25-26/1), Nhiệt độ cao nhất: 30-33 độ. 123.346.754.352.236.763e125.532.234"
test_Str3 = "I II III IV V VI VII VIII IX X XI XII XIII XIV XV XVI XVII XVIII XIX XX XXI XXII XXIII XXIV XXV XXVI"
t = num2text_vi.normalize_numbers(test_Str2 + " ---> " + test_Str3)
sys.stdout.buffer.write(t.encode('utf8'))