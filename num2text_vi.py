import re


# định nghĩa các yếu tố cấn thiết
_UNITS = [ "mươi", "trăm", "nghìn", "mươi", "trăm", "triệu", "mươi", "trăm", "tỷ" ]
_LETTERS = {"0":"không", "1":"một", "2":"hai", "3":"ba", "4":"bốn", "5":"năm", "6":"sáu", "7":"bảy", "8":"tám", "9":"chín"}

_full_date_re = re.compile(r'(\d{1,2})/(\d{1,2})/(\d{1,4})')
_short_date_re = re.compile(r'(\d{1,2})/(\d{1,2})')
_full_time_re = re.compile(r'(\d+):(\d{1,2}):(\d{1,2})')
_short_time1_re = re.compile(r'(\d+):(\d{1,2})')
_short_time2_re = re.compile(r'(\d+)h(\d{1,2})')

def uintStr2Str(input:str, isSingle=False):
    # định nghĩa kết quả trả về
    result = ""
    # bắt đầu xử lý từng kí tự trong chuỗi
    if isinstance(input, str) and len(input)>0:
        # nếu chỉ là lấy các chữ số thông thường
        if isSingle==True:
            for c in input:
                if (c in _LETTERS):
                    result += " " + _LETTERS[c]
                else:
                    result = ""
                    break
        # không thì thực hiện chuyển số sang chữ
        else:
            # strip leading zero
            if (len(input)>1):
                input = input.lstrip('0')
            # kiểm tra độ dài input sau khi loại trừ số 0 ở đầu chuỗi
            if input is None or len(input)==0:
                return "không"
            # độ dài chuỗi đầu vào
            inputLength = len(input)
            # đếm kí tự
            idx = 0;
            for c in input:
                if (c in _LETTERS):
                    #
                    bilCount = (inputLength - 1 - idx) // 9
                    # xác định hàng đơn vị
                    unitIdx = (inputLength - 2 - idx) % len(_UNITS)
                    if unitIdx < 0: 
                        unitIdx = len(_UNITS) - 1
                    # chữ số và đơn vị hiện tại
                    num = _LETTERS[c]
                    unit = _UNITS[unitIdx]
                    # xem xét hàng đơn vị trước
                    if idx == inputLength - 1:
                        unit = None
                        if c=='0':
                            if idx>0:
                                num = None
                        elif c == '1':
                            if idx>0 and input[idx-1] != "1" and input[idx-1] != '0':
                                num = "mốt"
                        elif c=='4':
                            if idx>0 and input[idx-1]!='1' and input[idx-1]!='0': # and input[idx-1]!='2' and input[idx-1]!='4':
                                num = "tư"
                        elif c=='5':
                            if idx>0 and input[idx-1]!='0':
                                num = "lăm"
                    # xem xét số tại các vị trí khác
                    else:
                        if unitIdx==0 or unitIdx==3 or unitIdx==6:
                            if c=='0':
                                if idx+1 < inputLength and input[idx+1]!='0':
                                    num = "linh"
                                    unit = None
                                else:
                                    num = None
                                    unit = None
                            elif c=='1':
                                num = "mười"
                                unit = None
                        elif unitIdx==1 or unitIdx==4 or unitIdx==7:
                            if c=='0' and idx+2<inputLength and input[idx+1]=='0' and input[idx+2]=='0':
                                num = None
                                unit = None
                        elif unitIdx==2 or unitIdx==5 or unitIdx==8:
                            # sửa đơn vị nghìn/triệu/tỷ tỷ
                            if bilCount>0 and unitIdx==8 and (idx<2 or input[idx-1]!='0' or input[idx-2]!='0'):
                                for i in range(0, bilCount -1):
                                    unit += " tỷ"
                            if idx>0:
                                if c=='0':
                                    num = None
                                    if unitIdx != 8:
                                        if idx>1 and input[idx-1]=='0' and input[idx-2]=='0':
                                            unit = None
                                elif c=='1':
                                    if input[idx-1]!='0' and input[idx-1]!='1':
                                        num = "mốt"
                                elif c=='4':
                                    if input[idx-1]!='0' and input[idx-1]!='1': #  and input[idx -1]!='2' and input[idx -1]!='4':
                                        num = "tư"
                                elif c=='5':
                                    if input[idx-1]!='0':
                                        num = "lăm"
                            if unit is not None:
                                pass
                    # thêm số vào kết quả
                    if num is not None:
                        result += " " + num
                    # thêm đơn vị vào kết quả
                    if unit is not None:
                        result += " " + unit;
                else:
                    result = ""
                    break
                # tăng biến đếm
                idx +=1
    # trả về kết quả
    return result.strip()


def floatStr2Str(input:str, dot=",", isPoweredNumber=False):
    result = ""
    if len(input)>0:
        signStr = ""
        if input[0]=='-':
            if isPoweredNumber==True:
                signStr = "trừ "
            else:
                signStr = "âm "
            input = input[1:]
        elif input[0]=='+':
            signStr = "dương "
            input = input[1:]
        parts = input.split(dot)
        if len(parts)>1:
            result = signStr + uintStr2Str(parts[0]) + " phẩy " + uintStr2Str(parts[1], True)
        else:
            result = signStr + uintStr2Str(parts[0])
    return result


def doubleStr2Str(input:str, dot=","):
    input = input.lower()
    parts = input.split("e")
    if (len(parts)>1):
        return floatStr2Str(parts[0], dot) + " nhân mười mũ " + floatStr2Str(parts[1], dot, True)
    else:
        return floatStr2Str(parts[0], dot)


# replace 00/00/0000
def _replace_full_date(m):
    return "ngày " + doubleStr2Str(m.group(1)) + " tháng " + doubleStr2Str(m.group(2)) + " năm " + doubleStr2Str(m.group(3))


# replace 00/00/0000
def _replace_short_date(m):
    return "ngày " + doubleStr2Str(m.group(1)) + " tháng " + doubleStr2Str(m.group(2))   


# replace 000:00:00
def _replace_full_time(m):
    return doubleStr2Str(m.group(1)) + " giờ " + doubleStr2Str(m.group(2)) + " phút " + doubleStr2Str(m.group(3)) + " giây"


# replace 000:00
def _replace_short_time_1(m):
    return doubleStr2Str(m.group(1)) + " giờ " + doubleStr2Str(m.group(2)) + " phút"


# replace 000h00
def _replace_short_time_2(m):
    return doubleStr2Str(m.group(1)) + " giờ " + doubleStr2Str(m.group(2)) + " phút"       


def normalize_numbers(text:str):
    # lower
    text = text.lower()
    # full date
    text = re.sub(_full_date_re, _replace_full_date, text)
    text = re.sub(_short_date_re, _replace_short_date, text)
    # full time
    text = re.sub(_full_time_re, _replace_full_time, text)
    # short time
    text = re.sub(_short_time1_re, _replace_short_time_1, text)
    text = re.sub(_short_time2_re, _replace_short_time_2, text)
    # return result
    return text