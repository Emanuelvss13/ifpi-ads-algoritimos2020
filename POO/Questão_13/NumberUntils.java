
public class NumberUntils {
	int n;
	
	String isPair() {
		if (n % 2 == 0) {
			return "Verdadeiro";
		} else {
			return null;
		}
	}
	
	String isOdd() {
		if( n % 2 != 0) {
			return "Falso";
		} else {
			return null;
		}
	}
	
	String isPrime() {
		if(n % 2 != 0 && n % 3 != 0 && n % 5 != 0 && n % 7 != 0 && n % 9 != 0 ) {
			return "True";
			
		} else if (n == 1 || n == 2 || n == 3 || n == 5 || n == 7 || n == 9){
			return "True";
		} else {
			return "False";
		}
		
	}
	
	String primeCount() {
			String contagem = "";
			for(int i = 0; i < n; i++ ) {
				contagem += i + ", ";
			}
			return contagem + n;
	}
	
	String printReverseCount() {
		String contagem = "";
		int n1 = n;
		for(int i = 0; n1 > i; n1-- ) {
			contagem += n1 + ", ";
		}
		return contagem + 0;
	}
}
