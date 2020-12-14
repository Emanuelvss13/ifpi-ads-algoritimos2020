
public class TesteProduto {
	public static void main(String[] args) {
		Produto p1 = new Produto();
		Produto p2 = new Produto();
		
		p1.def(123, "legal", 22.90, 5);
		p2.def(456, "barato", 5.0, 100);
		
		System.out.println(p1.equals(p1, p2));
		
		System.out.println(p1.desc());
	}
}
