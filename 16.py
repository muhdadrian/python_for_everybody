while True:
    line = input("> ")
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line)
print("Done!")

"""
> hello there
hello there
> # don't print this
> print this!
print this!
> done
Done!
"""