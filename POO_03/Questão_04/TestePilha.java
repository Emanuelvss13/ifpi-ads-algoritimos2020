package Teste;

public class TestePilha {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Pilha p1 = new Pilha();
	
		p1.empilhar(22);
		p1.empilhar(70);
		p1.empilhar(22);
		p1.empilhar(70);
		p1.empilhar(70);
		p1.desempilhar();		
		System.out.println(p1.retornarTopo());
		System.out.println(p1.exibir());
		
	}

}
