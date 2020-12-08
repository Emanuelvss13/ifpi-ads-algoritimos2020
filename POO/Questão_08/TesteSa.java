
public class TesteSa {
	public static void main(String[] args) {
		Saudacao sa = new Saudacao();
		sa.texto = "Bom dia";
		sa.destinatario = "Emanuel";
		
		System.out.println(sa.oterSaudacao());
	}
}
