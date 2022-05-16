import os

def getRating(rules: list[int] = None):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    directory = f"{dir_path}\\test_results"
    results = []
    for filename in os.listdir(directory):
        if rules is None or int(filename.split('_')[1]) in rules:
            filePath = os.path.join(directory, filename)
            # checking if it is a file
            if os.path.isfile(filePath):
                with open(filePath, "r") as file:
                    text = file.read().split("SUMMARY")[1]
                    values = text.replace('-', '').replace('\n', ' ').split()
                    failedTests = []
                    for i in range(len(values) // 3):
                        if values[i * 3 + 2] == "FAIL":
                            failedTests.append(values[i * 3])

                    results.append((filename.split('.')[0], 15 - len(failedTests), failedTests))

    results.sort(key=lambda x: x[1])
    results.reverse()

    for res in results:
        print(res[0], "-", res[1], "failed:", res[2])
