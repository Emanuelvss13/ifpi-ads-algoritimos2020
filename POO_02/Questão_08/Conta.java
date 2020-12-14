
public class Conta {
	String numero;
	private double saldo;
	
	Conta(String numero, double valor) {
		this.numero = numero;
		this.saldo = valor;
	}

	void sacar(double valor) {
		if (saldo < valor) {
			System.out.println("False");
		} else {
			saldo = saldo - valor;
			System.out.println("True");
		}
		
	}
	
	void depositar(double valor) {
		saldo = saldo + valor;
	}
	
	double consultarSaldo() {
		return saldo;
	}
	
	void transferir(Conta destino, double valor) {
		//saldo = saldo - valor;
		//destino.saldo = destino.saldo + valor;
		if (valor > this.saldo){
			System.out.println("False");
		} else {
			this.sacar(valor);
			destino.depositar(valor);
		}
		
	}		

}
