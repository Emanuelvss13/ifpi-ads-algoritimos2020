package Exe004.classes; 

import Exe004.classes.*;
import java.util.Scanner;

public class ExecutaBanco {
	public static void main(String[] args) {
		Banco b = new Banco();
		Scanner sc = new Scanner(System.in);
		String opcao = "";
		do {
			System.out.println("1-Cadastrar 2-Alterar 3-Excluir ...9-Sair");
		
		opcao = sc.next();
		switch (opcao) {
			case"1" : Conta c = new Conta();
							  System.out.println("Digite o número");
							  c.numero = sc.next ();
							  c.saldo = sc.nextDouble();
							  b.inserir(c);
							  break;
			case"2" : String numero1;
							  int n_saldo;
							  int id;
							  System.out.println("Digite o número");
							  numero1 = sc.next();
							  id = b.consultarIndice(numero1);
							  System.out.println("Digite o saldo da conta: ");
							  n_saldo = sc.nextInt();
							  b.contas[id].saldo = n_saldo;
							  break;
			case"3": String numero2;
							 System.out.println("Digite o numero da conta de deseja excluir: ");
							 numero2 = sc.next();
							 b.excluir(numero2);
							 break;
			case"4": String numero3;
							  int n;
							  System.out.println("Digite o numero da conta: ");
							  numero3 = sc.next();
							  n = b.consultarIndice(numero3);
							  System.out.println(b.contas[n].numero);
							  System.out.println(b.contas[n].saldo);
							  break;
			case"5": String numero4;
							  int id1;
							  int sald;
							  System.out.println("Digite o numero da conta: ");
							  numero4 = sc.next();
							  id1 = b.consultarIndice(numero4);
							  System.out.println("Digite o valor do deposito: ");
							  sald = sc.nextInt();
							  b.contas[id1].saldo += sald;
							  break;
			case"6": String numero5;
							  int id2;
							  int saldo1;
							  System.out.println("Digite o numero da conta: ");
							  numero5 = sc.next();
							  id2 = b.consultarIndice(numero5);
							  System.out.println("Digite o valor do deposito: ");
							  saldo1 = sc.nextInt();
							  b.contas[id2].saldo -= saldo1;
							  break;
			case"7": int destino;
							  int atual;
							  int valor;
							  System.out.println("Digite o numero da conta atual: ");
							  atual = sc.nextInt();
							  System.out.println("Digite o numero da conta de destino: ");
							  destino = sc.nextInt();
							  System.out.println("Digite o valor da transferencia: ");
							  valor = sc.nextInt();
							  b.contas[atual].saldo -= valor;
							  b.contas[destino].saldo += valor;
							  break;
				}
		} while (!opcao.equals("9") );
	}
}