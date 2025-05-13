from zipfile import ZipFile

def extract_metadata(zip_path):
    # ZIP 파일 열기
    with ZipFile(zip_path) as z:
        metadata = []
        
        # 모든 파일에 대해 extra field 추출
        for info in z.infolist():
            if info.extra:
                print(f"Filename: {info.filename}, Extra field: {info.extra.hex()}")
                metadata.append(info.extra)

        return metadata

def process_metadata(metadata):
    # 메타데이터를 분석하여 비밀번호를 찾는 과정
    # 여기서는 예시로 extra field에서 추출된 값을 OR 연산 없이 바로 확인
    combined_data = b''.join(metadata)
    
    # byte 데이터를 ASCII로 변환 시도
    try:
        password = combined_data.decode('ascii')
    except UnicodeDecodeError:
        # 만약 ASCII로 변환 불가능하면 latin1으로 시도
        password = combined_data.decode('latin1', errors='replace')
    
    return password

if __name__ == "__main__":
    zip_path = 'fun.zip'  # ZIP 파일 경로
    metadata = extract_metadata(zip_path)
    password = process_metadata(metadata)
    print("Recovered password:", password)
