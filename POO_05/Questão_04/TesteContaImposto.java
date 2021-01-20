
public class TesteContaImposto {
	public static void main(String[] args) {
		ContaImposto ci = new ContaImposto(100, 1);
		
		ci.debito(50);
		
		System.out.println(ci.getSaldo());
		
		
	}
}
