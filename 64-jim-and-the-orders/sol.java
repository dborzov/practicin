import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class sol {

  public static void debug(Object... args) {
    System.out.println(Arrays.deepToString(args));
  }

  public static void main(String... args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    PrintWriter pw = new PrintWriter(System.out, true);
    solve(br, pw);
    pw.flush();
  }

  private static void solve(BufferedReader br, PrintWriter pw)
      throws Exception {
    int N = Integer.parseInt(br.readLine());
    List<P> v = new ArrayList<>();
    for(int i=1;i<=N;i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      int ti = Integer.parseInt(st.nextToken());
      int di = Integer.parseInt(st.nextToken());
      v.add(new P(ti + di, i));
    }
    Collections.sort(v);
    for (P vi : v) {
      pw.print(vi.id);
      pw.print(" ");
    }
    pw.println();
  }

  private static final class P implements Comparable<P> {
    int tm;
    String id;
    public P(int tm, int id) {
      this.tm = tm;
      this.id = "" + id;
    }
    @Override
    public int compareTo(P o) {
      if (tm == o.tm) {
        return id.compareTo(o.id);
      }
      return tm - o.tm;
    }
  }
}
