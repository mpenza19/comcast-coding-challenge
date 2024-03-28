class CodingChallenge:
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            this_sum = numbers[i] + numbers[j]
            if this_sum == target:
                return [i+1, j+1]
            elif this_sum < target:
                i += 1
            else:
                j -= 1
