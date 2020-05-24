# Problem https://pbs.twimg.com/media/EYy3K4uXsAAiNVa?format=jpg&name=medium
def single_patron(number: int):
 result = float(number * (number + 1) / (2 ** (number + 1)))
 return result


final = 0.0
number = int(input('Value to record: '))
for x in range(1, number):
  final += single_patron(x)
  print(f'Iteration {x} with value {final}')

print(f'Result of all operation is: {final}')
