import java.util.ArrayList;

public class Estoque {
	ArrayList<Produto> estoque = new ArrayList<>();
	
	String adc(Produto produto) {
		int id_ = produto.id;
		
		for(Produto p : estoque) {
			if(p.id == id_) {
				return "Id ou produto ja cad�strado";
			}
		}
		estoque.add(produto);
		return "Produto cadastrado";
	}
	
	String consultar(int id) {
		for(Produto p : estoque) {
				if(p.id == id) {
					return "Existe um produto com esse id\nDescri��o: " + p.descricao + "\nQuantidade: " + p.quantidade;
				} 
		}
		return "Produto n�o encontrado.";
	}
	
	String excluir(int id) {
		for(Produto p : estoque) {
			if(p.id == id) {
				estoque.remove(p);
				return "Produto excluido";
			}
		}
		return "Produto n�o encontrado";
	}
	
	String darBaixa(int id, int qtd){
		for(Produto p : estoque) {
			if(p.id == id) {
				System.out.println("Quantidade:" + p.quantidade);
				p.quantidade -= qtd;
				return qtd + "retirado do estoque";
			}
		}
		
		return "Produto n�o encontrado.";
		
	}
	
	String repor(int id, int qtd){
		for(Produto p : estoque) {
			if(p.id == id) {
				System.out.println("Quantidade:" + p.quantidade);
				p.quantidade += qtd;
				return qtd + " adicinado ao estoque";
			}
		}
		
		return "Produto n�o encontrado.";
		
	}
	
}

