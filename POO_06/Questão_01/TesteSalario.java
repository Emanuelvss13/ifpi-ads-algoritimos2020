
public class TesteSalario {
	public static void main(String[] args) {
		Empregado e = new Empregado();
		Diarista d = new Diarista();
		Horista h = new Horista();
		
		System.out.println("Empregado: " + e.calcularSalario());
		System.out.println("Diarista: " + d.calcularSalario());
		System.out.println("Horista: " + h.calcularSalario());
	}
}
