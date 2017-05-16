/**
 * Created by Si lei on 2017/5/16.
 */
import java.io.*;

public class TxtProcess {
    public static boolean createNewFile(String filePath) {
        boolean isSuccess = true;
        String filePathTurn = filePath.replaceAll("\\\\", "/");
        int index = filePathTurn.lastIndexOf("/");
        String dir = filePathTurn.substring(0, index);
        File fileDir = new File(dir);
        isSuccess = fileDir.mkdirs();
        File file = new File(filePathTurn);
        try {
            isSuccess = file.createNewFile();
        } catch (IOException e) {
            isSuccess = false;
            e.printStackTrace();
        }
        return isSuccess;
    }

    public static boolean writeIntoFile(String content, String filePath, boolean isAppend) {
        boolean isSuccess = true;
        int index = filePath.lastIndexOf("/");
        String dir = filePath.substring(0, index);
        File fileDir = new File(dir);
        fileDir.mkdirs();
        File file = null;
        try {
            file = new File(filePath);
            file.createNewFile();
        } catch (IOException e) {
            isSuccess = false;
            e.printStackTrace();
        }
        FileWriter fileWriter = null;
        try {
            fileWriter = new FileWriter(file, isAppend);
            fileWriter.write(content);
            fileWriter.flush();
        } catch (IOException e) {
            isSuccess = false;
            e.printStackTrace();
        } finally {
            try {
                if (fileWriter != null)
                    fileWriter.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return isSuccess;
    }

    public static void readTxtFile(String filePath,String web_site_key){
        try {
            String encoding="utf-8";
            File file=new File(filePath);
            if(file.isFile() && file.exists()){ //判断文件是否存在
                InputStreamReader read = new InputStreamReader(
                        new FileInputStream(file),encoding);//考虑到编码格式
                BufferedReader bufferedReader = new BufferedReader(read);
                String lineTxt = null;
                while((lineTxt = bufferedReader.readLine()) != null){
                    //System.out.println(lineTxt);
                    String content="";
                    String label="";
                    content=lineTxt.substring(lineTxt.indexOf("掲載") + 1, lineTxt.indexOf("[続きを読む]"));
                    label=lineTxt.substring(lineTxt.indexOf("アクセスランキング") + 10, lineTxt.indexOf("アクセスランキング")+13);
                    System.out.println(lineTxt.substring(lineTxt.indexOf("掲載") + 1, lineTxt.indexOf("[続きを読む]")));
                    System.out.println(lineTxt.substring(lineTxt.indexOf("アクセスランキング") + 10, lineTxt.indexOf("アクセスランキング")+13));
                    writeIntoFile(content,"./data/yahoo/process/"+label+"/"+web_site_key+".txt", true);
                }
                read.close();
            }else{
                System.out.println("找不到指定的文件");
            }
        } catch (Exception e) {
            System.out.println("读取文件内容出错");
            e.printStackTrace();
        }
    }

    public static void main(String argv[]){
        int web_site_key_int = 6229974;
        for (;web_site_key_int<=6249974;web_site_key_int++) {
            String web_site_key = String.valueOf(web_site_key_int);
            String filePath = "C:\\Code\\Jetbrain\\NPL_japanese_text_classification\\data\\yahoo\\"+ web_site_key +".txt";
            readTxtFile(filePath,web_site_key);
        }
    }
}
