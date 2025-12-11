class Solution {
    public double findMedianSortedArrays(int[] arr1, int[] arr2) {
        int[] mergedArr = new int[arr1.length + arr2.length];
        System.arraycopy (arr1, 0, mergedArr, 0, arr1.length);
        System.arraycopy (arr2, 0, mergedArr, arr1.length, arr2.length);
       
        Arrays.sort(mergedArr);
         System.out.println("Sorted Array" +java.util.Arrays.toString (mergedArr));

        int length = mergedArr.length;
        int middleIndex = length /2;

        if (length % 2 == 1) {
            return mergedArr[middleIndex]; 
        } else{
            return ((mergedArr[middleIndex - 1] + mergedArr[middleIndex]) / 2.0);
        }
    }

   
}