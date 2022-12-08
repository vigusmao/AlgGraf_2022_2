import java.util.Map;

public class Grafo {

    public static final int CUSTO_DEFAULT_ARESTAS = 1;

    private Map<String, Vertice> verticePorRotulo;

    public void addVertice(String rotulo) throws VerticeJaExisteException {

        if (verticePorRotulo.containsKey(rotulo)) {
            throw new VerticeJaExisteException("Vertice já existe!");
        }

        Vertice novo = new Vertice(rotulo);

        verticePorRotulo.put(rotulo, novo);
    }

    /**
     * @param rotulo
     *
     * @return o Vertice, se existir; null, caso contrário
     */
    public Vertice getVertice(String rotulo) {
        return this.verticePorRotulo.get(rotulo);
    }

    public Aresta adicionarAresta(String origem,
                                  String destino,
                                  int custo) {

        Vertice verticeOrigem = getVertice(origem);
        Vertice verticeDestino = getVertice(destino);

        if (verticeDestino == null || verticeOrigem == null) {
            throw new IllegalArgumentException("Aresta inválida!");
        }

        if (verticeOrigem.temVizinho(verticeDestino)) {
            throw new IllegalArgumentException("Aresta já existe!");
        }

        return verticeOrigem.adicionarVizinhoSaida(verticeDestino, custo);
    }


    public int getSize() {
        return verticePorRotulo.size();
    }

}
