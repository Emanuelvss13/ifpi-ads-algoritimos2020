
public class ContaImposto {
	private double saldo;
	private double numero;
	
	ContaImposto(double saldo, double numero){
		this.saldo = saldo;
		this.numero = numero;
	}
	
	double getSaldo(){
		return this.saldo;
	}
	
	void credito(double valor) {
		saldo += valor;
	}
	
	void debito(double valor) {
		double deb;
		deb = retemImposto(valor);
		saldo -= valor;
		valor -= deb;
		System.out.println("Foram debitados: " + valor + " com " + deb + " de imposto.");
		
		
	}
	
	private double retemImposto(double valorDebito) {
		double deb;
		deb = 0.38 * (valorDebito/100);
		return deb;
	}
	
}
