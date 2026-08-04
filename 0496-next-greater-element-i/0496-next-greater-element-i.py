class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []

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

        return answer