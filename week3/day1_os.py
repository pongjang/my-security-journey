import os
import time

print("시스템 정찰 시작...")

current_path = os.getcwd()
print(f"현재 위치:{current_path}")

print("3초 뒤에 현재 폴더의 파일 목록을 털어옵니다.")
time.sleep(3)

files = os.listdir(current_path)
print(f"발견된 파일들: {files}")

#제미니가 한것
print(os.name)

#내가 생각한것
name = os.name
print(f"현재 os는:{name}")
#더 잘했데~~~ 야호!! 