
public class TesteEstoque {
	
	public static void main(String[] arg) {
		Estoque e = new Estoque();
		Produto p1 = new Produto(123, "Arroz", 5, 20);
		Produto p2 = new Produto(12, "Feijão", 5, 10);
		
		//Incluir
		System.out.println(e.adc(p1));
		System.out.println(e.adc(p2));
		//Excluir
		System.out.println(e.excluir(12));
		//Consultar
		System.out.println(e.consultar(123));
		//Repor
		System.out.println(e.repor(123,10));
		//DarBaixa
		System.out.println(e.adc(p2));
		System.out.println(e.repor(12,10));
		
		
		}

}
