vulnerabilities = ["SQL injection", "XSS", "Weak Password"]

with open("report.txt", "w", encoding="utf-8") as f:
    f.write("security scan report:2025-11-20\n")
    f.write("-" * 30 + "\n")

    count =1
    for bug in vulnerabilities:
        f.write(f"{count}. {bug}\n")
        count = count + 1

    f.write("\n[complit]")
print("report complite check report.txt")

try:
    with open("없는파일.txt", "r") as f:
        print(f.read())

except FileNotFoundError:
    print("not found file check file")