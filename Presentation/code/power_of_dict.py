import time
import matplotlib.pyplot as plt

def two_sum_list(nums: list, target: int):
    for x in range(len(nums)):
        remain_list = nums[:x] + nums[x + 1:]
        for y in range(len(nums) - 1):
            if nums[x] + remain_list[y] == target:
                return [nums[x], remain_list[y]]
            


def two_sum_dict(nums: list, target: int):
    dict = {}
    for index in range(len(nums)):
        dict[nums[index]] = index
    for number_1_index in range(len(nums)):
        remain = target - nums[number_1_index]
        if remain in dict and dict[remain] != number_1_index:
            return [nums[number_1_index], remain]


def create_list(n):
    nums = []
    for i in range(n):
        nums.append(i)
    target = nums[-1] + nums[-2]
    return nums, target


def main():
    sizes = [x for x in range(1000,20000,1000)]
    results = {'list': [], 'dict': [], 'sizes': sizes}
    
    for n in sizes:
        print(f"run list and dict funtions in {n} numbers.")
        list_data, target = create_list(n)
        # run the list fnction
        start = time.time()
        two_sum_list(list_data, target)
        end = time.time()
        results['list'].append(end - start)
        print("The runtime of list :", round(end - start,8), "seconds")

        # run the dict fnction
        start = time.time()
        two_sum_dict(list_data, target)
        end = time.time()
        results['dict'].append(end - start)
        print("The runtime of dict :", round(end - start,8), "seconds\n")

    plt.figure(figsize=(10, 6))
    plt.plot(results['sizes'], results['list'], label='List Implementation')
    plt.plot(results['sizes'], results['dict'], label='Dict Implementation')
    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.title('Time Complexity Comparison')
    plt.legend()
    plt.grid(True)
    plt.show()

    return results

def sample(n):
    list_data, target = create_list(n)
    print(f"run list and dict funtions in {n} numbers.")
    start = time.time()
    print(two_sum_list(list_data, target))
    end = time.time()
    print("The runtime of recursive fibonacci without memoization :", round(end - start,8), "seconds")

    start = time.time()
    print(two_sum_dict(list_data, target))
    end = time.time()
    print("The runtime of recursive fibonacci without memoization :", round(end - start,8), "seconds")

if __name__ == "__main__":
    main()
    # sample(2000)
