import pandas as pd
import plotly.express as px
import os

def main():
    csv = "cancelamentos.csv"
    if not os.path.exists(csv):
        print(f"Arquivo {csv} não encontrado no diretório atual.")
        return

    df = pd.read_csv(csv)
    if "CustomerID" in df.columns:
        df = df.drop(columns="CustomerID")
    df = df.dropna()

    os.makedirs("figures", exist_ok=True)

    # gráfico principal: cancelou
    try:
        fig = px.histogram(df, x="cancelou", color="cancelou",
                           title="Contagem de Cancelamentos por Motivo")
        fig.write_html("figures/cancelou_hist.html")
        try:
            fig.write_image("figures/cancelou_hist.png", scale=2)
        except Exception:
            print("Aviso: não foi possível exportar PNG (verifique se 'kaleido' está instalado).")
    except Exception as e:
        print(f"Erro ao criar gráfico 'cancelou': {e}")

    # gerar gráficos por coluna
    for col in df.columns:
        if col == "cancelou":
            continue
        safe = col.replace(" ", "_")
        try:
            f = px.histogram(df, x=col, color="cancelou",
                             title=f"Distribuição de {col} por cancelamento")
            f.write_html(f"figures/{safe}_by_cancelou.html")
            try:
                f.write_image(f"figures/{safe}_by_cancelou.png", scale=2)
            except Exception:
                pass
        except Exception:
            continue

    print("Gráficos gerados em 'figures/' (HTML e, se possível, PNG).")

if __name__ == "__main__":
    main()
