
public class Equipamento {
	boolean a = false;
	
	boolean liga() {
		if (a == true) {
			return a;
		} else {
			return a = true;
		}
		
	}
	
	boolean desliga() {
		if(a == false) {
			return a;
		}
		return a = false;
	}
	
	boolean inverte() {
		if ( a == true) {
			return a = false;
		} else {
			return a = true;
		}
	}
	
	boolean estaLigado(){
		return a = true;
	}
}
