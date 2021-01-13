
public class Produto {
	int id;
	String descricao;
	int quantidade;
	double valor;
	
	void repor(int qtd) {
		this.quantidade += qtd;
	}
	
	void darBaixa(int qtd) {
		this.quantidade -= qtd;
	}
}
