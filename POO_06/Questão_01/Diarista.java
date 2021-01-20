
public class Diarista extends Empregado {
		
	public static double calcularSalario() {
		return Empregado.calcularSalario() / 30;
	}
}