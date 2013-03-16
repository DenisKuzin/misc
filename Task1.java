public class Task1 {
    public static void main(String[] args) {
        System.out.printf("Result is %d\n", evenFibonacciSum(4000000));
    }

    public static int evenFibonacciSum(int limit) {
	int odd = 1;
	int even = 2;
	int currentSum = 3;
	int evenSum = 2;
	while (currentSum <= limit) {
	    if (currentSum % 2 == 0) {
		evenSum += currentSum;
	    }
	    odd = even;
	    even = currentSum;
	    currentSum = odd + even;
	}
	return evenSum;
    }
}
