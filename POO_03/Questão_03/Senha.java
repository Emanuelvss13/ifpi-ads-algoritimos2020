package Teste;

public class Senha {
	
	String valor;
	
	boolean iguais(String senha) {
		if(valor.equals(senha)) {
			return true;
		} else {
			return false;
		}
	}
	
	boolean iguaisTrim(String senha) {
		String res = valor.trim();
	
		if(res.equals(senha)) {
			return true;
		} else {
			return false;
		}
	}
	
	boolean tamanhoSeguro() {
		if(valor.length() > 5) {
			return true;
		} else {
			return false;
		}
	}
	
	boolean possuiMaiusculaMinuscula() {
		char c;
		boolean M = false;
		boolean m = false;
		for(int i = 0; i < valor.length(); i++) {
			c = valor.charAt(i);
			
			if(Character.isUpperCase(c)) {
				M = true;
			}
			
			if(Character.isLowerCase(c)) {
				m = true;
			}
		}
		
		if(M == false && m == false) {
			return false;
		} else {
			return true;
		}
	}
	
	boolean possuiNumero() {
		char d;
		boolean n = false;
		
		for(int i = 0; i < valor.length(); ++i) {
			d = valor.charAt(i);
			
			if(Character.isDigit(d)) {
				n = true;
			}
		}
		
		return n;
	}
	
	boolean ehvalida() {
		if(tamanhoSeguro() == true && possuiMaiusculaMinuscula() == true && possuiNumero() == true) {
			return true;
		} else {
			return false;
		}
	}
}
