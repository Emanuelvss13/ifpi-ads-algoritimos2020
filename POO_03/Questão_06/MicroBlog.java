public class MicroBlog {
	int indice;
	int top;
	Postagem[] postagens;
	
	MicroBlog(int num) {
		postagens = new Postagem[num];
	}
	
	
	void adcPost(Postagem p) {
		postagens[indice] = p;
		indice++;
	}
	
	void delete(int i) {
		
	}
	
	int consultarIndice(String numero) {
		int pos = -1;
		for (int i = 0; i < indice; i++) {
			if (postagens[i].id.equals(numero)) {
				pos = i;
				break;
			}
		}
		return pos;
	}
	
	void excluir(String numero) {
		int posicao = consultarIndice(numero);
		if (posicao != -1) {
			for (int i = posicao; i < indice; i++) {
				postagens[i] = postagens[i + 1];
			}

			indice--;
		}
	}
	
	String mostlkd() {
		int id = 0;
		int mc = 0;
		
		for(int i = 0; i < indice; i++) {
			if(postagens[i].qtdCurtidas > mc) {
				mc = postagens[i].qtdCurtidas;
				id = i;
			}
		}
		
		return "O post com mais curtidas é o de indice " + postagens[id].id;
	}
	
	void toCurtir(String id) {
		for(int i = 0; i < indice; ++i) {
			if(postagens[i].id.equals(id)) {
				postagens[i].curtir();
			}
		}
	}
	
	
}
