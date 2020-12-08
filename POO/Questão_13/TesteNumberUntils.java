
public class TesteNumberUntils {
	public static void main(String[] args) {
		NumberUntils nu = new NumberUntils();
		
		nu.n = 11;
		
		
		System.out.println(nu.isPair());
		System.out.println(nu.isOdd());
		System.out.println(nu.isPrime());
		System.out.println(nu.primeCount());
		System.out.println(nu.printReverseCount());
	}
}
