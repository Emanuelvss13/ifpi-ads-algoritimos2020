package Exe004.classes;

public class Conta {
	String numero;
	double saldo;
	
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

}
