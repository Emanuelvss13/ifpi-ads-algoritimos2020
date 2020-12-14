public class Jogador {
	int forca, nivel, pontos_atuais;
	
	
	void Definir(int a, int b, int c) {
		this.forca = a;
		this.nivel = b;
		this.pontos_atuais = c;
	}
	
	int Pontos_relativos(int pr) {
		pr = forca * nivel;
		return pr;
	}
	
	void Atacar(Jogador destino) {
		destino.pontos_atuais -= this.pontos_atuais;
	}
	
}
