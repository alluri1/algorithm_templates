def find_kth_largest(nums, k):
    # hoare's partition
    k = len(nums)- k

    def quickselect(l,r):
        pivot = r
        p = l
        for i in range(l,r):
            # 1. move the ptr if element is less than pivot
            if nums[i] <= nums[pivot]:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1
            #2. swap r (pivot) element and p element
            nums[r], nums[p] = nums[r], nums[p]

            #3. recurse on one side of the array
            if k == p :
                return nums[p]
            elif k < p:
                return quickselect(l, p-1)
            else:
                return quickselect(p+1, r)
    return quickselect(0, len(nums)-1)
