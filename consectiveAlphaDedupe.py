def dedupe(s):
    seen =set()
    result=[]
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

inputString = "Hello World"
out = dedupe(inputString)
print("ORIGINAL STRING:",inputString)
print("DEDUPED STRING:",out)


