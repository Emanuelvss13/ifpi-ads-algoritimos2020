
public class Hora {
	private int hora, minuto, segundo;
	
	void hora(int hora) {
		this.hora = hora;
	}
	
	void minuto(int minuto) {
		this.minuto = minuto;
	}
	
	void segundo(int segundo) {
		this.segundo = segundo;
	}
	
	void show() {
		System.out.println(this.hora + ":" + this.minuto + ":" + this.segundo);
	}
}
