package br.edu.ifpi.poo.banco.testes;

import java.util.InputMismatchException;
import java.util.Scanner;



public class Questao_10 {
	
	public static void main(String[] args) {
	
		Scanner sc = new Scanner(System.in);
		
		try {
			System.out.println("Digite o número menor que 5:");
			int num = sc.nextInt();
			int[] numeros = {1,2,3,4,5};
			
			for (int i = 0; i < num; i++) {
				System.out.print(numeros[i] + " ");
			}
			
			} catch (InputMismatchException e) {
				System.out.println("Digite apenas números");
			} catch (ArrayIndexOutOfBoundsException a) {
				System.out.println("Limite do array estourado");
			} finally {
				System.out.println("Programa finalizado.");
			}
		}
	
}
