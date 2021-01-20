
public class TesteClasses {
	public static void main(String[] args) {
		Animal a = new Animal();
		Bovino b = new Bovino();
		Peixe p = new Peixe();
		
		a.setEspecie("Cachorro");
		System.out.println(a.getEspecie());
		
		b.setProducaoLeite(7);
		System.out.println(b.getProducaoLeite());
		
		p.setProfundidade(5);
		System.out.println(p.getProfundidade());
		
	}
}
