# 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요
s = '/usr/local/bin/python'
result = s.split("/")
result.pop(0)
print(result)
print(s.rsplit('/', 1))
