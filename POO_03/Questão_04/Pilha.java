package Teste;

public class Pilha {
	int top;
	int pilha[] = new int[5];
	
	Pilha() {
		top = -1;
	}
	
	void empilhar(int x) {
	      	pilha[++top] = x;
	   }
	
	boolean estaCheia() {
		boolean a = false;
		
		if (top >= (5-1)) {
	         System.out.println("A Pilha tem mais de 5 elementos!");
	         a = true;
	      }
		
		return a;
	}
	
	void desempilhar() {
		for(int i = 0; i < pilha.length; i++) {
			if(pilha[i] == 0) {
				pilha[i-1] = 0;
				break;
			}
		}
		
		if(pilha[4] != 0) {
			pilha[4] = 0;
		}
		
	}
	
	int retornarTopo() {
		
		int topo = 0;
		
		for(int i = 0; i < pilha.length; i++) {
			if(pilha[i] == 0) {
				topo =  pilha[i-1];
			}
		}
		
		return topo;
		
	}
	
	String exibir() {
		String total = " ";
		for(int i = 0; i < pilha.length; ++i) {
			total += pilha[i] + " ";
		}
		
		return total;
	}
}
