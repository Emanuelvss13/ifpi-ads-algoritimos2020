
public class Funcionario extends Pessoa{
	int Matricula;
	double Salario;
	
	void setMatricula(int matricula) {
		this.Matricula = matricula;
	}
	
	void setSalario(double salario) {
		if(salario < 0) {
			System.out.println("O salário não pode ser negativo.");
		} else {
			this.Salario = salario;
		}
	}
	
	int getMatricula() {
		return Matricula;
	}
	
	double getSalario() {
		return Salario;
	}
	
	double getSalarioPrimeiraParcela() {
		return Salario * 0.6;
	}
	
	double getSalarioSegundaParcela() {
		return Salario * 0.4;
	}
}
