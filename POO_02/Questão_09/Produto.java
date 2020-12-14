public class Produto {
	int codigo;
	String descricao;
	private double valor;
	int quantidade;
	int quantidade_min;
	
	void def(int codigo, String descricao, double valor, int quantidade){
		this.codigo = codigo;
		this.descricao = descricao;
		this.valor = valor;
		this.quantidade = quantidade;
	}
	
	void baixar(int quantidade_e, int quantidade_s) {
		this.quantidade += quantidade_e;
		
		int a = quantidade -= quantidade_s;
		
		if ( a >= quantidade_min) {
			quantidade -= quantidade_s;
		}
	}
	
	void taxa(double taxa) {
		this.valor = (valor * (taxa / 100) + valor);
	}
	
	String desc() {
		String v,c, q, d;
		
		v = Double.toString(this.valor);
		c = Integer.toString(this.codigo);
		q = Integer.toString(this.quantidade);
		d = this.descricao;
		
		return v + " " + c + " " + q + " " + d;
	}
	
	boolean equals(Produto p1, Produto p2) {
		if(p1.codigo == p2.codigo) {
			return true;
		} else {
			return false;
		}
	}


}


