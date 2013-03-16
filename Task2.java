public class Task2 {
    public static void main(String[] args) {
        System.out.printf("Result is %d\n", greatestPrimeDivisor(600851475143L));
    }

    public static long greatestPrimeDivisor(long number) {
	long divisor = 2;
	while (divisor * divisor <= number) {
	    if (number % divisor == 0) {
		number /= divisor;
	    }
	    else {
		divisor += 1;
	    }
	}
	if (number != 1) {
	    return number;
	}
	else {
	    return divisor;
	}
    }
}
