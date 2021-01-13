
public class TesteVeiculo {

	public static void main(String[] args) {
		Carro c = new Carro();
		carroEletrico ce = new carroEletrico();
		
		c.placa = "ABC123";
		c.ano = 2020;
		c.modelo = "Argos";
		
		ce.placa = "XYZ321";
		ce.ano = 2021;
		ce.modelo = "Prius";
		ce.autnomiaBateria = 200;

	}

}
