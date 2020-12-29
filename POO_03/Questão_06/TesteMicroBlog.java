public class TesteMicroBlog {

	public static void main(String[] args) {
		MicroBlog MB = new MicroBlog(5);
		
		Postagem p1 = new Postagem("1", "Primeiro Post do blog", 5);
		Postagem p2 = new Postagem("2", "Segundo", 10);
		
		MB.adcPost(p1);
		MB.adcPost(p2);
		
		MB.toCurtir("1");
		
		
		System.out.println(p1.qtdCurtidas);
		
		
	}

}
