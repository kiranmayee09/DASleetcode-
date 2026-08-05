class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ answer = []

        for number in nums1:
            found = False

            for i in range(len(nums2)):
                if nums2[i] == number:

                    for j in range(i+1, len(nums2)):
                        if nums2[j] > number:
                            answer.append(nums2[j])
                            found = True
                            break
                    break
            
            if found == False:
                answer.append(-1)

        return answer """

        """ stack = []
        next_grater = {}

        for num in nums2:
            while stack and num > stack[-1]:
                next_grater[stack.pop()] = num
            stack.append(num)

        while stack:
            next_grater[stack.pop()] = -1

        answer = []
        for num in nums1:
            answer.append(next_grater[num])

        return answer """

        nums1Idx = { n:i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in nums1Idx:
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = nums1Idx[nums2[i]]
                    res[idx] = nums2[j]
                    break
        return res