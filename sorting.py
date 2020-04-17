numbers = [1, 2, 56, 32, 51, 2, 8, 92, 15]
print(numbers)
i=0
N=len(numbers)

def swap_neigbour(numbers, j):
    if j<=len(numbers):
        temp=numbers[j-1]
        numbers[j-1]=numbers[j]
        numbers[j]=temp


while i<N-1:
    for j in range(1,len(numbers)):
        if numbers[j]<numbers[j-1]:
            swap_neigbour(numbers, j)
    i=i+1
print(numbers)