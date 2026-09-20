# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    question = '03'

    with open(f"{question}.in.txt", "r") as f:
        N = int(f.readline())
        A = f.readline().split()
        A = list(map(int, A))
        print(N, A)

        find = 1

        for Ai in A:
            print(Ai)
            if Ai == find:
                print('됨')
                find += 1
            else:
                print('안됨')
        i = find - 1
        print('답',N-i)
        with open(f"{question}.out.txt", "w+") as f2:
            f2.write(str(N-i))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
