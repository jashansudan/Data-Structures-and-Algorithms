class Solution(object):
    def merge(self, nums1, m, nums2, n):
        m -= 1
        n -= 1

        insertionPoint = len(nums1) - 1
        while m >= 0 or n >= 0:
            if m < 0 or n < 0:
                nums1[insertionPoint] = nums1[m] if n < 0 else nums2[n]
                m -= 1
                n -= 1
            else:
                if nums1[m] > nums2[n]:
                    nums1[insertionPoint] = nums1[m]
                    m -= 1
                else:
                    nums1[insertionPoint] = nums2[n]
                    n -= 1
            insertionPoint -= 1
        return
