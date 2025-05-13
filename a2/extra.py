import zipfile
from datetime import date, timedelta

# --- 여기를 원하는 연도 범위로 수정하세요 ---
START_YEAR = 2000
END_YEAR   = 2025
# -----------------------------------------

def brute_force_zip_with_year(zip_path: str, start_year: int, end_year: int):
    zf = zipfile.ZipFile(zip_path)
    
    for year in range(start_year, end_year + 1):
        current = date(year, 1, 1)
        last_day = date(year, 12, 31)
        
        while current <= last_day:
            mmdd = current.strftime('%m%d')                   # MMDD 형식
            password = f"{year}{mmdd}20250929"                # YYYYMMDD20250929
            try:
                zf.extractall(pwd=password.encode('utf-8'))
                print(f"✅ 비밀번호 찾음: {password}")
                return True
            except RuntimeError:
                # 잘못된 비밀번호
                pass
            except zipfile.BadZipFile:
                print("❌ ZIP 파일이 손상되었습니다.")
                print(password)
                return False
            
            current += timedelta(days=1)
    
    print("❌ 비밀번호를 찾지 못했습니다.")
    return False

if __name__ == '__main__':
    zip_file = 'fun.zip'
    brute_force_zip_with_year(zip_file, START_YEAR, END_YEAR)
