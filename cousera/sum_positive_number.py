def sum_positive_numbers(n):
  sum=0
  if n==0:
    return 0
  return n+sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15
