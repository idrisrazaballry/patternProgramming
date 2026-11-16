'''
------d------
----d-c-d----
--d-c-b-c-d--
d-c-b-a-b-c-d
--d-c-b-c-d--
----d-c-d----
------d------
'''
n = 4
alpha = [chr(97 + i) for i in range(n)] # ['a', 'b', 'c', 'd']
lines = []

for i in range(n):
    # Slice letters from nth down to current, then mirror back
    s = "-".join(alpha[n - 1 : i : -1] + alpha[i:n])
    lines.append(s.center(4 * n - 3, "-"))

# Combine top half (reversed) and bottom half
full_rangoli = lines[::-1] + lines[1:]
print("\n".join(full_rangoli))

