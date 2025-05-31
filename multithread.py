import threading


def coder(row, col):
    print(f'Coder ID: ({row}, {col})')

threads = []
for i in range(1, 5):
    for j in range(1, 5):
        t = threading.Thread(target=coder, args=(i, j))
        threads.append(t)
        t.start()

for t in threads:
    t.join()
