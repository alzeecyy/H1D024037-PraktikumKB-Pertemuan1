import random
import datetime

todo = []

print("=== Program To-Do List ===")

for i in range(3): 
    tugas = input("Tugasku: ")
    todo.append(tugas)

print("\nDaftar tugasku:")
for t in todo:
    print("-", t)

if len(todo) >= 3:
    print("List tugas kamu full")

print("Kerjain ini dulu aja:", random.choice(todo))
print("Waktu dibuat:", datetime.datetime.now())
