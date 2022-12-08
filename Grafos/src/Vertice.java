import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

public class Vertice {

    private final String rotulo;

    private Map<String, Vertice> vizinhoDeSaidaPorRotulo;
    private Map<Vertice, Aresta> arestaPorVizinhoDeSaida;

    public Vertice(String rotulo) {
        this.rotulo = rotulo;
        this.vizinhoDeSaidaPorRotulo = new HashMap<>();
        this.arestaPorVizinhoDeSaida = new HashMap<>();
    }

    public boolean temVizinho(Vertice outro) {
        return arestaPorVizinhoDeSaida.containsKey(outro);
    }

    public Aresta adicionarVizinhoSaida(Vertice vizinho, int custo) {
        Aresta novaAresta = new Aresta(this, vizinho, custo);
        arestaPorVizinhoDeSaida.put(vizinho, novaAresta);
        vizinhoDeSaidaPorRotulo.put(vizinho.getRotulo(), vizinho);
        return novaAresta;
    }

    public int getGrauDeSaida() {
        return vizinhoDeSaidaPorRotulo.size();
    }

    public String getRotulo() {
        return rotulo;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Vertice vertice = (Vertice) o;
        return Objects.equals(rotulo, vertice.rotulo);
    }

    @Override
    public int hashCode() {
        return Objects.hash(rotulo);
    }
}
