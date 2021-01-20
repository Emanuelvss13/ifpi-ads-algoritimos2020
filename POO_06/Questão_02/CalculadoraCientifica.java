
public class CalculadoraCientifica extends Calculadora {
	
	
	CalculadoraCientifica(int n1, int n2) {
		super(n1, n2);
	}

	double exponenciar(double base, double expo) {
		double res;
		res = 1;
		for(int i = 0;  i < expo; i++ ) {
			res  *= base;
		}	
		return res;
	}
	
	double div(double n1, double n2, Boolean arre) {
		if(arre == true) {
			return Math.round(n1 / n2);
		} else {
			return n1 / n2;
		}
	}
	
	
}
