a= input("날짜 (연:월:일)를 입력하세요")
b=a.split(":")

print("10년후 날짜:", end="")
print(str(int(b[0])+15)+":"+b[1]+":"+b[2])
