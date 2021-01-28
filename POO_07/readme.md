7) - Sim, porque ele utiliza os metodos "sacar" e "depositar" que ja estão refatorados.
     Sim, pois a repetição de codigo foi evitada, e os erros foram melhor tratados; 

9) - Exceções checadas:
     PROS:
     - Dão robuste ao programa.
     - O compilador obriga o programador a tratar a exceção ou então declarar, conscientemente, que ela será propagada.
     
     CONTRA:
     - Um método é obrigado a estabelecer uma política para todas as exceções checadas lançadas por sua implementação (ou passar a exceção checada mais acima na pilha, ou              manipulá-la de alguma forma).
     - O tratamento de exceções em Java introduz uma penalidade no desempenho do programa, uma vez que construir o stack trace da exceção é uma operação potencialmente custosa.        Assim, evite usar try/catch dentro de um loop com muitas iterações se o desempenho for uma preocupação.
     
     Exemplo:
     FileInputStream FIS = null;
     try {
         FIS = new FileInputStream("D:/arquivo.txt");
     } catch (FileNotFoundException ex) {
         Logger.getLogger(Teste.class.getName()).log(Level.SEVERE, null, ex);
     }

     int x;
     try {
         while ((x = FIS.read()) != 0) {
         }
     } catch (IOException ex) {
         Logger.getLogger(Teste.class.getName()).log(Level.SEVERE, null, ex);
     }
     
     Exceções não checadas:
     PROS:
     - Um método não é obrigado a estabelecer uma política para as exceções não checadas lançadas por sua execução (e quase sempre nunca o fazem).
     
     CONTRAS:
     - Representam defeitos no programa (bugs).
     - Com exceções não-checadas, o programador pode não saber que está chamando um método que lança exceções, e pode acabar propagando essas exceções sem saber.
     
     Exemplo:
     int num1 = 10;
     int num2 = 0;
     int res = 0;

     res = num1 / num2; // ArithmeticException: / by zero;
     
     
     Quando uma exceção checada é usada herdando "Exception", o código deve capturá-la usando throws no método para delegar sua captura. As exceções de runtime não                    precisam fazer isto, como o próprio nome indica elas não devem ser consideradas pelo compilador.
     
     Terão de ser alterados todos os métodos que usam exceções.
     
11) - "Unreachable catch block for TipoExcecao2. It is already handled by the catch block for TipoExcecao1,".
      Esse erro é apresentado.
