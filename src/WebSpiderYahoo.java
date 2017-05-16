import java.io.*;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class WebSpiderYahoo {
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

    public static String delHTMLTag(String htmlStr){
        String regEx_script="<script[^>]*?>[\\s\\S]*?<\\/script>";
        String regEx_style="<style[^>]*?>[\\s\\S]*?<\\/style>";
        String regEx_html="<[^>]+>";
        Pattern p_script=Pattern.compile(regEx_script,Pattern.CASE_INSENSITIVE);
        Matcher m_script=p_script.matcher(htmlStr);
        htmlStr=m_script.replaceAll("");
        Pattern p_style=Pattern.compile(regEx_style,Pattern.CASE_INSENSITIVE);
        Matcher m_style=p_style.matcher(htmlStr);
        htmlStr=m_style.replaceAll("");
        Pattern p_html=Pattern.compile(regEx_html,Pattern.CASE_INSENSITIVE);
        Matcher m_html=p_html.matcher(htmlStr);
        htmlStr=m_html.replaceAll("");
        return htmlStr.trim();
    }

    public static String stripHtml(String content) {
        content = content.replaceAll("<p .*?>", "\r\n");
        content = content.replaceAll("<br\\s*/?>", "\r\n");
        content = content.replaceAll("\\<.*?>", "");
        return content;
    }

    public static void main(String[] args) {
        String web_site_key="6239974";
        String web_site_url="https://news.yahoo.co.jp/pickup/"+web_site_key;
        try{
            URL u = new URL(web_site_url);
            URLConnection connection = u.openConnection();
            HttpURLConnection htCon = (HttpURLConnection) connection;
            int code = htCon.getResponseCode();
            if (code == HttpURLConnection.HTTP_OK)
            {
                System.out.println("找到网页地址。。。");
                BufferedReader in=new BufferedReader(new InputStreamReader(htCon.getInputStream()));
                String inputLine;
                System.out.println("正在读取网页文本内容。。。");
                System.out.println("网页文本内容写入"+"./data/yahoo/"+web_site_key+".txt"+"。。。");
                while ((inputLine = in.readLine()) != null) {
                    inputLine=delHTMLTag(inputLine);
                    inputLine=stripHtml(inputLine);
                    inputLine=inputLine.replaceAll("\\d+","");
                    inputLine=inputLine.replaceAll("[a-zA-Z]","" );
                    //System.out.println(inputLine);
                    writeIntoFile(inputLine,"./data/yahoo/"+web_site_key+".txt", true);
                }
                in.close();
            }
            else
            {
                System.out.println("Can not access the website");
            }
        }
        catch(MalformedURLException e )
        {
            System.out.println("Wrong URL");
        }
        catch(IOException e)
        {
            System.out.println("Can not connect");
        }
    }
}
