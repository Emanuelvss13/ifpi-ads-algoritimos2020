
public class TesteEquipamento {
	public static void main(String[] args) {
		Equipamento equip1 = new Equipamento();
		Equipamento equip2 = new Equipamento();
		
		equip1.liga();
		equip2.desliga();
		
		equip1.inverte();
		equip2.inverte();
		
		if(equip1.a == true) {
			System.out.println("O equipamento 1 esta ligado.");
		} else {
			System.out.println("O equipamento 1 esta desligado.");
		}
		
		
		if(equip2.a == true) {
			System.out.println("O equipamento 2 esta ligado.");
		} else {
			System.out.println("O equipamento 2 esta desligado.");
		}
		
	}
}
