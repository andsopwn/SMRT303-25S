from datetime import datetime, timedelta

def filetime_to_datetime(filetime):
    # FILETIME은 1601년 1월 1일부터의 100ns 단위
    base = datetime(1601, 1, 1)
    delta = timedelta(microseconds=filetime // 10)
    return base + delta

def extract_password_from_metadata(hex_data):
    # FILETIME 추출
    filetime_hex = hex_data[8:24]
    filetime = int.from_bytes(bytes.fromhex(filetime_hex), 'little')
    
    # FILETIME -> 날짜로 변환
    dt = filetime_to_datetime(filetime)
    # 비밀번호 형식으로 변환
    password = dt.strftime('%Y%m%d%H%M%S')
    
    return password

# 주어진 데이터
hex_data = "0a0020000000000001001800002c761686acdb0100000000000000000000000000000000"
password = extract_password_from_metadata(hex_data)
print("Extracted password:", password)
