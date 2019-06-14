# 다음과 같은 텍스트에서 모든 태그를 제외한 텍스트만 출력하세요.

s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
        	To connect to the most powerful tools in the world.
        </p>
    </body>
</html>"""

counts = s.count("<")

for i in range(0,counts):
    startIdx = s.find("<")
    endIdx = s.find(">")
    s = s.replace(s[startIdx:endIdx+1], "")
print(s)