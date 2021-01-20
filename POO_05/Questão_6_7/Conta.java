
public class Conta {
	private String numero;
	private double saldo;
	
	Conta(String numero, double valor) {
		this.setNumero(numero);
		this.saldo = valor;
	}

	void sacar(double valor) {
		saldo = saldo - valor;
	}
	
	void depositar(double valor) {
		saldo = saldo + valor;
	}
	
	double consultarSaldo() {
		return saldo;
	}
	
	void transferir(Conta destino, double valor) {
		saldo = saldo - valor;
		destino.saldo = destino.saldo + valor;
		//this.sacar(valor);
		//destino.depositar(valor);
	}

	public String getNumero() {
		return numero;
	}

	public void setNumero(String numero) {
		this.numero = numero;
	}		

}
