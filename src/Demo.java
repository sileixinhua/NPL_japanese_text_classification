import java.io.*;

public class Demo {
    public static void main(String[] args) {
        try {
            String[] command = { "cmd.exe", "/C", "mecab", "./data/アメリカ合衆国の経済史.txt" };
            Process ps = Runtime.getRuntime().exec(command);
            BufferedReader bReader_i = new BufferedReader(new InputStreamReader(ps.getInputStream()));
            String targetLine;

            InputStreamReader inputReader = null;
            BufferedReader bufferReader = null;
            File file = new File("./data/mecab.txt");
            InputStream inputStream = new FileInputStream(file);
            inputReader = new InputStreamReader(inputStream);
            bufferReader = new BufferedReader(inputReader);

            String str_text_name=bufferReader.readLine();
            File f = new File("./data/"+str_text_name+".txt");
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
                    str_print[0].replaceAll("[,./<>?；‘：“+;@#$%*]","");
                    if (targetType.equals("名詞")) {
                        //System.out.println(targetType);
                        fw.write(str_print[0]+ System.getProperty("line.separator"));
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