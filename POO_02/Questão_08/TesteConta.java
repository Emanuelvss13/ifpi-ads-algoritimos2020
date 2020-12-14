public  class TesteConta{
	public static void main(String[] args) {
		Conta c1 = new Conta("1",100);
		Conta c2 = new Conta("2",100);
		
		c1.sacar(1000);
		c2.sacar(10);
		
		c1.transferir(c2, 10);
		c2.transferir(c1, 1000);
		
		System.out.println(c1.consultarSaldo());
		System.out.println(c2.consultarSaldo());
	}
}
