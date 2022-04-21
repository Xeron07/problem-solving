import math


def median(nums1,nums2):
    merged = []
    if len(nums1)<1 : merged = nums2
    if len(nums2)<1 : merged = nums1
    if len(nums1) > 0 and len(nums2)>0 :
        merged = [*nums1, *nums2]
    merged.sort()
    if len(merged)%2!=0:
        return merged[math.floor(len(merged)/2)]
    else:
        return (merged[math.floor(len(merged)/2)]+merged[math.floor((len(merged)/2)-1)])/2

print(median([1,2],[3]))