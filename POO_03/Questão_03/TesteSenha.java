package Teste;

public class TesteSenha {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Senha s1 = new Senha();
		Senha s2 = new Senha();
		Senha s3 = new Senha();
		Senha s4 = new Senha();
		Senha s5 = new Senha();
		
		s1.valor = "Emanuel";
		s2.valor = "          Emanuel  ";
		s3.valor = "Emanuel";
		s4.valor = "Emanuel1";
		s5.valor = "123456789aA";
		
		System.out.println(s1.iguais("Emanuel"));
		System.out.println(s2.iguaisTrim("Emanuel"));
		System.out.println(s3.tamanhoSeguro());
		System.out.println(s4.possuiMaiusculaMinuscula());
		System.out.println(s5.possuiNumero());
		System.out.println(s5.ehvalida());

	}

}
