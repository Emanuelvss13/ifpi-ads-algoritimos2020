public class Calculadora {
	private int operando1, operando2;
	
	Calculadora(int n1, int n2){
		this.operando1 = n1;
		this.operando2 = n2;
	}
	
	
	public void adc() {
		 int res = this.operando1 + this.operando2;
		 System.out.println("O resultado dessa adi��o �: " + res);
	}
	
	public void sub() {
		 int res = this.operando1 - this.operando2;
		 System.out.println("O resultado dessa subtra��o �: " + res);
	}
	
	public void div() {
		 int res = this.operando1 / this.operando2;
		 System.out.println("O resultado dessa divis�o �: " + res);
	}
	
}
