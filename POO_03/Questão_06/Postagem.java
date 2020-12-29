
public class Postagem {
	String id;
	String texto;
	int qtdCurtidas;
	
	Postagem(String id, String texto, int qtdCurtidas){
		this.id = id; 
		this.texto = texto;
		this.qtdCurtidas = qtdCurtidas;
	}
	
	void curtir() {
		qtdCurtidas++;
	}
	
	String ToString() {
		return this.texto + ' ' + this.qtdCurtidas;
	}
	
	
	
}
