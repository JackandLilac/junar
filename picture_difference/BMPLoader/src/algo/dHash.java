package algo;

import java.awt.Graphics;
import java.awt.Image;
import java.awt.color.ColorSpace;
import java.awt.image.BufferedImage;
import java.awt.image.ColorConvertOp;
import java.io.File;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.List;

import javax.imageio.ImageIO;

/**
 * 
 * @author zhangjie
 * 完成差异哈希算法
 */
public class dHash {
	
	private final int WIDTH = 101;
	private final int HEIGHT = 100;
	
    /**
     * 缩放图像到指定尺寸
     * @param src
     * @param width
     * @param height
     * @return
     */
    private BufferedImage resize(Image src,int width,int height){
        BufferedImage result = new BufferedImage(width, height,  
                BufferedImage.TYPE_3BYTE_BGR); 
         Graphics g = result.getGraphics();
         try{
             g.drawImage(src.getScaledInstance(width, height, Image.SCALE_SMOOTH), 0, 0, null);
         }finally{
             g.dispose();
         }
        return result;      
    }
	
    /**
     * 转灰度图像
     * @param src
     * @return
     */
    private BufferedImage toGray(BufferedImage src){
        if(src.getType()==BufferedImage.TYPE_BYTE_GRAY){
            return src;
        }else{
            // 图像转灰
            BufferedImage grayImage = new BufferedImage(src.getWidth(), src.getHeight(),  
                    BufferedImage.TYPE_BYTE_GRAY);
            new ColorConvertOp(ColorSpace.getInstance(ColorSpace.CS_GRAY), null).filter(src, grayImage);
            return grayImage;       
        }
    }
    
	private List<Integer> getHashCode(BufferedImage hashImage) {
		byte[] matrixGray = (byte[]) toGray(hashImage).getData().getDataElements(0, 0, WIDTH, HEIGHT, null); 
		byte[][] arr = new byte[WIDTH][HEIGHT];
		List<Integer> ret = new ArrayList<Integer>();
		for (int i = 0; i < WIDTH; i++) {
		    arr[i] = new byte[HEIGHT];
		    System.arraycopy(matrixGray, i * HEIGHT, arr[i], 0, HEIGHT);
		}
		for(int i=0; i < WIDTH - 1; i++) {
			
			for(int j=0; j <  HEIGHT; j++) {
				
				if(arr[i][j] > arr[i+1][j]) ret.add(1);
				else ret.add(0);
			}
		}
		return ret;
	}
	
	private int compHashCode(List<Integer> hc1, List<Integer> hc2) {
	    int cnt = 0;
	    if(hc1 == null || hc2 == null || hc1.size() != hc2.size())
			try {
				throw new Exception("Hashcode length not match");
			} catch (Exception e) {
				e.printStackTrace();
			} 
	    int size = hc1.size();
	    for(int i=0; i<size; i++) if(hc1.get(i) == hc2.get(i)) cnt+=1;
	    return cnt;
	}

    
    public String caldHashSimilarity(String img1, String img2) {
    	try {
	    	BufferedImage image1 = ImageIO.read(new File(img1));
	    	BufferedImage image2 = ImageIO.read(new File(img2));
	    	//
	    	BufferedImage gray1 = toGray(resize(image1, WIDTH, HEIGHT));
	    	BufferedImage gray2 = toGray(resize(image2, WIDTH, HEIGHT));
	    	//hash值
	    	List<Integer> hc1 = getHashCode(gray1);
	    	List<Integer> hc2 = getHashCode(gray2);
	    	int compare = compHashCode(hc1, hc2);
	    	System.out.println(compare);
	    	DecimalFormat df=new DecimalFormat("0.00");
	    	return df.format((float)compare / ((WIDTH-1) * HEIGHT));
	    	
    	} catch(Exception e) {
    		e.printStackTrace();
    		return "0.0";
    	}
    }

}
