
public class TesteDesconto {
	public static void main(String[] args) {
		Desconto desc = new Desconto();
		
		desc.valorOriginal = 120;
		desc.desconto = 10;
		
		System.out.println(desc.calcula());
	}
}
