
public class Teste {

	public static void main(String[] args) {
		Pessoa pessoa1 = new Pessoa("Emanuel", "Vitor");
		Funcionario f1 = new Funcionario();
		Professor p1 = new Professor();
		
		f1.setMatricula(123);
		f1.setSalario(2500.50);
		
		p1.setTitulacao("Mestrado");
		
		System.out.println(pessoa1.getNomeCompleto());
		System.out.println(f1.getMatricula());
		System.out.println(f1.getSalario());
		System.out.println(f1.getSalarioPrimeiraParcela());
		System.out.println(f1.getSalarioSegundaParcela());
		System.out.println(p1.getTitulacao());

	}

}
