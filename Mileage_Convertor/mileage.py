print("How many kilometers do you want to convert to miles ? ")
mls=input()
print(f"OK, you said {mls} miles")
kms=float(mls)*1.609
kms=round(kms,2)
print(f"{mls} miles is {kms} km")
