
public class Banco {
	Conta[] contas;
	int indice = 0;

	public Banco() {
		contas = new Conta[50];
	}

	public Banco(int tamanho) {
		contas = new Conta[tamanho];
	}

	void inserir(Conta c) {
		if(indice > 49) {
			System.out.println("Numero maximo de contas ultrapassado");
		} else {
			contas[indice] = c;
			indice++;
		}
	}

	Conta consultar(String numero) {
		Conta c = null;
		for (int i = 0; i < indice; i++) {
			if (contas[i].numero.equals(numero)) {
				c = contas[i];
				break;
			}
		}
		return c;
	}

	int consultarIndice(String numero) {
		int pos = -1;
		for (int i = 0; i < indice; i++) {
			if (contas[i].numero.equals(numero)) {
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
		int indice = consultarIndice(c.numero);
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
	
	void creditar(String numero, double valor) {
		int num = consultar(numero);
		
		if(num != null) {
			contas[num].saldo += valor;
		} else {
			System.out.println("Conta não encontrada!")
		}
	}
	
	void transferir(String numCredito, String numDebito, double valor){
		nc  = consultarIndice(numCredito);
		nd = consultarIndice(numDebito);
		
		contas[nc].saldo += valor;
		contas[nd].saldo -= valor;
	}
	
	int tContas(){
		return indice;
	}
	
	int tDinheiro(){
		int total = 0;
		for(int i = 0; i < indice; i++){
			total += contas[i].saldo;
		}
		
		return total
	}
	
	int mSaldo(){
		int t = tContas();
		int d = tDinheiro();
		
		return t / d;
	}
	
	
}
