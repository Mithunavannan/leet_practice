nums1= [1,3,4,11,2]
nums2= [2,4,3,1,7,5,15]


if set(nums1).issubset(set(nums2)):
    print("nums is a subset")
else:
    print("not a subset")