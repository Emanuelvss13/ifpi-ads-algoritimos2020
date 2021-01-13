import java.util.Calendar;

public class ProdutoPerecivel extends Produto{
	int validadeMes;
	int validadeDia;
	int validadeAno;
	int dia, mes, ano;
	
	Calendar c = Calendar.getInstance();
	
	String validade() {
		
		validadeMes--;
		
		dia = c.get(Calendar.DAY_OF_MONTH);
		mes = c.get(Calendar.MONTH);
		ano = c.get(Calendar.YEAR);
		
		if(validadeAno < ano) {
			return "O produto esta vencido.";
		} else if (validadeAno > ano) {
			return "O produto não esta vencido";
		} else if( validadeMes > mes) {
			return "O produto não esta vencido";
		} else if( validadeMes < mes) {
			return "O produto esta vencido";
		} else if (validadeDia < dia) {
			return "O produto esta vencido";
		} else if (validadeDia > dia) {
			return "O produto não esta vencido";
		}
		
		return "O produto não esta vencido";
		
	}	
}

