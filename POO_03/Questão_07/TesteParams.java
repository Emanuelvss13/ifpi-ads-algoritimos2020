
public class TesteParams {

	public static void main(String[] args) {
		
		int indice[] = new int[args.length];
		
		for(int i = 0; i < args.length; i++) {
			indice[i] = Integer.parseInt( args[i]);
		}		
		
		for (int i = 1; i < indice.length; i++) {
		    for (int j = 0; j < i; j++) {
		        if (indice[i] > indice[j]) {
		            int temp = indice[i];
		            indice[i] = indice[j];
		            indice[j] = temp;
		        }
		    }
		}
		
		for(int i = 0; i < indice.length; i++) {
			System.out.println(indice[i]);
		}
		
		
	}

}
