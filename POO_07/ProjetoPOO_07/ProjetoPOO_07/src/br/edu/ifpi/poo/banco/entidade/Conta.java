package br.edu.ifpi.poo.banco.entidade;

public class Conta {
	private String numero;
	private double saldo;
	
	public void validarValor(double valor) {
		if (valor <= 0) {
			throw new AplicacaoException("Valor menor ou igual a zero");
		}
	}

	public Conta(String numero, double valor) {
		this.depositar(valor);
		this.numero = numero;
	}

	public void sacar(double valor) {
		if (valor > saldo) {
			throw new AplicacaoException("Saldo insuficiente.");
		}
		
		//if(valor <= 0){
				//	throw new AplicacaoException("Valor menor ou igual a zero");
				//}
		
		validarValor(valor);
		
		saldo = saldo - valor;
	}

	public void depositar(double valor) {
		//if(valor <= 0){
				//throw new AplicacaoException("Valor menor ou igual a zero");
			//}
		
		validarValor(valor);
		
		saldo = saldo + valor;
	}

	public void transferir(Conta destino, double valor) {
		this.sacar(valor);
		destino.depositar(valor);
	}
	
	public double getSaldo() {
		return saldo;
	}

	public String getNumero() {
		return numero;
	}

}
