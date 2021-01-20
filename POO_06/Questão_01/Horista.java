
public class Horista extends Diarista {
	public static double calcularSalario() {
		return Diarista.calcularSalario() / 24;
	}
}
