import java.io.*;

public class Demo {
    public static void main(String[] args) {
        int web_site_key_int = 6231289;
        String url_1="";
        String url_2="";
        //エンタ,スポー,地域,国際,国内,経済,科学
        for(;web_site_key_int<=6239980;web_site_key_int++) {
            try {
                url_1="./data/yahoo/process/科学/"+web_site_key_int+".txt";
                url_2="./data_2/科学/"+web_site_key_int+".txt";
                System.out.println(url_1);
                String[] command = {"cmd.exe", "/C", "mecab",url_1};
                Process ps = Runtime.getRuntime().exec(command);
                BufferedReader bReader_i = new BufferedReader(new InputStreamReader(ps.getInputStream()));
                String targetLine;

                InputStreamReader inputReader = null;
                BufferedReader bufferReader = null;
                File file = new File(url_1);
                InputStream inputStream = new FileInputStream(file);
                inputReader = new InputStreamReader(inputStream);
                bufferReader = new BufferedReader(inputReader);

                String str_text_name = bufferReader.readLine();
                File f = new File(url_2);
                FileWriter fw = new FileWriter(f);

                while (true) {
                    targetLine = bReader_i.readLine();
                    if (targetLine == null) {
                        break;
                    } else if (targetLine.equals("EOS")) {
                        continue;
                    } else {
                        String targetType = targetLine.split("[\t|,]")[1];
                        String[] str_print = targetLine.split("[\t]");
                        //str_print[0].replaceAll("[,./<>?；‘：“+;@#$%*]", "");
                        if (targetType.equals("名詞")) {
                            //System.out.println(targetType);
                            fw.write(str_print[0] + System.getProperty("line.separator"));
                            System.out.println(str_print[0]);
                        }
                    }
                }
                fw.flush();
                ps.waitFor();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}