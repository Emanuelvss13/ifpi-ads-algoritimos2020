
public class TesteJogador {
	public static void main(String[] args) {
		Jogador j1 = new Jogador();
		Jogador j2 = new Jogador();
		
		j1.Definir(1, 2, 10);
		j2.Definir(4, 5, 20);
		
		j1.Atacar(j2);
		j2.Atacar(j1);
		
		System.out.println(j2.pontos_atuais);
		System.out.println(j1.pontos_atuais);
		
		
		// O jogador2 ficou com 10;
		// O jogador1 ficou com 0;
	
	}
}
