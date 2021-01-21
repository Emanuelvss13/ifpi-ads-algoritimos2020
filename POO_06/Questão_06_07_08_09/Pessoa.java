
public class Pessoa {
	private String Nome;
	private String SobreNome;
	
	Pessoa(){
	}
	
	Pessoa(String Nome, String SobreNome){
		this.Nome = Nome;
		this.SobreNome = SobreNome;
	}
	
	void setNome(String Nome) {
		this.Nome = Nome;
	}
	
	void setSobreNome(String SobreNome) {
		this.Nome = SobreNome;
	}
	
	String getNome() {
		return Nome;
	}
	
	String getSobreNome() {
		return SobreNome;
	}
	
	String getNomeCompleto() {
		return Nome + " " + SobreNome;
	}
}
