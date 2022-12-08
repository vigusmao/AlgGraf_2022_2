import java.math.BigInteger;
import java.util.HashMap;
import java.util.Map;

public class Principal {

    static Map<Long, BigInteger> memo = new HashMap<>();

    public static BigInteger f(long x) {
        if (x < 2) {
            return BigInteger.valueOf(1);
        }
        if (x == 2) {
            return BigInteger.valueOf(3);
        }

        BigInteger resultFromMemo = memo.get(x);
        if (resultFromMemo != null) {
            return resultFromMemo;
        }

        BigInteger r = BigInteger.valueOf(2).multiply(f(x - 1)).add(f(x - 2));

        memo.put(x, r);

        return r;
    }

    public static void main(String[] args) {
        for (int i = 1; i <= 100; i++) {
            memo.clear();
            System.out.printf("\nf(%d) = %s",
                    i, f(i));
        }
    }
}
