def count_divisible_substrings_by_3(num_str):
    count = 0
    n = len(num_str)
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = num_str[i:j]
            print(sub)
            if int(sub) % 3 == 0:
                count += 1
    return count

numlist = ["456","6666"]
for item in numlist:
    print(f"{item} in {count_divisible_substrings_by_3(item)} substrings")
