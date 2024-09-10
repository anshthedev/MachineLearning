import os


directory = '/Users/ansh/Downloads/S Nallamothu and C Culbertson 2023'

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    print(f)

    if os.path.isdir(f):
        for filename2 in os.listdir(f):
            f2 = os.path.join(f, filename2)

            print(f2)

            if os.path.isdir(f2):
                for filename3 in os.listdir(f2):
                    f3 = os.path.join(f2, filename3)

                    print(f3)

