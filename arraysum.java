public class arraysum {

    int array_sum(int arr[], int size) {
        int total = 0;

        for (int i = 0; i < size; i++) {
            total += arr[i];
        }

        return total;
    }

    public static void main(String[] args) {
        int[] a = {1, 2, 3, 4, 5};

        arraysum obj = new arraysum();

        int sum = obj.array_sum(a, a.length);

        System.out.println(sum);
    }
}