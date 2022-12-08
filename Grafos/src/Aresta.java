public class Aresta {

    private final Vertice origem;
    private final Vertice destino;
    int custo;

    public Aresta(Vertice origem, Vertice destino) {
        this(origem, destino, Grafo.CUSTO_DEFAULT_ARESTAS);
    }

    public Aresta(Vertice origem, Vertice destino, int custo) {
        this.origem = origem;
        this.destino = destino;
        this.custo = custo;
    }

    public Vertice getOrigem() {
        return origem;
    }

    public Vertice getDestino() {
        return destino;
    }

    public int getCusto() {
        return custo;
    }

    public void setCusto(int custo) {
        this.custo = custo;
    }
}
