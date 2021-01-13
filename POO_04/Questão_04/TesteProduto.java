public class TesteProduto {

	public static void main(String[] args) {
		ProdutoPerecivel pp = new ProdutoPerecivel(123, "Arroz", 5, 20);
		pp.validadeAno = 2021;
		pp.validadeMes = 1;
		pp.validadeDia = 13;
		
		System.out.println(pp.validade());
		
		
	}

}
