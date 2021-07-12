values = []
# Test every possible value for A
for A in range(1, 21, 1):
    # Reject any even values
    if A % 2 == 0: 
        continue
    # Test every possible value for B
    for B in range(1, 21, 1): 
        if B % 2 == 0:
            continue
        TmpA = A
        TmpB = B
        max_years = 0
		# Keep adding A to TmpA and B to TmpB until they are within 1 of each other
        while True:
            if TmpA - TmpB == 1 or TmpA - TmpB == 0:
                max_years = TmpA
                break
            elif TmpA - TmpB == -1:
                max_years = TmpB
                break
            elif TmpA > TmpB:
                TmpB += B
            elif TmpA < TmpB:
                TmpA += A
        values.append((f"A: {A}, B: {B}", max_years))
		
# Find the largest value in the list
years = []
max_years = 0
for item in values:
    if item[1] > max_years:
        max_years = item[1]
	years = item[0]
print(years[0])
print(max_years)





