
public class Banco {
	private Conta[] contas;
	private int indice = 0;

	public Banco() {
		contas = new Conta[50];
	}

	public Banco(int tamanho) {
		contas = new Conta[tamanho];
	}

	void inserir(Conta c) {
		contas[indice] = c;
		indice++;
	}

	Conta consultar(String numero) {
		Conta c = null;
		for (int i = 0; i < indice; i++) {
			if (contas[i].getNumero().equals(numero)) {
				c = contas[i];
				break;
			}
		}
		return c;
	}

	private int consultarIndice(String numero) {
		int pos = -1;
		for (int i = 0; i < indice; i++) {
			if (contas[i].getNumero().equals(numero)) {
				pos = i;
				break;
			}
		}
		return pos;
	}

	void debitar(String numero, double valor) {
		Conta c;
		c = consultar(numero);
		if (c != null)
			c.sacar(valor);
		else
			System.out.println("Conta inexistente.");
	}

	void alterar(Conta c) {
		int indice = consultarIndice(c.getNumero());
		if (indice != -1) {
			contas[indice] = c;
		}

	}

	void excluir(String numero) {
		int posicao = consultarIndice(numero);
		if (posicao != -1) {
			for (int i = posicao; i < indice; i++) {
				contas[i] = contas[i + 1];
			}

			indice--;
		}
	}
}