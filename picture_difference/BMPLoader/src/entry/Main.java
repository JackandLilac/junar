package entry;

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

import algo.FingerPrint;
import algo.dHash;

public class Main {
	
	public static void main(String args[]) throws IOException {
		
//        FingerPrint fp1 = new FingerPrint(ImageIO.read(new File("/Users/zhangjie/Desktop/3.png")));
//        FingerPrint fp2 =new FingerPrint(ImageIO.read(new File("/Users/zhangjie/Desktop/4.png")));
//        System.out.println(fp1.toString(true));
//        System.out.printf("sim=%f",fp1.compare(fp2));
		
//        BufferedImage image1 = ImageIO.read(new File("/Users/zhangjie/Desktop/1.png"));
//        BufferedImage image2 = ImageIO.read(new File("/Users/zhangjie/Desktop/2.png"));
//        ImagePerceptualHashSimilarity is = new ImagePerceptualHashSimilarity();
//        boolean code = is.perceptualHashSimilarity(image1,image2);
//        System.out.println(code);
		String img1 = "/Users/zhangjie/Desktop/1.png";
		String img2 = "/Users/zhangjie/Desktop/1.png";
		dHash d = new dHash();
		System.out.println(d.caldHashSimilarity(img1, img2));
		
	}

}
