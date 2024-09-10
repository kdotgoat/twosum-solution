class Solution:
    def two_sum(self, nums, target):
        num_to_index = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
        
        return []  # No solution found

# Example usage
def main():
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    
    indices = solution.two_sum(nums, target)
    
    if indices:
        print(f"Indices of the numbers that add up to {target} are: {indices}")
    else:
        print("No two numbers add up to the target.")

if __name__ == "__main__":
    main()
